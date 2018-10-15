import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os

from mygpu import MyGpu

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class Delete(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		url = ''
		url_string = ''
		welcome = 'Welcome back'	
		user = users.get_current_user()

		if user:
			url = users.create_logout_url(self.request.uri)
			url_string = 'logout'
			
		else:
			url = users.create_login_url(self.request.uri)
			url_string = 'login'

		mygpu = ndb.Key("MyGpu", self.request.get("name")).get()
		
		if not mygpu: 
			return self.redirect('/')
		mygpu.key.delete()
		
		return self.redirect("/")