import asyncio
from threading import Thread
from concurrent.futures import Future
import functools

class WorkerThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.loop = None

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def stop(self):
        self.loop.call_soon_threadsafe(self.loop.stop)

    def _add_task(self, future, coro):
        task = self.loop.create_task(coro)
        future.set_result(task)

    def add_task(self, coro):
        future = Future()
        p = functools.partial(self._add_task, future, coro)
        self.loop.call_soon_threadsafe(p)
        return future.result() #block until result is available

    def cancel(self, task):
        self.loop.call_soon_threadsafe(task.cancel)