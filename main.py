from typing import Collection
from dictionaries_class import Dictionaries
from List_class import List
from tuples_class import Tuples
from set_class import Sets
from string_class import Strings
from collection_class import Collections
def main(args):
    #List_call()
    #tuple_call()
    #dict_call()
    #set_call()
    #string_call()
    #collections_call()
    return 0
def tuple_call():
    Tuples
    tuple_inst = Tuples()
    tuple_inst.tuple_func()    
def List_call():
    List
    list =  List()
    list.list_func()
    List.comphrehension_list()
def dict_call():
    Dictionaries
    dictionaries = Dictionaries()
    dictionaries.dict_func()
def set_call():
    Sets
    sets = Sets()
    sets.set_func()
def string_call():
    Strings
    strings = Strings()
    strings.string_func()
def collections_call():
    Collections
    collections = Collections()
    collections.counter_method()
    collections.named_tuple_method()
    collections.ordered_dict_method()
    collections.default_dict_method()
    collections.deque_method()
    
if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))        