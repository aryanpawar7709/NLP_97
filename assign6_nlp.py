import spacy
from spacy import displacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# New multiline input text
multiline_text = """
Artificial intelligence (AI) is transforming industries around the world by automating tasks, 
analyzing vast amounts of data, and improving decision-making processes. 
From healthcare to finance, AI applications are becoming increasingly integrated into our daily lives.
"""

# Process the text
multiline_doc = nlp(multiline_text)

# Token analysis
for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
tag_: {token.tag_}
head.text: {token.head.text}
dep_: {token.dep_}
        """
    )

# Visualize the dependencies in your browser
displacy.serve(multiline_doc, style="dep")
