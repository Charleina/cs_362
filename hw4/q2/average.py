#average between number is adding up all the elements divided by the total number of elements

class average:
    def __init__(self):
        pass
    
    def average1(self,l1):
        total = 0
        for number in l1:
            float(number)
            total += number
        if(total <= 0):
            print "empty list"
            return
        else:
            avg = total / float(len(l1))
            return avg
        
    def average2(self,l2):
        total = 0
        for number in l2:
            float(number)
            total += number
        if(total <= 0):
            print "empty list"
            return
        else:
            avg = total / float(len(l2))
            return avg
    
    def average3(self,l3):
        total = 0
        for number in l3:
            float(number)
            total += number
        if(total <= 0):
            print "empty list"
            return
        else:
            avg = total / float(len(l3))
            return avg


