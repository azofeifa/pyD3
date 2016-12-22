class temp:
	def __init__(self):
		pass
	def first_part(self):
		STR 	= '''
		<html>
		  <head>
		    <meta charset="utf-8">
		    <title>Visualization</title>
		    <!-- <link rel="stylesheet" href="scatter.css" charset="utf-8"> -->
		  </head>
		  <style>
		    div.tooltip { 
		      position: absolute; 
		      display:inline-block;    
		      text-align: center;     
		      padding: 5px;       
		      font: 16px sans-serif #FFFFFF;    
		      background: #282828 ; 
		      color: #FFFFFF;
		    }
		    rect {
		      fill: transparent;
		      shape-rendering: crispEdges;
		    }
		    .axis path,
		    .axis line {
		      fill: none;
		      stroke: rgba(0, 0, 0, 0.1);
		      shape-rendering: crispEdges;
		    }

		    .axisLine {
		      fill: none;
		      shape-rendering: crispEdges;
		      stroke: rgba(0, 0, 0, 0.5);
		      stroke-width: 2px;
		    }
		    circle {
		      fill: steelblue;
		    }
		  </style>

		  <body>
		    <div id="scatter"></div>      
		    <script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
		    <script src="http://labratrevenge.com/d3-tip/javascripts/d3.tip.v0.6.3.js"></script>
		    <script>
		'''
		return STR
	def second_part_scatter(self):
		STR 	= '''
		      var margin                  = { top: 50, right: 100, bottom: 100, left: 100 },
                  outerWidth      = window.innerWidth,
                  outerHeight     = window.innerHeight,
                  width           = outerWidth - margin.left - margin.right,
                  height          = outerHeight - margin.top - margin.bottom;


		      var xMin        = d3.min(data, function(d) { return d[0]; });
		      var xMax        = d3.max(data, function(d) { return d[0]; })

		      var yMin        = d3.min(data, function(d) { return d[1]; });
		      var yMax        = d3.max(data, function(d) { return d[1]; })

		      var Rx          = 0.05*(xMax - xMin),Ry=0.05*(yMax - yMin)

		      var x           = d3.scale.linear()
		                          .domain([xMin-Rx, xMax+Rx])
		                          .range([ 0, width ]) ;

		      var y           = d3.scale.linear()
		                          .domain([yMin-Ry, yMax+Ry] )
		                          .range([ height, 0 ]) ;

		      var zoomBeh = d3.behavior.zoom()
		                      .x(x)
		                      .y(y)
		                      .scaleExtent([0, 500])
		                      .on("zoom", zoom);

		      var svg = d3.select("#scatter")
		                  .append("svg")
		                  .attr("width", outerWidth)
		                  .attr("height", outerHeight)
		                  .append("g")
		                  .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
		                  .call(zoomBeh);



		      // draw the x axis
		      var xAxis = d3.svg.axis()
		                    .scale(x)
		                    .orient('bottom').tickSize(-height).ticks(tick_xN)

		      // draw the y axis
		      var yAxis = d3.svg.axis()
		                    .scale(y)
		                    .orient('left').tickSize(-width).ticks(tick_yN);

		      /*
		        xaxis and x font tick size
		      */ 

		      svg.append("g")
		          .attr("transform", "translate(0," + height + ")")
		          .classed("x axis", true)
		          .call(xAxis)
		          .style("font-size", fontsize_ticks_x)
		          .append("text")
		          .classed("labelx", true)
		          .attr("x", width)
		          .attr("y", margin.bottom/1.5)
		          .style("text-anchor", "end")
		          .text(xaxis_lbl);

		      /*
		        yaxis and y font tick size
		      */ 

		      svg.append("g")
		          .classed("y axis", true)
		          .call(yAxis)
		          .style("font-size", fontsize_ticks_y)
		          .append("text")
		          .classed("labely", true)
		          .attr("x", 0)
		          .attr("y", -margin.bottom/1.5 )
		          .attr("transform", "rotate(-90)")
		          .style("text-anchor", "end")
		          .text(yaxis_lbl);

		      /*
		        Set the font size of the x and y labels
		      */ 

		      svg.selectAll(".labelx")   
		          .style("font-size", fontsize_label_x + "px");

		      svg.selectAll(".labely")   
		          .style("font-size", fontsize_label_y + "px");


		      svg.append("rect")
		          .attr("width", width)
		          .attr("height", height);

		      /*
		        ticks
		      */
		      

		      var tip = d3.tip()
		          .attr('class', 'd3-tip')
		          .html(function(d) {
		            return d[2];
		          });

		      svg.call(tip);

		      var objects = svg.append("svg")
		                .classed("objects", true)
		                .attr("width", width)
		                .attr("height", height);

		      objects.append("svg:line")
		              .classed("axisLine hAxisLine", true)
		              .attr("x1", 0)
		              .attr("y1", 0)
		              .attr("x2", width)
		              .attr("y2", 0)
		              .attr("transform", "translate(0," + height + ")");

		      objects.append("svg:line")
		              .classed("axisLine vAxisLine", true)
		              .attr("x1", 0)
		              .attr("y1", 0)
		              .attr("x2", 0)
		              .attr("y2", height);

		      var div = d3.select("#scatter").append("div") 
		                  .attr("class", "tooltip")       
		                  .style("opacity", 0);

		      objects.selectAll(".circle")
		              .data(data)
		              .enter().append("circle")
		              .classed("circle", true)
		              .attr("transform", transform)
		              .style("fill", function(d){
		                return d[3];
		              })
		              .style("opacity", function(d){
		                return d[4];
		              })      
		              .attr("r", function(d){
		                return d[5];
		              })
		              .on("mouseover", function(d,i)
		              {
		                  d3.select(this).transition()
		                        .duration(10)   
		                        .attr("r",d[5]*2);
		                  d3.select(".d3-tip")
		                      .transition()
		                      .duration(600)
		                      .style("opacity",1);
		                  div.style("left", d3.event.clientX  + "px")
		                      .style("top",  d3.event.clientY - 50 + "px")
		                      .transition()    
		                      .duration(200)    
		                      .style("opacity", 1.0)
		                  div.html(d[2] + " (" + d[0] + "," + d[1] +  ")")
		              })
		              .on("mouseout", function(d,i)
		              {
		                  d3.select(this).transition()
		                        .duration(100)   
		                        .attr("r",d[5])
		                  d3.select(".d3-tip")
		                    .transition()
		                      .duration(600)
		                      .style("opacity",0)
		                  div.transition()    
		                      .duration(200)    
		                      .style("opacity", 0); 

		              });


		      function zoom() {
		        svg.select(".x.axis").call(xAxis);
		        svg.select(".y.axis").call(yAxis);

		        svg.selectAll(".circle")
		        .attr("transform", transform);
		      }

		      function transform(d) {
		        return "translate(" + x(d[0]) + "," + y(d[1]) + ")";
		      }



		    </script>
		  </body>
		</html>
		'''
		return STR		

