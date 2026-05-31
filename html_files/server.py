from http.server import BaseHTTPRequestHandler, HTTPServer 
from urllib.parse import parse_qs
import json 
import os

PORT =  3502

class MyServer(BaseHTTPRequestHandler) : 
   
    def do_GET(self): 
        if self.path == '/': 
            with open('index.html', 'r') as fp :
                html = fp.read()
                css_file = open('journalist.css', 'r')
                css = css_file.read()
                html = html.replace('{{css}}',css)
                self.send_response(200,'Everything is okay')
                self.send_header('Content-type',"text/html")
                self.end_headers()
                self.wfile.write(html.encode('utf-8'))

        elif self.path == '/reports': 
            with open('report.html', 'r') as fp :
                html = fp.read()
                self.send_response(200,'Everything is okay')
                self.send_header('Content-type',"text/html")
                self.end_headers()
                self.wfile.write(html.encode('utf-8'))



server = HTTPServer(('localhost',PORT), MyServer)
print(f'STARTING SERVER ON PORT {PORT}')
server.serve_forever()