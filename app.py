from flask import Flask, request, jsonify, json, redirect

app=Flask(__name__)

incomes =[
    {
        'descriptioin': 'salary',
        'amount':5000
    }
]

@app.route('/incomes')
def get_incomes():
    print("gets")
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def post_incomes():
    if request.is_json:
        data=json.loads(request.data)
        print(data)
        print("--------------")
        incomes.append(data)
        print(incomes)
    else:
        return 'Invalid Data'
    return data


@app.route('/')
def home():
    #return 'hello world'
    return redirect("/incomes")



if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000)