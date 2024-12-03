
document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("predictionForm");
    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the default form submission
        var formData = new FormData(form);
        var requestData = {};
        // formData.forEach(function(value, key) {
        //     requestData[key] = value;
        // });
    
        formData.forEach(function(value, key) {
            var numericValue = parseFloat(value);  // Convertir la valeur en nombre
            if (!isNaN(numericValue)) {  // Vérifier si la valeur est un nombre
                requestData[key] = -numericValue;  // Appliquer la négation
            } else {
                requestData[key] = value;  // Si ce n'est pas un nombre, garder la valeur d'origine
            }
        });

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('predictionResult').textContent = 'Estimated Price: $' + data.prediction[0].toFixed(2);
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById('predictionResult').textContent = 'Error predicting price.';
        });
    });
});
