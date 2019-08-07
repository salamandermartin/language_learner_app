#import section
import jinja2
import os
import webapp2

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)




#handlers
class WelcomePageHandler(webapp2.RequestHandler):
    def get(self):
        welcome_page_template = the_jinja_env.get_template

# uncomment these when the first page is done

# class ListPageHandler(webapp2.RequestHandler):
#     def get(self):
#         list_page_template = the_jinja_env.get_template
#
# class ConjugationPageHandler(webapp2.RequestHandler):
#     def post(self):



#app configuration section
app = webapp2.WSGIApplication([
    ('/',     ) #Welcome Page
    ('/',      ) #List Page
    ('',      ) #Results Page
], debug=True)
