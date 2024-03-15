function classifyText() {
    var artsKnownInput = document.getElementById("arts_known");
    var artsKnownValue = document.getElementById("arts_known_input").value;
    artsKnownInput.value = artsKnownValue;

    // Use AJAX to send userInput to the Flask backend
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/submit_form", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Update the result div with the classification result
            var resultDiv = document.getElementById("result");
            var response = JSON.parse(xhr.responseText);
            resultDiv.innerHTML = "Prediction: " + response.result;
        }
    };

    var data = "user_input=" + encodeURIComponent(userInput);
    xhr.send(data);
}
