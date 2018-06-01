from dao \
  import connection_dao
from model \
  import cast_model


def get_cast_member(file, id_cast):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT name, date_of_birth, place_of_birth, picture FROM isdb.cast WHERE id_cast = '{id_cast}'"
  cursor.execute(query)

  data = cursor.fetchone()

  cast_member = cast_model.Cast(id_cast,
                                data[0],
                                data[1],
                                data[2],
                                data[3])

  connection.close()

  return cast_member


def get_cast_members(file, ids_cast):
  connection, cursor = connection_dao.get_connection(file)

  ids_list = [i for i, in ids_cast]

  cast_members = []
  for id_c in ids_list:
    query = f"SELECT name, date_of_birth, place_of_birth, picture FROM isdb.cast WHERE id_cast = '{id_c}'"
    cursor.execute(query)

    data = cursor.fetchone()

    _cast_member = cast_model.Cast(id_c,
                                   data[0],
                                   data[1],
                                   data[2],
                                   data[3])

    cast_members.append(_cast_member)

  connection.close()

  return cast_members


def register_cast_member(file, cast_name, cast_date_of_birth, cast_place_of_birth, cast_picture):
  connection, cursor = connection_dao.get_connection(file)

  query = f"INSERT INTO isdb.cast (name, date_of_birth, place_of_birth, picture) " \
          f"VALUES ('{cast_name}', '{cast_date_of_birth}', '{cast_place_of_birth}', '{cast_picture}')"

  cursor.execute(query)
  connection.commit()


def delete_cast_member(file, id_cast_member):
  connection, cursor = connection_dao.get_connection(file)

  query = f"DELETE FROM isdb.cast WHERE id_cast = {id_cast_member}"

  cursor.execute(query)
  connection.commit()


def get_cast_members_by_search(file, search):
  connection, cursor = connection_dao.get_connection(file)

  query = f"SELECT id_cast, name, date_of_birth, place_of_birth, picture FROM isdb.cast " \
          f"WHERE name LIKE '%{search}%' " \
          f"OR place_of_birth LIKE '%{search}%'"
  cursor.execute(query)

  data = cursor.fetchall()

  cast_members = []
  for cast_member in data:
    _cast_member = cast_model.Cast(cast_member[0],
                                   cast_member[1],
                                   cast_member[2],
                                   cast_member[3],
                                   cast_member[4])

    cast_members.append(_cast_member)

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
