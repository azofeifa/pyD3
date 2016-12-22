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






## plot

## bar
