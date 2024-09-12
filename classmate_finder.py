import inflect
p = inflect.engine()

def wordify(number):
    wordify = {0: "first", 1: "second", 2: "third", 3: "fourth", 4: "fifth", 5: "sixth"}
    return wordify[number]

print("Supports up to 6 classes")
#prompts user and validates data
while True:
    while True:
        no_classes = input("How many classes would you like to check for the same classmates: ")
        if no_classes.isdigit():
            break
        else: 
            print("Please enter a digit")
    if int(no_classes) < 2 or int(no_classes) > 6:
        print("Please enter a digit between 2 and 6 included")
    else:
        break
no_classes = int(no_classes)

#accepts a long string as input and returns the list of people in a class
def extract(group):
    unsorted_string = group 
    unsorted_string = unsorted_string.replace("User's profile picture ", "")
    unsorted_string = unsorted_string.replace("SU.ADTPART", ",")
    unsorted_string = unsorted_string.replace("SU.ADTPSCI", ",")
    unsorted_string = unsorted_string.replace(".", "")
    unsorted_string = unsorted_string.replace("FT", "")

    #removes numbers
    for letter in unsorted_string:
        if letter.isdigit():
            unsorted_string = unsorted_string.replace(letter, "")
    #converts string into list
    l = unsorted_string.split(",")
    l.pop()
    return l


class_names = []
people_list = []
for i in range(no_classes):
    name = input(f"Please enter {wordify(i)} class name: ")
    people = input(f"Input the list of people in your {wordify(i)} class: ")
    class_names.append(name)
    people_list.append(people)

dictionary = {}
#c is for class
for c in range(no_classes):
    dictionary[class_names[c]] = extract(people_list[c])


output = p.join(class_names)
print("---------------------------------------------------------------")
print(f"List of people taking ", output)
print("---------------------------------------------------------------")

similar_list = []
confirm_list = []
for person in dictionary[class_names[0]]:
                similar_list.append(person)

#c is for class
for c in class_names:

    if c == class_names[0]:
        continue
    for l in dictionary:
        for person in similar_list:
            if person in dictionary[l]:
                confirm_list.append(person)
        similar_list = confirm_list.copy()
        confirm_list = []

for person in similar_list:
    print(person)