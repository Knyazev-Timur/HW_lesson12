import json
import logging

logging.basicConfig(level=logging.INFO)
consol_loger = logging.getLogger()


def read_json():
    with open('posts.json', 'r', encoding='UTF-8') as load_files:
        return json.load(load_files)


def search_posts(pk):
    """
    :param pk:
    :return:list
    Создает список словарей по параметрам поиска
    """
    all_posts = read_json()
    return [post for post in all_posts if pk.lower() in post.get('content').lower()]


def get_patch(picture):
    """
    :param picture:
    :return:str
    Получает данные о загружаемом файле и возвращает строку адреса записи
    """
    correct_type = ('jpg', 'bmp', 'png', 'gif', 'jpeg')
    file_name = picture.filename
    type_file = file_name.split('.')[-1]

    if type_file not in correct_type:
        logging.info(f"передан неверный формат файла")
        return False
    else:
        picture.save(f'./uploads/images/{file_name}')
        logging.info(f"записан файл: {file_name}")
        return f'/uploads/images/{file_name}'


def save_post(content):
    """
    :param content:
    :return:
    Записывает полученный пост в JSON
    """
    posts = read_json()
    posts.append(content)
    with open('posts.json', 'w', encoding='UTF-8') as save_file:
        json.dump(posts, save_file, ensure_ascii=False)
        logging.info(f"записан пост: {content}")
