# importing flask module in the project in mandatory
# An object of Flask is our WSGI application
from flask import Flask

# flask constructor takes the name of
# current module (__name__) as argument
app = Flask(__name__)

# The route() function of the Flask class is a decorator
# which tells the application which URL should call
# the associated function.
@app.route('/hello/<name>')
def hello_name(name):
  return 'Hello %s!' % name

@app.route("/")
# the `/` URL is bound with hello_world() function.
def hello_world():
  return 'Hello world'

# main driver function
if __name__ == '__main':

  # run() method of Flask class runs the application
  # on the local development server.
  app.run(host='0.0.0.0', port=5000, debug=True)
