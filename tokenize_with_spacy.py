import spacy
import sys

if __name__ == "__main__":
  nlp = spacy.load("en")
  for line in sys.stdin:
    print(" ".join(token.text for token in nlp(line.strip())))

