class Train():
    def init(self,seato,number,fare):
        self.tseato = seato
        self.fare = fare
        self.number = number
        self.seat = seato
        self.fund = 0

    #def getDetail(self):
     #   print(f"Train No. :-{self.number} Fare is :-${self.fare}/- Available Seat :-{self.seat}" )
     #   print(f"Total Fund :- ${self.fund}")
     
    def cancelBook(self,noOfTick):
        if(self.seat == self.tseato):             
           print("Seats Are Not Book at all Yet ") 
        else:
            while(noOfTick)and(self.seat <= self.tseato):   
             self.seat = self.seat + 1
             print(f"Seat Booked Cancelled :-{self.seat} in Train :-{self.number}") 
             self.fund -= self.fare
             noOfTick = noOfTick - 1
            
    def getBook(self,noOfTick):
        if(self.seat):             
         while(noOfTick):
          print(f"Seat Booked :-{self.seat} in Train :-{self.number}")   
          self.seat = self.seat - 1
          self.fund += self.fare
          noOfTick = noOfTick - 1
        
           
        else:
            print("Seats Are Full : ( ")  
           

    
intersity = Train(300,100232,20)
intersity.getDetail()
intersity.getBook(4)
intersity.cancelBook(3)

while(intersity.seat != 0):
 p = input("Enter If U Want BOOk Seat Press 'B' For cancel 'C' and 'D ' for detail")
 if(p == "B")or(p == "b"):
     l = int(input("Enter The No.Tickets for Booking :-"))
     intersity.getBook(l)
     intersity.getDetail()
 elif(p == "C")or(p == "c"):
    l = int(input("Enter The No.Tickets for cancel :-"))
    intersity.cancelBook(l)
    intersity.getDetail()    
 else:
    print("Thanks For Visiting")
    intersity.getDetail()  
print("Train is Full : )")