import time
from colors import *

def insertion_sort(array,barDraw,timediff):
	start = time.time()
	n = len(array)
	for i in range(1,n):
		key = array[i]
		j=i-1

		barDraw(array,[dblue if x==i else turquoise for x in range(n)])
		time.sleep(timediff)
		while(j>=0 and key<array[j]):
			barDraw(array,[yellow if x==j or x==j+1 else turquoise for x in range(n)])
			time.sleep(timediff)
			array[j+1] = array[j]
			j-=1
		array[j+1] = key
		barDraw(array,[red if x==j+1 or x==j+2 else turquoise for x in range(n)])
		time.sleep(timediff)
	
	barDraw(array, [green for _ in range(n)])
	end = time.time()
	print("Time taken by Insertion Sort here is :- ",(end-start))