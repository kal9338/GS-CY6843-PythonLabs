
### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #The student doesn't have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?":
        answer = "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA? - mTLS"
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "Are encoding and encryption the same? - No"
    if question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "Is it possible to decrypt a message without a key? - No"
    if question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Is it possible to decode a message without a key? - Yes"
    if question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "Is a hashed message supposed to be un-hashed? - No"
    if question == "What is the MD5 hashing value to the following message: NYU Computer Networking":
        answer = "What is the MD5 hashing value to the following message: NYU Computer Networking 68c74b1fe84ac8c662849915bc9002f4"
    if question ==  "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "Is MD5 a secured hashing algorithm? - No"
    if question == "What layer from the TCP/IP model the protocol DHCP belongs to?":
        answer = 0
    elif question ==  "What layer of the TCP/IP model the protocol TCP belongs to?":
           answer = 4
    return(answer)
# Complete all the questions.

if __name__ == "__main__":

    print(welcome_assignment_answers("In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?"))
    print(welcome_assignment_answers("Are encoding and encryption the same? - Yes/No"))
    print(welcome_assignment_answers("Is it possible to decrypt a message without a key? - Yes/No"))
    print(welcome_assignment_answers("Is it possible to decode a message without a key? - Yes/No"))
    print(welcome_assignment_answers("Is a hashed message supposed to be un-hashed? - Yes/No"))
    print(welcome_assignment_answers("What is the MD5 hashing value to the following message: NYU Computer Networking"))
    print(welcome_assignment_answers("Is MD5 a secured hashing algorithm? - Yes/No"))
    print(welcome_assignment_answers("What layer from the TCP/IP model the protocol DHCP belongs to?"))
    print(welcome_assignment_answers("What layer of the TCP/IP model the protocol TCP belongs to?"))