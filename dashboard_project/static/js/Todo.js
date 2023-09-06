// script.js
document.addEventListener('DOMContentLoaded', function () {
    const taskList = document.querySelector('.task-list');
    const taskInput = document.getElementById('taskInput');
    const addTaskButton = document.getElementById('addTask');

    addTaskButton.addEventListener('click', function () {
        const taskText = taskInput.value.trim();
        if (taskText) {
            const taskItem = document.createElement('div');
            taskItem.classList.add('task-item');
            taskItem.innerHTML = `
                <span>${taskText}</span>
                <button class="delete-button">Delete</button>
            `;

            taskList.appendChild(taskItem);

            // Clear the input field
            taskInput.value = '';
        }
    });

    taskList.addEventListener('click', function (event) {
        if (event.target.classList.contains('delete-button')) {
            event.target.parentElement.remove();
        }
    });
});
