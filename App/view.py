import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from time import process_time 
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def initCatalo():
    return controller.initcatalog()
def intiCategoria():
    return controller.intiCategoria()

def loadData():
    controller.loaddata(catalog)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos por categoria y pais ")
    print("3- Video tendencia por pais")
    print("4- Video tendencia por categoria")
    print ("5- Video por mas likes")

catalog = None
Categoria=None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initcatalog()
        #print("Se cargo la informacion del catalogo")
        #print("se cargaron:" +str(lt.size(catalog["videos"]))+ "videos")
        print(catalog["views"])
sys.exit(0)