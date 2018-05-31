from control \
  import app
from flask \
  import request, render_template
from dao \
  import tv_show_cast_episode_dao


@app.route("/register_tv_show_cast_episode")
def register_tv_show_cast_episode():
  ids_episode = request.args.getlist("id_episode")
  id_tv_show = request.args.get("id_tv_show")
  id_cast_member = request.args.get("id_cast_member")
  cast_member_name = request.args.get("cast_member_name")

  tv_show_cast_episode_dao.register_tv_show_cast_episode(app,
                                                         ids_episode,
                                                         id_tv_show,
                                                         id_cast_member)

  return render_template("registered.html", type="elenco", name=cast_member_name)

