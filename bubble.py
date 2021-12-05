from colors import *
import time


def Bubble(array,barDraw,timediff):
	start = time.time()
	n = len(array)

	for i in range(n-1):

		for j in range(n-i-1):

			if(array[j]>array[j+1]):
				barDraw(array,[yellow if x==j or x==j+1 else turquoise for x in range(n)])
				time.sleep(timediff)
				array[j], array[j+1] = array[j+1], array[j]
				barDraw(array,[red if x==j or x==j+1 else turquoise for x in range(n)])
				time.sleep(timediff)

			else:
				barDraw(array,[dblue if x==j or x==j+1 else turquoise for x in range(n)])
				time.sleep(timediff)
	
	barDraw(array, [green for _ in range(n)])
	end = time.time()
	print("Time taken by Bubble Sort here is :- ",(end-start))				