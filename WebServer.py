from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class WebServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        params = parse_qs(urlparse(self.url).query)

        if params['demo'] == 'fractal':
            #todo
            self.wfile.write(gif)
