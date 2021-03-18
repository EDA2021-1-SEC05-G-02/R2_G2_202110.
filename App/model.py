import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf

def newCatalog():
    catalog = {'title': None,
                'channel_title': None,
                'views': None,
                'likes': None,
                'dislikes': None,
                "categoria":None}

    catalog['title'] = lt.newList('SINGLE_LINKED', compareVideosIds)
    catalog['channel_title'] = lt.newList('SINGLE_LINKED', compareVideosIds)
    catalog['views'] = mp.newMap(375943,
                                maptype='CHAINING',
                                loadfactor=4.0,
                                comparefunction=compareVideosIds)
    catalog['likes'] = mp.newMap(375943,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareVideosIds)
    catalog['dislikes'] = mp.newMap(375943,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareVideosIds)
    catalog["categoria"] = mp.newMap(375943,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareVideosIds)
    return catalog

def addVideoDetails(catalog, video):
    lt.addLast(catalog['title'], video)
    mp.put(catalog['title'], video["video_id"], video)
def addMovieCasting(catalog, video):
    lt.addLast(catalog['channel_title'],video)
    mp.put(catalog['channel_title'], video['video_id'], video)
def compareVideosIds(id1, id2):
    if (int(id1) == int(id2)):
        return 0
    elif int(id1) > int(id2):
        return 1
    else:
        return -1
def requerimiento1(categoria,catalog,n):
    valor_a_busar=[]
    for i in categoria["categorias"]["elements"]:
        for k,v in i.items():
            if categoria in v:
                valor_a_busar.append(v)
    valor=valor_a_busar[0][0:2]

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
