from flask import*
import sqlite3

app= Flask(__name__)

@app.route('/')
def index():
    con=sqlite3.connect("mydata.db")
    cur=con.cursor()

    cur.execute("select * from task")

    data =cur.fetchall()
    con.close()

    return render_template("index.html",data=data)




@app.route("/add",methods=["POST","GET"])

def add():
    if request.method=="POST":
       title= request.form["title"]
       con=sqlite3.connect("mydata.db") 

       cur =con.cursor()
 
       cur.execute("insert into task(title) values(?)",(title,))
       con.commit()

       return redirect(url_for("index"))
    
    

@app.route("/delete/<int:id>")

def delete(id):
    con=sqlite3.connect("mydata.db")
    cur=con.cursor()
    cur.execute("delete from task where id=?",[id])

    con.commit()
    return redirect(url_for("index"))

   


if __name__ =="__main__":
    app.run(debug=True)