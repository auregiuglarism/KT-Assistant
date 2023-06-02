from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow import keras
from keras.models import load_model
import nltk

app = Flask(__name__)
CORS(app)


class Model:
    def __init__(self):
        print("where")
        self.preprocessed_passage = None
        print("are")
        nltk.download("punkt")
        print("you")
        self.trained = False
        print("stuck")
        self.model = load_model('saved_model_1')
        print("mate")

    def clean(self, text, stem_words=True):
        import re  # for regular expressions
        from string import punctuation

        text = re.sub("\'s", " ", text)
        text = re.sub(" whats ", " what is ", text, flags=re.IGNORECASE)
        text = re.sub("\'ve", " have ", text)

        text = re.sub("can't", "cannot", text, flags=re.IGNORECASE)
        text = re.sub("don't", "do not", text, flags=re.IGNORECASE)
        text = re.sub("won't", "will not", text, flags=re.IGNORECASE)
        text = re.sub("shouldn't", "should not", text, flags=re.IGNORECASE)
        text = re.sub("couldn't", "could not", text, flags=re.IGNORECASE)
        text = re.sub("isn't", "is not", text, flags=re.IGNORECASE)
        text = re.sub("wasn't", "was not", text, flags=re.IGNORECASE)
        text = re.sub("weren't", "were not", text, flags=re.IGNORECASE)
        text = re.sub("haven't", "have not", text, flags=re.IGNORECASE)
        text = re.sub("hasn't", "has not", text, flags=re.IGNORECASE)
        text = re.sub("hadn't", "had not", text, flags=re.IGNORECASE)

        # remove comma between numbers, i.e. 15,000 -> 15000
        text = re.sub('(?<=[0-9])\,(?=[0-9])', "", text)

        # remove punctuation
        text = re.sub(r'[^\w\s]', ' ', text)

        # Return a list of words
        return text

    def preprocess(self, text):
        # Apply pre-processing to data
        t = self.clean(text)
        #t = nltk.tokenize.word_tokenize(t)

        return t

    def train(self, text):
        print('Training model with text: {}'.format(text))
        #
        self.preprocessed_passage = self.preprocess(text)
        self.trained = True

    def predict(self, claim):
        if not self.trained:
            return None
        else:
            print('Making prediction for claim: {}'.format(claim))
            preprocessed_claim = self.preprocess(claim)

            x = self.preprocessed_passage + " __SEP__ " + preprocessed_claim
            prediction = self.model.predict([x])

            return prediction[0][0]


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
    print(prediction)
    print(type(prediction))

    return jsonify({'answer': float(prediction)})


if __name__ == '__main__':
    model = Model()
    app.run(host='0.0.0.0', port=5000)
    print('Model loaded')
    print('waiting for requests...')
