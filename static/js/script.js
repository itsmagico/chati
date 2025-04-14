document.getElementById('chat-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const user = document.getElementById('user').value;
    const message = document.getElementById('message').value;

    if (user && message) {
        // Envia a mensagem via AJAX
        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `user=${encodeURIComponent(user)}&message=${encodeURIComponent(message)}`
        })
        .then(response => response.json())
        .then(data => {
            const chatBox = document.getElementById('chat-box');
            const newMessage = document.createElement('div');
            newMessage.classList.add('message');
            newMessage.innerHTML = `<strong>${data.user}:</strong> ${data.message}`;
            chatBox.appendChild(newMessage);
            chatBox.scrollTop = chatBox.scrollHeight; // Rolagem automática para a última mensagem
            document.getElementById('message').value = ''; // Limpa a caixa de texto
        });
    }
});
