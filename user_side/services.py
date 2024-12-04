from contextlib import closing
from django.db import connection


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_product_by_id(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from user_side_product where id={}""".format(pk))
        product = dict_fetchone(cursor)
        return product


def get_user_by_phone_number(phone):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from user_side_customer usc where usc.phone_number = %s;""", [phone])
        user = dict_fetchone(cursor)
        return user
