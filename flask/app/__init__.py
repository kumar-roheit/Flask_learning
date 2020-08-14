# Think of the __init__.py file as a contructor that pulls all of the parts of our application together into a package and then tells Python to treat it as a package.

from flask import Flask

app = Flask(__name__)

from app import views
from app import admin_views
