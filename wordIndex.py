# This program count occurrence of specific words in a txt file

# Open, read and close the file
infile = open("book of John text.txt", "r")
read_file = infile.read()
infile.close()

# Convert the file object to a list
read_file = read_file.split()

# Define the list of the target words
target_words = ["Father", "God", "Christ", "Spirit", "spirit", "life", "man"]

# Create an empty dictionary to hold the words and count
to_dict = {}

# Run the word count
for i in read_file:
    if i in target_words:
        count = read_file.count(i)
        to_dict[i] = count

# Display target words and the count
print("--------------------------------")
print("Target Word\t\tOccurrence")
print("--------------------------------")

for j in to_dict:
    row_space = (15 - len(j)) * " "
    print(j, ": ", row_space, to_dict[j], sep="")
