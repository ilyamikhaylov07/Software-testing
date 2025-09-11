const addBtn = document.getElementById('add-btn');
const input = document.getElementById('todo-input');
const list = document.getElementById('todo-list');

addBtn.addEventListener('click', addTodo);

function addTodo() {
    const text = input.value.trim();

    // БАГ #1: Позволяет добавить пустую задачу
    if (text === '') {
        alert("Введите задачу"); // баг: alert иногда не отображается в Firefox
    }

    const li = document.createElement('li');
    li.textContent = text;

    // БАГ #2: Скрытая кнопка удаления, которая не всегда работает
    const removeBtn = document.createElement('button');
    removeBtn.textContent = 'X';
    removeBtn.className = 'remove-btn';
    removeBtn.addEventListener('click', function() {
        // баг: удаляет не тот элемент при двойном клике
        list.removeChild(li);
    });

    li.appendChild(removeBtn);

    // БАГ #3: Невозможно отметить задачу завершенной при первом клике
    let firstClick = true; // флаг для имитации бага

    li.addEventListener('click', function(e) {
        if (e.target.tagName !== 'BUTTON') {
            if (firstClick) {
                firstClick = false; 
                return; // первый клик игнорируется (баг)
            }
            li.classList.toggle('completed'); 
        }
    });

    list.appendChild(li);
    input.value = '';
}

// БАГ #4: При нажатии Enter ничего не происходит
input.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTodo(); // должно работать, но иногда не срабатывает
    }
});
