import contextlib
import sqlite3

@contextlib.contextmanager
def sqlite3_connection(db_name):
    connection = sqlite3.connect(db_name)
    yield connection
    connection.close()


with sqlite3_connection('dhcp_snooping.db') as conn:
    for row in conn.execute('select * from dhcp'):
        print(row)

conn.in_transaction


with contextlib.closing(sqlite3.connect('dhcp_snooping.db')) as conn:
    for row in conn.execute('select * from dhcp'):
        print(row)

conn.in_transaction

