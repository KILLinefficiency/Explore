const http = require("http");
const fs = require("fs");

const SERVER_PORT = 2166;

const index_page = `<html>
	<head>
		<title>Explore Server</title>
	</head>

	<body>
		<h1 align = "center">Explore Sever</h1>
		<br>
		<h3>Routes for Explore Server:</h3>
			<code>/mess</code>
			<br><br>
			<code>/cluster</code>
	</body>

	</html>
`;

const mess_file = ".mess_server_file.txt";
const cluster_file = ".cluster_server_file.txt";

server = http.createServer((req, res) => {
	if(req.url == "/") {
		res.write(index_page);
		res.end();
	}
	if(req.url == "/mess") {
		fs.readFile(mess_file, (err, mess_contents) => {
			if(err) {
				console.log("Error: Update the server from your Explore instance.")
			}
			else {
				res.write(mess_contents);
				res.end();
			}
		});
	}
	if(req.url == "/cluster") {
		fs.readFile(cluster_file, (err, cluster_contents) => {
			if(err) {
				console.log("Error: Update the server from your Explore instance.")
			}
			else {
				res.write(cluster_contents);
				res.end();
			}
		});
	}
});

var reqs = 1;
server.on("connection", (socket) => {
	console.log(`Request recieved... (${reqs})`);
	reqs = reqs + 1;
});

server.listen(SERVER_PORT, "0.0.0.0", () => { console.log(`\nServer running on port ${SERVER_PORT}...\n`); });
