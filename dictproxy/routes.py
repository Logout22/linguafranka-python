from dictproxy.dictproxy import app

@app.route('/')
@app.route('/index')
def index():
    return """{
        "items": [{
                "origin": "Hello",
                "translation": "World!"
        }]
}"""
