# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def timeConversion(time):
    
    a=time[8:10]

    if time[0:2]=="12"and a=="PM":
        new=time
    elif time[0:2]=="12" and a=="AM":
        new=time.replace("12","00")
  
    elif(a=="AM"):
        new=time
    else:
        b=int(time[0:2])+12
        new=time.replace(time[0:2],str(b),1)

    if a=="AM":
        x=new.replace("AM","")
    else:
        x=new.replace("PM","")

    return x
