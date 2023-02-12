#!/bin/sh

# Store the current exit status
EXIT_STATUS=0

# A function to validate the commit message
validate_commit_message() {
  # Get the commit message
  COMMIT_MESSAGE=$1

  # Check if the commit message starts with a tag
  if ! echo "$COMMIT_MESSAGE" | grep -qE '^(\[.*\])\s' ; then
    echo "The commit message should start with a tag in square brackets"
    EXIT_STATUS=1
  fi

  # Check if the commit message is less than 72 characters long
  if [ $(echo "$COMMIT_MESSAGE" | wc -L) -gt 72 ] ; then
    echo "The commit message should not be longer than 72 characters"
    EXIT_STATUS=1
  fi

  # Check if the commit message ends with a period
  if ! echo "$COMMIT_MESSAGE" | grep -qE '\.$' ; then
    echo "The commit message should end with a period"
    EXIT_STATUS=1
  fi
}

# Get the commit message from the command line argument
COMMIT_MESSAGE=$1

# Validate the commit message
validate_commit_message "$COMMIT_MESSAGE"

# Exit with the proper status
exit $EXIT_STATUS
