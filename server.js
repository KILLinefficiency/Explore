const http = require("http");
const fs = require("fs")

server = http.createServer((req, res) => {
	if(req.url == "/") {
		res.write("you know the rules and so do i...");
		res.end();
	}
	if(req.url == "/mess") {
		mess_content = fs.readFileSync("mess_file.txt");
		mess = mess_content.toString();
		res.write(mess);
		res.end();
	}
	if(req.url == "/cluster") {
		cluster_content = fs.readFileSync("cluster_file.txt");
		cluster = cluster_content.toString();
		res.write(cluster);
		res.end();
	}
});

server.listen(2166, "0.0.0.0", () => { console.log("Server running on port 2166"); });

