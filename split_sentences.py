import unicodedata
import csv

"""
def split_sentences(text):

  sentences = []
  for sentence in text.split(","):
    if sentence:
      sentences.append(unicodedata.normalize("NFD", sentence))
  return sentences
"""

def split_sentences(text):
    sentences = []
    for sentence in text.split("."):
        sentences.extend(sentence.split(","))
    return [unicodedata.normalize("NFD", s.strip()) for s in sentences if s]


def main():
  
  with open("input.txt", "rb") as f:
    text = f.read().decode("utf-8")

  sentences = split_sentences(text)

  with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for sentence in sentences:
      writer.writerow([sentence])

if __name__ == "__main__":
  main()
