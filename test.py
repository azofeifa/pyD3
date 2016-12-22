import HTML
import random
import sys

def main():
	ax 	= HTML.axes()
	N 		= 10
	x 		= range(N)
	y 		= [i+random.uniform(0,1)  for i in x]

	ax.scatter(x,y)
	ax.set_xlabel("N",fontsize=30)
	ax.set_xtick_res(25,fontsize=20)
	ax.set_ylabel("MD Score",fontsize=30)
	ax.savefig("test.html")
	ax.show()
	return True
	
if __name__ == "__main__":
	#main()
	main_2()






