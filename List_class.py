class list:
    """lists,ordered,mutable,allow duplicate data""" 
    def list_func(self):
        mylist=[1,23,45,778,99,0,666,88,22,67,88,112,34,89,34,567]
        reversed_list= mylist[::-1]
        print(reversed_list)
        x=list(set(reversed_list))
        print(x)
        original_list='out of the light is the born of the darkest shadow'.split()
        refrence_equal_to_original = list(original_list)
        refrence_equal_to_original.append('as')
        print(original_list)
        print(refrence_equal_to_original)
        value_equal_to_original = original_list.copy()
        value_equal_to_original.append('obscure the truth deception pierces our souls'.split())
        print(original_list)
        print(value_equal_to_original)
    def comphrehension_list():
        num_list = [1,2,3,4,5,6,7,8,9,10]
        multiple_list = [i*i for i in num_list]
        print(multiple_list)     


        