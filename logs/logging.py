from datetime import datetime


def log(tag="", msg=""):
    with open("log.txt", "w+", encoding="utf-8") as file:
        current_time = datetime.now()
        file.write(f"--[{current_time}]-- {tag}:\t\t >>> {msg}\n")
