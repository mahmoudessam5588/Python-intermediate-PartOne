import sys
import timeit
class Tuples:
    """Ordered ,Immutable,allow duplixate elemenets """
    def tuple_func(self):
      my_tuple1 = 'Max' , 28 , 'boston' #parentaces are optional
      my_tuple2 = tuple('mahmoud') #from iterable
      my_tuple3 = ("omar",)
      print(f'{my_tuple1} , {my_tuple2} , {my_tuple3}')
      unique_tuple = (1,2,3,4,5,6,7,8,9,10)
      splitted_tuple = unique_tuple[2:4]
      print(splitted_tuple)
      #tuple unpacking
      packed_tuple = (1,2,3,4,5,6,7,8,9,10)
      i1 ,*i2 ,i3 = packed_tuple
      print(i1)
      print(i3)
      print(i2)
      #comparing lists && tuples efficacy
      list_bytes = [0,1,2,3,'hello',True]
      tuple_bytes = (0,1,2,3,'hello',True)
      print(sys.getsizeof(list_bytes))
      print(sys.getsizeof(tuple_bytes))
      #comparing list and tuples speed of iteration
      print(timeit.timeit(stmt='[1,2,3,4,5,6,7,8,9,10]',number=100000))
      print(timeit.timeit(stmt='(1,2,3,4,5,6,7,8,9,10)',number=100000))
