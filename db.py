import sqlite3
from datetime import datetime


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
        "name"	TEXT, "record" INTEGER, "record_time" DATE)
        """
        session_table = """
                CREATE TABLE IF NOT EXISTS "board" (
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

    def save_session(self, name, table, score):
        drop_table = 'DROP TABLE "board"'
        drop_account = 'DROP TABLE "account"'
        session_table = """
                CREATE TABLE IF NOT EXISTS "board" (
                "cell" INTEGER, "value" INTEGER)
                """
        session_account = """
                        CREATE TABLE IF NOT EXISTS "account" (
                        "name" TEXT, "record" INTEGER)
                        """
        save_table = "INSERT INTO board VALUES" + ", ".join([f'({i}, {table[i]})' for i in range(16)])
        print(save_table)
        save_account = f"INSERT INTO account VALUES  ('{name}',{score})"
        cur = self.conn.cursor()
        cur.execute(drop_table)
        cur.execute(drop_account)
        cur.execute(session_table)
        cur.execute(save_table)
        cur.execute(session_account)
        cur.execute(save_account)
        self.conn.commit()

    def load_session(self):
        cur = self.conn.cursor()
        account_query = 'SELECT name, record from account'
        result = cur.execute(account_query)
        try:
            name, score = result.fetchall()[0]
        except:
            name = ""
            score = 0
        board_query = 'SELECT value from board order by cell'
        result = cur.execute(board_query)
        try:
            board = [cell[0] for cell in result.fetchall()]
        except:
            board = []
        return name, board, score



    def save_leader(self, name, score):
        cur_date = datetime.today()
        query = f'''
                insert into  leaders values ('{name}', {score}, '{cur_date}')
                '''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def get_record(self):
        query = '''
        SELECT record from leaders
        order by record DESC
        limit 1
        '''
        cur = self.conn.cursor()
        result = cur.execute(query)
        try:
            return result.fetchall()[0][0]
        except:
            return 0


if __name__ == '__main__':
    base = Statistic()
    t = base.get_leaders()
    print(t)
