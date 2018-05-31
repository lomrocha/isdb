from dao \
  import connection_dao
from model \
  import tv_show_model


def get_tv_show(file, id_tv_show):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT name, genre, poster, description FROM isdb.tvshows WHERE id_tv_show = {id_tv_show}"
  cursor.execute(query)

  data = cursor.fetchone()

  tv_show = tv_show_model.TvShow(id_tv_show,
                                 data[0],
                                 data[1],
                                 data[2],
                                 data[3])

  connection.close()

  return tv_show


def get_tv_shows(file):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_tv_show, name, genre, poster, description FROM isdb.tvshows"
  cursor.execute(query)

  data = cursor.fetchall()

  tv_shows = []
  for tv_show in data:
    _tv_show = tv_show_model.TvShow(tv_show[0],
                                    tv_show[1],
                                    tv_show[2],
                                    tv_show[3],
                                    tv_show[4])

    tv_shows.append(_tv_show)

  connection.close()

  return tv_shows


def register_tv_show(file, tv_show_name, tv_show_genre, tv_show_poster, tv_show_description):
  connection, cursor = connection_dao.get_connection(file)

  query = f"INSERT INTO isdb.tvshows (name, genre, poster, description) " \
          f"VALUES ('{tv_show_name}', '{tv_show_genre}', '{tv_show_poster}', '{tv_show_description}')"

  cursor.execute(query)
  connection.commit()


def delete_tv_show(file, id_tv_show):
  connection, cursor = connection_dao.get_connection(file)

  query = f"DELETE FROM isdb.tvshows WHERE id_tv_show = {id_tv_show}"

  cursor.execute(query)
  connection.commit()


def get_tv_shows_by_genre(file, tv_show_genre):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_tv_show, name, poster, description FROM isdb.tvshows WHERE genre = '{tv_show_genre}'"
  cursor.execute(query)

  data = cursor.fetchall()

  tv_shows = []
  for tv_show in data:
    _tv_show = tv_show_model.TvShow(tv_show[0],
                                    tv_show[1],
                                    tv_show_genre,
                                    tv_show[2],
                                    tv_show[3])

    tv_shows.append(_tv_show)

  connection.close()

  return tv_shows


def get_tv_show_directors_ids(file, id_tv_show):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_director FROM isdb.directors_tvshows WHERE id_tv_show = {id_tv_show}"
  cursor.execute(query)

  tv_show_data = cursor.fetchall()

  connection.close()

  return tv_show_data


def get_tv_show_cast_members_ids(file, id_tv_show):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_cast FROM isdb.cast_tvshows WHERE id_tv_show = '{id_tv_show}'"
  cursor.execute(query)

  tv_show_data = cursor.fetchall()

  connection.close()

  return tv_show_data


def get_tv_show_episodes_ids(file, id_tv_show):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_episode FROM isdb.episodes WHERE id_tv_show = {id_tv_show}"
  cursor.execute(query)

  tv_show_data = cursor.fetchall()

  connection.close()

  return tv_show_data
