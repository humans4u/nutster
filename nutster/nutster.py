import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
from nutster.routing import HandlePath

def BuildError(handler):
    handler.send_response(400)
    return handler

class HTTPHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        return