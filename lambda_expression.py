from functools import reduce
class lambda_expression:
    def lambda_method(self):
        #general syntax
        add10 = lambda x:x + 10 #function with one argument + return result
        print(add10(5))
        #lambda func with multiple arguments
        mult = lambda x,y :x*y
        print(mult(5,5))
        points2D = [(1,15),(12,5),(10,54),(10,23)]
        points_2D_sorted = sorted(points2D,key=lambda x:x[0]+x[1])
        print(points2D)
        print(points_2D_sorted)
        #lambda with map function example
        elements = [1,2,3,4,5]
        maped_list = map(lambda v:v*2 ,elements)
        print(list(maped_list))
        #lambda with filter function example
        flitered_list = filter(lambda z:z%2 == 0,elements)
        print(list(flitered_list))
        #lambda with reduce function example
        reduced_list = reduce(lambda x,y : x+y ,elements)
        print(reduced_list)
        
        