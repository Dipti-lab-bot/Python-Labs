#Lab1
#Task1
#Create Variables
train_name="Rajdhani Express"
train_number=12951
source_station="Mumbai"
destination_station="Delhi"
ticket_price=2450.75

#Task2
#Display it
print("Welcome To Indian Railway Reservation System")
print("Train_Name:",train_name)
print("Train_Number:",train_number)
print("Source_Station:",source_station)
print("Ticket_Price:",ticket_price)

#Identify its data types
print(type(train_name))
print(type(train_number))
print(type(source_station))
print(type(ticket_price))

#create identifier & literal 
Passenger_Name="Rahul Sharma"
Seat_Number="B2-45"
Is_Confirmed=True

#Type _Casting 

#Float to integer
ticket_price_integer=int(ticket_price)
print(type(ticket_price_integer))

#integer data to string 
train_number_string=str(train_number)
print(type(train_number_string))


#Task5:-

# #Railway Reservation output System

#Passenger Information
passenger_name="Rahul Sharma"

#Ticket_confirmation_status
#confirmation_status=True


#Task6:-
Passenger_Name="Rahul Sharma"
Seat_Number="B2-45"
confirmation_status="Confirmed"

#Display Ticket
print("------Railway Ticket-----")
print("passenger Name:",Passenger_Name)
print("Seat_Number:",Seat_Number)
print("Ticket Status:",confirmation_status)
print("--------------------------")

# Lab 2
#Task1:Store Passenger Details
passenger_name="Rahul Sharma" 
passenger_age=28
gender="male"
mobile_number=9876543210

#Display Passenger Details using print()
print("Passenger Name:",passenger_name)
print("Passenger age:",passenger_age)
print("Gnder:",gender)
print("Mobile Number:",9876543210)

#Task2:Store ticket price & Seat Number

train_name =  "Rajdhani Express"
seat_number =  "B2-45"
ticket_price = 2450
journey_date = "25-May-2026"

#Display TIcket

print("Train_Name:",train_name)
print("Seat_Number:",seat_number)
print("Ticket_Price:",ticket_price)
print("Journey_Date:",journey_date)

#Task3:perform Ticket Fare Calculations

number_of_passenger = 3
ticket_price = 2450

Total_Fare=number_of_passenger*ticket_price
print("Total_Fare:",Total_Fare)

#Task4:Calculate GST on Ticket Fare 

gst_percentage=5
gst_amount=(Total_Fare*gst_percentage)/100
print("Gst_Amount:",gst_amount)

Total_Payable_Amount=Total_Fare + gst_amount
print("Total_Amount:",Total_Payable_Amount)

#Task 5 

#Display Complete Railway Ticket Info

print("---Indian Railway Ticket---")
print("Passenger Name:",passenger_name)
print("Train_Name:",train_name)
print("Seat_Number:",seat_number)
print("Journey_Date:",journey_date)
print("Passengers:",number_of_passenger)
print("Ticket_Fare:",Total_Fare)
print("Gst_Amount:",gst_amount)
print("Total_Amount:",Total_Payable_Amount)
print("------------------")

#Lab4
#Task1:Build Basic Ticket Checker 
passenger_name="Rahul Sharma"
ticket_status="Confirmed"

if ticket_status=="Confirmed":
    print("Ticket is Confirmed")

#Task2 : if else ticket for verification Apply

Waiting_List=3

if(Waiting_List==0):
    print("Ticket Is Confirmed")
else:
    print("Ticket is in waiting list")

#Use Elif Statemnet for multiple Ticekt Condition

ticket_status="RAC"

if ticket_status=="Confirmed":
    print("seat allocated sucessfully")
elif ticket_status=="RAC":
    print("partial Reservation Available" )
else:
    print("ticket is in waiting list ")

#Understanding indention python 
age=65
if age>=60:
   print("Passenger is eligible for Senior Citizenship Dsicount")

#Apply Logical Operators in Railway System 
age=65
is_ticket_confirmed=True

if age>=60 and is_ticket_confirmed == True:
       print("passenge is eligible for senior citizen Benifits ")

#Task6:Build Final Railway Tcket Validation  System 

#Create passenger Payment Details 
ticket_status="confirmed"
payment_status="paid"

#Apply Combined condition for logical Operator
if ticket_status=="confirmed" and payment_status=="paid":
    print("Ticket status is booked ")
elif ticket_status=="RAC":
    print(" partially seat available")
else:
    print("Booking Pending")

#Lab5
#Task1:Using AND operator

passenger_age = 25
ticket_confirmed=True

if passenger_age>=18 and ticket_confirmed == True:
    print("passenger Eligible for travel")

#Task2:Using OR Operator

confirmed_seat=False
rac_seat=True

if confirmed_seat==True or rac_seat==False:
   print("Reservation Available")

#Task3 Using NoT Operator

ticket_cancelled=False

if not ticket_cancelled:
    print("Ticket is active")

#Task4 Apply Reservation Rules for senior citizens

passenger_age=65
payment_completed=True

if passenger_age>=60 and payment_completed==True:
    print("senior Citizen Reservation Approved ")

#Build Ticket Confirmation System

available_seats=5
payment_status=True

if available_seats>0 and payment_status==True:
    print("Ticket Confirmed Sucessfully")
else:
    print("Reservation Failed")


#Task6:check passenger Eligiblity for Tatkal Booking 

valid_id_proof=True
booking_time_valid=True

if valid_id_proof==True and booking_time_valid==True:
       print("Tatkal Booking Is Allowed")
else:
        print("Tatkal Booking Is Not Allowed")

#Task7 Build Final Reservation Rule validation Module 

passenger_name="Rahul Sharma"
passenger_age=30
available_seats=2
payment_completed=True
ticket_cancelled=False

if(
    passenger_age>=18 and 
    available_seats>0 and
    payment_completed and
    not ticket_cancelled
):
    
    print("=============")
    print("Indian Railways Reservation ")
    print("==============")
    print("passenger Name:",passenger_name)
    print("Reservation Status:confirmed")

else:
    print("Reservation Failed")