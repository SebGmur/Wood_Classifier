# By defining __init__.py we are telling Python
# to treat the content of this folder as a package
# In here we initialise 

from flask import Flask


# In here we initialise our “app” as a Flask application object,
# so we can reference content of this application via "from app import app"
# where 
#  "from app" is folder name where "__init__.py" 
#  "import app" name of the Flask application object
#  we initialised inside "__init__.py"

#initialise flask application object
app = Flask(__name__)

# Here we include all the python files
# so the content of these files are 
# included to our application


# app refers to folder "app" 
# views refers to "views.py" inside folder "app"
from app import views


#-----------------------------------------------------------------------------#
#                            admin is dummy for now                           #
#-----------------------------------------------------------------------------#
# app refers to folder "app" 
# views refers to "admin_views.py" inside folder "app"
from app import admin_views
