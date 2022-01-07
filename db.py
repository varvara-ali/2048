import sqlite3


class Statistic:
    def __init__(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect('stat')
        except Exception as e:
            print(e)
        self.create_db()

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
        cur = self.conn.cursor()
        cur.execute(leaders_creation)
        cur.execute(session_table)
        cur.execute(session_account)
        self.conn.commit()

    def insert_dummy(self):
        query = '''
        insert into  leaders values ('test', 500, '2021-12-12'), ('test2', 600, '2021-12-24')
        '''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def get_leaders(self, count=10):
        list_leaders = f"""
        SELECT * FROM leaders
        ORDER BY record desc
        limit {count}
        """
        cur = self.conn.cursor()
        result = cur.execute(list_leaders)
        # results = ["{:<20s}|{:>5d}|{:>10s} ".format(r[0], r[1], r[2]) for r in result.fetchall()]
        return result.fetchall()

    def save_session(self, name, score, table):
        pass

    def load_session(self):
        pass


if __name__ == '__main__':
    base = Statistic()
    t = base.get_leaders()
    print(t)

