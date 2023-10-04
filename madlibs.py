def madlib():
  adj1 = input("1stAdjective:")
  adj2 = input("2nd Adjective:")
  adj3 = input("3rd Adjective:")
  adj4 = input("4th Adjective:")

  noun1 = input("1st Noun:")
  noun2 = input("2nd Noun:")
  noun3 = input("3rd Noun:")
  noun4 = input("4th Noun:")
  noun5 = input("5th Noun:")
  noun6 = input("6th Noun:")

  verb1 = input("Verb:")
  verb2 = input("Verb:")
  verb3 = input("Verb:")
  animal = input("Animal name:")
  adverb = input("Adverb:")

 

  madlib = f"One {adj1} day, I decided to take a trip to the {noun1}.As I walked along the {noun2}, \
    I noticed a {adj2} {animal} sitting under a {noun3}.It was {verb1} {adverb} and looked {adj3}.\
    I approached the {animal} cautiously and offered it a {noun4}. To my surprise,it [verb] the {noun5}\
    eagerly and started {verb2} around in {noun6}. I couldn't help but {verb3} along with it. After \
    spending some time with the {animal}, I continued my journey to the [noun]. It was a {adj4} adventure\
    that I would {verb3} cherish.\
    Now, please fill in the blanks with the appropriate types of words!"

  print(madlib)
if __name__ == "__main__":
    madlib()
    
    