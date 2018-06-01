from control \
  import app
from flask \
  import request, render_template
from dao \
  import director_dao


@app.route("/register_director")
def register_director():
  director_name = request.args.get("director_name")
  director_date_of_birth = request.args.get("director_date_of_birth")
  director_place_of_birth = request.args.get("director_place_of_birth")
  director_picture = request.args.get("director_picture")

  director_dao.register_director(app,
                                 director_name,
                                 director_date_of_birth,
                                 director_place_of_birth,
                                 director_picture)

  return render_template("registered.html", type="diretor", name=director_name)


@app.route("/delete_director")
def delete_director():
  id_director = request.args.get("id_director")

  director_dao.delete_director(app, id_director)

  return render_template("deleted.html", type="diretor")


@app.route("/search_director")
def search_director():
  search = request.args.get("search")

  data = director_dao.get_directors_by_search(app, search)

  return render_template("search_templates/search_director.html", data=data)
