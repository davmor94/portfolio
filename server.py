# export FLASK_APP=server.py  # need to do this in terminal before running flask
# export FLASK_ENV=development # turns the debug mode on to be able to make changes and see results faster
import os
import csv
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)  # create an instance of a Flask class


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}: {subject}\n {message}')
        print(file)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# @app.route('/<string:username>')  # variable rules to pass on to html file
# def hello_world(username=None):
#     return render_template('index.html', name=username)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# Request object
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thank_you.html')
        except:
            return 'Failed to save...'
    else:
        return 'something went run, try again!'


# # @app.route('/components.html')
# # def components():
# #     return render_template('components.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/burnerfavicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'burnerfavicon.ico', mimetype='image/vnd.microsoft.icon')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
