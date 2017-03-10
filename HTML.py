from math import isnan,isinf
from templates import temp
import os,numpy as np,pandas as pd
class option:
	def __init__(self, identifier , data, Type):
		self.identifier 	= identifier
		self.data 	= data
		self.type 	= Type
	def write(self):
		STR = "var " + self.identifier + "="
		if self.type=="list":
			f 	= lambda x : "\"" +str(x)+ "\"" 
			return STR+ "[" + ",".join(map(f, self.data)) + "]"
		elif self.type=="numerical":
			return STR+str(self.data)
		elif self.type=="string":
			return STR+"\""+str(self.data)+"\""
		print "Warning option: ", self.data, " was not given a type"
		return ""

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
		self.HMAP 			= False
		self.NET 			= False
		self.T 				= temp()

		'''
			D is the raw python data input
			data is the string converted for javascript
		'''
		self.D 				= None
		self.data 			= None

		self.available=dict([(c,1) for c in ("green", "red", "blue", "purple", "black", "grey", "yellow", "orange")])


		self.options 	= list()

		'''
			Network Specific stuff!
		'''
		self.nodes, self.links 	= dict(),list()


	def __str__(self):
		return "pyD3 axes object"
	def __del__(self):		
		pass
	'''
		this data will largely be shared regardless of module
	'''
	def set_title(self, lbl, fontsize=30):
		self.options.append(option("title", lbl, "string"))
		self.options.append(option("fontsize_title",fontsize, "numerical"))
	def set_xlabel(self, lbl, fontsize=30):
		self.options.append(option("xaxis_lbl", lbl, "string"))
		self.options.append(option("fontsize_label_x",fontsize, "numerical"))
	def set_ylabel(self, lbl, fontsize=30):
		self.options.append(option("yaxis_lbl", lbl, "string"))
		self.options.append(option("fontsize_label_y",fontsize, "numerical"))
	
	'''
		right now scatter() specific
	'''

	def set_xtick_res(self, N, fontsize=20):
		self.options.append(option("tick_xN", N, "numerical"))
		self.options.append(option("fontsize_ticks_x",fontsize, "numerical"))
	def set_ytick_res(self, N, fontsize=20):
		self.options.append(option("tick_yN", N, "numerical"))
		self.options.append(option("fontsize_ticks_y",fontsize, "numerical"))

	'''
		right now hmap() specific
	'''
	def set_xticklabels(self,lbls,fontsize=10,rot=0):
		'''
			check to make sure row labels are the same dimension 
			as the input matrix
		'''
		if self.HMAP and self.D is None:
			print "please call hmap() with a valid input matrix"
			return -1
		elif self.HMAP and self.D.shape[0]!=len(lbls) and len(lbls):
			print "your input size for the row labels does not equal"
			print "your row dimension of the matrix"
			return -1
		self.options.append(option("xlabels", lbls, "list"))
		self.options.append(option("xlabels_fontsize", fontsize, "numerical"))
		self.options.append(option("xlabels_rot",rot, 'numerical'))
	def set_column_labels(self,lbls,fontsize=2):
		'''
			check to make sure row labels are the same dimension 
			as the input matrix
		'''
		if self.HMAP and self.D is None:
			raise TypeError, "please call hmap() with a valid input matrix"
			return -1
		elif self.HMAP and self.D.shape[1]!=len(lbls) and len(lbls):
			raise TypeError, "your input size for the row labels does not equal\nyour row dimension of the matrix"
		self.options.append(option("ylabels", lbls, "list"))
		self.options.append(option("ylabels_fontsize", fontsize, "numerical"))
	def set_show_labels(self,var=0):
		self.options.append(option("SHOW_LABELS", int(var), "numerical"))
	def set_cmap(self, cmap):
		if cmap not in self.available:
			print "cmap color specified is not available only: "+ ", ".join(self.available.keys())
			return -1
		self.options.append(option("color", cmap, "string"))
	def set_aspect(self, lbl):
		if lbl in ("stretch", "square"):
			self.aspect 	= lbl
			self.options.append(option("aspect", lbl, "string"))
		else:
			print "unrecognized option for aspection"
			return -1
	def set_edge_width(self, N):
		self.options.append(option("edge_width", N, "numerical"))
	def set_edge_distance(self, N):
		self.options.append(option("edge_distance", N, "numerical"))
	def set_tooltip_font(self, N):
		self.options.append(option("tooltip_font", N, "numerical"))
	def set_edge_opacity(self, N):
		self.options.append(option("edge_opacity", N, "numerical"))
	def set_edge_strength(self,N):
		self.options.append(option("edge_strength", N, "numerical"))

	def set_pad(self, value):
		self.options.append(option("pad", value, "numerical"))
	def _set_node(self,a,node_size, color):
		self.nodes[a] 	= {"id":a, "size":node_size, "color":color }
	def add_edge(self, a,b,edge_color="grey", weight=1,size_a=10,size_b=10,color_a="steelblue",color_b="steelblue"):
		current 	= {"source":a,"target":b,"value":weight, "color":edge_color}
		self.links.append(current)
		self._set_node(a,size_a, color_a)
		self._set_node(b,size_b, color_b)



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
	def _is_num(self,x):
		if isnan(x) or isinf(x):
			return False
		return True

	def network(self,edge_width=3,edge_distance=300,tooltip_font=15,edge_opacity=0.1,edge_strength=-1000):
		'''
			check to make sure that the users has inputed some edges!
		'''
		assert len(self.links), "please add some edges via ax.add_edge(arg1,arg2,kargs**) before calling network" 
		self.data 			= dict()
		self.data["nodes"]= self.nodes.values()
		self.data["links"]= self.links
		self.data 			= str(self.data)


		self.set_edge_distance(edge_distance)
		self.set_edge_width(edge_width)
		self.set_tooltip_font(tooltip_font)
		self.set_edge_opacity(edge_opacity)
		self.set_edge_strength(edge_strength)
		self.NET 			= True


	def hmap(self, D,cmap="green",SHOW_LABELS=0,row_labels=[],
					col_labels=[],aspect="stretch",pad=1.0,xlabel="", ylabel=""):
		'''
			check to make sure this can be converted to numpy array
		'''

		try:
			D 	= np.array(D)
		except:
			raise TypeError, "can not interpret shape of input matrix"

		'''
			check to make sure everything is finite and not nan
		'''
		if len([1 for i in range(D.shape[0]) for j in range(D.shape[1]) if not self._is_num(D[i,j])]) >0:
			raise TypeError, "one or more numbers is nan or not finite"
		if cmap not in self.available:
			raise TypeError, "cmap color specified is not available only: "+ ", ".join(self.available.keys())

		'''
			check the labels
		'''
		if len(row_labels) and len(row_labels)!=D.shape[0]:
			print "xlabels were specified but they do not equal the row dimension" 
			return -1
		self.D 		= D
		self.data 	= str([[i for i in x] for x in D])
		self.HMAP 	= True

		self.set_xticklabels(row_labels)
		self.set_column_labels(col_labels)
		self.set_show_labels(var=SHOW_LABELS)
	
		self.set_cmap(cmap)
		self.set_aspect(aspect)
		self.set_pad(pad)
		self.set_xlabel(xlabel)
		self.set_ylabel(ylabel)

	def scatter(self, xs,ys,lbls="", alpha=1.0, color="steelblue", 
						size=5.0,title="",tick_xN=10,tick_yN=10,xlabel="",ylabel=""):
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

		self.set_title(title)
		self.set_xtick_res(tick_xN)
		self.set_ytick_res(tick_yN)
		self.set_xlabel(xlabel)
		self.set_ylabel(ylabel)
		self.data 	= str([ [xs[i], ys[i], self.lbls[i],self.color[i],self.alpha[i],self.size[i]] for i in range(self.N)])
		self.SCATTER= True 
	def plot(self):
		print "currently in development"
	def bar(self, D, xlabels=[], 
						series_labels=[],pad=10, color="steelblue",SHOW_xlabels=True):
		'''
			check to see if this is a pandas dataframe
		'''
		if type(D) is pd.core.frame.DataFrame:
			Series_labels 	= list(D.columns)
			
			Series_labels 	= [s for s in Series_labels if sum([ isinstance(i, (int, long, float)) for i in D[s]    ]) == D.shape[0]  ]
			A 					= D[Series_labels].as_matrix()
			if xlabels in list(D.columns):
				xlabels 	= list(D[xlabels])
			elif type(xlabels)!=list :
				print "Warning: " + str(xlabels) +" was not found in pandas dataframe object"
				xlabels 	= range(D.shape[0])
			if type(series_labels) == list and len(series_labels):
				print "Warning: Overwriting DataFrame attribute ids to specified series_labels" 
			else:
				series_labels 	= Series_labels

		else:
			A 	= np.matrix(D)
			if A.shape[0]==1:
				A 	= A.T

		'''
			check the x label dimensions
		'''
		if type(xlabels)==list and len(xlabels) > 0 and len(xlabels)!= A.shape[0] :
			raise TypeError, "xlabels specified as a list but does not equal the dimension of dataframe/input array" 
		elif type(xlabels)==list and len(xlabels) == 0:
			xlabels 	= range(A.shape[0])
		'''
			check the y/series label dimensions
		'''
		if not len(series_labels):
			series_labels 	= ["Series " + str(i+1) for i in range(A.shape[1])]
		elif type(series_labels)==list and len(series_labels)!= A.shape[1]:
			raise TypeError, "series_labels was specified as a list but does not equal the column dimension of dataframe/input array" 
		if type(color)==list and len(color)==A.shape[0]:
			A 	= [ [ A[i,j] for j in range(A.shape[1]) ] + [color[i]] for i in range(A.shape[0]) ]
		elif type(color)==str:
			A 	= [ [ A[i,j] for j in range(A.shape[1]) ] + [color] for i in range(A.shape[0]) ]
		elif type(color)==list and len(color)!=A.shape[0]:
			raise TypeError, "color was specified as a list but does not equal the dimension of dataframe/input array"

		self.set_xticklabels(xlabels)
		self.set_column_labels(series_labels)
		self.set_show_labels(var=int(SHOW_xlabels))
		self.set_pad(pad)
		self.set_xtick_res(len(xlabels))
		self.set_ytick_res(10)
		self.set_ylabel("")
		self.set_xlabel("")
		self.BAR 	= True
		self.data 	= str(A)


	def savefig(self, path_to_file):
		self.html 	= path_to_file
		try:
			FHW 		= open(path_to_file, "w")
		except:
			FHW 		= None
		assert FHW is not None, "could not open for writing: " + path_to_file
		if path_to_file.split(".")[-1]!="html":
			path_to_file+=".html"
		assert self.SCATTER or self.PLOT or self.BAR or self.HMAP or self.NET, "need to call either scatter(), bar(), hmap(), network(),plot() first"
		FHW.write(self.T.first_part(scatter=self.SCATTER, hmap=self.HMAP,bar=self.BAR,network=self.NET))
		FHW.write("var data="+self.data+";\n")

		FHW.write(";\n".join([o.write() for o in self.options]))
		FHW.write(self.T.second_part(scatter=self.SCATTER, hmap=self.HMAP,bar=self.BAR,network=self.NET))
	def show(self):
		os.system("open " + self.html)


