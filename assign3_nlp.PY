import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text = """
    "Sundar Pichai met with Prime Minister Narendra Modi in New Delhi "
    "on September 15, 2021, to discuss Google's $10 billion investment "
    "in India's digital economy. Later, they attended the Digital India Summit."
    "Pichai also visited the Taj Mahal in Agra and the Red Fort in Delhi."
"""

doc = nlp(text)

print("----- Named Entities -----")
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

displacy.serve(doc, style="ent", host="127.0.0.1", port=5000)


