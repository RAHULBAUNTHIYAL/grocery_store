from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template("index.html")

# Define another route with a dynamic parameter
@app.route('/orders')
def orders():
    return render_template("orders.html")


@app.route('/products')
def products():
    return render_template("Products.html")


@app.route('/category')
def category():
    return render_template("Category.html")


# Start the Flask app when this script is run
if __name__ == '__main__':
    app.run(debug=True)
