// -------------------- ELEMENTS --------------------
const form = document.getElementById("searchForm");
const input = document.getElementById("wordInput");
const resultDiv = document.getElementById("result");
const suggestions = document.getElementById("suggestions");

let timer; // for debounce

// -------------------- EXACT SEARCH --------------------
form.addEventListener("submit", function (e) {
    e.preventDefault();

    const word = input.value.trim();

    if (!word) {
        resultDiv.innerHTML = "<p>Please enter a word</p>";
        return;
    }

    fetch(`http://127.0.0.1:5000/api/search/${word}`)
        .then(res => {
            if (!res.ok) {
                throw new Error("Not found");
            }
            return res.json();
        })
        .then(data => {
            resultDiv.innerHTML = `
                <h3>${data.word}</h3>
                <p>${data.meaning}</p>
            `;
        })
        .catch(err => {
            resultDiv.innerHTML = `<p>Word not found</p>`;
            console.log(err);
        });
});


// -------------------- AUTOCOMPLETE (LIVE SEARCH) --------------------
input.addEventListener("input", () => {
    clearTimeout(timer);

    timer = setTimeout(() => {
        const query = input.value.trim();

        if (!query) {
            suggestions.innerHTML = "";
            return;
        }

        fetch(`http://127.0.0.1:5000/api/autocomplete?q=${query}`)
            .then(res => res.json())
            .then(data => {
                renderSuggestions(data.slice(0, 8));
            })
            .catch(err => console.log(err));
    }, 300); // debounce delay
});


// -------------------- RENDER SUGGESTIONS --------------------
function renderSuggestions(data) {
    suggestions.innerHTML = data
        .map(item => `<li class="suggestion-item">${item.word}</li>`)
        .join("");
}


// -------------------- CLICK SUGGESTION --------------------
suggestions.addEventListener("click", (e) => {
    if (e.target.classList.contains("suggestion-item")) {
        input.value = e.target.innerText;
        suggestions.innerHTML = "";
    }
});


// -------------------- HIDE SUGGESTIONS ON OUTSIDE CLICK --------------------
document.addEventListener("click", (e) => {
    if (!e.target.closest("#searchForm")) {
        suggestions.innerHTML = "";
    }
});