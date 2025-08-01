# app/routes/translate.py
from flask import Blueprint, request, jsonify
from googletrans import Translator

translate_api = Blueprint('translate_api', __name__)
translator = Translator()

@translate_api.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    content = data.get("content", {})
    target_lang = data.get("lang", "en")

    def recursive_translate(obj):
        if isinstance(obj, dict):
            return {k: recursive_translate(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [recursive_translate(i) for i in obj]
        elif isinstance(obj, str):
            return translator.translate(obj, dest=target_lang).text
        return obj

    translated = recursive_translate(content)
    return jsonify(translated)
