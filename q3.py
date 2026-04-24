# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)
with open ("romeo_and_juliet.txt", "r") as f:
    text = f.read()

####
#### YOUR CODE HERE 
####

# Count how many times the word "Juliet" appears
count = text.count("Juliet")
####
#### YOUR CODE HERE 

print(count)
####
