
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/hello')
def welcome():
    return render_template("index.html")


@app.route("/calculation",methods = ['GET','POST'])
def calculation():
    if(request.method=='POST'):
        Item1 = request.form["Item1"]
        Price1 = int(request.form["Price1"])
        Item2 = request.form["Item2"]
        Price2 = int(request.form["Price2"])
        Item3 = request.form["Item3"]
        Price3= int(request.form["Price3"])
        Item4 = request.form["Item4"]
        Price4 = int(request.form["Price4"])
        discount_price=0
        discount_applied=0
        total_price = Price1+Price2+Price3+Price4
        if(total_price <= 1000):
            discount_applied = total_price * 0.1
            discount_price = total_price - discount_applied
        elif(total_price > 100 and total_price <= 2000):
            discount_applied = total_price * 0.2
            discount_price = total_price - discount_applied
        elif(total_price > 2000):
            discount_applied = total_price * 0.3
            discount_price = total_price - discount_applied

        return render_template("result.html",product1= Item1,product2 = Item2,product3 = Item3,product4=Item4,total_price=total_price,discount_applied=discount_applied,discount_price = discount_price,)







if __name__ == "__main__":
    app.run('0.0.0.0',port=5000)