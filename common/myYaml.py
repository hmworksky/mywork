import yaml


class MyYaml(object):
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    def read(self,keys):
        data = yaml.load()
