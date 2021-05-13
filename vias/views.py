from vias import app

@app.route("/")
def vias():
    return "Flask esta funcionando desde views"