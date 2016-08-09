import time
import webbrowser
x=0
no_of_breaks=5
print("current time is ",time.ctime())
while (x < no_of_breaks):
    time.sleep(2*60*60)
    x=x+1
    webbrowser.open("https://www.youtube.com/watch?v=DQ4mraAx23I")