from datetime import datetime
class Trip:
    def __init__(self,trip_id,point_a,point_b,start_time,end_time):
        self.point_a=point_a
        self.point_b=point_b
        self.start_time=start_time
        self.end_time=end_time
        self.trip_id=trip_id
    def calculate_duration(self):
       duration=self.end_time-self.start_time
       return(
           f"Trip Dtails:\n"
           f"Start time :{self.start_time}\n"
           f"End time :{self.end_time}\n"
           F"Duration {duration}"
       ) 
    def show_info(self):
        return f"Point A:{self.point_a}\nPoint B: {self.point_b}\nTrip ID {self.trip_id}"
class Person:
    max_rating=5
    def __init__(self,full_name,id):
        self.full_name=full_name
        self.id=id
    def show_info(self):
        return f"Full Name: {self.full_name}\nID:{self.id}"
    
class Passenger(Person):
    def __init__(self, full_name, id,):
        super().__init__(full_name, id)
        self.number_trip=0
        self.number_rating=0
        self.rating=0
        self.ratings=[]
    def add_trip(self):
        self.number_trip+=1
    def add_rating(self,rating):
        if rating<1 or rating>Passenger.max_rating:
            return "Invalid rating"
        self.ratings.append(rating)
        self.number_rating+=1
        self.rating=sum(self.ratings)/self.number_rating
        return self.rating
    def show_info(self):
        return f"{super().show_info()}\nNumber trips {self.number_trip} Passenger Rating{self.rating}"
class Driver(Person):
    def __init__(self, full_name,id,phone_number,age):
        super().__init__(full_name, id)
        self.phone_number=phone_number
        self.age=age
        self.number_trip=0
        self.bank_account=None
        self.licence=None
        self.certificate=None
        self.number_rating=0
        self.rating=0
        self.ratings=[]      
    def add_trip(self):
        self.number_trip+=1
    def add_certificate(self,certificate):
        self.certificate=certificate
    def check_driver_police_certificate(self):
        if self.certificate is None:
            return False
        else:
            return True
    def check_age(self):
        if self.age<20:
            return False
        elif self.age>65:
            return False
        else:
            return True
    def add_licence(self,licence):
        self.licence=licence
    def check_licence(self):
        if self.licence is None:
            return False
        else:
            return True
    def add_bank_account(self,bank_account):
        self.bank_account=bank_account
    def check_bank_account(self):
        if self.bank_account is None:
            return False
        else:
            return True
    def check_driver_eligibility(self):
        if self.check_age() and  self.check_driver_police_certificate() and self.check_licence() and self.check_bank_account():
            print("Driver is eligible to Work")
            return True
        else:
            print("Driver is not eligible to work")
            return False
    def add_rating(self,rating):
        if rating<1 or rating>Person.max_rating:
            return "Invalid rating"   
        self.ratings.append(rating)
        self.number_rating+=1
        self.rating=sum(self.ratings)/self.number_rating
        return self.rating
    def show_info(self):
        return f"{super().show_info()}\nPhone number:{self.phone_number}\nAge:{self.age}\nnumber of trip{self.number_trip}\nrating:{self.rating}\nDriver Bank Account:{self.bank_account}\nDriver licence:{self.licence}\nPolice Clearance Certificate:{self.certificate}"
class Taxi:
    def __init__(self,car_brand,car_model,fuel_sort,kilometres,car_id):
        self.car_model=car_model
        self.car_brand=car_brand
        self.fuel_sort=fuel_sort
        self.kilometres=kilometres
        self.car_id=car_id
        self.insurance=None
        self.date_manufacture=None
        self.insurance_expiry=None
        self.service_date=None
        self.status="available"
    def add_car_insurance(self,insurance):
        self.insurance=insurance
    def check_car_insurance(self):
        if self.insurance is None:
            return False
        else:
            return True
    def set_manufacturing_date(self,date_manufacture):
        self.date_manufacture=date_manufacture
    def check_date(self):
        if self.date_manufacture is None:
            return False
        if self.date_manufacture.year<2016:
            return False
        else:
            return True
    def set_insurance_expiry(self,insurance_expiry):
        self.insurance_expiry=insurance_expiry
    def check_insurance_expiry(self,current_date):
       if self.insurance_expiry is None:
           return False
       if self.insurance_expiry>=current_date:
           return True
       return False
    def car_eligibility(self,current_date):
        if self.check_car_insurance() and self.check_date() and self.check_insurance_expiry(current_date):
            print("Your car is eligible to work")
            return True
        else:
            print("This car no allowed to work choice another car or contact support for more information")
            return False
    def update_kilometres(self,new_kilometres):
        self.kilometres+=new_kilometres
        return self.kilometres
    def car_status(self,status):
        self.status=status.lower().strip()
        if self.status=="available":
            return"car is available to work"
        elif self.status=="busy":
            return"Car is busy right now"
        elif self.status=="maintenance":
            return"Car is under maintenance right now"
        else:
             return"Invalid car status"
    def last_service_date(self,service_date):
        self.service_date=service_date
    def show_car_info(self):
        return(
            f"Car Model: {self.car_model}\n"
            f"Brand:{self.car_brand}\n"
            f"Fuel:{self.fuel_sort}\n"
            f"kilometres:{self.kilometres}\n"
            f"Car ID: {self.car_id}\n"
            f"Insurance: {self.insurance}\n"
            f"Manufacturing date: {self.date_manufacture}\n"   
            f"Car insurance Expiry {self.insurance_expiry}\n"
            f"Car last service : {self.service_date}\n"
            f"Car status : {self.status}"
        )
