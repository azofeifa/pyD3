class temp:
	def __init__(self):
		pass
	def first_part(self,scatter=False,hmap=False,bar=False):
		if scatter:
			return self.first_part_scatter()
		if hmap:
			return self.first_part_hmap()
		if bar:
			return self.first_part_bar()
	def second_part(self,scatter=False,hmap=False,bar=False):
		if scatter:
			return self.second_part_scatter()
		if hmap:
			return self.second_part_hmap()
		if bar:
			return self.second_part_bar()

	def first_part_hmap(self):
		STR 	= '''
		<html>
		  <head>
		    <meta charset="utf-8">
		    <title>pyD3</title>
		    <!-- <link rel="stylesheet" href="scatter.css" charset="utf-8"> -->
		  </head>
		  <style>
		      div.tooltip { 
		      position: absolute; 
		      display:inline-block;    
		      text-align: center;     
		      padding: 15px;       
		      font: 6px sans-serif #FFFFFF;    
		      background: #282828 ; 
		      color: #FFFFFF;
		    }



		  </style>

		  <body>
		    <div id="scatter"></div>      

		    <script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>

		    <script>
		      function range(N){
		        var L = [];
		        for (i = 0 ; i < N ; i++){
		          L.push(i);
		        }
		        return L
		      }
		      /*
		        This is the pertinent data
		      */
		'''
		return STR
	def first_part_scatter(self):
		STR 	= '''
		<html>
		  <head>
		    <meta charset="utf-8">
		    <title>pyD3</title>
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
	def first_part_bar(self):
		STR ='''	
			<!DOCTYPE html>
				<html>
				  <head>
				    <meta charset="utf-8">
				    <title>pyD3</title>
				    <!-- <link rel="stylesheet" href="scatter.css" charset="utf-8"> -->
				  </head>
				  <body>
				    <div id="scatter"></div>      
				        <style>
				            .toolTip {
				              position: absolute;
				              display: none;
				              height: auto;
				              background: none repeat scroll 0 0 #ffffff;
				              background: rgba(0, 0, 0, 0.8);
				              color: #fff;
				              line-height: 1;
				              font-weight: bold;
				              padding: 6px;
				              font-size: 10px;

				              border-radius: 2px;
				              text-align: left;
				              content: "\25BC";
				            }
				        </style>

				    <script src="https://d3js.org/d3.v4.js"></script>
				    <script>
		'''
		return STR


	def second_part_scatter(self):
		STR = '''
		      var margin                  = { top: 100, right: 300, bottom: 100, left: 300 },
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


		      svg.append("text")
		        .attr("x", (width / 2))             
		        .attr("y", 0 - (margin.top / 2))
		        .attr("text-anchor", "middle")  
		        .style("font-size", fontsize_title) 
		        .text(title);

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
		          .attr("y", -margin.bottom )
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
		                  div.html(d[2]  )
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
	def second_part_hmap(self):
		STR = '''
			console.log(SHOW_LABELS)
	      var n = data.length,m = data[0].length;
	      if (!xlabels.length || !ylabels.length){
	        xlabels = range(n),ylabels = range(m);
	      }
	      /*
	        unroll data matrix
	      */
	      var Data=[];
	      var lbls=[];
	      for (i = 0 ; i < n ; i++){
	        for (j = 0 ; j < m ; j++){
	          Data.push([data[i][j],j,i]);
	          lbls.push(xlabels[i]+","+ylabels[j] )
	        }
	      }
	      var min   = d3.min(data, function(d){ return d3.min(d)} );
	      var max   = d3.max(data, function(d){ return d3.max(d)} );


	      /*
	        this is the colormap;
	        this is NOT diverging!!
	        will need to work on that soonish
	      */
	      var color = d3.scale.linear()
	                .domain([min,max])
	                .range(["white", color]);

	      var outerWidth        = window.innerWidth,
	            outerHeight     = window.innerHeight,
	            Bottom          = 100,
	            Top             = 100;
	            Left 	 			 = 100;
	            Right           = 100;

	      var cell_width  = (outerWidth  -(Left + Right) ) /m;
	      var cell_height = (outerHeight -(Bottom+ Top) )/n;


	      if (aspect=="square"){
		      if (cell_width < cell_height){
			      cell_height= cell_width
		      }
		      else{
			      cell_width =cell_height

		      }

		   }

	      var margin                  = { top: Top, right: Right, bottom: Bottom, left: Left };
	                  
	                  width           = outerWidth - margin.left - margin.right,
	                  height          = outerHeight - margin.top - margin.bottom;



	      var x           = d3.scale.linear()
	                          .domain([0 , m ])
	                          .range([ 0, cell_height*m ]) ;

	      var y           = d3.scale.linear()
	                          .domain([0 , n  ] )
	                          .range([ 0,cell_width*n ]) ;

	      var padding=-10


	      var svg = d3.select("#scatter")
	                  .append("svg")
	                  .attr("width", outerWidth)
	                  .attr("height", outerHeight)
	                  .append("g")
	                  .attr("transform", "translate(" + margin.left + "," + margin.top + ")")


	      var div = d3.select("#scatter").append("div") 
	                  .attr("class", "tooltip")       
	                  .style("opacity", 0)
	                  .style("font-size", 30);


	      var Rx          = 0.05*(m),Ry=0.05*(n)


	      var grp = svg.selectAll('g')
	              .data(Data)
	              .enter()
	              .append('rect')
	              .attr('transform',transform)
	              .attr("fill", function(d,i){
	                return color(d[0]);
	                })
	              .attr('width',  cell_width-pad )
	              .attr('height', cell_height-pad )
	              .on("mouseover", function(d,i)
	              {
	                d3.select(this).transition()
	                      .duration(100)   
	                      .attr('fill', "grey")
	                d3.select(".d3-tip")
	                      .transition()
	                      .duration(600)
	                      .style("opacity",1);
	                  div.style("left", d3.event.clientX + 50 + "px")
	                      .style("top",  d3.event.clientY - 50 + "px")
	                      .transition()    
	                      .duration(200)    
	                      .style("opacity", 1.0)
	                  div.html(d[0].toString().match(/^-?\d+(?:\.\d{0,2})?/)[0] +"<br>(" + lbls[i]+ ")" )

	              })
	              .on("mouseout", function(d,i)
	              {
	                d3.select(this).transition()
	                      .duration(100)   
	                      .attr('fill', color(d[0]))
	                d3.select(".d3-tip")
	                    .transition()
	                      .duration(600)
	                      .style("opacity",0)
	                  div.transition()    
	                      .duration(200)    
	                      .style("opacity", 0); 

	              })
	      if (SHOW_LABELS){

	        var text = svg.selectAll("text")
	                           .data(xlabels)
	                          .enter()
	                           .append("text")
	                          .attr("transform", function(d,i){
	                            return "translate(" + y(-0.25) + "," + x(i+0.75) + ")"
	                          })
	                          .text(function(d,i){
	                            return d;
	                          })
	                          .style("text-anchor", "end")
	                          .attr("font-size", "30px");

	        var text2 = svg.selectAll("text2")
	                           .data(ylabels)
	                          .enter()
	                           .append("text")
	                          .attr("transform", function(d,i){
	                            return "translate(" + y(i+0.25) + "," + x(-0.25) + ")"
	                          })
	                          .text(function(d,i){
	                            return d;
	                          })
	                          .attr("font-size", "30px")

	      }

       svg.append("text")
            .attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
            .attr("transform", "translate("+ (cell_width*m+25) +","+(cell_height*n/2)+")rotate(-90)")  // text is drawn off the screen top left, move down and out and rotate
            .text(yaxis_lbl)
            .style("font-size", fontsize_label_y) ;


        svg.append("text")
            .attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
            .attr("transform", "translate("+ (cell_width*m/2) +","+(cell_height*n+25)+")")  // centre below axis
            .style("font-size", fontsize_label_x)
            .text(xaxis_lbl);



	      function transform(d,i) {
	            var column = i%m ;
	            var row    = Math.floor(i/m) ;
	            return 'translate(' + y(column) + "," + x(row)  + ')';
	      }



	    </script>
		  </body>
		</html>
		'''
		return STR
	def second_part_bar(self):
		STR='''



      var type    = 0
      var min   = d3.min(data, function(d){ return  d[type]} );
      var max   = d3.max(data, function(d){ return d[type] } );

      var type_code = d3.map()      

      ylabels.forEach(function(d,i){type_code.set(d,i) })


      var outerWidth        = window.innerWidth,
            outerHeight     = window.innerHeight,
            Bottom          = 300,
            Top             = 200;

      var margin                  = { top: Top, right: 300, bottom: Bottom, left: 100 };                  
                  width           = outerWidth - margin.left - margin.right,
                  height          = outerHeight - margin.top - margin.bottom;

      var dispatch = d3.dispatch("load", "statechange");
      // A drop-down menu for selecting a state; uses the "menu" namespace.
      dispatch.on("load.menu", function(ylabels) {

        var select = d3.select("#scatter")
                        .append("select")
                        .style("border-width",0)
                        .style("font-family","Times New Roman")
                        .style("font-size",10)
                        .on("change", function(DD) { 
                          dispatch.call("statechange",this,this.value
                          ); });

        select.selectAll("option")
            .data(ylabels)
          .enter().append("option")
            .attr("value", function(d) { return d; })
            .text(function(d) { return d; })
        
        dispatch.on("statechange.menu", function(state) {
            type=type_code.get(state);

            rescale();


            svg.selectAll("rect")
              .transition()

              .attr("y", function(d,i){
                if ((d[type]) > 0){
                  return  y(d[type])
                }
                return y(0)
              })  

              .attr("height", function(d,i){
                if ((d[type]) > 0){
                  return y(0)-y(d[type])
                }
                return y( d[type])-y(0)
              })

             return state
        });
        
      });
      dispatch.call("load", this,ylabels)
      var svg = d3.select("#scatter")
                  .append("svg")
                  .attr("width", outerWidth)
                  .attr("height", outerHeight)
                  .append("g")
                  .attr("transform", "translate(" + margin.left + "," + margin.top + ")")


      var x           = d3.scaleLinear()
                          .domain([-1, data.length])
                          .range([ 0, width]) ;

      var y           = d3.scaleLinear()
                          .domain([Math.min(0,min),max])
                          .range([height,0]) ;

      svg.selectAll(".labelx")   
          .style("font-size", fontsize_label_x + "px");

      svg.selectAll(".labely")   
          .style("font-size", fontsize_label_y + "px");


      var wh  = width / (data.length+1)


      var tooltip = d3.select("#scatter").append("div").attr("class", "toolTip");

      var grp = svg.selectAll('g')
              .data(data)
              .enter()
              .append('rect')
              .attr("x", function(d,i){
                return  x(i)-((wh-pad)/2)
              })  
              .attr("width", (wh)-pad)
              .attr("fill", function(d,i){
                return d[ylabels.length];
              })
              .on('mouseover',function(d,i){


                  tooltip
                      .html("Value: " + data[i][type]+ "<br>" +
                            "Label: " + xlabels[i]   )
                      .style("left", x(i)-(pad/2) + 100 + "px")
                      .style("top", y(d[type])+170 + "px")
                      .style("display", "inline-block")

                                    

                d3.select(this).transition()
                    .duration(100)   
                    .attr('fill', "grey")
              })

              .on('mouseout',function(d,i){
                  tooltip
                      .style("display", "none")

                d3.select(this).transition()
                    .duration(100)   
                    .attr('fill', function(d,i){
                      return d[ylabels.length];
                    })

              })

              .attr("height",0)
              .attr("y",y(0))
                
              .transition()
              .duration(1000)
              .ease(d3.easeBounce)
              .attr("y", function(d,i){
                if ((d[type]) > 0){
                  return  y(d[type])
                }
                return y(0)
              }).attr("height", function(d,i){
                if ((d[type]) > 0){

                  return y(0)-y(d[type])
                }
                return y( d[type])-y(0)
              })
                
      // draw the x axis
      var xAxis = d3.axisBottom(x).tickSize(1).ticks(tick_xN)

      // draw the y axis
      var yAxis = d3.axisLeft(y).tickSize(1).ticks(tick_yN);

      gX  = svg.append("g")
                .classed("x axis", true)
                .attr("transform", "translate(0," + height + ")")
                .call(xAxis)
      gX.style("font-size", fontsize_ticks_x)
          .append("text")
          .classed("labelx", true)
          .attr("x", width)
          .attr("y", height)

      /*
        yaxis and y font tick size
      */ 

      gY  = svg.append("g")
          .classed("yaxis", true)
          .call(yAxis)

      gY.style("font-size", fontsize_ticks_y)
          .append("text")
          .classed("labely", true)
          .attr("x", 0)
          .attr("y", -margin.bottom/1.5 )
          .attr("transform", "rotate(-90)")
      svg.append("text").attr("class", "y label") 
          .attr("transform", "translate("+-margin.left/2 +","+ height/2 + ")rotate(-90)")
          .attr("text-anchor", "middle") 
          .style("font-size", fontsize_label_y)
          .text(yaxis_lbl)

      svg.append("text").attr("class", "y label") 
          .attr("transform", "translate("+width/2 +","+ (height+(margin.left)) + ")rotate(0)")
          .attr("text-anchor", "middle") 
          .style("font-size", fontsize_label_x)
          .text(xaxis_lbl)
      gX.selectAll("text").text("")
      if (SHOW_LABELS){
          gX.selectAll("text").text(function(i){
            if (i < 0 || i > xlabels.length){
              return ""
            }
            return xlabels[i];
          })
          .attr("transform", "translate(0,10)rotate(" + xlabels_rot+ ")" )
          .style("text-anchor", "start") 
      }
		svg.append("text")
					.attr("x", (width / 2))             
					.attr("y", 0 - (margin.top / 2))
					.attr("text-anchor", "middle")  
					.style("font-size", fontsize_title) 
					.text(title);

      function rescale() {

            var min   = d3.min(data, function(d){ return  d[type]} );
            var max   = d3.max(data, function(d){ return d[type] } );

            y.domain([Math.min(0,min),max]).range([height,0])  // change scale to 0, to between 10 and 100
            var yAxis = d3.axisLeft(y).tickSize(1).ticks(tick_yN);
            svg.select("g.yaxis").call(yAxis)

        }


		    </script>
		  </body>
		</html>

		'''
		return STR







