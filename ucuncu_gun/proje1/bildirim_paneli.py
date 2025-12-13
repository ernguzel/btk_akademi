from dataclasses import dataclass
from typing import Protocol
@dataclass
class Mesaj:
    to: str
    content: str

class Sender(Protocol):
    def send(self, msg: Mesaj) -> None: ...

class EmailSender:
    def send(self, msg: str) -> None:
        print("email gonderildi ",msg)

class SmsSender:
    def send(self, msg: str) -> None:
        print("Sms gönderildi ", msg)

class Notifier:
    def __init__(self,sender: Sender):
        self.sender = sender

    def notify(self, message: Mesaj):
        self.sender.send(f"{message.to} : {message.content}")


notifier = Notifier(EmailSender())
notifier.notify(Mesaj("Ali","eve geç kalma"))

notifier_ = Notifier(SmsSender())
notifier_.notify(Mesaj("Ayşe","okula git"))