class Fare:
    def __init__(self,distance,duration):
        self.distance=distance  
        self.duration=duration
        self.fare=0
        self.price_km=0
        self.price_minute=0
    def base_fare(self,base_fare):
        self.fare=base_fare
    def price_per_km(self,price_km,):
        self.price_km=price_km
        return self.price_km*self.distance
    def price_per_minute(self,price_minute):
        self.price_minute=price_minute
        return self.price_minute*self.duration
    def calculate_fare(self):
         return self.fare+(self.distance*self.price_km)+(self.duration*self.price_minute)
    def show_fare(self):
        return(
            f"Base Fare : {self.fare}\n"
            f"Price per KM:{self.price_km}\n"
            f"Price per minute: {self.price_minute}\n"
            f"Final Total :{self.calculate_fare()}"
        )
class Payment:
    def __init__(self,amount,payment_id,payment_method):
        self.amount=amount
        self.payment_id=payment_id
        self.payment_method=payment_method
        self.status="pending"
    def process_payment(self):
        if self.amount>0:
            print("payment done")
            self.status="Paid"
            return self.status
            
        else:
            print("payment unsuccessful")
            self.status="failed"
            return self.status
    def check_payment(self):
        if self.status=="pending":
            return "payment pending"
        elif self.status=="Paid":
            return "Payment done"
        else:
            return "payment failed"
    def show_info(self):
        return (
            f'Amount:{self.amount}\n'
            f"Payment ID:{self.payment_id}\n"
            f"Payment Method: {self.payment_method}\n"
            f"{self.check_payment()}"
        )
class TripManager:
    def __init__(self):
        self.passengers=[]
        self.drivers=[]
        self.trips=[]
        self.taxis=[]
    def add_passenger(self,passenger):
        self.passengers.append(passenger)
    def add_driver(self,driver):
        self.drivers.append(driver)
    def add_taxi(self,taxi):
        self.taxis.append(taxi)
    def add_trip(self,trip):
        self.trips.append(trip)
    def remove_passenger(self,passenger):
        self.passengers.remove(passenger)
    def remove_driver(self,driver):
        self.drivers.remove(driver)
    def remove_taxi(self,taxi):
        self.taxis.remove(taxi)
    def remove_trip(self,trip):
        self.trips.remove(trip)
    def show_passengers(self):
        for passenger in self.passengers:
            print(passenger.show_info())
    def show_drivers(self):
        for driver in self.drivers:
            print(driver.show_info())
    def show_taxis(self):
        for taxi in self.taxis:
            print(taxi.show_car_info())
    def show_trips(self):
        for trip in self.trips:
            print(trip.show_info())
    def find_passenger(self,passenger_id):
        for passenger in self.passengers:
            if passenger.id.lower().strip()==passenger_id.lower().strip():
                return passenger
        return None
    def find_driver(self,driver_id):
        for driver in self.drivers:
            if driver.id.lower().strip()==driver_id.lower().strip():
                return driver
        return None
    def find_taxi(self,taxi_id):
        for taxi in self.taxis:
            if taxi.car_id.lower().strip()==taxi_id.lower().strip():
            
                return taxi
        return None
    def find_trip(self,trip_id):
        for trip in self.trips:
            if trip.trip_id.lower().strip()==trip_id.lower().strip():
                return trip
        return None
    def update_passenger(self,passenger_id,new_name):
        passenger=self.find_passenger(passenger_id)
        if passenger:
            passenger.full_name=new_name
            return passenger
        return None
    def update_driver(self,driver_id,new_name,new_phone,new_age):
        driver=self.find_driver(driver_id)
        if driver:
            driver.full_name=new_name
            driver.phone_number=new_phone
            driver.age=new_age
            return driver
        return None
    def update_taxi(self,taxi_id,new_brand,new_model,new_fuel,new_kilometers):
        taxi=self.find_taxi(taxi_id)
        if taxi:
            taxi.car_brand=new_brand
            taxi.car_model=new_model
            taxi.fuel_sort=new_fuel
            taxi.kilometres=new_kilometers
            return taxi
        return None
    def update_trip(self,trip_id,new_point_a,new_point_b,new_start_time,new_end_time):
        trip=self.find_trip(trip_id)
        if trip:
            trip.point_a=new_point_a
            trip.point_b=new_point_b
            trip.start_time=new_start_time
            trip.end_time=new_end_time
            return trip
        return None
