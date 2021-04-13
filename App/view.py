import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from time import process_time 

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

videos="videos/videos-large.csv"

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
        catalog=controller.cargar_videos()
        Categoria=controller.cargarCategorias_1()
        print("Se cargaron :"+str(len(catalog))+" videos.")
        print("Se cargaron: "+str(len(Categoria))+" categorías.")

    elif int(inputs[0]) == 2:
        categoria_a_buscar=input("Deme una categoria: ")
        country=input("Deme un país: ")
        n=int(input("Deme ranking: ")) 
        lista=controller.primer_requerimiento(Categoria,catalog,country,categoria_a_buscar,n)
        for i in lista:
            for k,v in i.items():
                if k=="trending_date":
                    print("trending_date: ",v)
                elif k=="title":
                    print("title: ",v)
                elif k=="channel_title":
                    print("channel_title: ",v)
                elif k=="publish_time":
                    print("publish_time: ",v)
                elif k=="views":
                    print("views: ",v)
                elif k=="likes":
                    print("likes: ",v)
                elif k=="dislikes":
                    print("dislikes: ",v)

    elif int(inputs[0]) == 3:
        country=input("Dame el país: ")
        tupla=controller.segundo_requerimiento(catalog,country)
        for k,v in tupla[0].items():
            if k=="title":
                    print("title: ",v)
            elif k=="channel_title":
                    print("channel_title: ",v)
            elif k=="country":
                print("country: ",v)
        print("Días que fue tendencia: "+str(tupla[1]))

    elif int(inputs[0]) == 4:
        category_name=input("Deme la categoría: ")
        tupla=controller.tercer_requerimiento(Categoria,catalog,category_name)
        for k,v in tupla[0].items():
            if k=="title":
                    print("title: ",v)
            elif k=="channel_title":
                    print("channel_title: ",v)
            elif k=="category_id":
                print("Category_id: ",v)
        print("Días que fue tendencia: "+str(tupla[1]))

    elif int(inputs[0])==5:
        tag_a_buscar=input("Deme un tag a buscar: ")
        n=int(input("Deme el ranking: "))
        country=input("Deme el país: ")
        lista=controller.cuarto_requerimiento(catalog,tag_a_buscar,n,country)
        for i in lista:
            for k,v in i.items():
                if k=="title":
                    print("title: ",v)
                elif k=="channel_title":
                    print("channel_title: ",v)
                elif k=="publish_time":
                    print("publish_time: ",v)
                elif k=="views":
                    print("views: ",v)
                elif k=="likes":
                    print("likes: ",v)
                elif k=="dislikes":
                    print("dislikes: ",v)
                elif k=="tags":
                    print("Tags: ",v)
    else:
        sys.exit(0)
sys.exit(0)