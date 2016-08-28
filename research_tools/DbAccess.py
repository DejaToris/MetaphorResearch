import pymssql
from enum import Enum
import random


class FakeSqlCursor(object):
    def execute(self, sql_query):
        pass

    def fetchone(self):
        return [random.random()]


class FakeSqlConn(object):
    def cursor(self):
        return FakeSqlCursor()


class TestConnection(object):
    def __enter__(self):
        self.conn = FakeSqlConn()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __init__(self, a, b, c):
        pass


class ServerConnection(object):
    def __enter__(self):
        self.conn = pymssql.connect(self.server_name, self.user, self.password)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def __init__(self, server_name, user, password):
        self.server_name = server_name
        self.user = user
        self.password = password


class AvailableConnections(Enum):
    test = 1
    bgu = 2


def get_connection(db_type):
    if db_type == AvailableConnections.test:
        return TestConnection("a", "a", "a")
    elif db_type == AvailableConnections.bgu:
        return ServerConnection("sqlsrv.cs.bgu.ac.il", "noamant", "1qa@WS")
    else:
        raise Exception("Non-familiar DB type. DB types: {0}".format(repr(AvailableConnections)))


