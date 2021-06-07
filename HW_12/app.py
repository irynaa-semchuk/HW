# flask_web/app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hey, this is a calculator!\nEnter - "/ calc / x / y / operation" \nWhere the operator is: dif, sum, div or mul'
    
    

@app.route('/calc/<int:x>/<int:y>/<string:oper>')
def calc(x, y, oper):
    if oper == 'dif':
        return render_template('calc.html', x=x, y=y, result=x / y, symbol="/")
    elif oper == 'sum':
        return render_template('calc.html', x=x, y=y, result=x + y, symbol="+")
    elif oper == 'div':
        return render_template('calc.html', x=x, y=y, result=x - y, symbol="-")
    elif oper == 'mul':
        return render_template('calc.html', x=x, y=y, result=x * y, symbol="*")
    else:
        return render_template('calc.html', result="Data was entered incorrectly")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
