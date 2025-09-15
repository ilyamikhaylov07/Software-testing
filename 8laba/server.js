const express = require('express');
const app = express();
const PORT = 3000;

// Простая заглушка GET
app.get('/posts', (req, res) => {
    const posts = [
        { id: 1, title: 'Post 1', body: 'Content 1' },
        { id: 2, title: 'Post 2', body: 'Content 2' },
        { id: 3, title: 'Post 3', body: 'Content 3' },
    ];
    res.json(posts);
});

// GET по ID
app.get('/posts/:id', (req, res) => {
    const { id } = req.params;
    const post = { id, title: `Post ${id}`, body: `Content ${id}` };
    res.json(post);
});

// Запуск сервера
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
