from dao \
  import connection_dao
from model \
  import episode_model


def get_episode(file, id_episode):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT name, season, year FROM isdb.episodes WHERE id_episode = '{id_episode}'"
  cursor.execute(query)

  data = cursor.fetchone()

  episode = episode_model.Episode(id_episode,
                                  data[0],
                                  data[1],
                                  data[2])

  connection.close()

  return episode


def get_episodes(file, ids_episode):
  connection, cursor = connection_dao.get_connection(file)

  id_list = [i for i, in ids_episode]

  episodes = []
  for id_e in id_list:
    query = f"SELECT name, season, year FROM isdb.episodes WHERE id_episode = '{id_e}'"
    cursor.execute(query)

    data = cursor.fetchone()

    episode = episode_model.Episode(id_e,
                                    data[0],
                                    data[1],
                                    data[2])

    episodes.append(episode)

  connection.close()

  return episodes


def register_episode(file, episode_name, episode_season, episode_year):
  connection, cursor = connection_dao.get_connection(file)

  query = f"INSERT INTO isdb.episode (name, season, year) " \
          f"VALUES ('{episode_name}', '{episode_season}', '{episode_year}')"

  cursor.execute(query)
  connection.commit()


def delete_episode(file, id_episode):
  connection, cursor = connection_dao.get_connection(file)

  query = f"DELETE FROM isdb.episode WHERE id_episode = {id_episode}"

  cursor.execute(query)
  connection.commit()


def get_tv_show_directors_ids(file, id_episode):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_director FROM isdb.directors_tvshow WHERE id_episode = {id_episode}"
  cursor.execute(query)

  episodes_data = cursor.fetchall()

  connection.close()

  return episodes_data


def get_episode_cast_members_id(file, id_episode):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_cast FROM isdb.cast_tvshows WHERE id_episode = {id_episode}"
  cursor.execute(query)

  episodes_data = cursor.fetchall()

  connection.close()

  return episodes_data


def get_episode_tv_show_id(file, id_episode):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_tvshow FROM isdb.cast_tvshows WHERE id_episode = {id_episode}"
  cursor.execute(query)

  episodes_data = cursor.fetchall()

  connection.close()

  return episodes_data