def main_hmap():
	ax 	= axes()
	D 		= np.random.uniform(0,1,size=(20,10))


	ax.hmap(D,pad=1,aspect="stretch",cmap="green")

	ax.set_xlabel("Something Cool",fontsize=30)
	ax.set_ylabel("Something Cool 2",fontsize=30)
	#ax.set_show_labels(var=1)
	ax.savefig("test.html")
	ax.show()
def main_scatter():
	ax 	= axes()
	xs 	= np.random.uniform(0,1,100)
	ys 	= xs + np.random.normal(0,0.1,len(xs))

	labels=[str(i) for i in range(100)]
	df 			= pd.read_csv("/Volumes/Joeys_External/Motif_Displacements_RUNX1/SRR1745516_SRR1105736_225_175.csv")

	ax.scatter(np.log(df["counts"]+1),df["mds"],lbls=df["motif"])
	ax.set_xtick_res(10,fontsize=20)
	ax.set_ytick_res(10,fontsize=20)
	ax.set_xlabel("Counts")
	ax.set_ylabel("Change in MD score")
	ax.set_title("SRR1745516_SRR1105736_225_175")
	ax.savefig("SRR1745516_SRR1105736_225_175.html")
	ax.show()
def main_bar():
	LBL 	= "ABCDEFGHIJKLMNOP"
	ax 	= axes()


	D 		= np.random.uniform(0,10,size=(50,4))
	df 	= pd.DataFrame(D, columns=[ "Series "+ LBL[i%10] for i in range(D.shape[1]) ])

	ax.bar(df)
	ax.set_xlabel("Something X",fontsize=20)
	ax.set_ylabel("Something Y",fontsize=20)
	ax.set_xticklabels([ LBL[i%10] for i in range(D.shape[0]) ])


	ax.set_show_labels(var=True)
	ax.set_pad(1)
	ax.set_title("A Random Bar Chart")
	ax.savefig("test.html")
	ax.show()
def main_network():
	df 	= pd.read_csv("/Users/joazofeifa/Lab/Article_drafts/EMG_paper/files/STable_to_5_significant_TF_ct_associations.csv")
	ax 	= axes()
	for i,row in df.iterrows():
		motif,ct 	= row.motif, row.ct
		if row.pv < pow(10,-1):
			ax.add_edge(ct.replace("_", " "), motif.split("_")[1], 
				size_a=11,size_b=5,color_b="steelblue",color_a="green")

	ax.network(edge_strength=-40) 
	ax.savefig("SRR1552482_SRR1552480_425_350.html")
	ax.show()

if __name__ == "__main__":
	#main_hmap()
	main_scatter()
	#main_bar() d 
	#main_network()




