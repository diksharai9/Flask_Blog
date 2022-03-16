def greetings(msg):
    def greet():
        print("Hi "+msg)
        return
    return greet


var = greetings("diksha")
var()
