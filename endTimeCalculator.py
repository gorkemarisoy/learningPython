﻿hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

 
endhour = ((hour*60+mins+dura)//60)%24  #total mins division to 60 mins and module of 24 hours
endmin = (hour*60+mins+dura)%60         #total mins leftover when divided into 60

print(str(endhour)+":"+str(endmin))