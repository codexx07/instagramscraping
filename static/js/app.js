document.getElementById('scrapeForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    var formData = new FormData(event.target);
    var object = {};
    formData.forEach(function(value, key){
        object[key] = value;
    });
    var json = JSON.stringify(object);

    fetch('/scrape', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: json
    })
    .then(response => {
        if (response.status === 200) {
            // If the status is 200, click the button
            document.getElementById('downloadButton').click();
        }
        return response.json();
    })
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('downloadButton').style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('downloadButton').addEventListener('click', function() {
    fetch('/download')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.blob();
    })
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'comments.csv'); // or any other filename you want
        document.body.appendChild(link);
        link.click();

        document.body.removeChild(link);
    })
    .catch(error => console.error('Error:', error));
});