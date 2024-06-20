# Автотест для удаления пользователей

## Цель задачи

Написать автотест для функциональности, которая позволяет администраторам удалять существующих пользователей.

## Тестовые данные

- **Базовый URL release стенда**: 
  `https://release-gs.qa-playground.com/api/v1`

### Заголовки

```json
{
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzE5MzE0MDc2LCJpYXQiOjE3MTg3MTQwNzYsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6Ijc3NmQzMmRhLWU3OTktNDQ5OS1iNWZhLTI1ZjFhMzNkYzNhZiIsImVtYWlsIjoid2FsdGFmdW5rQGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ2l0aHViIiwicHJvdmlkZXJzIjpbImdpdGh1YiJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9hdmF0YXJzLmdpdGh1YnVzZXJjb250ZW50LmNvbS91LzgxMjg0NTUyP3Y9NCIsImVtYWlsIjoid2FsdGFmdW5rQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiJaaGlraGFyZXZfQWxleGV5IiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJaaGlraGFyZXZfQWxleGV5IiwicGhvbmVfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJaaGlraGFyZXZBbCIsInByb3ZpZGVyX2lkIjoiODEyODQ1NTIiLCJzdWIiOiI4MTI4NDU1MiIsInVzZXJfbmFtZSI6IlpoaWtoYXJldkFsIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE3MTY1NjAxMTJ9XSwic2Vzc2lvbl9pZCI6ImRiOTI4YzMxLTg3MjEtNGU4OC1iYjQyLTZlMjA4NjExYzI3YSIsImlzX2Fub255bW91cyI6ZmFsc2V9.PZB3eiH2zupHb0eCXU1Ow1Vpd6UDFI8a3zydqB9SvBs",
  "X-Task-Id": "API-1"
}
```

### Bearer-токен

`eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzE5MzE0MDc2LCJpYXQiOjE3MTg3MTQwNzYsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6Ijc3NmQzMmRhLWU3OTktNDQ5OS1iNWZhLTI1ZjFhMzNkYzNhZiIsImVtYWlsIjoid2FsdGFmdW5rQGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ2l0aHViIiwicHJvdmlkZXJzIjpbImdpdGh1YiJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9hdmF0YXJzLmdpdGh1YnVzZXJjb250ZW50LmNvbS91LzgxMjg0NTUyP3Y9NCIsImVtYWlsIjoid2FsdGFmdW5rQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiJaaGlraGFyZXZfQWxleGV5IiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJaaGlraGFyZXZfQWxleGV5IiwicGhvbmVfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJaaGlraGFyZXZBbCIsInByb3ZpZGVyX2lkIjoiODEyODQ1NTIiLCJzdWIiOiI4MTI4NDU1MiIsInVzZXJfbmFtZSI6IlpoaWtoYXJldkFsIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE3MTY1NjAxMTJ9XSwic2Vzc2lvbl9pZCI6ImRiOTI4YzMxLTg3MjEtNGU4OC1iYjQyLTZlMjA4NjExYzI3YSIsImlzX2Fub255bW91cyI6ZmFsc2V9.PZB3eiH2zupHb0eCXU1Ow1Vpd6UDFI8a3zydqB9SvBs`

Вы можете использовать этот токен на протяжении всей тестовой сессии, включая последующие задачи.

## Документация

- [Redoc](https://redocly.github.io/redoc/?url=https://release-gs.qa-playground.com/api/v1/swagger.json)
- [Swagger](https://petstore.swagger.io/?url=https://release-gs.qa-playground.com/api/v1/swagger.json)

## Предусловия

1. Авторизоваться в системе через Bearer token (взять его из заголовков выше).
2. Использовать Базовый URL релизного стенда, указанный в тестовых данных, для отправки запросов во время тестирования.
3. Отправить POST запрос на эндпоинт `/setup` для настройки/сброса вашей тестовой среды.
   - Если вы получили код 401, возможно, ваш токен отсутствует или истек. В этом случае, необходимо скопировать его снова из заголовка выше.
4. Настроенная тестовая среда работает на протяжении всей тестовой сессии, в том числе и для последующих задач.
5. Каждый этап тестирования использует одну и ту же базу данных.

## Тест-кейс для автоматизации

1. Отправить GET запрос на эндпоинт `/users` для получения списка пользователей.
2. Выбрать любого пользователя из списка и взять его `uuid`.
3. Отправить DELETE запрос на эндпоинт `/users/{uuid}` с ранее взятым `uuid` пользователя в качестве параметра.
4. Убедиться, что получен ответ со статусом 204.
5. Подтвердить, что пользователь был удален из списка пользователей, отправив GET запрос на эндпоинт `/users`.
6. Проверить, что информация о пользователе не возвращается, отправив GET запрос с `uuid` пользователя на эндпоинт `/users/{uuid}`.

## Постусловия

После написания автотеста и его запуска на release стенде (рабочей версии), запустить тест на dev стенде (версия с дефектами), чтобы

 проверить качество теста и его способность отлавливать дефекты.

- **Базовый URL dev стенда**: 
  `https://dev-gs.qa-playground.com/api/v1`

## Приемочные критерии

1. Код статуса ответа после удаления — 204.
2. Пользователь не отображается в списке пользователей.
3. Информация о пользователе не отображается при запросе по его `uuid`.