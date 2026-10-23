import os
import platform
from http.server import HTTPServer, SimpleHTTPRequestHandler
from os import getcwd, path

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()        
        SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

if platform.system() == "Windows":
    cwd = getcwd()
    os.chdir(cwd + "/public")
elif platform.system() == "Linux":
    os.chdir("/home/pi/Git/cafeteria-display/public")
serverAddress = ("", 8000)
httpd = HTTPServer(serverAddress, NoCacheHTTPRequestHandler)
print("\nThe server is open at http://127.0.0.1:8000")
httpd.serve_forever()
