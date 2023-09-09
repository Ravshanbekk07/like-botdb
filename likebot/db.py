import json
import os


class DB:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        # check if file exists
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                json.dump({}, f)
        else:
            with open(file_name, "r") as f:
                self.data = json.load(f)

    def save(self) -> None:
        with open(self.file_name, "w") as f:
            json.dump(self.data, f, indent=4)

    def add(self, chat_id: int, name: str) -> None:
        self.data[str(chat_id)] = {"likes": 0, "dislikes": 0, "name": name}
        self.save()

    def inc_like(self, chat_id: int) -> None:
        self.data[str(chat_id)]["likes"] += 1
        self.save()
    
    def inc_dislike(self, chat_id: int) -> None:
        self.data[str(chat_id)]["dislikes"] += 1
        self.save()