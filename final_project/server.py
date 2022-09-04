"""
This is the server app that will  host the french to english translation
"""

import json
from flask import Flask, render_template, request
import machinetranslation


app = Flask("Web Translator")


@app.route("/englishToFrench")
def english_to_french():
    """An endpoint for the English to French translation"""

    text_to_translate = request.args.get('textToTranslate')
    english_translation = machinetranslation.translator.english_to_french(text_to_translate)
    return f"Translated text to French: {english_translation}"


@app.route("/frenchToEnglish")
def french_to_english():
    """An endpoint for the French to English Translation"""

    text_to_translate = request.args.get('textToTranslate')
    french_translation = machinetranslation.translator.french_to_english(text_to_translate)
    return f"Translated text to English: {french_translation}"


@app.route("/")
def render_index_page():
    """Render the index page for the default endpoint"""

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
