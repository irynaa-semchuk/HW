SELECT * FROM articles
    LEFT JOIN article_categories a ON articles.id = a.articles.id
    LEFT JOIN category c ON  ac.category_id = c.id;