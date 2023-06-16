from django.shortcuts import render
from deep_translator import GoogleTranslator
from django.http import JsonResponse , HttpResponse

# Create your views here.
def translate(request):
    langs = [
        "afrikaans",
        "albanian",
        "amharic",
        "arabic",
        "armenian",
        "azerbaijani",
        "basque",
        "belarusian",
        "bengali",
        "bosnian",
        "bulgarian",
        "catalan",
        "cebuano",
        "chichewa",
        "chinese (simplified)",
        "chinese (traditional)",
        "corsican",
        "croatian",
        "czech",
        "danish",
        "dutch",
        "english",
        "esperanto",
        "estonian",
        "filipino",
        "finnish",
        "french",
        "frisian",
        "galician",
        "georgian",
        "german",
        "greek",
        "gujarati",
        "haitian creole",
        "hausa",
        "hawaiian",
        "hebrew",
        "hindi",
        "hmong",
        "hungarian",
        "icelandic",
        "igbo",
        "indonesian",
        "irish",
        "italian",
        "japanese",
        "javanese",
        "kannada",
        "kazakh",
        "khmer",
        "kinyarwanda",
        "korean",
        "kurdish (kurmanji)",
        "kyrgyz",
        "lao",
        "latin",
        "latvian",
        "lithuanian",
        "luxembourgish",
        "macedonian",
        "malagasy",
        "malay",
        "malayalam",
        "maltese",
        "maori",
        "marathi",
        "mongolian",
        "myanmar (burmese)",
        "nepali",
        "norwegian",
        "odia",
        "pashto",
        "persian",
        "polish",
        "portuguese",
        "punjabi",
        "romanian",
        "russian",
        "samoan",
        "scots gaelic",
        "serbian",
        "sesotho",
        "shona",
        "sindhi",
        "sinhala",
        "slovak",
        "slovenian",
        "somali",
        "spanish",
        "sundanese",
        "swahili",
        "swedish",
        "tajik",
        "tamil",
        "tatar",
        "telugu",
        "thai",
        "turkish",
        "turkmen",
        "ukrainian",
        "urdu",
        "uyghur",
        "uzbek",
        "vietnamese",
        "welsh",
        "xhosa",
        "yiddish",
        "yoruba",
        "zulu"
    ]

    if request.method == 'POST':
        text = request.POST['text']
        lang = request.POST['lang']
        translated_text = handle_translation(text, lang)
        context = {'translated_text': translated_text,'langs':langs,'text':text, 'lang':lang}
        return render(request, 'index.html', context)

    else:
        context = {'langs':langs}

    return render(request, 'index.html', context)

def handle_translation(text, lang):
    try:
        translator = GoogleTranslator(source='auto', target=lang)
        translated_text = translator.translate(text)
    except Exception as e:
        translated_text='Please Enter a valid Language'
    return translated_text