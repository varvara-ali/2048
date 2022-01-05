import sqlite3


class Statistic:
    def __init__(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect('stat')
            print(sqlite3.version)
        except Exception as e:
            print(e)

    def create_db(self):
        leaders_creation = """
        CREATE TABLE IF NOT EXISTS "leaders" (
        "name"	TEXT, "record" INTEGER, "record_time" DATETIME)
        """
        session_table = """
                CREATE TABLE IF NOT EXISTS "table" (
                "cell" INTEGER, "value" INTEGER)
                """
        session_account = """
                        CREATE TABLE IF NOT EXISTS "account" (
                        "name" TEXT, "record" INTEGER)
                        """
        cur = self.con.cursor()
        result = cur.execute(leaders_creation)
        result = cur.execute(session_table)
        result = cur.execute(session_account)
        self.con.commit()

    def get_leaders(self, count=10):
        pass

    def save_sassion(self, name, score, table):
        pass

    def load_sassion(self):
        pass
