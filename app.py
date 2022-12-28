from flask import Flask , render_template
app = Flask(__name__)
import json

@app.route('/')
def main_app():
    try:
        file = open("/root/infinity-seo/test.json") 
        json.loads(file)
    except:
        file = open("/root/infinity-seo/test-dummy.json") 
    data = json.load(file)
#def hello_name():
 #   file = open("/root/infinity-seo/test.json") 
  #  data = json.load(file)
    # print(data)
    return render_template('display_results.html',data_query=data) 
    
if __name__ == '__main__':
    app.run()
