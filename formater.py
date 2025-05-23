# format markdown text with approximately format like (word - definition) to good format for
# CardLearner (main.py in this case)

lines = []
with open('learning.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        lines.append(line.strip())

def delete_markdown_features(word):
    word = word.replace('`', '')
    word = word.replace('*', '')
    return word

result = []

# work with lines
for line in lines:
    try:
        meaning, definition = line.split("` - ")
        definition = delete_markdown_features(definition)
        meaning = delete_markdown_features(meaning)
        new_line = meaning + "<>" + definition
    except:
        splitter = line.split(" - ")
        meaning, definition = splitter[0], " - ".join(splitter[1:])
        definition = delete_markdown_features(definition)
        meaning = delete_markdown_features(meaning)
        new_line = meaning + "<>" + definition
    finally:
        result.append(new_line)

# update_learning.txt
with open("learning.txt", mode='w', encoding='utf-8') as f:
    for line in result:
        f.write(line + "\n")