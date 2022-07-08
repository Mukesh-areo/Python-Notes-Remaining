from flask import Flask
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)





class MyServer:

  def __init__(self):
    pass

  @route('/getSomeData')
  def math_operation():
      if (request.method == 'POST'):
          operation = request.form['operation']
          num1 = int(request.form['num1'])
          num2 = int(request.form['num2'])
          if (operation == 'add'):
              r = num1 + num2
              result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
          if (operation == 'subtract'):
              r = num1 - num2
              result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
          if (operation == 'multiply'):
              r = num1 * num2
              result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
          if (operation == 'divide'):
              r = num1 / num2
              result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
          return render_template('results.html', result=result)


MyServer.register(app, base_route="/")


if __name__ == "__main__":
  app.run(host='0.0.0.0')