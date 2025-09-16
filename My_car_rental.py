from datetime import datetime,timedelta
class Carrental:
    def __init__ (self,stock=100):
        """ 
        Define constructor for class.
        param stock: Total avilable cars for rent
        """
        self.stock = stock
        
    def display_cars(self):
        """
        Display the number of cars avilable for rent.
        """
        print(f"We have {self.stock} cars avilable for rent.")
        return self.stock
        
    def hourly_rental(self,n,hours):
        """
        Rent the car on hourly basis
        n= quantity of cars to rent 
        hours= number of hours to rent
        return= Rental time
        """
        if n<=0 or hours<=0:
            print("Minimum positive 1 car needs to select")
        elif n > self.stock:
            print(f"Only {self.stock} cars are avilable for rent ")
            return None
        else:
            self.stock -= n
            current_datetime = datetime.now()
            return current_datetime,hours
    def daily_rental(self,n,days):
        """
        Rent the car on daily basis
        n= quantity of cars to rent 
        days= number of days to rent
        return= Rental time
        """
        if n<=0 or days<=0:
            print("Minimum positive 1 car needs to select")
        elif n > self.stock:
            print(f"Only {self.stock} cars are avilable for rent ")
            return None
        else:
            self.stock -= n
            current_datetime = datetime.now()
            return current_datetime,days
    def weekly_rental(self,n,weeks):
        """
        Rent the car on weekly basis
        n= quantity of cars to rent 
        weeks= number of weeks to rent
        return= Rental time
        """
        if n<=0 or weeks<=0:
            print("Minimum positive 1 car needs to select")
        elif n > self.stock:
            print(f"Only {self.stock} cars are avilable for rent ")
            return None
        else:
            self.stock -= n
            current_datetime = datetime.now()
            return current_datetime,weeks
    def return_car(self,request):
        """
        Returns a rented car.
        request = tuple containing rental time,rental basis, rental duration and Number of cars rented.
        return= Bill amount.
        """
        rental_time, rental_basis, rental_duration, number_of_cars = request
        bill = 0

        if rental_time and rental_basis and rental_duration and number_of_cars:
            self.stock += number_of_cars
            current_datetime = datetime.now()
            rental_period = current_datetime - rental_time
            if rental_basis == 1 :  # hourly
                 bill = rental_duration * 100 * number_of_cars
            elif rental_basis == 2: # daily
                  bill = rental_duration * 500 * number_of_cars
            elif rental_basis == 3: # weekly
                  bill = rental_duration * 3000 * number_of_cars
            if number_of_cars >= 2:
                print ("you got 10% discount")
                bill *= 0.9

                print (f"Thankyou for visiting. Your bill is Rs {bill:.2f}")
                return bill

        else:
            print("Are you shure you have rented car with us?")
            return None

class Customer:
    def __init__(self):
        """
        Constroctor for class Customer
        """
        self.car = 0
        self.rental_basis = 0
        self.rental_time = None
        self.rental_duration = 0

    def request_car(self):
        """
        request the car_rental.
        return = Number of cars to rent.
        """
        cars = int(input("how many cars would you like to rent?"))
        try:
            cars = int(cars)
        except ValueError:
            print ("Invalid input!, Enter positive integer")
            return -1

        if cars <1:
            print("Invalid input!, Kindly, Enter positive integer")
            return -1
        else:
            self.cars = cars
        return self.cars
    def request_duration(self):
        """
        requset the rental duration.
        return = rental duration
        """
        duration = input("For how long would you like to rent the cars (in hours/days/weeks)? ")
        try:
            duration = int(duration)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if duration < 1:
            print("Invalid input. Duration should be greater than zero!")
            return -1
        else:
            self.rental_duration = duration
        return self.rental_duration
    def return_car(self):
        """
        Returns the car rental.
        return = A tuple containing rntal_time, rental_basis, rental_duration, and number_of_cars rented
        """
        if self.rental_basis and self.rental_time and self.cars:
            return self.rental_time, self.rental_basis, self.rental_duration,self.cars
        else:
            return None, None, None, None