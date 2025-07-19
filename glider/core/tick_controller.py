# glider/core/tick_controller.py

import threading
import time


class TickController:
    """
    Drives a GliderEngine forward at a constant tick interval.
    Designed to run in a background daemon thread so the Flask server
    remains responsive.
    """

    def __init__(self, engine, interval=0.5):
        """
        :param engine: An instance of GliderEngine (or compatible step-based engine)
        :param interval: Seconds between ticks (float)
        """
        self.engine = engine
        self.interval = interval
        self._running = False
        self._thread = None

    # public API - logic tie ins

    def start(self):
        """Begin the background tick loop."""
        if self._running:  # already running
            return
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop the background tick loop and wait for it to finish."""
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join()

    def clear(self, pattern):
        """Reset the engine to its original pattern."""
        self.stop()
        self.engine.reset(pattern)

    def step_once(self):
        """Advance the engine exactly one tick (synchronous)."""
        self.engine.tick()


    # -- ineternal method for looping with threads
    def _loop(self):
        """Background thread loop."""
        while self._running:
            start = time.time()
            self.engine.tick()
            elapsed = time.time() - start
            sleep_time = max(0.0, self.interval - elapsed)
            time.sleep(sleep_time)
