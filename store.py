from web3 import Web3
import time

def iot_read():
    # Baca suhu dan kelembaban dari sensor (misal sensor DHT)
    return "Temp: 27C;Humidity:93"

ipc_path = r'\\.\pipe\geth.ipc'

# Retry loop until successful connection to Geth IPC
while True:
    try:
        w3 = Web3(Web3.IPCProvider(ipc_path))
        if w3.eth.block_number is not None:
            print("Connected to Geth successfully.")
            break  # Exit loop when connected
    except OSError as e:
        print(f"OSError: {e}. Retrying in 5 seconds...")
    except Exception as e:
        print(f"Unexpected error: {e}. Retrying in 5 seconds...")
    time.sleep(1)  # Wait before retrying

# ABI for contract interaction
abi = [
    {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"dataList","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"string","name":"data","type":"string"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"getDataCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
    {"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"retrieveData","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
    {"inputs":[{"internalType":"string","name":"_data","type":"string"}],"name":"storeData","outputs":[],"stateMutability":"nonpayable","type":"function"}
]

contract_address = '0xB8FED6DCe645c3b9a8269565Fb3ba5647169670c'
sender_address = '0xb5d83AC8B1d4829FF68844DA34Fe9E7778a6D06B'
key_utc_file = r'data\keystore\UTC--2024-08-21T05-45-17.497435400Z--b5d83ac8b1d4829ff68844da34fe9e7778a6d06b'

with open(key_utc_file) as keyfile:
    key_data = keyfile.read()
    pwd = 'rahasia'  # Password to decrypt the private key
    private_key = w3.eth.account.decrypt(key_data, pwd)

contract = w3.eth.contract(address=contract_address, abi=abi)

def store_data(data, nonce):
    transaction = contract.functions.storeData(data).build_transaction({
        'from': sender_address,
        'gas': 2000000,
        'gasPrice': w3.to_wei('1.1', 'gwei'),
        'nonce': nonce
    })

    # Menandatangani transaksi
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt)
    print(w3.eth.get_transaction_count(sender_address))

# Mendapatkan nonce dan menyimpan data
nonce = w3.eth.get_transaction_count(sender_address)
store_data(iot_read(), nonce)