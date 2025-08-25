def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):

    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    if size > 0: 
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
            if keyexist:
                return keypos
    return -1 
    

def new_list():
    
    return {'size': 0, 'elements': []}

def add_first(my_list, element):
    
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    
    m= my_list["element"]
    m.append("element")
    my_list["size"] +=1
    return my_list
    
def is_empty(my_list):
    
    if len(my_list)!=[]:
        return False
    else:
        return True

def last_element(my_list):
    
    if my_list !=[]:
       m= my_list[-1]
       return m
    else:
        return "IndexError: list index out of range"
    
def delete_element(my_list, pos):
    pass

def remove_first(my_list):
    if my_list !=[]:
        m= my_list.remove (0)
        return m
    else:
        return "IndexError: list index out of range"
    
def remove_last(my_list):
    if my_list !=[]:
        m= my_list.remove (-1) 
        return m
    else:
        return "IndexError: list index out of range"

def insert_element(my_list, element, pos):
    return(al.insert_element(my_list, element, pos))


def change_info(my_list, pos, new_info):
    if pos in my_list:
      m=my_list[pos:new_info]
      return m
    else: 
      return "IndexError: list index out of range"

def exchange(my_list, pos_1, pos_2):
    if pos_1 or pos_2 not in my_list:
       return "IndexError: list index out of range"
    else:
       return (al.exchange(my_list, pos_1, pos_2))

def sub_list(my_list, pos_i, num_elements):
    if pos_1 not in my_list:
       return "IndexError: list index out of range"
    else:
       return (al.sub_list(my_list, pos_i, num_elements)) 