

$(document).ready(function() {

    // this function takes the data provided in the form in form.html and sends it as JSON 
    // to the /submit_form endpoint of the Flask app in a POST request. It then takes the 
    // response JSON from the /submit_form endpoint and puts the 'response' into the text of
    // the #response div element of the form.html page.

    $("#myForm").submit(function(event) {
        event.preventDefault();
        
        var formData = {
            "message": $("#message").val()
        };

        $.ajax({
            type: "POST",
            url: "/submit_form",
            data: JSON.stringify(formData),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(data) {
                $("#response").text(data.response);
            },
            error: function(errMsg) {
                console.error("Error:", errMsg);
            }
        });
    });
});









document.addEventListener('DOMContentLoaded', function () {
    // This function handles the file submission of the fileUploadForm in the form.html page
    // The selected file is submitted as a POST request to the upload_file Flask endpoint in main.py
    // The Flask endpoint then returns a message based on if it was able to upload the file or not.
    // This message is written to the fileUploadSubmitMessage element in form.html
    var form = document.getElementById('fileUploadForm');
    form.onsubmit = function(event) {
        event.preventDefault(); // Prevent the default form submission
        var formData = new FormData(form);
        fetch('/upload_file', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('fileUploadSubmitMessage').textContent = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };
});





