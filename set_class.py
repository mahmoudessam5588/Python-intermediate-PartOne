class Sets:
    def set_func(self):
        """unordered,mutables,ni-duplication"""
        my_set1 = {1,2,3,1,2,3}
        my_set2 = set([5,4,5,6,7,89,7])
        print(my_set1)
        print(my_set2)
        my_set3 = set()
        my_set3.add(100)
        my_set3.add(200)
        my_set3.add(300)
        my_set3.add(400)
        print(my_set3)
        my_set3.remove(200)
        print(my_set3)
        #union and intersection
        odd_set = {1,3,5,7,9}
        prime_set = {2,3,5,7}
        odd_intersect_prime = odd_set.intersection(prime_set)
        odd_diff_prime = odd_set.difference(prime_set)
        odd_diff_sym_prime = odd_set.symmetric_difference(prime_set)
        print(odd_intersect_prime)
        print(odd_diff_prime)
        print(odd_diff_sym_prime)
        even_set = {2,4,6,8,10}
        odd_union_even = odd_set.union(even_set)
        print(odd_union_even)
        odd_set.intersection_update(prime_set)
        print(odd_set)
        even_set.difference_update(prime_set)
        print(even_set)
        odd_diff_sym_prime.symmetric_difference_update(prime_set)
        print(odd_diff_sym_prime)
        print(odd_diff_prime.issubset(odd_diff_sym_prime))
        print(odd_diff_sym_prime.isdisjoint(odd_diff_prime))
        
        

