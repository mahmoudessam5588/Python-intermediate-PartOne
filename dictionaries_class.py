class Dictionaries:
    """(key+value)=>pairs , unorderd , mutable """
    def dict_func(self):
        dict1 = {"name":"mahmoud","age":33,"city":"singapore"}
        print(dict1)
        poped_dicted = dict1.pop("age")
        print(f'removed item is: {poped_dicted} and original dict is {dict1}')
        #looping on dict
        for key in dict1.keys():
            print(f'keys: {key}')
        dict2=dict(name = "ahmed", age ="25",city="malaysia")
        print(dict2)
        del dict2["city"]
        print(dict2)
        dict2["email"] = "wse@zas.com"
        print(dict2)
        #check if key inside dict
        if "name" in dict2:
            print('True')
        else:
            print('false')
        try:
            print(dict2['email'])
        except:
            print('error')
        #copy dict
        dict_copy = dict2
        dict_copy_value = dict(dict2)
        dict_copy['email'] = 'sss@sss.com'
        dict_copy_value['email'] = 'sssRRR@ssRRs.com'
        print(dict_copy)
        print(dict_copy_value)
        print(dict2)
        print(f'\nbefore overwritten:{dict1}')
        dict1.update(dict_copy_value)
        print(f'after overwritten:{dict1}')


