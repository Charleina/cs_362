#volume of cube is w*h*l
class cube:
    def __init__(self):
        pass
    
    def cube1(self,w1,h1,l1):
        w1 = float(w1)
        h1 = float(h1)
        l1 = float(l1)
        if(w1.is_integer() and h1.is_integer() and l1.is_integer()):
            if(w1 < 0 or h1 < 0 or l1 < 0):
                print "not positive numbers"
                return
            else:
                return w1*h1*l1
        else:
            print "not whole numbers"
            return
    
    def cube2(self,w2, h2, l2):
        w2 = float(w2)
        h2 = float(h2)
        l2 = float(l2)
        if(w2.is_integer() and h2.is_integer() and l2.is_integer()):
            if(w2 < 0 or h2 < 0 or l2 < 0):
                print "not positive numbers"
                return
            else:
                return w2*h2*l2
        else:
            print "not whole numbers"
            return
    
    def cube3(self,w3, h3, l3):
        w3 = float(w3)
        h3 = float(h3)
        l3 = float(l3)
        if(w3.is_integer() and h3.is_integer() and l3.is_integer()):
            if(w3 < 0 or h3 < 0 or l3 < 0):
                print "not positive numbers"
                return
            else:
                return w3*h3*l3
        else:
            print "not whole numbers"
            return

