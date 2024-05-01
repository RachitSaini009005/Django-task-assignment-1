// script.js

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('text-form');
    const results = document.getElementById('results');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Get input values
        const text1 = document.getElementById('text1').value;
        const text2 = document.getElementById('text2').value;
        const text3 = document.getElementById('text3').value;

        // Create new paragraphs with entered text
        const paragraph1 = document.createElement('p');
        paragraph1.textContent = text1;
        paragraph1.style.color = 'blue';

        const paragraph2 = document.createElement('p');
        paragraph2.textContent = text2;
        paragraph2.style.color = 'green';

        const paragraph3 = document.createElement('p');
        paragraph3.textContent = text3;
        paragraph3.style.color = 'red';

        // Clear previous results
        results.innerHTML = '';

        // Append paragraphs to results div
        results.appendChild(paragraph1);
        results.appendChild(paragraph2);
        results.appendChild(paragraph3);

        // Reset form
        form.reset();
    });
});
