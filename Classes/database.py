import sqlite3
import pandas as pd
import os


class Database:

    def readApplicationData(self):
        applications = pd.read_csv("./data/applications.csv")
        return applications

    def readFitnessTest(self):
        fitness_tests = pd.read_csv("./data/fitness_tests.csv")
        return fitness_tests

    def readPurchases(self):
        purchases = pd.read_csv("./data/purchases.csv")
        return purchases

    def readVisits(self):
        visits = pd.read_csv("./data/visits.csv")
        return visits

    def buildDb(self):
        if os.path.exists('example.db'):
            os.remove('example.db')
    
    def createDb(self):
        conn = sqlite3.connect('example.db')
        return conn

    def buildTable(self, visits, fitness_tests, applications, purchases, conn):
        visits.to_sql('visits', conn, dtype = {
            'firt_name':'VARCHAR(256)',
            'last_naem':'VARCHAR(256)',
            'email':'VARCHAR(256)',
            'visits_date':'DATE'
        })
        fitness_tests.to_sql('fitness_tests', conn, dtype = {
            'firt_name':'VARCHAR(256)',
            'last_naem':'VARCHAR(256)',
            'email':'VARCHAR(256)',
            'gender': 'VARCHAR(256)',
            'fitness_test_date':'DATE'
        })
        applications.to_sql('applications', conn, dtype = {
            'firt_name':'VARCHAR(256)',
            'last_naem':'VARCHAR(256)',
            'email':'VARCHAR(256)',
            'gender': 'VARCHAR(256)',
            'application_date':'DATE'
        })
        purchases.to_sql('purchases', conn, dtype = {
            'firt_name':'VARCHAR(256)',
            'last_naem':'VARCHAR(256)',
            'email':'VARCHAR(256)',
            'gender': 'VARCHAR(256)',
            'purchases_date':'DATE'
        })

    def sql_query(self,query,conn):
            try:
                df = pd.read_sql(query, conn)
            except Exception as e:
                print(e.message)
            return df        

    @staticmethod
    def run_database():
        db = Database()
        app = db.readApplicationData()
        fit = db.readFitnessTest()
        pur = db.readPurchases()
        vis = db.readVisits()
        db.buildDb()
        conn = db.createDb()
        db.buildTable(vis,fit,app,pur,conn)
        q1 = "SELECT * FROM visits LIMIT 5 "
        #print(db.sql_query(q1,conn))

        return conn
    
 




    