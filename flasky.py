import os
from app import create_app, db
from app.models import *
from flask_migrate import Migrate
from flask import render_template
# from flask_debugtoolbar import DebugToolbarExtension
app = create_app('default')
# toolbar = DebugToolbarExtension(app)
migrate = Migrate(app, db)
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db)

@app.errorhandler(404)
def page_not_found(error):
    """
    404
    """
    return render_template("home/404.html"), 404
