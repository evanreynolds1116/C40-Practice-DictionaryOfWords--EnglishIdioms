# You are going to build a Python Dictionary to represent an actual dictionary. Each key/value pair within the Dictionary will contain a single word as the key, and a definition as the value. Below is some starter code. You need to add a few more words and definitions to the dictionary.

# After you have added them, use square bracket notation to output the definition of two of the words to the console.

# Lastly, use the for in loop to iterate over the KeyValuePairs and display the entire dictionary to the console.

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["Scrumdidlyumptious"] = "extremely tasty; delicious"
word_definitions["Laziness"] = "Risking to drop everything you carry rather than walking twice"
word_definitions["Calories"] = "Tiny creatures that live in your closet and sew your clothes a little bit tighter every night"
word_definitions["Latte"] = "Italian for you paid too much for that coffee"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

# print(f'Calories: {word_definitions["Calories"]}')
# print(f'Laziness: {word_definitions["Laziness"]}')


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (key, value) in word_definitions.items():
    print(f'The definition of {key} is {value}')

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for (key, value) in idioms.items():
    new_value = " ".join(value)
    print(f'{key}: {new_value}')