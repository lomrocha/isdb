from dao \
  import connection_dao


def register_tv_show_cast_episode(file, ids_episode, id_tv_show, id_cast_member):
  connection, cursor = connection_dao.get_connection(file)

  for id_episode in ids_episode:
    query = f"INSERT INTO isdb.cast_tvshows (id_tv_show, id_cast, id_episode)" \
            f"VALUES ({id_tv_show}, {id_cast_member}, {id_episode})"

    cursor.execute(query)
    connection.commit()

  connection.close()
