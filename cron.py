import asyncio
from agroubot import client


@asyncio.coroutine
def test():
    yield from client.send_message("493132013914554369", "test")
