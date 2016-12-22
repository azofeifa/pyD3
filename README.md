# pyD3
This library hopes to be a python wrapper for D3. In this way, pyD3 takes in as input data (in the form of a python list or numpy array) and exports an HTML file with D3 visualization capabilities. The main contribution here are tool tips: either for mousing over scatter points, line plots or bar charts. Below is a quick tutorial on use cases. 
## download / install
```
  git clone https://github.com/azofeifa/pyD3/
```

## scatter
First create some data
```
import HTML

x = range(5)
y = [i+random.uniform(0,1)  for i in x]
```
Maybe you have some associations to that data?
```
labels = ["A", "B", "C", "D","E"]
sizes  = [10,1,4,7,100]
colors = ["red", "steelblue", "green", "green", "red"]
alphas = [1.0,1.0,0.7,0.8,0.1]

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
Now importantly, this whatever.html has some basic interactive functionality: mouse over of scatter points. When a scatter point is touched, it will double in radius and a the associated label will appear; along with its x and y coordinates! All figure axes come with drag and zoom capabilities as well. So that's kinda neet! 


You can call ax.show() to just open that html file in the default browser (only supported for linux/mac OS. Below is a screen shot of path/to/whatever.html.

![Alt text](https://github.com/azofeifa/pyD3/blob/master/images/ScatterShot.jpeg)

Last but not least you can set x axis and y-axis labels as such
```
ax.set_xlabel("N", fontsize=20)
ax.set_ylabel("MD Score", fontsize=30)
```















## plot

## bar
