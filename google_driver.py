class GoogleDriver: 
    @staticmethod 
    def search(string): 
        return Result(string) 

class Result: 
    messages = { 
        "test": "string test correta", 
        "batata": "frita", 
    } 

    def __init__(self, procurar_string): 
        result =  self.messages.get(procurar_string) 
        if result: 
            self.status_code = 200 
            self.content = result 
        else: 
            self.status_code = 404 
            self.content = "Ops, nao encontrado" 