from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/donation')
def donation():
    return render_template('donation.html')

@app.route('/networking')
def networking():
    return render_template('networking.html')

@app.route('/job-portal')
def job_portal():
    return render_template('job_portal.html')

@app.route('/directory')
def directory():
    return render_template('directory.html')

@app.route('/success-stories')
def success_stories():
    return render_template('success_stories.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)
