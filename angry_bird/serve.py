import os
from waitress import serve
from angry_bird.wsgi import application  

port = int(os.environ.get("PORT", 8000))  # Default to 8000 if no PORT environment variable is set

if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=port)
