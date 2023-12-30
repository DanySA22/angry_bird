import os
from waitress import serve
from angry_bird.wsgi import application  # replace 'myproject' with your Django project's name

port = int(os.environ.get("PORT", 8000))  # Default to 8000 if no PORT environment variable is set
serve(application, port=port)
