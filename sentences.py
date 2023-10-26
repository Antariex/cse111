import random

# Get determiner
def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word

# Get noun
def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
            "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
            "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun

# Get verb
def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]

    verb = random.choice(verbs)
    return verb

# Get preposition
def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    preposition = random.choice(prepositions)
    return preposition

# Get prepositional phrase
def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

def get_adjective():
  adjectives = ["Happy", "Beautiful", "Courageous", "Mysterious", "Delicious", "Exciting", "Peaceful", "Clever", "Playful", "Enchanting"]

  adjective = random.choice(adjectives)
  return adjective

# Make_sentence function to include a prepositional phrase
def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    adjective = get_adjective()

    sentence = f"{determiner} {noun} {verb} {prepositional_phrase} {adjective}."
    return sentence

# Main function to generate and print the sentences
def main():
    single_past = make_sentence(1, "past")
    single_present = make_sentence(1, "present")
    single_future = make_sentence(1, "future")
    plural_past = make_sentence(2, "past")
    plural_present = make_sentence(2, "present")
    plural_future = make_sentence(2, "future")

    print("a. Single past:", single_past)
    print("b. Single present:", single_present)
    print("c. Single future:", single_future)
    print("d. Plural past:", plural_past)
    print("e. Plural present:", plural_present)
    print("f. Plural future:", plural_future)

main()