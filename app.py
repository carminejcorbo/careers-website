from flask import Flask, render_template, jsonify


app = Flask(__name__)
JOBS =[
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Hartford, CT',
    'salary': '$100,000.00'
  },
  {
    'id': 2,
    'title': 'Software Engineer',
    'location': 'New Haven, CT',
    'salary': '$125,000.00'
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Senior Help Desk',
    'location': 'Waterbury,CT',
    'salary': '$75,000.00'
  }
]
@app.route('/')
def helloWorld():
  return render_template('home.html', jobs=JOBS)

@app.route('/jobs')
def list_job():
  return jsonify(JOBS)
  
print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  print('Im inside the if now')
