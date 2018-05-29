from control \
  import app
from flask \
  import request, render_template
from dao \
  import cast_dao


@app.route("/cast_member_data")
def cast_member_data_detail():
  id_cast = request.args.get("id_cast")

  cast_member = cast_dao.get_cast_member(app, id_cast)

  return render_template("cast_member_data.html", cast_member=cast_member)
