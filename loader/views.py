from flask import Blueprint, render_template, request
from functions import *
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', url_prefix='/')

logging.basicConfig(level=logging.INFO)
consol_loger = logging.getLogger()
# console_handler = logging.StreamHandler()
# formatter_one = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
# console_handler.setFormatter(formatter_one)
# consol_loger.addHandler(console_handler)


@loader_blueprint.route("/post")
def page_post():
    return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])
def page_post_form():
    picture = request.files.get('picture')
    content = request.form.get('content')
    file_path = get_patch(picture)
    if file_path is False:
        # Проверка на соответсвие типа файла до его записи
        logging.info(f"Пост не записан!")
        return render_template('post_form.html')
    else:
        logging.info(f"Передан пост: {file_path} : {content}")
        save_post({'pic': file_path, 'content': content})
        return render_template('post_uploaded.html', file_path=file_path, content=content)
