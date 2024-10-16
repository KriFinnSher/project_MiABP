# Telegram Bot with Notification Scheduler and OpenAI Integration

## Описание

Этот проект — Telegram-бот, который позволяет пользователям устанавливать напоминания, управлять ими, а также общаться с ботом на базе **OpenAI GPT-3.5-Turbo** для генерации ответов. Программа использует библиотеку **schedule** для выполнения задач по времени и **telegram.ext** для работы с командной оболочкой бота.

## Основные возможности

- Установка и управление напоминаниями через Telegram.
- Интеграция с OpenAI для генерации творческих ответов на запросы.
- Автоматическое выполнение задач с использованием планировщика `schedule`.
- Асинхронная обработка запросов с использованием **asyncio**.

## Команды бота

1. **/start**: Отправляет приветственное сообщение пользователю.
2. **/set_notif \<время> \<сообщение>**: Устанавливает напоминание на определенное время в формате HH:MM.
3. **/list_notif**: Выводит список всех активных напоминаний.
4. **/del_notif \<время>**: Удаляет напоминание, установленное на указанное время.

## Структура кода

### Основные библиотеки

- **`telegram.ext`**: Используется для создания и управления Telegram-ботом.
- **`schedule`**: Используется для планирования выполнения задач.
- **`openai`**: Используется для подключения к OpenAI GPT-3.5-Turbo.
- **`asyncio`**: Обеспечивает асинхронное выполнение задач.

### Основные компоненты

- **`start`**: Отправляет приветственное сообщение пользователю, когда бот запускается.
- **`set_notification`**: Устанавливает напоминание на указанное пользователем время. Если время уже прошло, напоминание не устанавливается.
- **`list_notifications`**: Выводит список всех активных напоминаний.
- **`delete_notification`**: Удаляет напоминание, установленное на указанное время.
- **`notif_helper`**: Помогает отправлять уведомления пользователям в нужное время.
- **`run_scheduler`**: Запускает планировщик задач в отдельном потоке.

![image](https://github.com/user-attachments/assets/568d7fd1-0b80-4786-a239-779d916922c3)
![image](https://github.com/user-attachments/assets/6044db87-f971-4c8a-8105-abd57c73b4f2)
![image](https://github.com/user-attachments/assets/24ab3f1e-61cd-434a-8daf-4abeef42e2ce)
![image](https://github.com/user-attachments/assets/2510d2c2-dc3e-4015-919c-361b1c3b42aa)
![image](https://github.com/user-attachments/assets/9d3b6004-8c22-4d41-96ed-2681ae684dea)
![image](https://github.com/user-attachments/assets/f535ee68-fa1a-44cc-b2a8-6920a5f1471d)




