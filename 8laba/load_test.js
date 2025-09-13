import http from 'k6/http';
import { sleep, check } from 'k6';

// Настройка сценариев нагрузки
export const options = {
    stages: [
        { duration: '30s', target: 10 },  // 10 пользователей 30 секунд
        { duration: '10s', target: 50 },  // 50 пользователей 10 секунд
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'], // 95% запросов < 500ms
        'http_req_failed': ['rate<0.01'], // Ошибки < 1%
    },
};

export default function () {
    const res = http.get('http://localhost:3000/posts'); // наш локальный API
    check(res, {
        'status is 200': (r) => r.status === 200,   // проверка, что ответ OK
        'has posts': (r) => r.json().length > 0,   // проверка, что вернулся массив
    });
    sleep(1); // пауза между запросами
}
