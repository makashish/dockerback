from docx.oxml.ns import qn
from docx.shared import Pt

font_map = {
  "Afrikaans": "Arial",
  "Amharic": "Nyala",
  "Arabic": "Arial",
  "Assamese": "Mangal",
  "Azerbaijani": "Arial",
  "Azerbaijani (Cyrillic)": "Arial",
  "Belarusian": "Times New Roman",
  "Bengali": "Vrinda",
  "Tibetan": "Jomolhari",
  "Bosnian": "Arial",
  "Breton": "Arial",
  "Bulgarian": "Times New Roman",
  "Catalan": "Arial",
  "Cebuano": "Arial",
  "Czech": "Arial",
  "Chinese (Simplified)": "SimSun",
  "Chinese (Simplified Vert.)": "SimSun",
  "Chinese (Traditional)": "MingLiU",
  "Chinese (Traditional Vert.)": "MingLiU",
  "Cherokee": "Plantagenet Cherokee",
  "Corsican": "Arial",
  "Welsh": "Arial",
  "Danish": "Arial",
  "German": "Arial",
  "German (Fraktur)": "Fette Fraktur",
  "Dhivehi": "MV Boli",
  "Dzongkha": "Jomolhari",
  "Greek": "Times New Roman",
  "English": "Arial",
  "Middle English": "Times New Roman",
  "Esperanto": "Arial",
  "Mathematical notation": "Cambria Math",
  "Estonian": "Arial",
  "Basque": "Arial",
  "Faroese": "Arial",
  "Persian": "Tahoma",
  "Filipino": "Arial",
  "Finnish": "Arial",
  "French": "Arial",
  "Middle French": "Times New Roman",
  "Western Frisian": "Arial",
  "Scottish Gaelic": "Arial",
  "Irish": "Arial",
  "Galician": "Arial",
  "Ancient Greek": "New Athena Unicode",
  "Gujarati": "Noto Sans Gujarati",
  "Haitian Creole": "Arial",
  "Hebrew": "David",
  "Hindi": "Mangal",
  "Croatian": "Arial",
  "Hungarian": "Arial",
  "Armenian": "Sylfaen",
  "Inuktitut": "Euphemia",
  "Indonesian": "Arial",
  "Icelandic": "Arial",
  "Italian": "Arial",
  "Old Italian": "Times New Roman",
  "Javanese": "Tuladha Jejeg",
  "Japanese": "MS Mincho",
  "Japanese (Vert.)": "MS Mincho",
  "Kannada": "Tunga",
  "Georgian": "Sylfaen",
  "Old Georgian": "Sylfaen",
  "Kazakh": "Times New Roman",
  "Khmer": "Khmer UI",
  "Kyrgyz": "Times New Roman",
  "Kurdish": "Arial",
  "Korean": "Malgun Gothic",
  "Lao": "Saysettha OT",
  "Latin": "Times New Roman",
  "Latvian": "Arial",
  "Lithuanian": "Arial",
  "Luxembourgish": "Arial",
  "Malayalam": "Kartika",
  "Marathi": "Mangal",
  "Macedonian": "Times New Roman",
  "Maltese": "Arial",
  "Mongolian": "Mongolian Baiti",
  "Māori": "Arial",
  "Malay": "Arial",
  "Burmese": "Myanmar Text",
  "Nepali": "Mangal",
  "Dutch": "Arial",
  "Norwegian": "Arial",
  "Occitan": "Arial",
  "Oriya": "Kalinga",
  "Ossetian": "Arial",
  "Punjabi": "Raavi",
  "Polish": "Arial",
  "Portuguese": "Arial",
  "Pashto": "Arial",
  "Quechua": "Arial",
  "Romanian": "Arial",
  "Russian": "Times New Roman",
  "Sanskrit": "Mangal",
  "Sinhala": "Iskoola Pota",
  "Slovak": "Arial",
  "Slovenian": "Arial",
  "Sindhi": "Arial",
  "Spanish": "Arial",
  "Old Spanish": "Times New Roman",
  "Albanian": "Arial",
  "Serbian (Cyrillic)": "Times New Roman",
  "Serbian (Latin)": "Arial",
  "Sundanese": "Noto Sans Sundanese",
  "Swahili": "Arial",
  "Swedish": "Arial",
  "Syriac": "Estrangelo Edessa",
  "Tamil": "Latha",
  "Tatar": "Arial",
  "Telugu": "Gautami",
  "Tajik": "Times New Roman",
  "Thai": "Tahoma",
  "Tigrinya": "Abyssinica SIL",
  "Tongan": "Arial",
  "Turkish": "Arial",
  "Uyghur": "Arial",
  "Ukrainian": "Times New Roman",
  "Urdu": "Nafees Nastaleeq",
  "Uzbek (Latin)": "Arial",
  "Uzbek (Cyrillic)": "Arial",
  "Vietnamese": "Arial",
  "Yiddish": "Times New Roman",
  "Yoruba": "Arial",
  
  "Arabic (script)": "Arial",
  "Armenian (script)": "Sylfaen",
  "Bengali (script)": "Vrinda",
  "Canadian Aboriginal (script)": "Euphemia",
  "Cherokee (script)": "Plantagenet Cherokee",
  "Cyrillic (script)": "Times New Roman",
  "Devanagari (script)": "Mangal",
  "Ethiopic (script)": "Nyala",
  "Fraktur (script)": "Fette Fraktur",
  "Georgian (script)": "Sylfaen",
  "Greek (script)": "Times New Roman",
  "Gujarati (script)": "Noto Sans Gujarati",
  "Gurmukhi (script)": "Raavi",
  "Han (Simplified, script)": "SimSun",
  "Han (Simplified Vertical)": "SimSun",
  "Han (Traditional, script)": "MingLiU",
  "Han (Traditional Vertical)": "MingLiU",
  "Hangul (script)": "Malgun Gothic",
  "Hangul Vertical": "Malgun Gothic",
  "Hebrew (script)": "David",
  "Japanese (script)": "MS Mincho",
  "Japanese Vertical": "MS Mincho",
  "Kannada (script)": "Tunga",
  "Khmer (script)": "Khmer UI",
  "Lao (script)": "Saysettha OT",
  "Latin (script)": "Arial",
  "Malayalam (script)": "Kartika",
  "Myanmar (script)": "Myanmar Text",
  "Oriya (script)": "Kalinga",
  "Sinhala (script)": "Iskoola Pota",
  "Syriac (script)": "Estrangelo Edessa",
  "Tamil (script)": "Latha",
  "Telugu (script)": "Gautami",
  "Thaana (script)": "MV Boli",
  "Thai (script)": "Tahoma",
  "Tibetan (script)": "Jomolhari",
  "Vietnamese (script)": "Arial"
}

def set_font(run, language):
    font_name = font_map.get(language, "Arial")
    run.font.name = font_name
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)
    run.font.size = Pt(14)