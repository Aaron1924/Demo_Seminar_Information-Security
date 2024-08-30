from web3.auto import w3
from eth_account.messages import encode_defunct
from web3 import Web3
import time
# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:5000"
web3 = Web3(Web3.HTTPProvider(ganache_url))
class msg_signature:
    
    def signature(msg,privatekey):
        private_key =web3.toBytes(hexstr=privatekey)
        
        message = encode_defunct(text=msg)
        signed_message = web3.eth.account.sign_message(message, private_key=private_key)
        print(signed_message)
        
        message = encode_defunct(text=msg)
        return message,signed_message.signature
    def signature_verify(messagehash,signature):
        a=web3.eth.account.recover_message(messagehash, signature=signature)
        
        return( "message is send by"+str(a))
#start_time = time.time()
#msg='qeq'
#key='b8dc057d97dfeb862c735833bdc7414451594f40f01e51a3255e6e22a62b5e82'
#a=msg_signature.signature(msg,key)
#print("--- %s seconds --- for signature create" % (time.time() - start_time))
#start_time = time.time()
#print(msg_signature.signature_verify(a[0],a[1]))
#print("--- %s seconds --- for signature verify" % (time.time() - start_time))