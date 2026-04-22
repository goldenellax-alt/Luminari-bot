import threading, os
from http.server import HTTPServer, BaseHTTPRequestHandler

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot running')

def run_bot():
    os.system('python main.py')

threading.Thread(target=run_bot).start()
HTTPServer(('0.0.0.0', int(os.getenv('PORT', 10000))), H).serve_forever()
