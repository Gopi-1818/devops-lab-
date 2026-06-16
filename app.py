# Simple web app - we'll containerize this in Docker week
import http.server
import socketserver

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from DevOps app v1")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
feature work line 1
