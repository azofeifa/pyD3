from math import isnan,isinf
from templates import temp
import os
'''
Current js options

var yaxis_lbl           = "Y-axis-1111",
    xaxis_lbl           = "X-axis-val",
    font_label_x        = 25,
    font_label_y        = 25,
    font_ticks_x        = 20,
    font_ticks_y        = 20,
    tick_xN             = 10,
    tick_yN             = 10;

'''
class axes:
	def __init__(self,facecolor="white",grid=False):
		self.facecolor 	= facecolor
		self.grid 		 	= grid
		self.html 			= None 
		self.N 				= 0
		self.params 		= {}

		self.SCATTER 		= False
		self.PLOT  			= False
		self.BAR 			= False
		self.T 				= temp()

		self.params["xaxis_lbl"] 			= "";		self.params["yaxis_lbl"] 			= ""
		self.params["fontsize_label_x"] 	= "25";	self.params["fontsize_label_y"] 	= "25"
		self.params["fontsize_ticks_x"] 	= "20"; 	self.params["fontsize_ticks_y"] 		= "20"
		self.params["tick_xN"] 				="10"; 	self.params["tick_yN"] 				= "10"
		self.params["title"] 				= "";    self.params["fontsize_title"] 	= "10"
	def __str__(self):
		return "pyD3 axes object"
	def __del__(self):		
		pass
	def set_title(self, lbl, fontsize=10):
		self.params["title"] 	= lbl

	def set_xlabel(self, lbl, fontsize=10):
		self.params["xaxis_lbl"] 			= lbl
		self.params["fontsize_label_x"] 	= fontsize
	def set_ylabel(self, lbl, fontsize=10):
		self.params["yaxis_lbl"] 			= lbl
		self.params["fontsize_label_y"] 	= fontsize
	def set_xtick_res(self, N, fontsize=10):
		self.params["tick_xN"] 				= N
		self.params["fontsize_ticks_x"] 	= fontsize
	def set_ytick_res(self, N, fontsize=10):
		self.params["tick_yN"] 				= N
		self.params["fontsize_ticks_y"] 	= fontsize


	def _get_list(self, arg):
		if hasattr(arg, "__iter__"): #compare to self.N
			if len(arg)==self.N:
				return arg
			return None
		else:
			return [arg for i in range(self.N)]
	def _error(self, val, error):
		if val is None:
			assert False, error
		return True

	def scatter(self, xs,ys,lbls="", alpha=1.0, color="steelblue", size=5.0):
		'''
			check to make sure these are iterable
		'''
		
		assert hasattr(xs,"__iter__"), 'first argument is not iterable'
		assert hasattr(ys,"__iter__"), 'second argument is not iterable'
		
		'''
			check to make sure these are the same length;len(x)==len(y)
		'''
		
		assert len(xs)==len(ys), "first and second argument must be the same size"
		self.N 	= len(xs)
		
		'''
			check to make sure all the values in x and y are actually numbers
		'''
		
		assert len([1 for x in xs if isnan(x) or isinf(x) ]) == 0, "one or more of elements in argment 1 is not a number"
		assert len([1 for x in ys if isnan(x) or isinf(x) ]) == 0, "one or more of elements in argment 2 is not a number"
		
		'''
			check the others
				1) if they are numbers then create list size of x and y
				2) else check to make sure they are equal to xs and ys
		'''

		self.lbls 	= self._get_list(lbls)
		self._error(self.lbls, "the lbls keyword argument is iterable and does not equal dimensions of argument 1 and 2")

		self.color 	= self._get_list(color)
		self._error(self.color, "the color keyword argument is iterable and does not equal dimensions of argument 1 and 2")

		self.alpha 	= self._get_list(alpha)
		self._error(self.alpha, "the alpha keyword argument is iterable and does not equal dimensions of argument 1 and 2")

		self.size 	= self._get_list(size)
		self._error(self.size, "the size keyword argument is iterable and does not equal dimensions of argument 1 and 2")

		xs,ys 		= map("{0:.3f}".format,xs),map("{0:.3f}".format,ys)
		xs,ys 		= map(float,xs), map(float, ys)
		self.data 	= str([ [xs[i], ys[i], self.lbls[i],self.color[i],self.alpha[i],self.size[i]] for i in range(self.N)])
		self.SCATTER= True 
	def plot(self):
		print "currently in development"
	def bar(self):
		print "currently in development"
	def savefig(self, path_to_file):
		self.html 	= path_to_file
		try:
			FHW 		= open(path_to_file, "w")
		except:
			FHW 		= None
		assert FHW is not None, "could not open for writing: " + path_to_file
		if path_to_file.split(".")[-1]!="html":
			path_to_file+=".html"
		assert self.SCATTER or self.PLOT or self.BAR, "need to call either scatter(), bar(), or plot() first"
		FHW.write(self.T.first_part())
		FHW.write("var data="+self.data+";\n")
		FHW.write("var " + ",".join([str(x) + "=" +"\""+ str(y)+"\"" for x,y in zip(self.params.keys(), self.params.values())  ])+";\n" )
		if self.SCATTER:
			FHW.write(self.T.second_part_scatter())
	def show(self):
		os.system("open " + self.html)







