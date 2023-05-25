from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


class Model:
    def __init__(self):
        self.trained = False

    def train(self, text):
        print('Training model with text: {}'.format(text))
        #
        self.trained = True

    def predict(self, claim):
        if not self.trained:
            return False
        else:

            print('Making prediction for claim: {}'.format(claim))
            return 'True' in claim


model = Model()


@app.route('/path-to-model-training', methods=['POST'])
def train_model():
    data = request.get_json()

    if 'text' not in data:
        return jsonify({'message': 'No text provided'}), 400

    model.train(data['text'])

    return jsonify({'message': 'Model trained successfully'})


@app.route('/path-to-model-prediction', methods=['POST'])
def make_prediction():
    data = request.get_json()

    if 'claim' not in data:
        return jsonify({'message': 'No claim provided'}), 400

    prediction = model.predict(data['claim'])

    return jsonify({'answer': prediction})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
