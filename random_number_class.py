import random
import secrets
class random_class:
    def random_method(self):
        #sudo random module use to generate sudo random numbers for various distrubtions called sudo random because they seem as random but they are reproducible
        #different functions
        a=random.random()#print random float from zero to one
        print(a)
        b=random.uniform(1,10)#specific float range
        print(b)
        c=random.randint(5,10)#specific int range**include upper bound**
        print(c)
        d=random.randrange(1,5)#int range not include upperbound
        print(d)
        e=random.normalvariate(0,1)#range mu=mean sigma=standard deviation
        print(e)
        f=list("atdsfjgdmnxzl")#chossing from list of elements
        choose =random.choice(f)
        print(choose)
        multi_choose=random.sample(f,3)#choose mulitple elements to given number
        print(multi_choose)
        random.shuffle(f)
        print(f)
    
    def secret_method(self):
        a=secrets.randbelow(10)
        print(a)
        b=secrets.randbits(4)
        print(b)
        mylist = list('awefgtyu')
        choo = secrets.choice(mylist)
        print(choo)    