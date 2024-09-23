def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    character_counter = {}

    for character in file_contents:
        if character.isalpha():
            if character in character_counter:
                character_counter[character] +=1 
            else:
                character_counter[character] = 1
    sorted_characters = sorted(character_counter.items(),key = lambda x: x[1], reverse =True)
    print(f"--- Begin report of books/frankenstein.txt --- \n{len(file_contents.split())} words found in the document ")
    for character in sorted_characters:
        print(f"The {character[0]} character was found {character[1]} times")

main()