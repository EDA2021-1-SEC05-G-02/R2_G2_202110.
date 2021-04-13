import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as it
import csv
import controller 

def newCatalog():
    catalog = {'title': None,
                'channel_title': None,
                'views': None,
                'likes': None,
                'dislikes': None}
 
    catalog['title'] = lt.newList('SINGLE_LINKED', compareVideosIds)
    catalog['channel_title'] = lt.newList('SINGLE_LINKED', compareVideosIds)
    
    catalog['views'] = mp.newMap(375943,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareViews)
    catalog['likes'] = mp.newMap(375943,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=compareLikes)
    catalog['dislikes'] = mp.newMap(375943,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=compareDislikes)
    return catalog
def addVideoDetails(catalog, video):
    lt.addLast(catalog['title'], video)
    mp.put(catalog['title'], video["video_id"], video)
def addchannel_title(catalog, video):
    lt.addLast(catalog['channel_title'],video)
    mp.put(catalog['channel_title'], video['video_id'], video)
 
def compareVideosIds(id1, id2):
    if (int(id1) == int(id2)):
        return 0
    elif int(id1) > int(id2):
        return 1
    else:
        return -1
 
def compareLikes(like1, like2):
    if (int(like1) == int(like2)):
        return 0
    elif int(like1) > int(like2):
        return 1
    else:
        return -1
 
def compareDislikes(Dlike1, Dlike2):
    if (int(Dlike1) == int(Dlike2)):
        return 0
    elif int(Dlike1) > int(Dlike2):
        return 1
    else:
        return -1
 
def compareViews(view1, view2):
    if (int(view1) == int(view2)):
        return 0
    elif (int(view1) > int(view2)):
        return 1
    else:
        return 0
 
def compareCategoria(keyname, Categoria):
    catentry = me.getKey(Categoria)
    if (keyname == catentry):
        return 0
    elif (keyname > catentry):
        return 1
    else:
        return -1

def cargardatosvideoslarge():
    vfile = cf.data_dir + "videos/videos-large.csv"
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

def primer_requerimiento(categoria,catalogo,country,categoria_buscar,n):
    id_cat=0
    lista={"categorias":lt.newList("ARRAY_LIST")}
    a=[]
    for z in categoria:
        for k,v in z.items():
            if categoria_buscar in v:
                id_cat=v[0:4]
    for i in catalogo:
        for k,v in i.items():
            if (k=="category_id" and str(id_cat) in v):
                        a.append(i)
    for i in a:
        for k,v in i.items():
            if k=="country" and country in v:
                lt.addLast(lista["categorias"],i)
    newlist = sorted(lista["categorias"]["elements"], key=lambda k: int(k['views']),reverse=True)
    return newlist[:n]

def segundo_requerimiento(catalog,country):
    paises=[]
    for i in catalog:
        for k,v in i.items():
            if k=="country" and v in country:
                paises.append(i)
    nombres=[]
    dates=[]
    for i in paises:
        for k,v in i.items():
            if k=="title":
                nombres.append(v)
            if k=="trending_date":
                dates.append(v)
    dicts = {key: [] for key in nombres}
    for k, v in zip(nombres, dates):
        dicts[k].append(v)
    unicas_fechas=[]
    for key,value in dicts.items():
          unicas_fechas.append(set(value))
    duracion=[]
    for i in unicas_fechas:
        duracion.append(len(i))
    maximo=max(duracion)
    indice_mayor=duracion.index(maximo)
    return (paises[indice_mayor], maximo)

def tercer_requerimiento(categoria,catalogo,category_name):
    id_cat=0
    lista={"videos":lt.newList("ARRAY_LIST")}
    for z in categoria:
        for k,v in z.items():
            if category_name in v:
                id_cat=v[0:4]
    for i in catalogo:
        for k,v in i.items():
            if (k=="category_id" and str(id_cat) in v):
                 lt.addLast(lista["videos"],i)
    titulo=[]
    fechas=[]
    for i in lista["videos"]["elements"]:
        for k,v in i.items():
            if k=="title":
                titulo.append(v)
            elif k=="trending_date":
                fechas.append(v)
    dicts = {key: [] for key in titulo}
    for k, v in zip(titulo, fechas):
        dicts[k].append(v)
    unicas_fechas=[]
    for key,value in dicts.items():
          unicas_fechas.append(set(value))
    duracion=[]
    for i in unicas_fechas:
        duracion.append(len(i))
    maximo=max(duracion)
    indice_mayor=duracion.index(maximo)
    cont=0
    tupla=()
    for i in lista["videos"]["elements"]:
            if cont==indice_mayor:
                tupla=(i,maximo)
                cont+=1
            else:
                cont+=1
    return tupla

def cuarto_requerimiento(catalogo,tag_a_buscar,n,country):
    lista={"videos":lt.newList("ARRAY_LIST")}
    paises=[]
    for i in catalogo:
        for k,v in i.items():
            if k=="country" and country in v:
                paises.append(i)
    for i in paises:
        for k,v in i.items():
            if k=="tags" and tag_a_buscar in v:
                lt.addLast(lista["videos"],i)
    newlist = sorted(lista["videos"]["elements"], key=lambda k: int(k['likes']),reverse=True)
    return newlist[:n]