from agroubot import client


def test():
    yield from client.send_message("493132013914554369", "test")
