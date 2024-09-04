from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class UUIDRecieve(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text-html")
        self.end_headers()
        self.wfile.write(bytes("<html><head> UUID </head> <body> <p> Server for UUID Testing </p> </body> </html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), UUIDRecieve)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server closed")

    