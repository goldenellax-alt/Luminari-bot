import threading
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

print("Server file loaded")

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def bot():
    os.system("python main.py")

threading.Thread(target=bot).start()
HTTPServer(("0.0.0.0", int(os.getenv("PORT", 10000))), H).serve_forever()
