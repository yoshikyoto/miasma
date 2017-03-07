# -*- coding: utf-8 -*-
from dao import Dao

# connectionやcommitのしかたがイマイチなので直したい
class ChampionDao(Dao):

    def __init__(self):
        super(ChampionDao, self).__init__()

    def select_all(self):
        connection = super(ChampionDao, self).connect()
        cursor = super(ChampionDao, self).cursor(connection)
        cursor.execute("SELECT * FROM `champion`")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def select(self, key):
        connection = super(ChampionDao, self).connect()
        cursor = super(ChampionDao, self).cursor(connection)
        cursor.execute(
            "SELECT * FROM `champion` WHERE `key` = %s",
            [key])
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        if(len(result) < 1):
            return None
        else:
            return result[0]

    def insert(self, id, key, name, icon_url):
        connection = super(ChampionDao, self).connect()
        cursor = super(ChampionDao, self).cursor(connection)
        cursor.execute(
            """
            INSERT INTO `champion` (`id`, `key`, `name`, `icon_url`)
            VALUES (%s, %s, %s, %s)
            """,
            [id, key, name, icon_url])
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, key):
        connection = super(ChampionDao, self).connect()
        cursor = super(ChampionDao, self).cursor(connection)
        cursor.execute(
            "DELETE FROM `champion` WHERE `key` = %s",
            [key])
        connection.commit()
        cursor.close()
        connection.close()

if __name__ == "__main__":
    dao = ChampionDao()
    dao.insert(1, "test", "テスト", "url")
    print dao.select("test")["name"]
    print dao.select_all()
    dao.delete("test")
    print dao.select("test")
    print dao.select_all()
