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
