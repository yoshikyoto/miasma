# -*- coding: utf-8 -*-
from dao import Dao

# connectionやcommitのしかたがイマイチなので直したい
class ItemDao(Dao):

    def __init__(self):
        super(ItemDao, self).__init__()

    def select_all(self):
        connection = super(ItemDao, self).connect()
        cursor = super(ItemDao, self).cursor(connection)
        cursor.execute("SELECT * FROM item")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def insert(self, id, name, description_html, icon_url):
        connection = super(ItemDao, self).connect()
        cursor = super(ItemDao, self).cursor(connection)
        cursor.execute(
            """
            INSERT INTO item (id, name, description_html, icon_url)
            VALUES (%s, %s, %s, %s)
            """,
            [id, name, description_html, icon_url])
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, id):
        connection = super(ItemDao, self).connect()
        cursor = super(ItemDao, self).cursor(connection)
        cursor.execute(
            "DELETE FROM item WHERE id = %s",
            [id])
        connection.commit()
        cursor.close()
        connection.close()

if __name__ == "__main__":
    dao = ItemDao()
    dao.insert(1, "test", "テスト", "url")
    print dao.select_all()
    dao.delete(1)
    print dao.select_all()
