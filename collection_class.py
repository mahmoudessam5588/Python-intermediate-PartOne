from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
class Collections:
    """Counter , OrderedDict , DefaultDict ,NamedTuple , Deque"""
    def counter_method(self):
        """Store elements as dictionary keys
            their counts as Dictionary Value"""
        a = "aaaaabbbbbcccdddd"
        my_count = Counter(a)
        print(my_count)
        print(my_count.items())
        print(my_count.keys())
        print(my_count.values())
        print(my_count.most_common(1))
        print(my_count.most_common(1)[0][0])
        print(list(my_count.elements()))
    def named_tuple_method(self):
        """Similar to Struct 2 argument given first one str similar to variable name and the other one is the an element ot number of elements seperated by a coumma also str assigned to another variable to set the values"""
        point = namedtuple('point','here,there')
        pt = point('egypt','singapore')
        print(pt)
        print(pt.here,pt.there) 
    def ordered_dict_method(self):
        """Just like the ordinary dict but the items are sorted the same way you added / inserted them"""
        order = OrderedDict()
        order['b'] = 2
        order['c'] = 3
        order['a'] = 1
        order['d'] = 4
        order['e'] = 5
        print(order)
    def default_dict_method(self):
        """Default value with the key not set yet"""
        demos = defaultdict(int)
        demos['a'] = 1
        demos['b'] = 2
        demos['c'] = 3
        print(demos.keys())
    def deque_method(self):
        """add or remove elements from both ends"""
        add_to_deque = deque()
        add_to_deque.append(1)
        add_to_deque.append(2)
        add_to_deque.append(3)
        add_to_deque.append(4)
        add_to_deque.append(5)
        add_to_deque.appendleft(-1)
        add_to_deque.appendleft(-2)
        add_to_deque.appendleft(-3)
        add_to_deque.appendleft(-4)
        add_to_deque.appendleft(-5)
        print(add_to_deque)
        add_to_deque.pop()
        print(add_to_deque)
        add_to_deque.popleft()
        print(add_to_deque)
        add_to_deque.extend([55,66,77])
        print(add_to_deque)
        add_to_deque.extendleft([-33,-55,-88])
        print(add_to_deque)
        add_to_deque.rotate(2)
        print(add_to_deque)
        add_to_deque.reverse()
        print(add_to_deque)

