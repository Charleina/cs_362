#combines strings and checks for empty strings

class full_name:
    def __init__(self):
        pass
    
    def full_name1(self, first, last):
        space = " "
        fullname = first + space + last
        if( not first or not last):
            print "empty"
            return
        else:
            return fullname



