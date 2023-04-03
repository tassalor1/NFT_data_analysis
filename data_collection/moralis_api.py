from moralis import evm_api
import time

api_key = "RaIYwygywhhv3PyS2BXs8ty85CYWY2Qys3XBFDPhdrqE8tdO1yD5CojR1Z7RYuNU"

start_block = 16308190  # First block of 2023

# End block params
params = {
    "date": str(int(time.time())), # unix time
    "chain": "eth"
}

# End block
result = evm_api.block.get_date_to_block(
    api_key=api_key,
    params=params,
)
end_block = result["block"]

sales = []

# For loop
for block_number in range(start_block, end_block + 1):
    params1 = {
        "block_number_or_hash": str(block_number),
        "chain": "eth",
    }

    result1 = evm_api.nft.get_nft_transfers_by_block(
        api_key=api_key,
        params=params1,
    )

    # Only show value above 0 - which is a sale
    for transfer in result1["result"]:
        if int(transfer["value"]) > 0:
            sales.append(transfer)

# Only print value
# Convert wei to eth
for sale in sales:
    time_stamp = sale["block_timestamp"]
    ether_value = int(sale["value"]) / 10**18
    print(time_stamp)
    print(ether_value)
