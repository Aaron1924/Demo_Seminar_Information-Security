from flask import Flask,render_template,request,redirect,url_for,session
import json
import ipfsApi
from werkzeug.utils import secure_filename
import configs

from web3 import Web3
from web3 import Web3, middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from upload_data import check
from signature import msg_signature
# Set up web3 connection with Ganache
ganache_url = configs.GANACHE_URL
web3 = Web3(Web3.HTTPProvider(ganache_url))
api = ipfsApi.Client(**configs.ipfsAPI_host)
with open('contract.sol', 'r') as file:
    escrow_contract = file.read()

compiled_contract = web3.eth.compileSolidity(escrow_contract)
# deploy the contract
contract_interface = compiled_contract['<stdin>:SimpleStorage']

Escrow = web3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin']
)
app = Flask(__name__,
            static_url_path='/assets', 
            static_folder='assets',
            template_folder='template')

app.secret_key = 'any random string'
   	  	
    		
# set pre-funded account as sender
web3.eth.defaultAccount = web3.eth.accounts[0]
#web3.eth.defaultAccount='0xD37266B8447C9095CB2ae7345694192aa417f0B1'
# Instantiate and deploy contract
tx_hash = Escrow.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    
contract_address = tx_receipt.contractAddress
# Wait for the transaction to be mined, and get the transaction receipt

print(contract_address)



@app.route('/')
def home(): 
    return render_template("home.html")

#session['medical_record']=abi
@app.route('/site', methods=['GET', 'POST'])
def index():
    #sites = ['', 'DC2', 'DC3', 'DC4']
    if request.method == 'POST':
        gather = request.form["site"]
        session['gather']=gather
        print(gather)
        #if gather=='DC2':
            #return redirect(url_for('switchinfo'))
        return redirect(url_for('switchinfo'))

    return render_template('index2.html', sites=['Doctor', 'Patient', 'Medical lab', 'Medicine store'])

@app.route('/login', methods=['GET','POST'])
def switchinfo():
    if request.method == 'POST':
        session['address']= request.form['Address']
        privatekey = request.form['PrivateKey']
        #session['address']=address
        session['privatekey']=privatekey
        #session.pop('gather', None)
        print(session['address'],privatekey)
        if session['gather']=='Patient':
            return redirect(url_for('patient'))
        elif session['gather']=='Doctor':
            return redirect(url_for('patient'))
        return redirect(url_for('switchinfo'))
    return render_template("login.html")

@app.route('/patient',methods=['GET', 'POST'])
def patient():
    if request.method == 'POST':
        gather = request.form["site"]
        session['gather']=gather
        if 'upload' in request.form:
            return redirect(url_for('upload_file'))
        elif 'check' in request.form:
            result=check.check_data(session['gather'],tx_receipt.contractAddress,session['address'],1)
            print(result)
            session['result']=result[1]
            b='data uploaded'
            try:
                b=msg_signature.signature_verify(session['msghash'],session['msgsignature'])
            except:
                None
            
            return render_template('patient.html',sit1=['Lab', 'pascription', 'DC4'],sit2=[1,23,4],value=('https://ipfs.io/ipfs/'+str(result[1])),v=b)
        #if f!=None:
        elif 'submit' in request.form:
            publickey=request.form['Publickey']
            session['publickey']=publickey
            print('public',publickey,session['result'],session['gather'])
            a=msg_signature.signature(session['result'],session['privatekey'])
            session['msghash']=a[0]
            session['msgsignature']=a[1]
            b=msg_signature.signature_verify(session['msghash'],session['msgsignature'])
            check.data_upload(contract,session['gather'],publickey,session['result'])
            return render_template('patient.html',sit1=['Lab', 'pascription', 'DC4'],sit2=[1,2,3],value=('https://ipfs.io/ipfs/'+str(session['result'])),v=session['msgsignature'])
        else:
            None
        return redirect(url_for('patient'))
    elif request.method=='GET':
        None
    return render_template('patient.html',sit1=['Lab', 'pascription', 'DC4'],sit2=[1,2,3,'last message'])

@app.route('/upload')
def upload_file():

    return render_template('uploader.html',sit1=['Lab', 'pascription', 'DC4'])
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      print(f)
      new_file = api.add(f)
      session['datatype']=request.form['site']
      print(new_file)
      check.data_upload(contract,session['datatype'],session['address'],new_file['Hash'])
      #f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == "__main__":
    app.run()