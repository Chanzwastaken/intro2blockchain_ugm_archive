import time
from web3 import Web3

ipc_path = r'\\.\pipe\geth.ipc'

while True:
    try:
        w3 = Web3(Web3.IPCProvider(ipc_path))
        if w3.is_connected():
            print("Connected to the node!")
            break
        else:
            print("Connection failed, retrying...")
    except OSError as e:
        print(f"OSError: {e}, retrying in 1 seconds...")
        time.sleep(1)

receiver_address = '0x572fdAD8DB65b28500987c194e9A5f49655Fd431'
sender_address = '0xb5d83AC8B1d4829FF68844DA34Fe9E7778a6D06B'
key_utc_file = r'data\keystore\UTC--2024-08-21T05-45-17.497435400Z--b5d83ac8b1d4829ff68844da34fe9e7778a6d06b'

with open(key_utc_file) as keyfile:
    key_data = keyfile.read()
    pwd = 'rahasia'
    private_key = w3.eth.account.decrypt(key_data, pwd)

nonce = w3.eth.get_transaction_count(sender_address)
transaction = {
    'chainId': 110261,
    'nonce': nonce,
    'gasPrice': w3.to_wei(1.0001, 'gwei'),
    'gas': 2000000,
    'from': sender_address,
    'to': receiver_address,
    'value': w3.to_wei(0.00000005, 'ether'),
}

signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Transaction hash: {tx_hash.hex()}")
print(f"Transaction receipt: {tx_receipt}")
print(f"Recipient Balance: {w3.eth.get_balance(receiver_address)}")