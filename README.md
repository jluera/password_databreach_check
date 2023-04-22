# password_databreach_check

## This script utilizes the pwnedpasswords API to check if a password has been listed in their data breach records.
- If the password is listed, it will tell you how many times. (So how many different data breaches that password was referenced in.)
- Or it will tell you if the password was not found in its data breach records.

When you run the script via cli, you can enter one or more passwords to check.

![Screenshot 2023-04-22 at 5 34 25 PM](https://user-images.githubusercontent.com/367461/233810494-bf2c9e3e-47cc-4980-b072-1e009b18dd65.png)

## Security Note: 
Per the pwnedpasswords/ documentation:

"No plaintext passwords ever leave your machine using pwnedpasswords.

How does that work? Well, the Pwned Passwords v2 API has a pretty cool k-anonymity implementation.

From https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/:

Formally, a data set can be said to hold the property of k-anonymity, if for every record in a released table, there are k − 1 other records identical to it.

This allows us to only provide the first 5 characters of the SHA-1 hash of the password in question. The API then responds with a list of SHA-1 hash suffixes with that prefix. On average, that list contains 478 results.

People smarter than I am have used math to prove that 5-character prefixes are sufficient to maintain k-anonymity for this database.

In short: your plaintext passwords are protected if you use this library. You won't leak enough data to identity which passwords you're searching for."

## Also:
"pwnedpasswords automatically checks if your provided input looks like a SHA-1 hash. If it does, it won't do any further processing. If it looks like plain text, it'll automatically hash it before sending it to the Pwned Passwords API.

If you'd like to provide an already-hashed password as input to pwnedpasswords, you don't need to do anything--pwnedpasswords will detect that it looks like a SHA-1 hash and won't hash it again before sending it to the range endpoint."
