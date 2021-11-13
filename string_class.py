from timeit import default_timer as timer
class Strings:
    """ordered,immutable,text_representation"""
    def string_func(self):
        my_string = 'hello'
        for i in my_string:
            print(i.format())
        sub_string = my_string[1:3]
        print(sub_string)
        my_string1 = 'world '
        my_string1 += my_string
        print(my_string1)
        print(type(my_string1))
        #join multiple list to string
        list_to_string1 = ['a'] * 100000
        #bad practice expensive on resources
        start = timer()
        final_string = '' 
        for i in list_to_string1:
            final_string += i
        stop = timer()    
        #print(final_string)
        print(stop-start)    
        #OPTIMAL pratice
        start = timer()
        final_string = ''.join(list_to_string1)
        #print(final_string)
        stop = timer()
        print(stop-start)
        #3 ways to format strings f-string for the win 