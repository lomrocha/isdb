from dao \
  import connection_dao
from model \
  import episode_model


def get_episode(file, id_episode):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT name, season, original_air_date " \
          f"FROM isdb.episodes WHERE id_episode = '{id_episode}'"
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
    query = f"SELECT id_tv_show, name, season, original_air_date " \
            f"FROM isdb.episodes WHERE id_episode = '{id_e}'"
    cursor.execute(query)

    data = cursor.fetchone()

    episode = episode_model.Episode(id_e,
                                    data[0],
                                    data[1],
                                    data[2],
                                    data[3])

    episodes.append(episode)

  connection.close()

  return episodes


def get_seasons(file, id_tv_show):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT DISTINCT (season) FROM isdb.episodes WHERE id_tv_show = '{id_tv_show}'"
  cursor.execute(query)

  data = cursor.fetchall()

  seasons_list = [i for i, in data]

  connection.close()

  return seasons_list


def register_episode(file, episode_name, episode_season, episode_original_air_date, episode_id_tv_show):
  connection, cursor = connection_dao.get_connection(file)

  query = f"INSERT INTO isdb.episodes (id_tv_show, name, season, original_air_date)" \
          f"VALUES ({episode_id_tv_show}, '{episode_name}', '{episode_season}', '{episode_original_air_date}')"

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
