import modules.folderChecks as folderChecks # has the directories stored

def valid(username: str) -> None:
    with open(folderChecks.valid, "a") as file:
        file.write(f"{username}")

def invalid(username: str) -> None:
    with open(folderChecks.invalid, "a") as file:
        file.write(f"{username}")