class AboutAPP:
    def Show_inf(self):
        print("=" * 60)
        print("              ABOUT TAXI TRIP TAKER")
        print("=" * 60)
        print()
        print("Developed by: Mohamed Wassim Tatari")
        print("Python Developer | Aspiring Data Analyst")
        print()
        print("This project was developed in")
        print("Tangier, Morocco.")
        print("Completion Date: October 16, 2026")
        print("Completion Time: 1:20 PM")
        print()
        print("Built step by step, class by class,")
        print("this project represents another milestone")
        print("in my journey of learning Python and")
        print("Object-Oriented Programming (OOP).")
        print()
        print("Thank you for following my journey with CodeFlow.")
        print()
        print("Stay tuned for more applications,")
        print("future improvements, and exciting")
        print("data analysis projects!")
        print()
        print("CodeFlow - Building Skills, Creating Solutions.")
        print("=" * 60)

manager=TripManager()
while True:
    print("Welcome to IN Morroco Taxi Application")
    print("_"*25)
    print("1-Trips")
    print("2-Passengers")
    print("3-Drivers")
    print("4-Taxis")
    print("5-Fare")
    print("6-Payment")
    print("7-Managment")
    print("8-About Application")
    print("9-exit")
    print("_"*25)
    try:
        choice=int(input("Enter number of choice to start :"))
        if choice<1 or choice>9:
            print("Invalid choice: You should enter number in range 1 and 9 !")
            continue
    except ValueError:
        print("You should enter number of your choice")
        continue
    if choice==1:
        while True:
            print("Trip Menu")
            print("_"*25)
            print("1-add trip")
            print("2-Calculate Duration")
            print("3-Trip Information")
            print("4-Exit")
            try:
                trip_choice=int(input("Enter number of your choice to start :"))
                if trip_choice<1 or trip_choice>4:
                    print("Invalid Choice:You should enter number in range 1 and 4 ")
                    continue
            except ValueError:
                print("You should enter a number for your choice")
                continue
            if trip_choice==1:
                print("Follow all steps to add a trip")
                trip_id=input("Enter Trip Id:")
                point_a=input("Enter Point A :")
                point_b=input("Enter Point B :")
                try:
                    start_time=datetime.strptime(input("Enter start time follow the form 1987-11-18 10:30:15 :"),"%Y-%m-%d %H:%M:%S")
                    end_time=datetime.strptime(input("Enter End time follow the form 1987-11-18 11:00:15 :"),"%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print("You should follow the correct type of date and time") 
                    continue
                new_trip=Trip(trip_id,point_a,point_b,start_time,end_time)
                manager.add_trip(new_trip)
                print("Trip added")
            elif trip_choice==2:
                print("follow all steps to calculate duration of trip")
                trip_calculate_id=input("Enter Trip ID to calculate duration :")
                trip=manager.find_trip(trip_calculate_id)
                if trip is not None:
                    duration=trip.calculate_duration()
                    print(duration)
                else:
                    print("there are not any trip to calculate duration") 
            elif trip_choice==3:
                trip_id_show=input("Enter Trip ID to show Trip information : ")
                trip=manager.find_trip(trip_id_show)
                if trip is not None:
                    show_info=trip.show_info()
                    print(show_info)
                else:
                    print("Trip ID does not exist!")
            else:    
                print("You choice to Exit")
                break
    elif choice==2:
        while True:
            print("Passengers Menu")
            print("-"*25)
            print("1-Add Passenger")
            print("2-Add Trip")
            print("3-Add Passenger Rate")
            print("4-Show Passenger")
            print("5-Exit")
            try:
                passenger_choice=int(input("Enter number of Your choice to start :"))
                if passenger_choice<1 or passenger_choice>5:
                    print("Invalid choice: you should Enter number in range 1 and 5")
                    continue
            except ValueError:
                print("Erorr: You should enter number to start")
                continue
            if passenger_choice==1:
                print("Follow all steps to Add a passenger")
                passenger_full_name=input("Enter passenger full name:")
                passenger_id=input("Enter passenger ID:")
                new_passenger=Passenger(passenger_full_name,passenger_id)
                manager.add_passenger(new_passenger)
                print("Passenger Added")
            elif passenger_choice==2:
                passenger_id_for_trip=input("Enter passenger ID to add a trip to passenger trip number :")
                id_pa=manager.find_passenger(passenger_id_for_trip)
                if id_pa is not None:
                    id_pa.add_trip()
                    print(f"Trip Added,Total Trips {id_pa.number_trip}")
                else:
                    print("Passenger ID does no exist!")
            elif passenger_choice==3:
                passenger_id_for_rate=input("Enter passenger id to add a rate:")
                id_pa=manager.find_passenger(passenger_id_for_rate)
                if id_pa is not None:
                    try:
                        rating_value=int(input("Enter Passenger rating:"))    
                    except ValueError:
                        print("ValueError:You should enter a number for passenger rating")
                        continue
                    result=id_pa.add_rating(rating_value)
                    if result=="Invalid rating":
                        print("Invalid Rating:You should enter a rating in range 1 and 5")
                    else:
                        print("Rating Added successufully")
                        print(f"Rating number{id_pa.number_rating}")
                        print(f"Average Rating {id_pa.rating}")
                else:
                    print(f"Passnger ID {passenger_id_for_rate} does not Exist")
            elif passenger_choice==4:
                passenger_id_for_show=input("Enter passenger ID to show passenger information:")
                pa_info=manager.find_passenger(passenger_id_for_show)
                if pa_info is not None:
                    show=pa_info.show_info()
                    print(show)
                else:
                    print(f"Passenger ID {passenger_id_for_show} does not show")
            else:
                print("You choice to exist")
                break
    elif choice==3:
        while True:
           print("Driver Menu")
           print("-"*25)
           print("1-Add Driver")
           print("2-Add Driver certificate")
           print("3-Add Driver licence")
           print("4-add Driver bank account")
           print("5-check driver eligibility")
           print("6-Add Driver Rating")
           print("7-Show Driver")
           print("8-Exit")
           try:
               driver_choice=int(input("Enter number of your choice to start :"))
               if driver_choice<1 or driver_choice>8:
                    print("Invalid choice:You should enter number in range 1 and 8")
                    continue
           except ValueError:
                print("Value Error:You should enter number for your choice!")
                continue
           if driver_choice==1:
                print("Follow all steps to add a driver")
                driver_full_name=input("Enter driver full name:")
                driver_id=input("Enter Driver ID:")
                driver_phone_number=input("Enter Driver Phone number:")
                try:
                    driver_age=int(input("Enter driver Age:"))
                except ValueError:
                    print("ValueError:You shoud enter numbers for Driver's age")
                    continue
                new_driver=Driver(driver_full_name,driver_id,driver_phone_number,driver_age)
                manager.add_driver(new_driver)
                print("Driver Added")
           elif driver_choice==2:
                driver_id_certificate=input("Enter Driver ID to Add certificate:")
                id_dr=manager.find_driver(driver_id_certificate)
                if id_dr is not None:
                    new_driver_certificate=input("Enter certificate code :")
                    id_dr.add_certificate(new_driver_certificate)
                    print(f"certificate {new_driver_certificate} Added successfully")
                else:
                    print(f"Driver ID {driver_id_certificate} does not exist")
           elif driver_choice==3:
                driver_id_licence=input("Enter Driver ID to Add licence :")
                id_dr=manager.find_driver(driver_id_licence)
                if id_dr is not None:
                    driver_new_licence=input("Enter licence Code to enter:")
                    id_dr.add_licence(driver_new_licence)
                    print(f"Licence {driver_new_licence} Added successfully")
                else:
                    print(f"Driver ID {driver_id_licence} does not exist")
           elif driver_choice==4:
                driver_id_for_bank_account=input("Enter Driver Id to Add Bank Account:")
                id_dr=manager.find_driver(driver_id_for_bank_account)
                if id_dr is not None:
                    bank_account=input("Enter Bank Account RIB:")
                    id_dr.add_bank_account(bank_account)
                    print(f"Bank Account {bank_account}Added Successfully")
                else:
                    print(f"Driver ID {driver_id_for_bank_account} does not exist")
           elif driver_choice==5:
                driver_id_check_elig=input("Enter Driver ID to Check driver eligibility: ")
                id_dr=manager.find_driver(driver_id_check_elig)
                if id_dr is not None:
                    id_dr.check_driver_eligibility()    
                else:
                    print(f"Driver ID {driver_id_check_elig} does not exist")
           elif driver_choice==6:
                driver_id_rating=input("Enter driver Id to Add Rating to the driver:")
                id_dr=manager.find_driver(driver_id_rating)
                if id_dr is not None:
                    try:
                        rating_value=int(input("Enter Driver Rating:"))
                    except ValueError:
                        print("ValueError:You should Enter a number for ratinig")
                        continue
                    result=id_dr.add_rating(rating_value)
                    if result=="Invalid rating":
                        print(" Invalid Rating:You should enter Rating in range 1 and 5 ")
                    else:
                        print("Rating Added successufully")
                        print(f"Rating Number:{id_dr.number_rating}")
                        print(f"Average Rating: {id_dr.rating} ") 
                else:
                    print(f"Driver ID {driver_id_rating} Does not exist")
           elif driver_choice==7:
                driver_id_show=input("Enter Driver ID to show information:")
                id_dr=manager.find_driver(driver_id_show)
                if id_dr is not None:
                    show=id_dr.show_info()
                    print(show)
                else:
                    print(f"Driver ID {driver_id_show} does not exist")
           else:
                print("You choice to exit")
                break
    elif choice==4:
        while True:
            print("Taxis Menu")
            print("-"*25)
            print("1-Add taxi")
            print("2-Add car insurance")
            print("3-Add manufacturing date")
            print('4-Insurance expiry')
            print("5-Check car eligibility")
            print("6-update kilometres")
            print("7-change car status")
            print("8-Add last service date")
            print("9-Show car")
            print("10-Exit")
            try:
                taxi_choice=int(input("Enter number of your choice:"))
                if taxi_choice<1 or taxi_choice>10:
                    print("InvalidChoice:You shoud enter number in range 1 and 10")
                    continue
            except ValueError:
                print("You should enter number for choice")
                continue
            if taxi_choice==1:
                print("Follow all steps to Add a taxi")
                brand=input("Enter Taxi brand:")
                model=input("Enter Taxi model:")
                fuel=input("Enter taxi fuel sort:")
                taxi_id=input("Enter Taxi Id:")
                try:
                    kilometres=int(input("Enter taxi kilometres :"))
                except ValueError:
                    print("Invalid Value:You shoud enter numbers for kilometres")
                    continue
                new_taxi=Taxi(brand,model,fuel,kilometres,taxi_id)
                manager.add_taxi(new_taxi)
                print("New Taxi Added ")
            elif taxi_choice==2:
                taxi_id=input("Enter taxi ID to add car insurance:")
                id_ta=manager.find_taxi(taxi_id)
                if id_ta is not None:
                    car_insurance=input("Enter car insurance Code:")
                    id_ta.add_car_insurance(car_insurance)
                    print(f"car insurance: {car_insurance} Added")
                else:
                    print("Taxi ID Does not exist")
            elif taxi_choice==3:
                taxi_i=input("Enter taxi ID to Add Manufacturing date:")
                id_ta=manager.find_taxi(taxi_i)
                if id_ta is not None:
                    try:
                        manufacturing_date=datetime.strptime(input("Enter Manufacturing date :"),"%Y-%m-%d")
                        id_ta.set_manufacturing_date(manufacturing_date)
                        print(" Manufacturing date set")
                        continue
                    except ValueError:
                        print("ValueError: you should enter Manufacturing date in correct form 2026-10-12")
                        continue
                else:
                    print("Taxi ID does not exist")
            elif taxi_choice==4:
                taxi_id_insurance=input("Enter Taxi ID to add Insurance expiry :")
                id_ta=manager.find_taxi(taxi_id_insurance)
                if id_ta is not None:
                    try:
                        insurance_exp=datetime.strptime(input("Enter Insurance expiry(2026-10-18):"),"%Y-%m-%d")
                        id_ta.set_insurance_expiry(insurance_exp)
                        print("Insurance expiry date set")
                        continue
                    except ValueError:
                        print("ValueError:You should follow the form(2026-10-28) to set Insurance expiry ")
                        continue
                else:
                    print(f"Taxi ID {taxi_id_insurance} does not exist")
            elif taxi_choice==5:
                taxi_id_check=input("Enter Taxi ID to Check car eligibility : ")
                id_ta=manager.find_taxi(taxi_id_check)
                if id_ta is not None:
                    id_ta.car_eligibility(datetime.now())
                else:
                    print(f"Taxi ID {taxi_id_check} does not exist")
            elif taxi_choice==6:
                taxi_id_km=input("Enter Taxi ID to update kilometres ")
                id_ta=manager.find_taxi(taxi_id_km)
                if id_ta is not None:
                    try:
                        new_km=int(input("Enter new km to -update kilometres:"))
                        total_km=id_ta.update_kilometres(new_km)
                        print(f"update kilometres, new kilometres {total_km} ")
                        continue
                    except ValueError:
                        print("Value Error You should enter numbres for kilometres")
                        continue
                else:
                    print(f"Taxi ID {taxi_id_km} does not find")
            elif taxi_choice==7:
                taxi_check_status=input("Enter Taxi ID to check status :")
                id_ta=manager.find_taxi(taxi_check_status)
                if id_ta is not None:
                    taxi_status=input("Enter New Taxi status(available/busy/maintenance)  :")
                    result=id_ta.car_status(taxi_status)
                    print(f"Taxi Status : {result}")
                else:
                    print("Taxi ID does not exist")
            elif taxi_choice==8:
                taxi_id_last_srv=input('Enter Taxi ID to Add last service date:')
                id_ta=manager.find_taxi(taxi_id_last_srv)
                if id_ta is not None:
                    try:
                       last_srv_date=datetime.strptime(input("Enter last service date(2026-10-10):"),"%Y-%m-%d")
                       id_ta.last_service_date(last_srv_date)
                       print(f"last service date: {id_ta.service_date}")
                       continue
                    except ValueError:
                        print("ValueError:You should follow this form (2027-1-1) to Add last service date ")
                        continue
                else:
                    print(f"Taxi ID {taxi_id_last_srv} does not exist")
            elif taxi_choice==9:
                taxi_id_show=input("Enter Taxi ID to show information:")
                id_ta=manager.find_taxi(taxi_id_show)
                if  id_ta is not None:
                    show=id_ta.show_car_info()
                    print(show)
                else:
                    print(f"Taxi ID {taxi_id_show} does not exist")
            else:
                print("You choice to exit")
                break
    elif choice==5:
        fares=[]
        while True:
            print("Fare Menu")
            print("-"*25)
            print("1-Add Fare")
            print("2-Add Base Fare")
            print("3-Add price per km")
            print("4-Add price per minute")
            print("5-calculate fare")
            print("6-show Fare")
            print("7-Exit")
            try:
                fare_choice=int(input("Enter a number to start:"))
                if fare_choice<1 or fare_choice>7:
                    print("Invalid choice you should enter number in range 1 and 7")
                    continue
            except ValueError:
                print("ValueError:You should enter number for your choice")
                continue
            if fare_choice==1:
                print("Follow all steps to add fare")
                try:
                    new_distance=float(input("Enter Distance :"))
                    new_duration=float(input("Enter Duration:"))
                    new_fare=Fare(new_distance,new_duration)
                    fares.append(new_fare)
                    print("Fare Added")
                    continue
                except ValueError:
                    print("ValueError: You should enter numbers for distance and duration")
                    continue
            elif fare_choice==2:
                if len(fares)==0:
                    print("NO Fairs Available PLease Add Fair first!")
                    continue
                try:
                    new_base_fare=float(input("Enter Base Fare:"))
                except ValueError:
                    print("You Should enter number for base fare")
                    continue
                fare_object=fares[-1]
                fare_object.base_fare(new_base_fare)
                print("Base fare Added successfully")
                continue
            elif fare_choice==3:
                if len(fares)==0:
                    print("No Fairs available please Add fair first")
                    continue
                try:
                    price_km=float(input("Enter price per km:"))
                except ValueError:
                    print("ValueError:You should enter number for price per km")
                    continue
                fare_object=fares[-1]
                fare_object.price_per_km(price_km)
                print("Price per KM Add Successfully")
                continue
            elif fare_choice==4:
                if len(fares)==0:
                    print("No Fares Available please add fare first")
                    continue
                try:
                    fare_mi=float(input("Enter price per minute:"))
                except ValueError:
                    print("ValueError:You should enter number for price per minute")
                    continue
                fare_object=fares[-1]
                fare_object.price_per_minute(fare_mi)
                print("Fare per minute added successfully")
                continue
            elif fare_choice==5:
                if len(fares)==0:
                    print("NO Fares Available please Add fare first")
                    continue
                fare_object=fares[-1]
                print(f"Final Fare:{fare_object.calculate_fare()}")
                continue
            elif fare_choice==6:
                if len(fares)==0:
                    print("No Fares Available please add fare first!")
                    continue
                fare_object=fares[-1]
                print(fare_object.show_fare())
                continue
            else:
                print("You choice to exit")
                break
    elif choice==6:
        payments=[]
        while True:
           print("Payment Menu")
           print("-"*25)
           print("1-Add payment")
           print("2-process payment")
           print("3-check payment")
           print("4-show payment")
           print("5-Exit")
           try:
               payment_choice=int(input("Enter number of your choice to start:"))
               if payment_choice<1 or payment_choice>5:
                   print("InvalidChoice:You should enter number for your choice")
                   continue
           except ValueError:
               print("ValueError:You should enter number for your choice")
               continue
           if payment_choice==1:
               try:
                   new_amount=float(input("Enter amount:"))
               except ValueError:
                   print("You should enter number for amount")
                   continue
               payment_id=input("Enter payment ID:")
               payment_method=input("Enter payment method(Cach/credit card) :")
               new_payemnt=Payment(new_amount,payment_id,payment_method)
               payments.append(new_payemnt)
               print("Payment Added")
           elif payment_choice==2:
               payment_id_pr=input("Enter payment ID to process payment :")
               found=False
               for payment in payments:
                   if payment.payment_id.lower().strip()==payment_id_pr.lower().strip():
                       payment.process_payment()
                       print(f"Payment {payment_id_pr} is processed")
                       found=True
                       break
               if not found:
                   print(f"Payment ID {payment_id_pr} does not exist")
           elif payment_choice==3:
               payment_id_ch=input("Enter Payment ID to Check:")
               found=False
               for payment in payments:
                   if payment.payment_id.lower().strip()==payment_id_ch.lower().strip():
                       print(f"Payment {payment_id_ch} is cheked")
                       found=True
                       break
               if not found:
                   print(f"Payment ID {payment_id_ch} does not exist")
           elif payment_choice==4:
               payment_id_show=input("Enter Payment ID To show Payment:")
               found=False
               for payment in payments:
                   if payment.payment_id.lower().strip()==payment_id_show.lower().strip():
                        print(payment.show_info())
                        found=True
                        break
               if not found:
                   print(f"Payment ID does not Exist")
           else:
               print("You choice to exit")

               break
    elif choice==7:
        while True:
           print("Managment Menu")
           print("-"*25)
           print("Added options")
           print("-"*25)
           print("1-Add passenger")
           print("2-Add Driver")
           print("3-Add Taxi")
           print("4-Add trip")
           print("-"*25)
           print("Remove options")
           print("-"*25)
           print("5-Remove Passenger")
           print("6-Remove Driver")
           print("7-Remove Taxi")
           print("8-Remove Trip")
           print("-"*25)
           print("Show options")
           print("-"*25)
           print("9-show Passengers")
           print("10-show Drivers")
           print("11-show Taxis")
           print("12-show Trips")
           print("-"*25)
           print("find options")
           print("-"*25)
           print("13-Find Passenger")
           print("14-Find Driver")
           print("15-Find Taxi")
           print("16-Find trip")
           print("-"*25)
           print("update options")
           print("-"*25)
           print("17-Update Passenger")
           print("18-Update Driver")
           print("19-Update Taxi")
           print("20-Update Trip")
           print("-"*25)
           print("21-Exit")
           try:
               managment_choice=int(input("Enter number of your choice to start:"))
               if managment_choice<1 or managment_choice>21:
                   print("Invalid Choice:You should enter number in range 1 and 21")
                   continue
           except ValueError:
               print('ValueError:You should Enter number for your choice')
               continue
           if managment_choice==1:
               passenger_full_name=input("Enter passenger full name :")
               passenger_id=input("Enter passenger ID :")
               id_pa=manager.find_passenger(passenger_id)
               if id_pa is not None:
                   print(f"Passenger ID {passenger_id} IS already exist enter another passenger id to add")
               else:
                   new_passenger=Passenger(passenger_full_name,passenger_id)
                   manager.add_passenger(new_passenger)
                   print(f"Passenger Full Name: {passenger_full_name},ID {passenger_id} Added")
           elif managment_choice==2:
               driver_full_name=input("Enter Driver full name:")
               driver_id=input("Enter Driver ID:")
               driver_phone_number=input("Enter Driver phone number :")
               try:
                   driver_age=int(input("Enter driver age:"))
               except ValueError:
                   print("You should enter number for driver age !")
                   continue
               id_dr=manager.find_driver(driver_id)
               if id_dr is not None:
                   print(f"Driver ID {driver_id} Is already exist enter another driver id to add ")
               else:
                   new_driver=Driver(driver_full_name,driver_id,driver_phone_number,driver_age)
                   manager.add_driver(new_driver)
                   print(f"Driver {driver_full_name},ID:{driver_id} Added")
           elif managment_choice==3:
               brand=input("Enter car brand:")
               model=input("Enter car model:")
               fuel=input("Enter fuel sort :")
               taxi_id=input("Enter car ID:")
               try:
                   kilometres=float(input("Enter car kilometres:"))
               except ValueError:
                   print("ValueError:You should enter numbers for kilometres")
                   continue
               id_ta=manager.find_taxi(taxi_id)
               if id_ta is not None:
                   print(f"Taxi ID {taxi_id} is already exict enter another  taxi id to add ")
               else:
                   new_taxi=Taxi(brand,model,fuel,kilometres,taxi_id)
                   manager.add_taxi(new_taxi)
                   print(f"Taxi ID {taxi_id} is Added")
           elif managment_choice==4:
               trip_id=input("Enter trip ID:")
               point_a=input("Enter point A:")
               point_b=input("Enter point B:")
               try:
                   start_time=datetime.strptime(input("Enter start time (1998-1-1 09:01:01):"),"%Y-%m-%d %H:%M:%S")
                   end_time=datetime.strptime(input("Enter End time(1987-11-18 10:50:15):"),"%Y-%m-%d %H:%M:%S")
               except ValueError:
                   print("ValueError:You should enter start and time in correct form!!!")
                   continue
               id_tr=manager.find_trip(trip_id)
               if id_tr is not None:
                   print(f"Trip ID {trip_id} is already exist Enter another Trip ID to Add")
               else:
                   new_trip=Trip(trip_id,point_a,point_b,start_time,end_time)
                   manager.add_trip(new_trip)
                   print(f"Trip ID {trip_id} Added")
           elif managment_choice==5:
               passenger_id=input("Enter passenger ID to delete :")
               id_pa=manager.find_passenger(passenger_id)
               if id_pa is not None:
                   manager.remove_passenger(id_pa)
                   print(f"Passenger {passenger_id} removed")
               else:
                   print(f"Passenger ID {passenger_id} does not exist")
           elif managment_choice==6:
               driver_id=input("Enter driver ID to delete:")
               id_dr=manager.find_driver(driver_id)
               if id_dr is not None:
                   manager.remove_driver(id_dr)
                   print(f"Driver ID {driver_id} Removed")
               else:
                   print(f"Driver ID {driver_id} does not exist")
           elif managment_choice==7:
               taxi_id=input("Enter taxi ID to delete:")
               id_ta=manager.find_taxi(taxi_id)
               if id_ta is not None:
                   manager.remove_taxi(id_ta)
                   print(f"Taxi ID {taxi_id} Removed")
               else:
                   print(f'Taxi ID {taxi_id} does not exist')
           elif managment_choice==8:
               trip_id=input("Enter trip ID to delete:")
               id_tr=manager.find_trip(trip_id)
               if id_tr is not None:
                   manager.remove_trip(id_tr)
                   print(f"Trip ID {trip_id} Removed")
               else:
                   print(f"Trip ID {trip_id} does not exist")
           elif managment_choice==9:
               manager.show_passengers()
           elif managment_choice==10:
               manager.show_drivers()
           elif managment_choice==11:
               manager.show_taxis()
           elif managment_choice==12:
               manager.show_trips()
           elif managment_choice==13:
               passenger_id=input("Enter Passenger to find :")
               id_pa=manager.find_passenger(passenger_id)
               if id_pa is not None:
                   print(f"Passenger {passenger_id} is found")
                   print(id_pa.show_info())
               else:
                   print(f"Passenger {passenger_id} does not exist")
           elif managment_choice==14:
               driver_id=input("Enter Driver ID to find:")
               id_dr=manager.find_driver(driver_id)
               if id_dr is not None:
                   print(f"Driver {driver_id} is found")
                   print(id_dr.show_info())
           elif managment_choice==15:
               taxi_id=input("Enter Taxi ID to find:")
               id_ta=manager.find_taxi(taxi_id)
               if id_ta is not None:
                   print(f"Taxi ID {taxi_id} is found")
                   print(id_ta.show_car_info())
               else:
                   print(f"Taxi ID {taxi_id} does not exist")
           elif managment_choice==16:
               trip_id=input("Enter Trip ID to find:")
               id_tr=manager.find_trip(trip_id)
               if id_tr is not None:
                   print(f"Trip ID {trip_id} found")
                   print(id_tr.show_info())
           elif managment_choice==17:
               passenger_id=input("Enter Passenger ID :")
               new_name_passenger=input("Enter passenger full name:")
               update_pas=manager.update_passenger(passenger_id,new_name_passenger)
               if update_pas is not None:
                   print(f"Passenger {passenger_id} Updated")
               else:
                   print(f"Passenger ID {passenger_id} does not exist")
           elif managment_choice==18:
               driver_id=input("Enter Driver ID :")
               driver_n_full_name=input("Enter Driver full name:")
               driver_phone_number=input("Enter Driver phone number:")
               try:
                   driver_age=float(input("Enter driver age:"))
               except ValueError:
                   print("ValueError: You should enter a number for age!")
                   continue
               update_dr=manager.update_driver(driver_id,driver_n_full_name,driver_phone_number,driver_age)
               if update_dr is not None:
                   print(f"Driver {driver_id} updated")
               else:
                   print(f"Driver ID {driver_id} does not exist")
           elif managment_choice==19:
               taxi_id=input("Enter Taxi ID :")
               brand=input("Enter car brand:")
               model=input("Enter car model:")
               fuel=input("Enter fuel sort:")
               try:
                   kilometres=float(input("Enter Car kilometres:"))
               except ValueError:
                   print("ValueError:You should enter a number for kilometres")
                   continue
               update_ta=manager.update_taxi(taxi_id,brand,model,fuel,kilometres)
               if update_ta is not None:
                   print(f"Taxi ID {taxi_id} updated")
               else:
                   print(f"Taxi ID {taxi_id} does not exist")
           elif managment_choice==20:
               trip_id=input("Enter Trip ID :")
               point_a=input("Enter Point A :")
               point_b=input("Enter Point B :")
               try:
                   start_time=datetime.strptime(input("Enter Start time(2026-10-16 01:15:20) :"),"%Y-%m-%d %H:%M:%S")
                   end_time=datetime.strptime(input("Enter End time(2026-5-2 10:10:10): "),"%Y-%m-%d %H:%M:%S")
               except ValueError:
                   print("ValueError:You should follow The correct form (1987-1-1 12:20:05)!")
                   continue
               update_tr=manager.update_trip(trip_id,point_a,point_b,start_time,end_time)
               if update_tr is not None:
                   print(f"Trip ID {trip_id} is Updated")
               else:
                   print(f"Trip ID {trip_id} does not exist")
           else:
               print("You choice to exist")
               break
    elif choice==8:
        my_inf=AboutAPP()
        print(my_inf.Show_inf())          
    else: 
        print("You press exit")
        break




      

    
        

    
        

        

        
        

    
   



     
        
        
