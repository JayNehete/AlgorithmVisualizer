import sys
import time
from colors import *

def merge_sort(array,first,last,barDraw,timediff):
	start = time.time()
	merge_sort2(array, 0, len(array)-1,barDraw,timediff)
	end = time.time()
	barDraw(array, [green for _ in range(len(array))])
	print("Time taken by Merge Sort here is :- ",(end-start))
	
def merge_sort2(array, first, last, barDraw, timediff):
	if first < last:
		middle = (first + last)//2
		merge_sort2(array, first, middle, barDraw, timediff)
		merge_sort2(array, middle+1, last, barDraw, timediff)
		merge(array, first, middle, last, barDraw, timediff)
		barDraw(array,[dblue if x>=first and x<middle else yellow if x==middle else red if x>middle and x<=last else turquoise for x in range(len(array))])
		time.sleep(timediff)
	# barDraw(array, [green for _ in range(len(array))])
		

def merge(array, first, middle, last, barDraw, timediff):
	L = array[first:middle+1]
	R = array[middle+1:last+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i = j = 0
	
	for k in range (first, last+1):
		if L[i] <= R[j]:
			array[k] = L[i]
			i += 1
		else:
			array[k] = R[j]
			j += 1

	# while i < len(left) and j < len(right):
	# 	if left[i] < right[j]:
	# 		array[k] = left[i]
	# 		i += 1
	# 	else:
	# 		array[k] = right[j]
	# 		j += 1
	# 	k += 1

	# while i < len(left):
	# 	array[k] = left[i]
	# 	i += 1
	# 	k += 1

	# while j < len(right):
	# 	array[k]=right[j]
	# 	j += 1
	# 	k += 1

	
	