from flask import Flask, render_template
import os.path
app = Flask("DynamicLocus")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'content.html')

@app.route('/')
def static_page():
    return render_template(filename)