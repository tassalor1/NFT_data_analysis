# If import requests is not working try another IDE

import requests
import csv
from datetime import datetime

# Api key for etherscan
api_key = '    '
# Ethereum contract address
contract_address = "0x0000000000A39bb272e79075ade125fd351887Ac"
# etherscan url
base_url = 'https://api.etherscan.io/api'



def get_transactions(contract_address, api_key):
    # Define API URL parameters
    base_url = "https://api.etherscan.io/api"
    module = "account"
    action = "txlist"
    page = 1
    offset = 10000
    sort = "asc"

    # Calculate block numbers for one week ago and current block
    current_block_url = f"{base_url}?module=proxy&action=eth_blockNumber&apikey={api_key}"
    current_block = int(get(current_block_url).json()["result"], 16)
    one_week_ago_block = current_block - (1 * 24 * 60 * 4)

    # Create URL with parameters
    url = url = f"{base_url}?module={module}&action={action}&address={contract_address}&startblock={one_week_ago_block}&endblock={current_block}&page={page}&offset={offset}&sort={sort}&apikey={api_key}"


    # Send GET request to API and convert response to JSON
    response = get(url)
    data = response.json()

    # Write transaction data to CSV file
    with open("blur_bidding2.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Date", "From", "To", "Block Number", "Value (ETH)"])
        for txn in data["result"]:
            timestamp = int(txn["timeStamp"])
            date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            sender = txn["from"]
            receiver = txn["to"]
            value = int(txn["value"])/10**18
            block_number = txn["blockNumber"]
            writer.writerow([date, sender, receiver, block_number, value])

    print(f"Transaction data written to CSV file for contract address {contract_address}.")

contract_address = "0x0000000000A39bb272e79075ade125fd351887Ac"
api_key = ""
get_transactions(contract_address, api_key)