# import the random module.
import random

# Create 'jokes_list' with a list of jokes.
jokes_list = ["And the Lord said unto John, 'Come forth and you will receive eternal life.' But John came fifth - "
              "and won a toaster.",
              "Why did Adele cross the road?- To say hello from the other side!",
              "Knock, knock.- Who's there?- Nobel. Nobel who?- No bell, that's why I knocked.",
              "I don't trust stairs. They're always up to something.",
              "Did you hear about the Italian chef who died? He pasta-way.",
              "What do Santa's elves listen to whilst they work?- Wrap music"]

# Use random.choice() function to generate a random joke from 'jokes_list'.
print(random.choice(jokes_list))