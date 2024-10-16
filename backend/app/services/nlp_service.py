import spacy

nlp = spacy.load('en_core_web_sm')

def extract_important_information(text: str):
    doc = nlp(text)
    
    extracted_data = {
        "dates": [ent.text for ent in doc.ents if ent.label_ == "DATE"],
        "money": [ent.text for ent in doc.ents if ent.label_ == "MONEY"],
        "organizations": [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    }
    
    return extracted_data
