# pyD3
This library hopes to be a python wrapper for D3. In this way, pyD3 takes in as input data (in the form of a python list or numpy array) and exports an HTML file with D3 visualization capabilities. The main contribution here are tool tips: either for mousing over scatter points, line plots or bar charts. Below is a quick tutorial on use cases. 
## download / install
```
  git clone https://github.com/azofeifa/pyD3/
```
# Usage

## bar
First create some data to display as a bar chart. 
```
import numpy as np
y = np.random.uniform(0,1,7)
```

So now we have some really simple data that we'd like to visualize. The big thing when using any of these modules (bar,scatter, hmap) is that you have to create an axes object from the HTML module
```
import HTML
ax = HTML.axes()
```
ax now has access to some of the familar methods that a matplotlib axes would have acesses to. Stuff like set_title(str, font_size=10),set_xticklabeles([str,...,str], font_size=10) etc. A full description of the axes methods at the bottom of this page.
```

ax.bar(y)
'''
  set the x and y axis labels?
'''
ax.set_xlabel("Something X",fontsize=20)
ax.set_ylabel("Something Y",fontsize=20)

'''
  set the xticklabels?
'''
LBL 	= "ABCDEFGHIJKLMNOP"
ax.set_xticklabels([ LBL[i%10] for i in range(D.shape[0]) ])
'''
  do we want to display them
'''
ax.set_show_labels(var=True)
'''
  pad between adjacent bars
'''
ax.set_pad(10)
'''
  put on a title?
'''
ax.set_title("Some title",fontsize=40)

```
Now in order to render this is as an HTML file you need to call
```
ax.savefig("path/to/some/file.html)
```
and then you can call
```
ax.show()
```
to open it in a browser.

![Alt text](https://github.com/azofeifa/pyD3/blob/master/images/BarShot.jpeg)

Apart from a few other features, you can mouse over a specific rectangle and get a short little description about the data it is representing. 

A common occurrence though is if we had a multiple observations and a few measurments or features associated with each observation. Take for example, a netflix user. We might have information like name (this would be good for the set_xticklabels function), number of hours watched on Orange is the New Black, The Office etc.. In this way, we would make a matrix not a row vector. To page through each of these features, a drop down menu will appear in the upper left for which you can select The Office and the graph will adjust accordingly! 


```
ax = HTML.axes()
D  = np.random.uniform(0,10,size=(10,3) )
series = [ "Series "+ LBL[i%10] for i in range(D.shape[1]) ]

ax.bar(D,series_labels=series)

```














## scatter
First create some data
```
from pyD3 import HTML

x = range(5)
y = [i+random.uniform(0,1)  for i in x]
```
Maybe you have some associations to that data?
```
labels = ["A", "B", "C", "D","E"]
sizes  = [10,1,4,7,100]
colors = ["red", "steelblue", "green", "green", "red"]
alphas = [1.0,1.0,0.7,0.8,0.1]

ax     = HTML.axes()
ax.scatter(x,y,lbls=labels, size=sizes, color=colors,alpha=alphas)

```
Note you can set lbls, sizes,colors and alphas all equal to single value in which case all scatter points are set to that value; i.e.
```
ax.scatter(x,y,lbls="", size=10, color="red",alpha=1.0)
```
To save the associated HTML file.
```
ax.savefig("path/to/whatever.html")
```
Now importantly, this whatever.html has some basic interactive functionality: mouse over of scatter points. When a scatter point is touched, it will double in radius and the associated label (from lables in the above example) will appear; along with its x and y coordinates! All figure axes come with drag and zoom capabilities as well.  


You can call ax.show() to just open that html file in the default browser (only supported for linux/mac OS. Below is a screen shot of path/to/whatever.html.

![Alt text](https://github.com/azofeifa/pyD3/blob/master/images/ScatterShot.jpeg)

Last but not least you can set x axis and y-axis labels as such
```
ax.set_xlabel("N", fontsize=20)
ax.set_ylabel("MD Score", fontsize=30)
```


## plot
under development stay tuned
## bar
under development stay tuned









