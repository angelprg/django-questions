//console.log({response_ratio})
//console.log({questions_by_category})
//console.log({questions_by_created})


// Graph by dates
(() =>{
// set the dimensions and margins of the graph
let margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 900 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
let svg = d3.select("#graph_days")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

  const d3_questions_by_created = questions_by_created.map( d =>{
    return {
      value: d.is_responded+d.is_not_responded,
      date: d3.timeParse("%Y-%m-%d")(d.date)
    }
  })
  

    // Add X axis --> it is a date format
    let x = d3.scaleTime()
      .domain(d3.extent(d3_questions_by_created, function(d) { return d.date; }))
      .range([ 0, width ]);
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    // Add Y axis
    let y = d3.scaleLinear()
      .domain([0, d3.max(d3_questions_by_created, function(d) { return +d.value; })])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisLeft(y));

    // Add the line
    svg.append("path")
      .datum(d3_questions_by_created)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1.5)
      .attr("d", d3.line()
        .x(function(d) { return x(d.date) })
        .y(function(d) { return y(d.value) })
        )
})()



// Graph by responded or not responded
const graph_by_responded = (container, data) => {

    let width = 450
    let height = 450
    let margin = 40

  let radius = Math.min(width, height) / 2 - margin

  let svg = d3.select(container)
  .append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

  let color = d3.scaleOrdinal().domain(data).range(d3.schemeSet3);

  let pie = d3.pie().value(function(d) {return d.value; })
  let data_ready = pie(d3.entries(data))

  let arcGenerator = d3.arc()
  .innerRadius(0)
  .outerRadius(radius)

  svg
  .selectAll('mySlices')
  .data(data_ready)
  .enter()
  .append('path')
    .attr('d', arcGenerator)
    .attr('fill', function(d){ return(color(d.data.key)) })
    .attr("stroke", "black")
    .style("stroke-width", "2px")
    .style("opacity", 0.7)

  svg
  .selectAll('mySlices')
  .data(data_ready)
  .enter()
  .append('text')
  .text(function(d){ return  d.data.key})
  .attr("transform", function(d) { return "translate(" + arcGenerator.centroid(d) + ")";  })
  .style("text-anchor", "middle")
  .style("font-size", 17)

}
graph_by_responded("#graph_responses",response_ratio)
graph_by_responded("#graph_categories",questions_by_category)

