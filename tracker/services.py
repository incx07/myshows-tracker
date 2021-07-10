import requests
from .models import SerialLater, SerialComplete
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist


def myshows_search(title: str) -> dict:
    """Поиск сериалов по названию на ресурсе MyShows с использованием API
    на базе JSON-RPC 2.0
    """
    rpc = {
            'jsonrpc': '2.0',
            'method': 'shows.Search',
            'params': {
                'query': 'string'
                },
            'id': 1
          }
    rpc['params']['query'] = title
    response = requests.post('https://api.myshows.me/v2/rpc/', json = rpc).json()
    return response


def myshows_getbyid(id: str) -> dict:
    """Получение информации о сериале по его id на ресурсе MyShows
    с использованием API на базе JSON-RPC 2.0
    """
    rpc = {
            "jsonrpc": "2.0",
            "method": "shows.GetById",
            "params": {
                "showId": 0,
                "withEpisodes": False
                },
            "id": 1
          }
    rpc['params']['showId'] = id
    response = requests.post('https://api.myshows.me/v2/rpc/', json = rpc).json()
    return response


def delete_seriallater(myshows_id, user):
    """ Удаление связи пользователя с объектом из таблицы SerialLater """
    del_serial = SerialLater.objects.get(myshows_id = myshows_id)
    del_serial.user_link.remove(user)


def delete_serialcomplete(myshows_id, user):
    """ Удаление объекта из таблицы SerialComplete """
    del_serial = SerialComplete.objects.get(myshows_id = myshows_id)
    del_serial.user_link.remove(user)


def create_seriallater(response, user):
    """ Добавление объекта в таблицу SerialLater """
    myshows_id = response['result']['id']
    title_eng = response['result']['titleOriginal']
    year = response['result']['year']
    try:
        obj_seriallater = SerialLater.objects.get(myshows_id = myshows_id)
        obj_seriallater.user_link.add(user)
    except SerialLater.DoesNotExist:
        obj_seriallater = SerialLater(
            myshows_id = myshows_id,
            title_eng = title_eng,
            year = year
            )
        obj_seriallater.save()
        obj_seriallater.user_link.add(user)


def create_serialcomplete(response, user):
    """ Добавление объекта в таблицу SerialComplete и в случае наличия
        данного объекта в таблице SerialLater - удаление оттуда
    """
    myshows_id = response['result']['id']
    title_eng = response['result']['titleOriginal']
    year = response['result']['year']
    try:
        obj_serialcomplete = SerialComplete.objects.get(myshows_id = myshows_id)
        obj_serialcomplete.user_link.add(user)
    except SerialComplete.DoesNotExist:
        obj_serialcomplete = SerialComplete(
            myshows_id = myshows_id,
            title_eng = title_eng,
            year = year
            )
        obj_serialcomplete.save()
        obj_serialcomplete.user_link.add(user)
    if SerialLater.objects.filter(myshows_id = myshows_id):
        delete_seriallater(myshows_id, user)


def set_rating(myshows_id, user_id, rating):
    """ Установка пользовательского рейтинга для сериала в таблице
        SerialComplete
    """
    upd_serial = SerialComplete.objects.get(
        myshows_id=myshows_id,
        user_link=user_id)
    upd_serial.rating = rating
    upd_serial.save()


def set_all_seriallater(user):
    """ Получение всех объектов из SerialLater для пользователя """
    return user.seriallater_set.all()


def set_all_serialcomplete(user):
    """ Получение всех объектов из SerialComplete для пользователя """
    return user.serialcomplete_set.all()


def pagination(serials, page):
    """ Стандартная пагинация Django """
    paginator = Paginator(serials, 5)
    try:
        serials_page = paginator.page(page)
    except PageNotAnInteger:
        serials_page = paginator.page(1)
    except EmptyPage:
        serials_page = paginator.page(paginator.num_pages)
    return serials_page


def set_button_later(myshows_id, user_id):
    """ Установка флага отображения кнопки "Хочу посмотреть" """
    try:
        SerialLater.objects.get(
            myshows_id__exact = myshows_id,
            user_link__exact = user_id)
        show_button_later = False
    except ObjectDoesNotExist:
        show_button_later = True
    return show_button_later


def set_button_complete(myshows_id, user_id):
    """ Установка флага отображения кнопки "Полностью посмотрел" """
    try:
        SerialComplete.objects.get(
            myshows_id__exact = myshows_id,
            user_link__exact = user_id)
        show_button_complete = False
    except ObjectDoesNotExist:
        show_button_complete = True
    return show_button_complete
