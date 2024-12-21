from web3 import Web3
from datetime import datetime, timezone
import time

# Konfigurasi koneksi
ipc_path = r'\\.\pipe\geth.ipc'

def connect_to_geth(ipc_path, retries=33, delay=1):
    for attempt in range(retries):
        try:
            w3 = Web3(Web3.IPCProvider(ipc_path))
            # Check if the connection is successful by querying block number
            if w3.eth.block_number is not None:
                print("Connected to Geth successfully.")
                return w3
            else:
                raise ConnectionError("Failed to get block number.")
        except Exception as e:
            print(f"Connection failed: {e}. Retrying... (Attempt {attempt + 1})")
            time.sleep(delay)
    raise ConnectionError("Failed to connect to Geth after multiple attempts")

# Connect to Geth
w3 = connect_to_geth(ipc_path)

# ABI dan alamat kontrak
abi = [{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"dataList","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"string","name":"data","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getDataCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"retrieveData","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_data","type":"string"}],"name":"storeData","outputs":[],"stateMutability":"nonpayable","type":"function"}]

contract_address = '0xB8FED6DCe645c3b9a8269565Fb3ba5647169670c'
contract = w3.eth.contract(address=contract_address, abi=abi)

# Ambil jumlah data dari kontrak
try:
    count = contract.functions.getDataCount().call()
    print(f"Total data count: {count}")

    # Ambil dan cetak data
    for i in range(count):
        try:
            timestamp, data = contract.functions.retrieveData(i).call()
            dt = datetime.fromtimestamp(timestamp, timezone.utc)  # Use timezone-aware UTC datetime
            print(f'{i}. Data retrieved: Timestamp: {dt.strftime("%Y-%m-%d %H:%M:%S")}, Data: {data}')
        except Exception as e:
            print(f"Error retrieving data at index {i}: {e}")
except Exception as e:
    print(f"An error occurred: {e}")