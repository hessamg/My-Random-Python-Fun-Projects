import webbrowser
import time

count=0
print("the program started on " +time.ctime())
while count<3:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=5k_T_NDwT9I")
    count = count + 1    

