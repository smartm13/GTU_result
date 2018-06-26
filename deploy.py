# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
from flask import Flask,request,Flask, request, redirect, url_for, send_from_directory,Response


app = Flask(__name__)#,static_url_path='')
#app.config["DEBUG"]=True


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return ('gtu.py')#'Hello World!'#+request.args.get('en')
@app.route('/result')
def res():
	import gtu_2018 as gtu
	return '''<meta http-equiv="refresh" content="0; url=/gtu/pasted/results/{}.html" />'''.format(request.args.get('enrol',''))+gtu.getptr(request.args.get('enrol',''),request.args.get('exam',''),int(request.args.get('html','1')))

@app.route('/<path:path>')
def all(path):
	mimetypes = {
        "css": "text/css",
        "html": "text/html",
        "js": "application/javascript",
        "json": "application/json",
		"png":"image/png",
		"mp3":"audio/mpeg",
		
    }
	#path="static/airhorn2/app/"+path
	#return path #or app.send_static_file(path)
	with open(path) as f:return Response(f.read().replace('\\r','\r').replace('\\n','\n'),mimetype=mimetypes.get(path.split('.')[-1],'text/html'),headers={'access-control-allow-origin':'*'})

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

if __name__ == '__main__':
    app.run(host='' and '192.168.1.7', port=8082,threaded=True)
# [END app]
