from flask import Flask, request, jsonify
from ai_agent import AIAgent

app = Flask(__name__)
agent = AIAgent("model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json.get('input_data')
    prediction = agent.predict(input_data)
    return jsonify({'prediction': prediction.tolist()})

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.json.get('text')
    processed_text = agent.process_text(text)
    return jsonify({'processed_text': processed_text})

if __name__ == '__main__':
    app.run(debug=True)
