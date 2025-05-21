class Request:
    def __init__(self):
        self.url = 'https://viacep.com.br/'
        self.params = {}


    def search(self, cep):
        print('Buscando cep => ' + cep)