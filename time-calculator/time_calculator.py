import math

def add_time(start, duration, day = ""):
   lookupDays = {"monday" : 1, "tuesday" : 2 , "wednesday" : 3, "thursday" : 4, "friday" : 5, "saturday" : 6, "sunday" : 7}
   outputDays = {1 : "Monday" , 2 : "Tuesday" , 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday", 7 : "Sunday"}
  # split up al the values

   startHour = start.split(":")[0]
   startMinute = start.split(":")[1].split()[0]
   am_pm = start.split()[1]
   durationHour = duration.split(":")[0]
   durationMinute = duration.split(":")[1]


  # change all to minutes
   tStartMinutes = (int(startHour) * 60) + int(startMinute)
   tDurationMinutes = (int(durationHour) * 60) + int(durationMinute)


  
  # add pm hours 
   if am_pm == "PM":
     ntStartMinutes = tStartMinutes + (12 * 60)
   elif am_pm == "AM":
     ntStartMinutes = tStartMinutes 
     

  # add them all tgt 
   tMinutes = ntStartMinutes + tDurationMinutes
  
  #convert back to real timing
   endHour = math.floor(tMinutes / 60)
   endMinute = tMinutes % 60

  #days elapsed 
   daysElapsed = math.floor(endHour / 24)

   finalHour = endHour % 24
   if finalHour == 0:
     finalHour = 24

   if finalHour <12:
     amorpm = "AM"
   elif finalHour < 24:
     amorpm = "PM"
     finalHour = finalHour - 12
   elif finalHour == 24:
     amorpm = "AM"

  #catch the anything that ends up as 24 hours 
   if finalHour == 24 or finalHour == 0:
     finalHour = 12

   #parse and output 
   endTime = str(finalHour) + ":" + f"{endMinute:02d}" + " " + amorpm
   if day == "":
     if daysElapsed == 0:
       return endTime
     elif daysElapsed == 1:
       output = str(endTime) + " (next day)"
       return output
     elif daysElapsed > 1:
       daysElapsedStr = " (" + str(daysElapsed) + " days later)"
       output = str(endTime) + str(daysElapsedStr)
       return output
   else:
     dayLower = str(day).lower()
     currentDayInt = (lookupDays[dayLower] + daysElapsed) % 7
     if currentDayInt == 0:
       currentDayInt = 7
     currentDay = outputDays[currentDayInt]
    
     if daysElapsed == 0:
       output = str(endTime) +", " + str(currentDay)
       return output 
     elif daysElapsed == 1:
       output = str(endTime) + ", " +str(currentDay) + " (next day)"
       return output 
     elif daysElapsed > 1:
       daysElapsedStr = " (" + str(daysElapsed) + " days later)"
       output = str(endTime) + ", " +str(currentDay) + str(daysElapsedStr)
       return output
     


