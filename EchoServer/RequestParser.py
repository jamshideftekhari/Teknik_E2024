class parseRequest:
    def __init__(self, request):
        self.request = request
        self.operation = None
        self.content = None
     
    def ParseRequest(self):
        #request = self.request.decode()
        parseRequest = self.request.split(" ", 1)
        print(parseRequest)
        self.operation = parseRequest[0]
        self.content = parseRequest[1]
        print(self.operation)
        print(self.content)

    def GetOperation(self):
        return self.operation

    def GetContent(self):
        return self.content    
    
def DoOperation(request):
    pr = parseRequest(request)
    pr.ParseRequest()
    operation = pr.GetOperation()
    content = pr.GetContent()
    if operation == "lower":
        return content.lower()
    elif operation == "upper":
        return content.upper()

if __name__ == "__main__":
    request = "lower Hello World"
    print(DoOperation(request))
    request = "upper Hello World"
    print(DoOperation(request))        