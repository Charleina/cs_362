#average between number is adding up all the elements divided by the total number of elements

class average:
    def __init__(self):
        pass
    
    def average1(self,l):
        total = 0
        for number in l:
            float(number)
            total += number
        if(total <= 0):
            print "empty list"
            return
        else:
            avg = total / float(len(l))
            return avg
        
    
