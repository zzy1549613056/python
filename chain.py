class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
            return lambda x : Chain('%s/%s/%s' % (self._path,path,x))
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__



if __name__ == '__main__':
    print(Chain().users('michael').repos)
