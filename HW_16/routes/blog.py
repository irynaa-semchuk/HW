from os import abort

from app import app, api, db
from flask import render_template, request, Response
from config import Config, articles
from flask_restful import Resource, Api
from models.models import Article, User
from django.core.paginator import Paginator


@app.route('/', methods=["GET"])
def homepage():
    articles = Article.query.all()
    return render_template('blog/index.html', config=Config, articles=articles)


@app.route('/article/<string:slug>')
def article_details(slug):
    article = Article.query.filter_by(slug=slug).first()
    return render_template('blog/details.html', article=article)


class MenuItem(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.MENU_ITEMS
        }


class Articles(Resource):
    def post(self):
        data = request.json
        paginator = Paginator(tuple(data.items()), 1)
        page = request.GET.get('page')
        try:
            p = paginator.page(page)
        except PageNotAnInteger:
            p = paginator.page(pag for pag in paginator.page_range)
        article = Article(p)
        db.session.add(article)
        db.session.commit()
        return article.serialize

    def get(self):
        articles = Article.query
        if request.args.get('title'):
            articles = articles.filter_by(title=request.args.get('title'))

        if request.args.get("sort_by"):
            articles = articles.order_by(request.args.get("sort_by"))

        articles = articles.all()
        serialized_articles = [article.serialize for article in user.articles]

        return serialized_articles


class ArticlesEntity(Resource):
    def get(self, id):
        article = Article.query.get(id)
        if article == None:
            return Response(status=404)
        return article.serialize


class Users(Resource):
    def get(self):
        user = User.query.get(1)
        if user is None:
            return Response(status=404)
        serialized_articles = [article.serialize for article in user.articles]
        return serialized_articles


class User_Update(Resource):
    def post(self,id):
        user = User.query.get(id)
        data = request.json
        user.username = data.get('username')
        user.email = data.get('email')
        user.created = data.get('created')
        user.bio = data.get('bio')
        user.admin = data.get('admin')
        db.session.commit()
        return user.serialize


class User_Create(Resource):
    def post(self):
        data = request.json
        user = User(
            username=data.get('username'),
            email=data.get('email'),
            created=data.get('created'),
            bio=data.get('bio'),
            admin=data.get('admin')
        )
        if user is None:
            db.session.add(user)
            db.session.commit()
            return user.serialize, 201
        else:
            abort(409, f'User {user.username} exists already')


class User_Read(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user is None:
            return Response(status=404)
        else:
            abort(404, 'Person not found for Id: {id}'.format(id=id))
        serialized_articles = [article.serialize for article in user.articles]
        serialized_user = [user.serialize, serialized_articles]
        return serialized_user


api.add_resource(MenuItem, '/menu-items')
api.add_resource(Articles, '/articles')
api.add_resource(Users, '/users')
api.add_resource(ArticlesEntity, '/articles/<int:id>')
api.add_resource(User_Read, '/users/<int:id>')
api.add_resource(User_Update, '/users/update/<int:id>')
api.add_resource(User_Create, '/users/create')

