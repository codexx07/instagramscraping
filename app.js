document.getElementById('scrapeForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(event.target);

    fetch('/scrape', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => console.log(data));
});