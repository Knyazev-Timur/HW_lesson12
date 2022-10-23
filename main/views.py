from flask import Blueprint, render_template, request
from functions import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', url_prefix='/')


@main_blueprint.route("/")
def page_index():
    return render_template('index.html')


@main_blueprint.route("/search")
def page_search():
    error = None
    pk = request.args.get('s')
    # проверяем, передается ли параметр в URL-адресе
    if pk and pk != '':
        posts = search_posts(pk)
        return render_template('post_list.html', posts=posts, pk=pk)
    else:
        error = 'Не введен запрос!'
        return render_template('index.html', error=error)
