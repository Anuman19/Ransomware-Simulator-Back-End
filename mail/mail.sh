#!/bin/bash

# Email content and subject
SUBJECT="Exklusiver Mitarbeiterrabatt bei Jackie's Petshop: Holen Sie sich jetzt Ihren Rabattcode!"
FROM="no-reply@petshop.io"
CONTENT_TYPE="Content-type: text/html"
MAIL_CONTENT="mail.html"
RECIPIENTS_FILE="recipients.txt"

# Check if recipients file exists
if [ ! -f "$RECIPIENTS_FILE" ]; then
  echo "Recipients file not found!"
  exit 1
fi

# Read the recipients file line by line
while IFS= read -r RECIPIENT; do
  if [ -n "$RECIPIENT" ]; then
    mail -a "$CONTENT_TYPE" -s "$SUBJECT" -r "$FROM" "$RECIPIENT" < "$MAIL_CONTENT"
    echo "Email sent to: $RECIPIENT"
  fi
done < "$RECIPIENTS_FILE"

