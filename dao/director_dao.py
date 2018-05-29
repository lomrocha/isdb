from dao \
  import connection_dao
from model \
  import director_model


def get_director(file, id_director):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT name, date_of_birth, place_of_birth FROM isdb.director WHERE id_director = '{id_director}'"
  cursor.execute(query)

  data = cursor.fetchone()

  _director = director_model.Director(id_director,
                                      data[0],
                                      data[1],
                                      data[2])

  connection.close()

  return _director


def get_directors(file, ids_director):
  connection, cursor = connection_dao.get_connection(file)

  id_list = [i for i, in ids_director]

  directors = []
  for id_d in id_list:
    query = f"SELECT name, date_of_birth, place_of_birth FROM isdb.director WHERE id_director = '{id_d}'"
    cursor.execute(query)

    data = cursor.fetchone()

    _director = director_model.Director(id_d,
                                        data[0],
                                        data[1],
                                        data[2])

    directors.append(_director)

  connection.close()

  return directors


def get_director_tv_shows_ids(file, id_director):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_tv_show FROM isdb.directors_tvshow WHERE id_director = {id_director}"
  cursor.execute(query)

  director_data = cursor.fetchall()

  connection.close()

  return director_data


def get_director_episodes_ids(file, id_director):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_episode FROM isdb.directors_tvshow WHERE id_director = {id_director}"
  cursor.execute(query)

  director_data = cursor.fetchall()

  connection.close()

  return director_data
