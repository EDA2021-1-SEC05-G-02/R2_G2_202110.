import config as cf
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def initcatalog():
    catalog = model.newCatalog()
    return catalog
#<<<<<<< HEAD
def loaddata(catalog,Categoria):
    cargardatosvideoslarge(catalog)
    vfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for video in input_file:
        model.addVideoDetails(catalog, video)
def cargardatosvideoslarge(catalog):
    vfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for videol in input_file:
        model.addVideoDetails(catalog, videol)
"""def requerimiento1(category_name,country,n,catalog,Categoria):
    return model.requerimiento1(category_name,country,n,catalog,Categoria)

def requerimiento2(catalog,country):
    return model.requerimiento2(catalog,country)

def requerimiento3(catalog,Categoria,categoria):
    return model.requerimiento3(catalog,Categoria,categoria)
    
def requerimiento4(catalog,tag,country):
    return model.requerimiento4(catalog,tag,country)"""


# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
