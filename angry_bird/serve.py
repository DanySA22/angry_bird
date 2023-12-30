from waitress import serve
from angry_bird.wsgi import application  

if __name__ == "__main__":
    serve(application, port=8000)  # You can change the port number if needed
