from interpreter import Interpreter
from voice_recognition import Recognition
recognition = Recognition()
interpreter = Interpreter()
interpreter.reload()

#while True:
#interpreter.set_response(recognition.listen())
interpreter.set_response("jaka jest pogoda")
