#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request,render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))
    
@app.route("/result",methods=["GET","POST"])
def result():
    t = request.form.get("t")
    result = TextBlob(t).sentiment
    return(render_template("result.html",result=result))

if __name__ == "__main__":
    app.run()


# In[ ]:




