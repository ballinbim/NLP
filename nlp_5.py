import spacy

nlp = spacy.load("en_core_web_sm")

document = nlp("In 1994, Tim Berners-Lee founded the World Wide Web \
Consortium (WBC), devoted to developing web technologies")

# # Analyze syntax
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in document.ents:
    print(entity.text, ':', entity.label_)