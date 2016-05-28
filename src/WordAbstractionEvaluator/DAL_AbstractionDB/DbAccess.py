import pymssql


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




