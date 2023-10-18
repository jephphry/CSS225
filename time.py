currentTime = str(input("What is the current time (in hours 0-23)?"))
waitTime = str(input("How many hours do you want to wait"))

currentTime = int(currentTime)
waitTime = int(waitTime)

finalTime = currentTime + waitTime
print(finalTime)
