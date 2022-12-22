class File(object):
    try:

        def __init__(self, file_name, method):
            if method == "r":
                try:
                    self.file_obj = open(file_name, method)
                except IOError and FileNotFoundError:
                    self.file_obj = open(file_name, "w")
            else:
                self.file_obj = open(file_name, method)

        def __enter__(self):
            return self.file_obj

        def __exit__(self, type, value, traceback):
            self.file_obj.close()
    except Exception as err:
        pass


with File("nonexistantfile.txt", "r") as fr:
    fr.close()
