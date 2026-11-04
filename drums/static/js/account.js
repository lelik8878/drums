
document.getElementById('copy-btn').addEventListener('click', () => {
    // 1. Берем текст из элемента по его ID
    const text = document.getElementById('text-to-copy').innerText;
    const copyBtn = document.getElementById('copy-btn');

    // 2. Копируем в буфер обмена
    navigator.clipboard.writeText(text).then(() => {
        // 3. Простой отклик для пользователя
        try {
                // 4. Визуальный отклик (меняем иконку или цвет)
                const originalColor = copyBtn.style.color;
                copyBtn.style.color = '#22c55e'; // Зеленый цвет при успехе

                // Возвращаем цвет обратно через 1.5 секунды
                setTimeout(() => {
                    copyBtn.style.color = originalColor;
                }, 1500);

                console.log('Скопировано!');
            } catch (err) {
                console.error('Ошибка при копировании: ', err);
                alert('Не удалось скопировать текст');
            }

    });
});
