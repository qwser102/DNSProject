from flask import Flask,render_template,request
from modules import add_extensive_domain,add_domain,domain_search,extensive_domain_search,domain_delete,extensive_domain_delete,dns_status
app = Flask(__name__)

#index page
@app.route('/')
def index():
#    if request.method == 'GET':
    return render_template('index.html')

#search for extensive domain
@app.route('/extensive_domain_search',methods=['GET'])
def search_extnsive():
    if request.method == 'GET':
        data = extensive_domain_search()
        return render_template('extensive_domain_search.html',extensive_domain_list=data)

#search for single domain
@app.route('/domain_search',methods=['GET','POST'])
def search_domain():
    if request.method == 'GET':
        data= domain_search()
        return render_template('domain_search.html',domain_list=data)

#add extensive domain
@app.route('/extensive_domain_add',methods=['GET','POST'])
def creat_new_extensive():
    if request.method == 'GET':
        return render_template( 'extensive_domain_add.html' )
    else:
        name = request.form.get('extensive_name')
        ip = request.form.get('ip')
        status = add_extensive_domain(ip,name)
        d = {'result': status}
        return d

#add single domain
@app.route('/domain_add',methods=['GET','POST'])
def creat_new_domain():
    if request.method == 'GET':
        return render_template('domain_add.html')
    else:
        name = request.form.get('domain_name')
        ip = request.form.get('ip')
        status = add_domain(ip,name)
        d={'result': status}
        return d

#delete single domain
@app.route('/domain_delete',methods=['GET','POST'])
def delete_domain():
    if request.method == 'GET':
        return render_template('domain_delete.html')
    else:
        name = request.form .get('domain_name')
        status = domain_delete(name)
        d = {'result': status}
        return d

#delete extensive domain
@app.route('/extensive_domain_delete',methods=['GET','POST'])
def delete_extensive():
    if request.method == 'GET':
        return render_template('extensive_domain_delete.html')
    else:
        name = request.form.get('extensive_name')
        status = extensive_domain_delete(name)
        d = {'result': status}
        return d
#monitoring
@app.route('/monitoring',methods=['GET'])
def monitoring():
    if request.method == 'GET':
        status = dns_status()
        d = {'result': status}
        return d

# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
