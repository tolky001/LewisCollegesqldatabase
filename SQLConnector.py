# pip install pymysql
import pymysql.cursors
HOSTNAME = 'sql5.freesqldatabase.com'
HOSTPORT = 3306
HOSTUSER = 'sql5523983'
HOSTPASS = 'cENxR9aXwn'
DBNAME = 'sql5523983'


class MySQLConnector:
    # constructor (connection)
    def __init__(self, dbName):
        connection = pymysql.connect(
            host = HOSTNAME,
            port = HOSTPORT,
            user = HOSTUSER, 
            password = HOSTPASS, 
            db = dbName,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True)
        self.connection = connection

    # query method
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                qry = query.lower()
                print("Running Query:", query)
                cursor.execute(query, data)
                if qry.find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif qry.find("select") >= 0 or "show tables" in qry:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
            finally:
                self.connection.close()


# fetch a MySQLConnector instance
def connectSQL(dbName=None):
    if (dbName==None): dbName = DBNAME
    return MySQLConnector(dbName)

# run a quick query on database
def querySQL(query, data=None, dbName=None):
    if (dbName==None): dbName = DBNAME
    return MySQLConnector(dbName).query_db(query,data)