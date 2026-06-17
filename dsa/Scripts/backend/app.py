from flask import Flask, jsonify, request
from flask_cors import CORS
from trie import Trie

app = Flask(__name__)
CORS(app)

trie = Trie()

def load_data():
    with open("words.txt", "r") as f1, open("meanings.txt", "r") as f2:
        words = f1.readlines()
        meanings = f2.readlines()

        for w, m in zip(words, meanings):
            trie.insert(w.strip(), m.strip())

load_data()


# ---------------- EXACT SEARCH ----------------
@app.route("/api/search/<word>")
def search(word):
    meaning = trie.search(word)

    if meaning:
        return jsonify({
            "word": word,
            "meaning": meaning
        })

    return jsonify({"error": "Word not found"}), 404


# ---------------- AUTOCOMPLETE ----------------
@app.route("/api/autocomplete")
def autocomplete():
    prefix = request.args.get("q", "").strip().lower()

    if not prefix:
        return jsonify([])

    results = trie.starts_with(prefix)

    return jsonify([
        {"word": w, "meaning": m}
        for w, m in results
    ])


if __name__ == "__main__":
    app.run(debug=True)