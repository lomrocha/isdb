from control \
  import app
from flask \
  import request, render_template
from dao \
  import tv_show_dao, director_dao, cast_dao, episode_dao


@app.route("/")
def tv_shows():
  tv_shows_data = tv_show_dao.get_tv_shows(app)

  return render_template("index.html", tv_shows=tv_shows_data)


@app.route("/register_tv_show")
def register_tv_show():
  tv_show_name = request.args.get("tv_show_name")
  tv_show_genre = request.args.get("tv_show_genre")
  tv_show_poster = request.args.get("tv_show_poster")
  tv_show_description = request.args.get("tv_show_description")

  tv_show_dao.register_tv_show(app, tv_show_name, tv_show_genre, tv_show_poster, tv_show_description)

  return render_template("registered.html", type='seriado', name=tv_show_name)


@app.route("/delete_tv_show")
def delete_tv_show():
  id_tv_show = request.args.get("id_tv_show")

  tv_show_dao.delete_tv_show(app, id_tv_show)

  return render_template("deleted.html", type="seriado")


@app.route("/tv_show_data")
def tv_show_data_detail():
  id_tv_show = request.args.get("id_tv_show")

  tv_show = tv_show_dao.get_tv_show(app, id_tv_show)

  ids_directors = tv_show_dao.get_tv_show_directors_ids(app, id_tv_show)
  ids_cast = tv_show_dao.get_tv_show_cast_members_ids(app, id_tv_show)
  ids_episodes = tv_show_dao.get_tv_show_episodes_ids(app, id_tv_show)

  directors = director_dao.get_directors(app, ids_directors)
  cast_members = cast_dao.get_cast_members(app, ids_cast)
  episodes = episode_dao.get_episodes(app, ids_episodes)

  return render_template("tv_show_data.html",
                         tv_show=tv_show,
                         directors=directors,
                         cast_members=cast_members,
                         episodes=episodes)
