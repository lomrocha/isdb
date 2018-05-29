from dao \
  import connection_dao
from model \
  import cast_model


def get_cast_member(file, id_cast):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT name, date_of_birth, place_of_birth FROM isdb.cast WHERE id_cast = '{id_cast}'"
  cursor.execute(query)

  data = cursor.fetchone()

  cast_member = cast_model.Cast(id_cast,
                                data[0],
                                data[1],
                                data[2])

  connection.close()

  return cast_member


def get_cast_members(file, ids_cast):
  connection, cursor = connection_dao.get_connection(file)

  ids_list = [i for i, in ids_cast]

  cast_members = []
  for id_c in ids_list:
    query = f"SELECT name, date_of_birth, place_of_birth FROM isdb.cast WHERE id_cast = '{id_c}'"
    cursor.execute(query)

    data = cursor.fetchone()

    _cast_member = cast_model.Cast(id_c,
                                   data[0],
                                   data[1],
                                   data[2])

    cast_members.append(_cast_member)

  connection.close()

  return cast_members


def get_cast_member_tv_shows_ids(file, id_cast):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_tv_show FROM isdb.cast_tvshows WHERE id_cast = {id_cast}"
  cursor.execute(query)

  cast_member_data = cursor.fetchall()

  connection.close()

  return cast_member_data


def get_cast_member_episodes_ids(file, id_cast):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_episode FROM isdb.cast_tvshows WHERE id_cast = {id_cast}"
  cursor.execute(query)

  cast_member_data = cursor.fetchall()

  connection.close()

  return cast_member_data
