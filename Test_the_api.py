import requests
res = requests.post('http://127.0.0.1:5000/find_symbols_in_names', json={
    "chemicals": ['Amazon', 'Microsoft', 'Google'],
    "symbols": ['I', 'Am', 'cro', 'Na', 'le', 'abc']
})
if res.ok:
    print(res.json())
