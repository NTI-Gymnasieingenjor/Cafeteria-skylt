import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

os.chdir('/home/pi/Git/Cafeteria-skylt/public')
serverAddress = ("", 8000)  
httpd = HTTPServer(serverAddress, SimpleHTTPRequestHandler)
httpd.serve_forever()
