#import all the necessary libraries
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse

current_word = []

def index_page(req):
   return FileResponse("home.html")

def post_word(req):
   current_word.append(req.matchdict['word'])
   print("im here")
   print("current word: ", req.matchdict['word'])
   print("word is saved: ", current_word[-1])
   return 0

def get_word(req):
   return {'word': current_word[int(req.matchdict['index'])]}

#Line below tells executor to start from here
if __name__ == '__main__':
   with Configurator() as config:
       # Create a route called home
       config.add_route('home', '/')
       # Bind the view (defined by index_page) to the route named ‘home’
       config.add_view(index_page, route_name='home')

       # Create a route that handles server HTTP requests at: /words
       config.add_route('words', '/words/{word}')
       # Binds the function get_word to the words route and returns JSON
       # Note: This is a REST route because we are returning a RESOURCE!
       config.add_view(post_word, route_name='words', renderer='json')

       # Create a route that handles server HTTP requests at: /get_word
       config.add_route('get_word', '/get_word/{index}')
       # Binds the function get_word to the words route and returns JSON
       # Note: This is a REST route because we are returning a RESOURCE!
       config.add_view(get_word, route_name='get_word', renderer='json')

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

