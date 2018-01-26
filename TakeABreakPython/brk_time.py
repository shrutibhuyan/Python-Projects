import time
import webbrowser

print("This program started on "+time.ctime())

total_breaks = 3
break_count = 0


while (break_count < total_breaks):
       time.sleep(30)
       webbrowser.open("https://www.youtube.com/watch?v=GYFDRoJtfGM")
       break_count = break_count + 1
