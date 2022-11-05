#!/usr/bin/python
"""
@FilePath: py03.py
@Author: Huang Lingang
@Date: 2022-03-04 17:40:10
@LastEditors: Huang Lingang
@LastEditTime: 2022-03-04 18:00:56
"""

import sqlite3


class SQL(object):

    def __init__(self):
        self.cnn = None
        self.cursor = None
        pass

    def connect(self, db=None):
        if db is None:
            print("please specific database to open")

        self.cnn = sqlite3.connect(db)
        self.cursor = self.cnn.cursor()

    def selectAll(self, table=None):
        if table is None:
            print("please specific table to select data")
        self.cursor.execute("select * from %s" % table)
        for row in self.cursor:
            print(row)

    def selectById(self, table=None, id=0):
        if table is None:
            print("please specific table to select data")
        if isinstance(id, int):
            self.cursor.execute(f"select * from {table} where id={id}")
            for row in self.cursor:
                print(row)
        if isinstance(id, (list, tuple)):
            for _id in id:
                self.cursor.execute(f"select * from {table} where id={_id}")
                for row in self.cursor:
                    print(row)

    def close(self):
        self.cursor.close()
        self.cnn.close()


if __name__ == "__main__":
    sql = SQL()
    sql.connect("/home/huanglingang/sqlite3/test.db")
    sql.selectById("tabtest", id=1)
    sql.selectById("tabtest", id=(1, 2))
    sql.selectAll("tabtest")
    sql.close()