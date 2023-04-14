import pandas as pd
import sqlite3
from geopy.distance import geodesic


class FarmersMarket:
    def __init__(self, db_file, csv_file):
        self.db_file = db_file
        self.csv_file = csv_file
        self.conn = sqlite3.connect(self.db_file)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS farmers_market
                        (FMID INTEGER PRIMARY KEY,MarketName TEXT,Website TEXT,
                        Facebook TEXT, Twitter TEXT,Youtube TEXT,OtherMedia TEXT, street TEXT,city TEXT,County TEXT,State TEXT,zip TEXT,Season1Date TEXT,
                        Season1Time TEXT,Season2Date TEXT,Season2Time TEXT,Season3Date TEXT,Season3Time TEXT,Season4Date TEXT,Season4Time TEXT,x REAL,y REAL,Location TEXT,
                        Credit TEXT,WIC TEXT,WICcash TEXT,SFMNP TEXT,SNAP TEXT,Organic TEXT,
                        Bakedgoods TEXT,Cheese TEXT,Crafts TEXT,Flowers TEXT,Eggs TEXT,Seafood TEXT,Herbs TEXT,Vegetables TEXT,
                        Honey TEXT,Jams TEXT,Maple TEXT,Meat TEXT,Nursery TEXT,
                        Nuts TEXT,Plants TEXT,Poultry TEXT,Prepared TEXT,Soap TEXT,Trees TEXT,Wine TEXT,Coffee TEXT,
                        Beans TEXT,Fruits TEXT,Grains TEXT,Juices TEXT,Mushrooms TEXT,PetFood TEXT,Tofu TEXT,WildHarvested TEXT,updateTime TEXT)''')
        self.conn.commit()

    def load_data(self):
        df = pd.read_csv(self.csv_file, delimiter=',')
        df = df.fillna('No data')
        df.to_sql('farmers_market', self.conn,
                  if_exists='replace', index=False)

    # def view_all(self, page):
    #     page_size = 10
    #     offset = (page - 1) * page_size
    #     query = f"SELECT * FROM farmers_market LIMIT {page_size} OFFSET {offset}"
    #     self.c.execute(query)
    #     rows = self.c.fetchall()
    #     for row in rows:
    #         print(row)

    # def view_all(self, page):
    #     page_size = 10
    #     offset = (page - 1) * page_size
    #     query = f"SELECT * FROM farmers_market LIMIT {page_size} OFFSET {offset}"
    #     self.c.execute(query)
    #     rows = self.c.fetchall()
    #     df = pd.DataFrame(rows, columns=[desc[0]
    #                       for desc in self.c.description])
    #     print(df)
    def view_all(self, page, columns=None):
        page_size = 10
        offset = (page - 1) * page_size
        if columns is None:
            query = f"SELECT * FROM farmers_market LIMIT {page_size} OFFSET {offset}"
        else:
            cols = ', '.join(columns)
            query = f"SELECT {cols} FROM farmers_market LIMIT {page_size} OFFSET {offset}"
        self.c.execute(query)
        try:
            rows = self.c.fetchall()
            df = pd.DataFrame(
                rows, columns=[desc for desc in self.c.description])
            print(df)
        except sqlite3.OperationalError as e:
            print(e, 'Ошибка ввода')

    def search_by_city_state(self, city, state, radius):
        query = f"SELECT * FROM farmers_market WHERE city='{city}' AND State='{state}'"
        self.c.execute(query)
        rows = self.c.fetchall()
        results = []
        for row in rows:
            location = (row[-4], row[-3])
            distance = geodesic(location, (city, state)).miles
            if distance <= radius:
                results.append(row)
        return results

    def search_by_zip(self, zip_code, radius):
        query = f"SELECT * FROM farmers_market WHERE zip='{zip_code}'"
        self.c.execute(query)
        rows = self.c.fetchall()
        results = []
        for row in rows:
            location = (row[-4], row[-3])
            distance = geodesic(location, zip_code).miles
            if distance <= radius:
                results.append(row)
        return results

    def view_details(self, fmid):
        query = f"SELECT * FROM farmers_market WHERE FMID={fmid}"
        self.c.execute(query)
        try:
            row = self.c.fetchone()
            df = pd.DataFrame(
                [row], columns=[desc for desc in self.c.description])
            print(df.to_string(index=False, header=False))
        except ValueError as e:
            print(e, 'Ошибка ввода')

    def __del__(self):
        self.conn.close()
