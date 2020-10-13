from pathlib import Path
import spacy

nlp = spacy.load("en_core_web_sm")

document1 = nlp(Path('RomeoAndJuliet.txt').read_text())
document2 = nlp(Path('EdwardTheSecond.txt').read_text())

print(document1.similarity(document2))