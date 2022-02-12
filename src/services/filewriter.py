class Filewriter:

    def __init__(self, filename, path) -> None:
        self.file = path + filename

    def write_to_file(self, content):
        with open(self.file, "a") as log_file:
            log_file.write(content)
            