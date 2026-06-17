document.getElementById("searchForm").addEventListener("submit", function (e) {
    e.preventDefault(); // stop page reload

    let word = document.getElementById("wordInput").value;

    fetch(`http://127.0.0.1:5000/api/search/${word}`)
        .then(response => response.json())
        .then(data => {
            let resultDiv = document.getElementById("result");

            if (data.meaning) {
                resultDiv.innerHTML = `
                    <h3>${data.word}</h3>
                    <p>${data.meaning}</p>
                `;
                //console.log(data.word+"\n"+data.meaning)
            } else {
                resultDiv.innerHTML = `<p>Word not found</p>`;
            }
        })
        .catch(err => {
            console.log(err);
        });
});