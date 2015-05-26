from flask import Flask, render_template, request
app = Flask(__name__)


@weblogoapp_route('/')
def index():
	def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')
	return render_template('index.html')

@weblogoapp_route('/create_html_template')
def create_html_template():
	return render_template('index.html')

@weblogoapp_route('/examples')
def examples():
	return render_template('examples.html')

@weblogoapp_route('/manual')
def create_html_template():
	return render_template('manual.html')

@weblogoapp_route('/test')
def test():
	return render_template('test.html')

@weblogoapp_route('/thumbnail')
def thumbnails():
	return render_template('thumbnail.html')

if __name__=='__main__':
    app.run(debug=True)