from flask import Flask, render_template, request
import pickle

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict')
def index():
    return render_template("index.html")

@app.route('/data_predict', methods=['GET','POST'])
def predict():
    
    model = pickle.load(open('model.pkl', 'rb'))
    
    data = [[x for x in request.form.values()]]
    
    prediction= model.prediction(data)[0]
    print(prediction)
    
    return render_template('gdp_pred.html', prediction=prediction)

if __name__ == '__main__':
    app.run()

