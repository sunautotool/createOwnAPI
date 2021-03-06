import random
import os
postData={}

class TestObject():
    def __init__(self,name,description):
        self.name = name
        self.desciption = description
        self.id=random.randint(1,3)

    def getName(self):
        return self.name

    def setName(self,name):
        self.name=name

    def getDescription(self):
        return self.desciption

    def setDescription(self,description):
        self.desciption=description

    def getId(self):
        return self.id

    def setId(self,id):
        self.id=id

class Request():
    def __init__(self,ipAddress):
        self.ipAddress=ipAddress

    def getIpAddress(self):
        return self.setIpAddress

    def setIpAddress(self,ipAddress):
        if self.ipAddress == '1.2.3.4':
            self.ipAddress=ipAddress
        elif len(ipAddress)<7:
            return False
        else:
            return False

    def RequestPostRequest(self,TestObject):
        if self.ipAddress=='1.2.3.4':
            return Response(TestObject)
        elif len(self.ipAddress)<7:
            return 401
        else:
            return 404

    def RequestGetRequest(self,id):
        if self.ipAddress=='1.2.3.4':
            return Response(TestObject,id)
        elif len(self.ipAddress)<7:
            return 401
        else:
            return 404

class Response():
    def __init__(self,TestObject,id=None):
        self.TestObject=TestObject

    def getTestObject(self):
        return self.TestObject

    def setTestObject(self,TestObject):
        self.TestObject=TestObject

    def getStatusCode(self):
        return self.setStatusCode()

    def setStatusCode(self):
        if len(postData)==0:
            postData[self.TestObject.getId()] = self.TestObject.getName()
            return 201
        else:
           if self.TestObject.getId in postData.keys():
               statusCode=200
           else:
               postData[self.TestObject.getId()] = self.TestObject.getName()
               statusCode = 201
        return statusCode


def main():
    testRequest=Request('1.2.3.4')
    postData=TestObject("hjhu","hjhjh")
    res=testRequest.RequestPostRequest(postData)
    print(res)
    print(res.getStatusCode())
    print(res.getTestObject().getId())
    print(res.TestObject.getName())
    get=testRequest.RequestGetRequest(3)
    print(get)

if __name__=='__main__':
    main()
