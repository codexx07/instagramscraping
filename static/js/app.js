document.getElementById('scrapeForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(event.target);
    var data = {
        username: formData.get('username'),
        password: formData.get('password'),
        postlink: formData.get('postlink')
    };

    fetch('/scrape', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);

        var downloadButton = document.getElementById('downloadButton');
        downloadButton.style.display = 'block'; // or 'inline', 'inline-block', etc.
        downloadButton.addEventListener('click', function() {
            window.location.href = '/download';
        });

        // Add the button to the DOM
        document.getElementById('buttonContainer').appendChild(downloadButton);
    });
});