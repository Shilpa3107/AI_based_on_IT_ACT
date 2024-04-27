import fitz

def extract_sentences(pdf_path, user_text):
  """
  Extracts sentences containing the user-provided text until a bold number is found.

  Args:
      pdf_path: Path to the downloaded PDF file.
      user_text: Text to search for within sentences.

  Returns:
      A list of extracted sentences.
  """
  doc = fitz.open(pdf_path)

  sentences = []
  current_sentence = ""

  for page in doc:
    text = page.get_text("text")
    lines = text.splitlines()

    for line in lines:
      if user_text in line:
        current_sentence += line.strip() + " "
      elif current_sentence and any(word.isdigit() and word.isbold() for word in line.split()):
        # Found a bold number, end sentence extraction
        sentences.append(current_sentence.strip())
        current_sentence = ""
      else:
        current_sentence += line.strip() + " "

    # Check for leftover sentence at the end of the page
    if current_sentence:
      sentences.append(current_sentence.strip())
      current_sentence = ""

  return sentences

# Example usage
pdf_path = "C:\Users\shilp\OneDrive\Desktop\AI_based_on_IT_ACT\it_act_2000_updated.pdf"
user_text = "input your search text here"

extracted_sentences = extract_sentences(pdf_path, user_text)

if extracted_sentences:
  print("Extracted sentences:")
  for sentence in extracted_sentences:
    print(sentence)
else:
  print("No sentences found containing", user_text)
