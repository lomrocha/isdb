from control \
  import app
from flask \
  import request, render_template
from dao \
  import cast_dao, episode_dao, tv_show_dao


@app.route("/cast_member_data")
def cast_member_data_detail():
  id_cast = request.args.get("id_cast")

  tv_shows = tv_show_dao.get_tv_shows(app)
  tv_show_dictionary = {}
  season_dictionary = {}
  for tv_show in tv_shows:
    ids_episode = tv_show_dao.get_tv_show_episodes_ids(app, tv_show.id_tv_show)
    _episodes = episode_dao.get_episodes(app, ids_episode)
    tv_show_dictionary['%s' % tv_show.name] = _episodes
    seasons = episode_dao.get_seasons(app, tv_show.id_tv_show)
    season_dictionary['%s' % tv_show.name] = seasons

  cast_member = cast_dao.get_cast_member(app, id_cast)
  ids_e = cast_dao.get_cast_member_episodes_ids(app, id_cast)
  episodes = episode_dao.get_episodes(app, ids_e)

  episodes_names = []
  for episode in episodes:
    episodes_names.append(episode.name)

  return render_template("cast_member_data.html",
                         cast_member=cast_member,
                         episodes=episodes,
                         episodes_names=episodes_names,
                         tv_shows=tv_shows,
                         tv_show_dictionary=tv_show_dictionary,
                         season_dictionary=season_dictionary)


@app.route("/register_cast_member")
def register_cast_member():
  cast_name = request.args.get("cast_member_name")
  cast_date_of_birth = request.args.get("cast_member_date_of_birth")
  cast_place_of_birth = request.args.get("cast_member_place_of_birth")
  cast_picture = request.args.get("cast_member_picture")

  cast_dao.register_cast_member(app, cast_name, cast_date_of_birth, cast_place_of_birth, cast_picture)

  return render_template("registered.html", type="elenco", name=cast_name)


@app.route("/delete_cast_member")
def delete_cast_member():
  id_cast_member = request.args.get("id_cast_member")

  cast_dao.delete_cast_member(app, id_cast_member)

  return render_template("deleted.html", type="elenco")


@app.route("/search_cast")
def search_cast():
  search = request.args.get("search")

  data = cast_dao.get_cast_members_by_search(app, search)

  return render_template("search_templates/search_cast.html", data=data)
