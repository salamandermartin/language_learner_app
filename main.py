#import section
import jinja2
import os
import webapp2
import random

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def quotePicker():
    decider = random.randint(0,2)
    quotes = ['If you talk to a man in a language he understands, that goes to his head. If you talk to him in his language, that goes to his heart. \n - Nelson Mandela',
              'A different language is a different vision of life. \n -Federico Fellini',
              'With languages, you are at home anywhere. \n -Edmund de Waal ']
    chosen_quote = quotes[decider]
    return chosen_quote



#handlers
class WelcomePageHandler(webapp2.RequestHandler):
    def get(self):
        welcome_page_template = the_jinja_env.get_template('templates/welcome_page_template.html')
        self.response.write(welcome_page_template.render())



class ListPageHandler(webapp2.RequestHandler):
    def get(self):
        list_page_template = the_jinja_env.get_template('templates/list_page_template.html')
        self.response.write(list_page_template.render())
# class ResultPageHandler(webapp2.RequestHandler):
#     def post(self):



#app configuration section
app = webapp2.WSGIApplication([
    ('/', WelcomePageHandler) #Welcome Page
    #('/list-go', ListPageHandler) #List Page
    #('/result', ResultPageHandler) #Results Page
], debug=True)
