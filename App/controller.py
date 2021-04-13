import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def cargardatosvideoslarge():
    vfile = cf.data_dir + 'videos/videos-large.csv'
    reader = csv.DictReader(open(vfile,encoding="utf-8"))
    dict_list = []
    for line in reader:
        dict_list.append(dict(line))
    return dict_list
def cargarCategorias():
    vfile = cf.data_dir + 'videos/category-id.csv'
    reader = csv.DictReader(open(vfile,encoding="utf-8"))
    cat = []
    for line in reader:
        cat.append(dict(line))
    return cat
def newCatalog():
    catalog=model.newCatalog()
    return catalog
def primer_requerimiento(categoria,catalogo,country,categoria_buscar,n):
    return model.primer_requerimiento(cargarCategorias_1(),cargar_videos(),country,categoria_buscar,n)

def segundo_requerimiento(catalog,country):
    return model.segundo_requerimiento(cargar_videos(),country)

def tercer_requerimiento(categoria,catalogo,category_name):
    return model.tercer_requerimiento(cargarCategorias_1(),cargar_videos(),category_name)

def cuarto_requerimiento(catalogo,tag_a_buscar,n,country):
    return model.cuarto_requerimiento(cargar_videos(),tag_a_buscar,n,country)

def cargar_videos():
    return model.cargardatosvideoslarge()

def cargarCategorias_1():
    return model.cargarCategorias()