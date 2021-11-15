from typing import List
from itertools import product
from itertools import permutations
from itertools import combinations , combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count,cycle,repeat
import operator
class Itertools:
    """product,permutation,combination,accumlate,groupby and infinte iterators"""
    def product_method(self):
        a= [1,2]
        b= [4]
        prod = product(a,b, repeat=2)
        print(list(prod))
    def permutation_method(self):
        #all possible ordering of given elements
        elements = [1,2,3]
        perm = permutations(elements)
        print(list(perm))
        perm = permutations(elements,2)
        print(list(perm))
    def combination_method(self):
        #all possible combination with specified length
        ac= [100,200,300,400,500]
        comb = combinations(ac,2)
        print(list(comb))
        bc = [111,222,333]
        combs = combinations_with_replacement(bc,2)
        print(list(combs))
    def accumlate_method(self):
        #let iterator bring series of accumlated sums
        acc = [1,2,3,4,5,6]
        acc_max=[1,2,3,100,4,5,6]
        acc_sum = accumulate(acc,func= operator.mul)
        acc_maxium = accumulate(acc_max ,func= max)
        print(list(acc_sum))
        print(list(acc_maxium))
    def groupby_invoke (self):    
      a= [1,2,3,4]   
      group_obj =groupby(a ,key=lambda x:x<3)
      for key ,value in group_obj:
          print(key,list(value)) 
    def Infinite_iterators_method(self):
        # for i in count(10):
        #     print(i) infinite loop form number 10
        # cycle cyele given elements in list for infinte
        #repeat given element for infinite
        pass
        
        
        
        
        
            
                      