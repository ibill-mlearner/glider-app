// glider/static/js/ui/buttons.js

export function createButtonBar(container = document.body) {
    const bar = document.createElement('div');
    bar.id = 'button-bar';
    bar.style.position = 'absolute';
    bar.style.top = '10px';
    bar.style.left = '10px';
    bar.style.zIndex = '10';
    bar.style.display = 'flex';
    bar.style.gap = '10px';

    const buttons = [
        { id: 'btn-start', text: 'Start' },
        { id: 'btn-stop', text: 'Stop' },
        { id: 'btn-step', text: 'Step' },
        { id: 'btn-clear', text: 'Clear' }
    ];

    buttons.forEach(({ id, text }) => {
        const btn = document.createElement('button');
        btn.id = id;
        btn.textContent = text;
        btn.style.padding = '5px 10px';
        btn.style.fontSize = '14px';
        bar.appendChild(btn);
    });

    container.appendChild(bar);
}