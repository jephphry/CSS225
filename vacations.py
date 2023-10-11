#jeff Almaraz

#10/10/23
#days of week
dow = ["Sunday,", "Monday", "Tuesday", "Wedneday", "Thursday", "Friday", "saturday"]

#start day
Startday = int(input("Enter the starting day number (0 for Sunday, 1 for Monday, etc.): "))

#length
stay = int(input("Enter the length of your stay in nights: "))

#return date
returnday = (Startday + stay) % 7

#result
print(f"You will return on a a {dow[returnday]}.")