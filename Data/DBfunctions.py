import pickledb

db_connection = pickledb.load('keys.db', True)


def setkey_db(key, value):
    db_connection.set(key, value)


def getkey_db(key):
    return db_connection.get(key)


def delkey_db(key):
    return db_connection.rem(key)


def getallkey_db():
    return db_connection.getall()


def delete_db():
    return db_connection.deldb()
