class HelloWorld():
    
    def __init__(self, 
                 firstName: str,
                 lastName: str,
                 studentID: str) -> None:
        
        self._firstName = firstName
        self._lastName = lastName
        self._studentID = studentID
        
    def hello(self):
        print("Hello World, \nMy name is " + self._firstName + " "+ self._lastName + " and my student ID is " + self._studentID)
        
        
def main():
    obj = HelloWorld("Jager", "Cooper","201765344")
    
    obj.hello()
    
main()