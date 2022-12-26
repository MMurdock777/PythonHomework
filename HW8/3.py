class File(object):

    def __init__(self, file_name: str, method: str):
        self.file_name = file_name
        self.method = method

    def __enter__(self):
        try:
            self.file_obj = open(self.file_name, self.method)
        except IOError or FileNotFoundError:
            self.file_obj = open(self.file_name, "w")
        return self.file_obj

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type is IOError or FileNotFoundError:
            self.file_obj.close()
            return True
        self.file_obj.close()


with File("nonexistantfile.txt", "r") as fr:
    fr.close()
