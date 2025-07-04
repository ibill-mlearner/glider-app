// glider/static/js/ui/events.js

export function attachButtonHandlers({
    onStart = () => {},
    onStop = () => {},
    onStep = () => {},
    onClear = () => {}
} = {}) {
    document.getElementById('btn-start')?.addEventListener('click', onStart);
    document.getElementById('btn-stop')?.addEventListener('click', onStop);
    document.getElementById('btn-step')?.addEventListener('click', onStep);
    document.getElementById('btn-clear')?.addEventListener('click', onClear);
}