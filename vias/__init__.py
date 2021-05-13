from flask import Flask

app = Flask(__name__)

from vias import views #nos traemos las rutas de views despues de importar la app
