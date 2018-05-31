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
    episodes = episode_dao.get_episodes(app, ids_episode)
    tv_show_dictionary['%s' % tv_show.name] = episodes
    seasons = episode_dao.get_seasons(app, tv_show.id_tv_show)
    season_dictionary['%s' % tv_show.name] = seasons

  cast_member = cast_dao.get_cast_member(app, id_cast)

  return render_template("cast_member_data.html",
                         cast_member=cast_member,
                         tv_shows=tv_shows,
                         tv_show_dictionary=tv_show_dictionary,
                         season_dictionary=season_dictionary)


@app.route("/register_cast_member")
def register_cast_member():
  cast_name = request.args.get("cast_member_name")
  cast_date_of_birth = request.args.get("cast_member_date_of_birth")
  cast_place_of_birth = request.args.get("cast_member_place_of_birth")

  cast_dao.register_cast_member(app, cast_name, cast_date_of_birth, cast_place_of_birth)

  return render_template("registered.html", type="elenco", name=cast_name)


@app.route("/delete_cast_member")
def delete_cast_member():
  id_cast_member = request.args.get("id_cast_member")

  cast_dao.delete_cast_member(app, id_cast_member)

  return render_template("deleted.html", type="elenco")
