import json
with open('input.json', 'r') as f:
    json.dump(json.load(f), open('output.json', 'w'), indent=4, sort_keys=True)
print("JSON keys sorted and written to 'output.json'.")