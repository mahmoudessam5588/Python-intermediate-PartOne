from types import NoneType, NotImplementedType
from typing import Collection, NoReturn
from dictionaries_class import Dictionaries
from List_class import list
from itertools_class import Itertools
from logging_class import Logging
from tuples_class import Tuples
from set_class import Sets
from string_class import Strings
from collection_class import Collections
from lambda_expression import  lambda_expression
def main(args):
    #list_call()
    #tuple_call()
    #dict_call()
    #set_call()
    #string_call()
    #collections_call()
    #itertool_call()
    #lambda_call()
    logging_call()
    return 0
def tuple_call():
    Tuples
    tuple_inst = Tuples()
    tuple_inst.tuple_func()    
def list_call():
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
def itertool_call():
    Itertools
    itertools = Itertools()
    itertools.product_method()
    itertools.permutation_method()
    itertools.combination_method()
    itertools.accumlate_method()
    itertools.groupby_invoke()        
def lambda_call():
   lambda_expression
   lambda_exp = lambda_expression()
   lambda_exp.lambda_method()
def logging_call():
    Logging
    logging = Logging()
    logging.logging_method() 
    logging.logging_handler_method()
    #logging.logging_conf_file()
    logging.stack_traces()
    logging.rotationg_file_handler()
    logging.time_rotating_file_handler()  
if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))        