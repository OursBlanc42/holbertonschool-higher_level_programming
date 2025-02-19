#!/usr/bin/python3

import http.server
import socketserver

PORT = 8009


class BasicHttpServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, "Yiha !")
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Yiha !")


Handler = BasicHttpServer

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
