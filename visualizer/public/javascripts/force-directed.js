const width = 1920, //960,
	  height = 1080; //500

const threshold = 5;

var svg = d3.select("body").append("svg")
	.attr("width", width)
	.attr("height", height)
	.call(d3.zoom().on("zoom", function () {
		svg.attr("transform", d3.event.transform)
	 }))
	 .append("g")

var force = d3.forceSimulation()
	.force("charge", d3.forceManyBody().strength(-700).distanceMin(10).distanceMax(10000))
	.force("link", d3.forceLink().id(function(d) { return d.index }))
	.force("center", d3.forceCenter(width / 2, height / 2))
	.force("y", d3.forceY(0.001))
	.force("x", d3.forceX(0.001))

var size = function (ref, age) {
	if (ref > 5 || age < threshold){
		return 80
	} else return 15
}

var font_size = function (ref, age) {
	if (ref > 5 || age < threshold) {
		return "60px"
	} else return "12px"
}

var font_pos_x = function (ref, age) {
	if (ref > 5 || age < threshold) {
		return -50
	} else return -9
}

var font_pos_y = function (ref, age) {
	if (ref > 5 || age < threshold) {
		return 20
	} else return 5
}

var color = function (ref, age) {
	if (ref == 0) {
		if (age < threshold) {
			// tips
			return "#fbc280"
		} else {
			// deprecated tips
			return "#33678a"
		}
	}
	if (ref > 10) {
		return "#f64668"
	}
	if (age < threshold) {
		return "#78a6c9"
	} else if (age < 300) { 
		return "#777"
		// return "#405275"
	} else {
		return "#aaa"
	}
}

function dragstarted(d) {
	if (!d3.event.active) force.alphaTarget(0.5).restart();
	d.fx = d.x;
	d.fy = d.y;
}

function dragged(d) {
	d.fx = d3.event.x;
	d.fy = d3.event.y;
}

function dragended(d) {
	if (!d3.event.active) force.alphaTarget(0.5);
	d.fx = null;
	d.fy = null;
}

d3.json("network.json", function (error, json) {
	if (error) throw error;
	force
		.nodes(json.nodes)
		.force("link").links(json.links)

	var link = svg.selectAll(".link")
		.data(json.links)
		.enter()
		.append("line")
		.attr("class", "link");

	var node = svg.selectAll(".node")
		.data(json.nodes)
		.enter().append("g")
		.attr("class", "node")
		.call(d3.drag()
			.on("start", dragstarted)
			.on("drag", dragged)
			.on("end", dragended));

	node.append('circle')
		// .attr('r', 13)
		.attr('r', (d => {
			return size(d.ref, d.age)
		}))
		.attr('fill', d => {
			return color(d.ref, d.age);
		});

	node.append("text")
		.attr("dx", d => {
			return font_pos_x(d.ref, d.age)
		})
		.attr("dy", d => {
			return font_pos_y(d.ref, d.age)
		})
		.style("font-family", "overwatch")
		.style("font-size", d => {
			return font_size(d.ref, d.age)
		})
		.text(d => {
			// return d.name
			return d.accuracy
		});

	force.on("tick", function () {
		link.attr("x1", function (d) {
			return d.source.x;
		})
			.attr("y1", function (d) {
				return d.source.y;
			})
			.attr("x2", function (d) {
				return d.target.x;
			})
			.attr("y2", function (d) {
				return d.target.y;
			});
		node.attr("transform", function (d) {
			return "translate(" + d.x + "," + d.y + ")";
		});
	});
});
