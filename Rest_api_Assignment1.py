from flask import Flask, jsonify, request 
import re
app = Flask(__name__)  
def get_symbol(chemicals, symbols):
    squared = []
    for sym in symbols:
        for chem in chemicals:
            regex = re.search(sym, chem)
            if regex:
                squared.append(re.sub(sym, "[{}]".format(sym), chem))

    return ", ".join(squared)
@app.route('/find_symbols_in_names', methods = ['POST']) 
def home():
        request_data = request.get_json()
        chemicals=None
        symbols =None
        if request_data:
            if 'chemicals' in request_data:
                chemicals = request_data['chemicals']

            if 'symbols' in request_data:
                symbols = request_data['symbols']
        if symbols and chemicals:
            return jsonify({"result":get_symbol(chemicals, symbols)})
  
if __name__ == '__main__': 
  
    app.run(debug = True)
