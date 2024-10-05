from flask import Flask, Response

app = Flask(__name__)


# Route for the index view
@app.route("/")
def index():
    # Return only the <h1> tag as the test might be expecting plain content
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# Route for the print_string view
@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter


# Route for the count view
@app.route("/count/<int:parameter>")
def count(parameter):
    # Ensure an extra newline is added at the end
    response = "\n".join([str(i) for i in range(parameter)]) + "\n"
    return Response(response, mimetype="text/plain")


# Route for the math view
@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation", 400
    return str(result)


if __name__ == "__main__":
    app.run(port=5555)
