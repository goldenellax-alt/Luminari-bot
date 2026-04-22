import threading
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

print("Server file loaded - starting bot thread...")

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Luminari Bot is running')

def run_bot():
    print("Launching main.py...")
    os.system('python main.py')

threading.Thread(target=run_bot, daemon=True).start()
print("Web server starting on port", os.getenv('PORT', 10000))
HTTPServer(('0.0.0.0', int(os.getenv('PORT', 10000))), H).serve_forever()
