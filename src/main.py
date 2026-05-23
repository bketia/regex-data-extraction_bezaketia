import re
import json
#Reading the raw text file
with open("input/raw-text.txt", "r", encoding="utf-8") as file:
    text = file.read()

#Extract email address,url,phone number and credit card using regex
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
url_pattern = r'https?://[^\s]+'
phone_pattern = r'(\+\d{1,3}\s?\d{3}\s?\d{3}\s?\d{3}|\(\d{3}\)\s?\d{3}-\d{3}-\d{3})'
credit_card_pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'

#Remove the matching data from the text 
emails = re.findall(email_pattern, text)
urls = re.findall(url_pattern, text)
phones = re.findall(phone_pattern, text)
credit_cards = re.findall(credit_card_pattern, text)

alu_emails = []

for email in emails:
    if (
        email.endswith("@alueducation.com")
        or email.endswith("@alumni.alueducation.com")
        or email.endswith("@si.alueducation.com")
    ):
        alu_emails.append(email)

masked_cards = []
#Hiding/masking the credit card number before storing them or displaying
for card in credit_cards:
    clean = card.replace("-", "").replace(" ", "")
    masked = "**** **** **** " + clean[-4:]
    masked_cards.append(masked)

#validated data in a presentable format
results = {
    "emails": emails,
    "alu_valid_emails": alu_emails,
    "urls": urls,
    "phone_numbers": phones,
    "credit_cards": masked_cards
}

#save the results to the JSON file
with open("output/sample-output.json", "w") as outfile:
    json.dump(results, outfile, indent=4)

print(json.dumps(results, indent=4))