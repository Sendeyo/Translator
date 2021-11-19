from fastapi import FastAPI, Path, Query
app = FastAPI()

# This is the code responsible for translation
from googletrans import Translator
translator = Translator()

def translate_it(sentence, source, destination):
    if destination.lower() == "english" or destination.lower() == "en":
        destination = "en"
    elif destination.lower() == "swahili" or destination.lower() == "kiswahili" or destination.lower() == "sw": 
        destination = "sw"
    translated = translator.translate(sentence, src="auto", dest=destination)
    return translated

# End of code responsible for translation


@app.get("/")
def index():
    return {"data": "Am a serious developer"}


@app.get("/translation")
def get_translation(sentence : str, source :str = None, destination = "sw"):
    translated = translate_it(sentence, source, destination)
    return {"data":translated.text}