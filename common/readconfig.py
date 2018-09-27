import sys
sys.path.append('..')
import yaml
import config

class readConf(object):
    def __init__(self,name):
        self.name = name

    @property
    def getobj(self):
        '''
            get file object
        '''
        obj = getattr(config,self.name)
        return obj

    def read(self, data):
        with open('host.py','r',encoding='utf-8') as f:
            return f.read()


if __name__ == '__main__':
    r = readConf('user').read('hh')
    print(r)

