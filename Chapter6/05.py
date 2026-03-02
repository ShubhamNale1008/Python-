#program for spam/scam detection

phrase1="Hey this is not a spam message"
phrase2="Congratulations! You won ferrari"
phrase3="Click this link to claim your price"


a=input("Enter your comment:")

if(a in phrase1 or a in phrase2 or a in phrase3):
    print("This is a spam/scam message")
else:
    print("This is not a\n spam/scam message")