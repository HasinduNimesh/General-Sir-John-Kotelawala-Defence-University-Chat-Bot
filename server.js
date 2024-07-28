const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const fs = require('fs');
const app = express();
const server = http.createServer(app);
const io = socketIo(server);
const intents = JSON.parse(fs.readFileSync('intents.json'));

app.use(express.static('public'));

io.on('connection', (socket) => {
    console.log('A user connected');

    socket.on('message', (data) => {
        const userMessage = data.message.toLowerCase();
        let botResponse = getResponse(userMessage);
        socket.emit('response', { message: botResponse });
    });

    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

function getResponse(userMessage) {
    for (let intent of intents.intents) {
        for (let pattern of intent.patterns) {
            if (userMessage.includes(pattern.toLowerCase())) {
                const responses = intent.responses;
                return responses[Math.floor(Math.random() * responses.length)];
            }
        }
    }
    // Default response if no patterns match
    const unknownIntent = intents.intents.find(intent => intent.tag === 'unknown');
    return unknownIntent.responses[Math.floor(Math.random() * unknownIntent.responses.length)];
}

