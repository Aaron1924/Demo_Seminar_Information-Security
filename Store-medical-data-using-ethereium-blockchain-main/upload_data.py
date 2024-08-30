from web3 import Web3
import json
import configs
class check:
    def check_data(data_type,address1,public_key,index):
        # Set up web3 connection with Ganache
        ganache_url = configs.GANACHE_URL
        web3= Web3(Web3.HTTPProvider(ganache_url))
                
        with open('smartcontract.json') as json_file:
            abi = json.load(json_file)
        bytecode = configs.bytecode
                	
                # set pre-funded account as sender
                
                # Create the contract instance with the newly-deployed address
        contract = web3.eth.contract(
           address=address1,
           abi=abi,
        )
        if data_type=="Lab":
            datasend=contract.functions.getlabByIndex(public_key,index).call()
        if data_type=="prescription":
            datasend=contract.functions.getprescriptonByIndex(public_key,index).call()
        return datasend
    def data_upload(contract,data_type,public_key,data):
        if data_type=='Lab':
            contract.functions.Lab(public_key,data).transact()
        elif data_type=='prescription':
           contract.functions.Prescription(public_key,data).transact()
        else:
            None
        