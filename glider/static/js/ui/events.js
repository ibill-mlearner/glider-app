// glider/static/js/ui/events.js

/**
 * Bind control buttons to simulation endpoints.
 * 
 *  - Start -- POST /api/start  : begin continuous ticking on server
 *  - Stop  -- POST /api/stop   : halt continuous ticking
 *  - Step  -- POST /api/step   : advance one frame on server and return state
 *  - Tick  -- POST /api/tick   : alias for step (single frame for debugging)
 *  - Clear -- PUT  /api/clear  : (future) reset grid to empty pattern
 *
 * All callbacks default to calling the REST endpoints directly via fetch.
 * invoking attachButtonHandlers in bootstrap_combined.js.
 */


function defaultPost(endpoint, body = {}) {
    return fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
    });
}

function defaultPut(endpoint, body = {}) {
    return fetch(endpoint, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
    });
}

export function attachButtonHandlers({ // BP routes combined
    onStart = () => defaultPost('/api/start'),
    onStop  = () => defaultPost('/api/stop'),
    onStep  = () => defaultPost('/api/step'),
    onTick  = () => defaultPost('/api/tick'),
    onClear = () => defaultPut('/api/clear')
} = {}) {
    document.getElementById('btn-start')?.addEventListener('click', onStart);
    document.getElementById('btn-stop')?.addEventListener('click', onStop);
    document.getElementById('btn-step')?.addEventListener('click', onStep);
    document.getElementById('btn-tick')?.addEventListener('click', onTick);
    document.getElementById('btn-clear')?.addEventListener('click', onClear);
}