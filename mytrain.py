class Mytrain:
    def __init__(self,num,name):
        self.num =  num
        self.name = name
        self.fare = 750
        self.seats = 100

    def display(self):
        print("The Train Details are in below :")
        print(f"Train Name    : {self.name}")
        print(f"Train Number  : {self.num}")
        print(f"Fare          : Rs.{self.fare}/-")
        print(f"Avaible Seats : {self.seats}")
        print('\n')

    def getBook(self,noOfTickets):
        if(self.seats >= 1):
            while(noOfTickets):
                print(f"Seat Booked : {self.seats}")
                noOfTickets = noOfTickets -1
            self.seat = self.seat - 1
        else:
            print("Seats are Full, You may try for RAC!")


class Passenger():   
    def __init__(self,name,age,phone):
        self.name = name
        self.age = age
        self.phone = phone


    def display(self):
        print("Check and Confirm the Passenger Details are mentioned below :")
        print(f"Passenger Name      : {self.name}")
        print(f"Passenger Age       : {self.age}")
        print(f"Passenger Phone no. : {self.phone}")

x = int(input("Enter the Train Number  : "))
y = input("Enter the Train Name  : ")


a = input("\nEnter the Passenger Name  : ")
b = int(input("Enter the Passenger Age  : "))
c = int(input("Enter the Passenger Phone no.  : "))

z = int(input("\nEnter the No. of Passenger  : "))

object = Mytrain(x,y)
object2 = Passenger(a,b,c)
object.getBook(z)
object.display()
object2.display()


