class PhoneNumber:
    def __init__(self, number):
        
        
        #remove all non-numerical characters
        number = number.translate({ord(i): None for i in ')(+. -'})
        
        #if phone number too long, too short
        if len(number) > 11 or len(number) < 10 or (len(number) == 11 and number[0] != '1'):
            raise ValueError("Invalid amount of numbers")
        
        #remove 1 prefix 
        if len(number) == 11 :        
            number = number[1:]

        #get subscriber number (last 4 digits)
        self.subscriber_number = number[-4:]
        
        if number[-7] == '0' or number[-7] == '1':
            raise ValueError("Invalid Exchange Code Number")      
        self.exchange_code = number[-7:-4]

        if number[-10] == '0' or number[-10] == '1':
            raise ValueError("Invalid Area Number")  
        self.area_code = number[-10:-7]
        

         
        self.number = number


    def pretty(self):
        return "(" + self.area_code + ")-" + self.exchange_code + "-" + self.subscriber_number


    def _getAreaCode(self):
        pass


if __name__ == "__main__":

    num = PhoneNumber("+1 (613)-005-03")
    
    #goal: 6139950253

    print (num.pretty())
    

