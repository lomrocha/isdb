from flaskext.mysql \
  import MySQL


def get_connection(file):
  file.config["MYSQL_DATABASE_USER"] = "root"
  file.config["MYSQL_DATABASE_PASSWORD"] = "root"
  file.config["MYSQL_DATABASE_DB"] = "isdb"

  mysql = MySQL(file)
  mysql.init_app(file)

  connection = mysql.connect()
  cursor = connection.cursor()

  return connection, cursor
