from control \
  import app
from flask \
  import request, render_template
from dao \
  import episode_dao


@app.route("/register_episode")
def register_episode():
  episode_name = request.args.get("episode_name")
  episode_season = request.args.get("episode_season")
  episode_original_air_date = request.args.get("episode_original_air_date")
  episode_id_tv_show = request.args.get("episode_id_tv_show")

  episode_dao.register_episode(app, episode_name, episode_season, episode_original_air_date, episode_id_tv_show)

  return render_template("registered.html", type="episódio", name=episode_name)


@app.route("/delete_episode")
def delete_episode():
  id_episode = request.args.get("id_episode")

  episode_dao.delete_episode(app, id_episode)

  return render_template("deleted.html", type="episódio")


@app.route("/search_episode")
def search_episode():
  search = request.args.get("search")

  data = episode_dao.get_episodes_by_search(app, search)

  return render_template("search_templates/search_episode.html", data=data)
