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

def retrieve_table_data(cursor, query, colNames, log):
    cursor.execute(query)

    output = []

    for row in cursor:
        rowData = []

        for name in colNames:
            # Replace nulls with blank strings to allow proper 
            # entry generation in program
            text = row[name] if row[name] else ""
            rowData.append(text)

        output.append(rowData)

    return output