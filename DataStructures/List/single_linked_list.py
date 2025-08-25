def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }

    return newlist

#Punto 13
def get_element(my_list,pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]
                
def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element,temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count -= 1
    return count

#Punto tabla parte de abajo:
def is_empty(my_list):
    if my_list == []:
        return True
    else:
        return False

def size(newlist):
    """  
    Calcula el tamaño de la lista creada.
    
    """
    length = len(new_list)
    return length

def last_element(newlist):
    size = len(new_list)
    ultimo = new_list[size]
    return ultimo

def delete_element(newlist, palabra_clave,elemento):
    if newlist == []:
        return "No se puede eliminar ningún elemento porque es una lista vacia"
    
    elif palabra_clave == "eliminar": #Lo hice así, pero necesiuto que revisen, ya que no sé si hará una conexión para esto en la consola
        for i in list:
            if list[i] == elemento:
                new_list.remove(elemento)
    return elemento

def remove_first(newlist):
    if len == []:
        resp = "No hay nada que eliminar en una lista vacia"
    else:
        resp = newlist.remove(newlist[0])   
    return resp

def remove_last(newlist):
    if len == []:
        resp = "No hay nada que eliminar en una lista vacia"
    else:
        size = len(newlist)
        resp = newlist.remove(newlist[size])   
    return resp 

def insert_element(newlist,elemento): #Revisar esta, no dice si es un elemento especifico, pero si quieren especificar revisenlo, de lo contrario, no.
    newlist.append(elemento)
    return newlist

def change_info(my_list,):
    for i in new_list:
        if new_list[i] == elemento:
            new_list[i] = info
    return new_list

def exchange(newlist, elemento_1,posicion_elemento_1, elemento_2, posicion_elemento_2, tipo_de_cambio):
    if tipo_de_cambio == "2 a 1":
        for i in newlist:
            if newlist[i] == elemento_2 and i == posicion_elemento_2:
                cambio = new_list[i] #Terminar
