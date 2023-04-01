from moralis import evm_api

api_key = "RaIYwygywhhv3PyS2BXs8ty85CYWY2Qys3XBFDPhdrqE8tdO1yD5CojR1Z7RYuNU"
params = {
    "block_number_or_hash": "15846571",
    "chain": "eth",
    # "limit": 100,
    # "cursor": "",
}

result = evm_api.nft.get_nft_transfers_by_block(
    api_key=api_key,
    params=params,
)
sales = []
for transfer in result["result"]:
    if int(transfer["value"]) > 0:
        sales.append(transfer)

print(sales)

