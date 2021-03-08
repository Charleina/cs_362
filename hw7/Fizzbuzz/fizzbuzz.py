#should run when called python test_fizzbuzz.py

class fizzbuzz:
    def __init__(self):
        pass
    def method(self):
        fullstring = ""
        for i in range(1, 101):
            if(i%5 == 0 and i%3 == 0):
                fullstring = fullstring + "FizzBuzz "
            else:
                if(i%3 == 0):
                    fullstring = fullstring + "Fizz "
                if(i%5 == 0):
                    fullstring = fullstring + "Buzz "
                if(i%3 !=0 and i%5 !=0):
                    fullstring = fullstring + str(i) + " "
        return fullstring
