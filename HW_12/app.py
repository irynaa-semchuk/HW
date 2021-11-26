# flask_web/app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

oper = ['sum', 'dif', 'mult', 'div']
symbol = ['+', '-', '*', '/']
FUNC = dict(map(lambda *args: args, oper, symbol))


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hey, this is a calculator!\tEnter - "/ calc / x / y / operation" \t Where the operator is: dif, sum, div or mul'


@app.route('/calc/<int:x>/<int:y>/<string:oper>')
def calc(x, y, oper):
    func = FUNC.get(oper)
    if func:
        return render_template('calc.html', x=x, y=y, result=eval(f'{x} {func} {y}'), oper=str(func))
    else:
        return render_template('calc.html', result="Data was entered incorrectly")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
