import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
from datetime import datetime

app = Flask(__name__)


@app.route('/')                                 #'/' is the default/home URL
def index():
   #current_time = datetime.now().strftime("%H:%M:%S")
   #print('Current time is:', current_time)
   converted_time = int(datetime.now().hour)
   if (0 <= converted_time and converted_time <= 12):
    phrase = 'Good morning'
   elif (13 <= converted_time and converted_time <= 17):
    phrase = 'Good afternoon'
   elif (18 <= converted_time and converted_time <= 24):
    phrase = 'Good evening'
   else:
    phrase = 'Good morning'
      
   print('Request for index page received')
   return render_template('index.html', greetings = phrase)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
