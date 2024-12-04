from contextlib import closing
from django.db import connection


def dict_fetchall(cursor):
    columns = [cur[0] for cur in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return None
    columns = [cur[0] for cur in cursor.description]
    return dict(zip(columns, row))


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT id, name, created_at FROM user_side_category;""")
        categories = dict_fetchall(cursor)
        return categories


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT user_side_product.id, user_side_product.name, user_side_product.description,
        user_side_product.price, user_side_product.cost, user_side_product.image as image, user_side_product.created_at
        FROM user_side_product order by user_side_product.id;""")
        products = dict_fetchall(cursor)
        return products


def get_customers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select usc.id, usc.first_name, usc.last_name, usc.phone_number, usc.created_at 
        from user_side_customer usc;""")
        orders = dict_fetchall(cursor)
        return orders


def get_orders():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT user_side_order.id, user_side_customer.first_name as first_name, 
        user_side_customer.last_name as last_name, user_side_order.payment_type, user_side_order.address, 
        user_side_order.status, user_side_order.created_at FROM user_side_order 
        LEFT JOIN user_side_customer ON user_side_order.customer_id = user_side_customer.id 
        order by user_side_order.status asc, user_side_order.created_at desc;""")
        orders = dict_fetchall(cursor)
        return orders


def get_product_by_category():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT usc.name, count(category_id) as count FROM user_side_product usp
        right join user_side_category usc on usp.category_id = usc.id group by usc.id order by usc.name;""")
        product_by_category = dict_fetchall(cursor)
        return product_by_category


def get_top_sold_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select usp."name", sum(uso.amount) as total from user_side_product usp 
        left join user_side_orderproduct uso on usp.id = uso.product_id
        group by usp."name" having sum(uso.amount) > 0 order by total desc nulls last limit 10;""")
        top_products = dict_fetchall(cursor)
        return top_products


def get_orders_by_id(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select uso.id, usc.name as category_name, usp."name", usp.price, uso2.amount as count, usp.price * uso2.amount as total, 
        uso2.created_at from user_side_product usp left join user_side_orderproduct uso2 on usp.id = uso2.product_id
        left join user_side_order uso on uso.id = uso2.order_id left join user_side_category usc on usp.category_id = usc.id 
         where uso2.order_id = {pk};""")
        orders_by_id = dict_fetchall(cursor)
        return orders_by_id


def get_customer_order_id_list(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select usc.id, usc.first_name, usc.last_name, uso.address, uso.status, uso.payment_type, 
        uso.created_at, uso.id as order_id from user_side_customer usc 
        left join user_side_order uso on usc.id = uso.customer_id where usc.id = {pk};""")
        result = dict_fetchall(cursor)
        return result
