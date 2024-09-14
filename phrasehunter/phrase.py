class Phrase:

    def __init__(self, phrase):
        # Save the phrase and prepare a list for guessed letters
        self.phrase = phrase.lower()
        self.guessed_letters = []

    def display(self):
        # Show the phrase with guessed letters visible and underscores for unguessed letters
        displayed_phrase = ''
        for letter in self.phrase:
            # Show the letter if it's guessed or is a space, comma, exclamation mark, or period
            if letter in self.guessed_letters or letter in [' ', ',', '!', '.']:
                displayed_phrase += letter
            else:
                displayed_phrase += '_ '    # Show an underscore for unguessed letters
        return displayed_phrase.strip()    # Removes trailing spaces

    def check_letter(self, letter):
        # Add the letter to guessed_letters if it's in the phrase and not guessed before
        letter = letter.lower()
        if letter in self.phrase and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)

    def check_complete(self):
        # Check if all letters in the phrase have been guessed
        for letter in self.phrase:
            if letter not in [' ', ',', '!', '.'] and letter not in self.guessed_letters:
                return False
        return True    # Return True if the phrase is fully guessed
