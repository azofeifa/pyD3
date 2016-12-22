import HTML
import random
import sys

def main():
	ax 	= HTML.axes()

	x 		= range(5)
	y 		= [i+random.uniform(-10,10)  for i in x]
	labels = ["A", "B", "C", "D","E"]
	sizes  = [10,1,4,7,100]
	colors = ["red", "steelblue", "green", "green", "red"]
	alphas = [1.0,1.0,0.7,0.8,0.1]

	ax.scatter(x,y,lbls=labels, size=sizes, color=colors,alpha=alphas)

	ax.set_xlabel("N",fontsize=30)
	ax.set_xtick_res(25,fontsize=20)
	ax.set_ylabel("MD Score",fontsize=30)
	ax.savefig("test.html")
	ax.show()
	
	return True
	
if __name__ == "__main__":
	main()
