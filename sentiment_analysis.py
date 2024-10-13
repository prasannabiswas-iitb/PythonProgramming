from textblob import TextBlob 

print("Welome to sentiment analysis tool...")
user_input = input("Enter a sentence: Please type 'stop' to exit: ")

while(user_input.lower() != "stop"):
    sentimentAnalysis = TextBlob(user_input)
    if sentimentAnalysis.sentiment.polarity > 0.1:
        print("Positive emotion.")
    elif sentimentAnalysis.sentiment.polarity >= -0.1 and sentimentAnalysis.sentiment.polarity <= 0.1:
        print("Neutral emotion.")
    else:
        print("Negative emotion.")
    user_input = input("Enter a sentence again: ")
print("Exiting the tool... \n Thank you for using.")