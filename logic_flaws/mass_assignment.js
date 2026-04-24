app.post('/update', (req, res) => {
    // ❌ Vulnerável
    const user = { ...req.body };
});