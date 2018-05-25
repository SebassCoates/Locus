from flask import Flask, request
import os.path
app = Flask("DynamicLocus")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'content.html')

@app.route('/', methods=["GET"])
def home():
    return """
        <!DOCTYPE html>
        <html lang="en">

	        <head>
		        <meta charset="utf-8"/>
		        <title>Sample</title>
	        </head>
	
            <body>
                <h1>
                    test header 1 updated
                </h1>
                html content rendered!
            </body>
           
        </html>"""

@app.route('/', methods=['GET', 'POST'])
def content():
    error = None
    if request.method == 'POST':
        