#import all the necessary libraries
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse


def index_page(req):
   return FileResponse("home.html")

#Line below tells executor to start from here
if __name__ == '__main__':
   with Configurator() as config:
       # Create a route called home
       config.add_route('home', '/')
       # Bind the view (defined by index_page) to the route named ‘home’
       config.add_view(index_page, route_name='home')

       # Add a static view
       # This command maps the folder “./public” to the URL “/”
       # So when a user requests geisel-1.jpg as img_src, the server knows to look
       # for it in: “public/geisel-1.jpg”
       config.add_static_view(name='/', path='./', cache_max_age=3600)
      
       # Create an app with the configuration specified above
       app = config.make_wsgi_app()
   server = make_server('0.0.0.0', 6543, app) # Start the application on port 6543
   print("Server running at localhost:6543")
   server.serve_forever()

