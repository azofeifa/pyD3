import HTML
import random
import sys
import numpy as np
def main_scatter():
	ax 	= HTML.axes()

	x 			= range(15)
	y 			= [i+random.uniform(-1,1)  for i in x]
	labels 	= ["This is: " + str(i) for i in range(15)]
	
	sizes  	= np.random.uniform(0,1,15)*10

	ax.scatter(x,y,lbls=labels, size=sizes)

	ax.set_xlabel("N",fontsize=30)
	ax.set_xtick_res(25,fontsize=20)
	ax.set_ylabel("MD Score",fontsize=30)
	ax.savefig("test.html")
	ax.show()
	
	return True
def main_hmap():
	ax 	= HTML.axes()
	D 		= np.random.uniform(0,1,size=(20,6))

def main():
	test_scatter 	= False
	test_hmap 		= True
	if test_hmap:
		main_hmap()

	if test_scatter:
		main_scatter()

if __name__ == "__main__":
	main()
