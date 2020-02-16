from app import app
@app.route('/')
@app.route('/index')

def index():
	"""
	index render;
	"""
	return 'Hello, world!'
