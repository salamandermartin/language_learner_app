import jinja2
import os
import webapp2
import random
from other_func import translator
from other_func import listPluralizer
from other_func import make_plural

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def quotePicker():
    decider = random.randint(0,2)
    quotes = ['"If you talk to a man in a language he understands, that goes to his head. If you talk to him in his language, that goes to his heart." \n - Nelson Mandela',
              '"A different language is a different vision of life." \n -Federico Fellini',
              '"With languages, you are at home anywhere." \n -Edmund de Waal ']
    chosen_quote = quotes[decider]
    return chosen_quote


#handlers
class WelcomePageHandler(webapp2.RequestHandler):
    def get(self):
        welcome_page_template = the_jinja_env.get_template('templates/welcome_page_template.html')
        welcome_variables = {
            'quote': str(quotePicker())
        }
        self.response.write(welcome_page_template.render(welcome_variables))



class ListPageHandler(webapp2.RequestHandler):
    def get(self):
        list_page_template = the_jinja_env.get_template('templates/list_page_template.html')
        self.response.write(list_page_template.render())


class ResultPageHandler(webapp2.RequestHandler):
    def post(self):
        result_page_template = the_jinja_env.get_template('templates/result_page_template.html')
        item1 = self.request.get('Item 1')
        item2 = self.request.get('Item 2')
        item3 = self.request.get('Item 3')
        item4 = self.request.get('Item 4')
        item5 = self.request.get('Item 5')
        language = self.request.get('language')
        list_variables = {
            #word in english
            'firstitem': item1,
            'seconditem': item2,
            'thirditem': item3,
            'fourthitem': item4,
            'fifthitem': item5,
            #word in spanish (singular)
            'tr_item1':translator((item1),language),
            'tr_item2':translator((item2),language),
            'tr_item3':translator((item3),language),
            'tr_item4':translator((item4),language),
            'tr_item5':translator((item5),language),
            #word in spanish (plural)
            'tr_items1':translator((make_plural(item1)),language),
            'tr_items2':translator((make_plural(item2)),language),
            'tr_items3':translator((make_plural(item3)),language),
            'tr_items4':translator((make_plural(item4)),language),
            'tr_items5':translator((make_plural(item5)),language)
        }
        self.response.write(result_page_template.render(list_variables))

class AboutPageHandler(webapp2.RequestHandler):
    def get(self):
        about_page_template = the_jinja_env.get_template('templates/about_page_template.html')
        self.response.write(about_page_template.render())

class ContactPageHandler(webapp2.RequestHandler):
    def get(self):
        contact_page_template = the_jinja_env.get_template('templates/contact_page_template.html')
        self.response.write(contact_page_template.render())

#app configuration section
app = webapp2.WSGIApplication([
    ('/', WelcomePageHandler), #Welcome Page
    ('/list-go', ListPageHandler), #List Page
    ('/result', ResultPageHandler), #Results Page
    ('/about', AboutPageHandler), #About Page
    ('/contact',ContactPageHandler) #Contact Page
], debug=True)
