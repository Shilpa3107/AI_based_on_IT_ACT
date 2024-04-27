import re
import pdfplumber

# Function to extract relevant sentences from the PDF
def extract_relevant_sentences(user_input):
    # Open the PDF file
    with pdfplumber.open('C:\\Users\\shilp\\OneDrive\\Desktop\\AI_based_on_IT_ACT\\.venv\\it_act_2000_updated.pdf') as pdf:
        # Initialize an empty list to store the relevant sentences
        relevant_sentences = []

        # Loop through each page
        for page in pdf.pages:
            # Extract the text from the page
            text = page.extract_text()

            # Split the text into sentences
            sentences = re.split(r'[.!?]+', text)

            # Loop through each sentence
            for sentence in sentences:
                # Check if the sentence contains the user's input
                if user_input.lower() in sentence.lower():
                    relevant_sentences.append(sentence.strip())

    return relevant_sentences

# Get user input
user_input = input("Enter the text you want to search for: ")

# Extract relevant sentences
relevant_sentences = extract_relevant_sentences(user_input)

# Print the relevant sentences
for sentence in relevant_sentences:
    print(sentence + '.')