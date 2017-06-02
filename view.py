from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

view = Blueprint('view', __name__, template_folder='templates')

@view.route('/', defaults={'page': 'index'})
@view.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)