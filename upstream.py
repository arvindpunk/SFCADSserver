class Upstream:
    def __init__(self, base_url='', path='halt'):
        self.base_url = 'http://' + base_url + '/'
        self.path = path
        self.set_headers()

    def set_base_url(self, base_url=''):
        self.base_url = base_url

    def get_base_url(self):
        return self.base_url

    def set_path(self, path='halt'):
        self.path = path

    def get_path(self):
        return self.path

    def set_headers(self, headers={ 'Content-Type': 'text/plain' }):
        self.headers = headers

    def get_headers(self):
        return self.headers