from http.server import HTTPServer, BaseHTTPRequestHandler

class server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))

httpd = HTTPServer(('localhost', 8080), server)
httpd.serve_forever()
