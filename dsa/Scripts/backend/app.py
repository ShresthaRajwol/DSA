from flask import Flask, jsonify
from flask_cors import CORS
from trie import Trie

app = Flask(__name__)

# ✅ Enable CORS here (right after app creation)
CORS(app)

trie = Trie()

# Load dictionary data
def load_data():
    with open("words.txt", "r") as f1, open("meanings.txt", "r") as f2:
        words = f1.readlines()
        meanings = f2.readlines()

        for w, m in zip(words, meanings):
            trie.insert(w.strip(), m.strip())

load_data()

@app.route("/api/search/<word>")
def search(word):
    meaning = trie.search(word)

    if meaning:
        return jsonify({
            "word": word,
            "meaning": meaning
        })

    return jsonify({
        "error": "Word not found"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)