#!/usr/bin/env python3

import http.server
import socketserver
import os
import signal

def main():
    carpeta = os.path.dirname(os.path.abspath(__file__))
    os.chdir(carpeta)

    Handler = http.server.SimpleHTTPRequestHandler
    httpd = None

    def cleanup(signum, frame):
        print("\n\n🛑 Deteniendo servidor...")
        if httpd:
            httpd.shutdown()
        exit(0)

    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    for puerto in range(8000, 8100):
        try:
            httpd = socketserver.TCPServer(("0.0.0.0", puerto), Handler)
            break
        except OSError:
            continue

    if httpd is None:
        print("❌ No se encontró puerto disponible entre 8000-8099.")
        return

    print()
    print(f"✅ Botonera disponible en:")
    print(f"   http://localhost:{puerto}/botonera.html")
    print()
    print("Presiona Ctrl+C para detener el servidor.")
    httpd.serve_forever()

if __name__ == "__main__":
    main()