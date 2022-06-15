
from flask import Flask, request, jsonify
from configs.config import getEnv
from repository.news import getAllNews


ENV = getEnv('ENV')
PORT = getEnv('PORT')


app = Flask('__name__')

if ENV.lower() == 'development':
    app.config['DEBUG'] = True



_VERSION = 1 #version 1

@app.errorhandler(400)
def page_empty_payload(error):
	response = jsonify({'err': True, 'message': 'payload cannot be empty', 'data':False})
	return response, 400

@app.errorhandler(401)
def page_unauthorized(error):
	response = jsonify({'err': True, 'message': 'invalid authorization', 'data':False})
	return response, 401

@app.errorhandler(404)
def page_not_found(error):
	response = jsonify({'err': True, 'message': 'page not found', 'data':False})
	return response, 404

@app.errorhandler(500)
def internal_server_error(error):
	response = jsonify({'err': True, 'message': 'internal server error', 'data':False})
	return response, 500

@app.route('/', methods=['GET'])
def index():
    return 'welcome'

@app.route('/api/health-check', methods=['GET'])
def healthCheck():
    result = jsonify({'message': 'Your application running properly'})
    return result

@app.route('/api/news', methods=['GET'])
def ocr():
    args = request.args
    search = args.get('search')
    size = args.get('size')
    page = args.get('page')
    
    result,code = getAllNews(search, size, page)
    return jsonify(result),code

app.run(host='0.0.0.0', port=int(PORT))