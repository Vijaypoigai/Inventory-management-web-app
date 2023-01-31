from flask import Flask,render_template
from flask_mysqldb import MySQL 
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Vijay@06'
app.config['MYSQL_DB']='stocks'
mysql = MySQL(app)
@app.route("/")
def index():
	return render_template("index.html")
@app.route('/product')
def product():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM product")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template("product.html",data=fetchdata)

@app.route('/location')
def location():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM location")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template("location.html",data=fetchdata)
@app.route('/product_movement')
def product_movement():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM productmovement")
    fetchdata= cur.fetchall()
    cur.close()
    return render_template('product_movement.html', data=fetchdata)
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    cur = mysql.connection.cursor()
    cur.execute("INSERT into product VALUES")
    fetchdata= cur.fetchall()
    cur.close()
    return render_template('add_product.html', data=fetchdata)
@app.route('/edit_product/<string:id>', methods=['GET', 'POST'])

def edit_product(id):
    #Create cursor
    cur = mysql.connection.cursor()

    #Get article by id
    result = cur.execute("SELECT * FROM product where product_id = %s", [id])

    product = cur.fetchone()

    #Get form
    form = ProductForm(request.form)

    #populate product form fields
    form.product_id.data = product['product_id']

    if request.method == 'POST' and form.validate():
        product_id = request.form['product_id']
        #create cursor
        cur = mysql.connection.cursor()

        #execute
        cur.execute("UPDATE product SET product_id=%s WHERE product_id=%s",(product_id, id))

        #commit to DB
        mysql.connection.commit()

        #close connection
        cur.close()

        flash("Product Updated", "success")

        return redirect(url_for('products'))

    return render_template('edit_product.html', form=form)

    
    
if __name__ == '__main__':
	app.run(debug=True)