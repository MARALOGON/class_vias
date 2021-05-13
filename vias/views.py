from vias import app
import csv
import json
#Un fichero .json es un fichero en texto plano

@app.route("/provincias")#app.route muestra la ruta 
def provincias():
    #1. abrir el archivo
    fichero = open("data/provincias.csv", "r")
    #2. leer cada registro del archivo
    csvreader = csv.reader(fichero, delimiter=",") #Delimiter indica el caracter que delimita las entradas del registro, en este caso está separada por comas (csv = coma separated values)
    #3. procesar el fichero y darle el formato que necesitamos para que lo lea el navegador, que es un diccionario
    lista = []
    for registro in csvreader:
        d = {'codigo': registro[0], 'valor':registro[1]}
        lista.append(d)
    #4. cerrar fichero
    fichero.close()
    #5. pasar el diccionario a un archivo .json
    #6. devolver el .json
    print(lista)
    return json.dumps(lista)


@app.route("/provincia/<codigoProvincia>") #Para meter un parametro aqui se hace entre los simbolos mayor-menor
def laprovincia(codigoProvincia):
    fichero = open("data/provincias.csv", "r")
    dictreader = csv.DictReader(fichero, fieldnames=["codigo","provincia"])

    for registro in dictreader:
        if registro['codigo'] == codigoProvincia:
            return registro['provincia']
    
    fichero.close()
    return "La provincia no existe"

@app.route("/vias/<int:year>/<int:mes>", defaults=('dia':None))#Este defaults es para limitar la busqueda a solo determinados parametros
@app.route("/vias/<int:year>/", defaults=('mes':None, 'dia':None))
@app.route("/vias/<int:year>/<int:mes>/<int:dia>") #Poner el int delante de los parametros fuerza a que las peticiones (entrada de datos) sean correctas.
def casos(year, mes, dia):
pass

'''
1er caso: devolver el numero total de vias en un dia del año determinado para atoadas las provincias
2do caso: Lo mismo pero detallado por grados: V, 6, 7, 8, 9 en formato .json
'''