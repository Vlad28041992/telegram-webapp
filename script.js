function sendTask(task) {
  Telegram.WebApp.sendData(task);  // Отправить данные в бота
  Telegram.WebApp.close();         // Закрыть WebApp
}

Telegram.WebApp.expand(); // Сделать окно на весь экран