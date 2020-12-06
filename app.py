#!/usr/bin/env python
# coding: utf-8

# In[26]:


import flask
from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle


# In[27]:


app=Flask(__name__)


# In[28]:


model = pickle.load(open('BstCanpipeline','rb'))


# In[29]:


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Cell growth is $ {}'.format(output))


# In[30]:


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




