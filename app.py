from flask import Flask
 
app = Flask(__name__)
 
@app.route('/',  methods=['GET', 'POST'])
def index():
    return '안녕 난 플라스크야'
 
app.run(host='0.0.0.0')