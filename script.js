document.addEventListener("DOMContentLoaded", () => {
    const textContainer = document.getElementById('text-container');

    fetch('text.txt')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(text => {
            const splitText = text.split('\\');
            let index = 0;

            const displayNextPart = () => {
                if (index < splitText.length) {
                    textContainer.innerText = splitText[index].trim();
                    index++;
                    setTimeout(displayNextPart, 3000); // 3秒ごとに表示
                }
            };

            displayNextPart();
        })
        .catch(error => {
            console.error('Error fetching the text file:', error);
            textContainer.innerText = 'Error loading text file.';
        });
});
