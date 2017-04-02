class DB(object):
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

def setup_db_connection(conf, log):
    """Sets up MySQL database connections and cursor"""
    import pymysql.cursors

    db = conf.get("mysql", "db")
    host = conf.get("mysql", "host")
    user = conf.get("mysql", "user")
    pw = conf.get("mysql", "password")

    try:
        connection = pymysql.connect(host=host, 
                                     user=user, 
                                     password=pw, 
                                     db=db, 
                                     charset="utf8",
                                     cursorclass=pymysql.cursors.DictCursor)
    except:
        log.exception("Unable to connect to database")
        connection = None

    try:
        cursor = connection.cursor()
    except:
        log.exception("Unable to establish database cursor")
        cursor = None

    db = DB(connection, cursor)

    return db

def retrieve_table_data(cursor, log):
    s = ("SELECT bsrf, brand_name, strength, route, dosage_form "
         "FROM abc_subs_bsrf ORDER BY bsrf ASC LIMIT 10")
    cursor.execute(s)

    output = []

    for row in cursor:
        output.append([row["bsrf"], row["brand_name"], row["strength"], 
                       row["route"], row["dosage_form"]])

    return output