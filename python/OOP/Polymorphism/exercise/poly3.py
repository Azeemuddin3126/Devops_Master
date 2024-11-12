class Characters:
    def __init__(self, phrases):
        self.phrases = phrases

    # Helper method to calculate total characters
    def total_characters(self):
        return sum(len(phrase) for phrase in self.phrases)

    # Overload the > operator
    def __gt__(self, other):
        return self.total_characters() > other.total_characters()

    # Overload the < operator
    def __lt__(self, other):
        return self.total_characters() < other.total_characters()

    # Overload the == operator
    def __eq__(self, other):
        return self.total_characters() == other.total_characters()

# Testing the class with sample phrases
sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

c1 = Characters(sample_phrases1)
c2 = Characters(sample_phrases2)

print(c1 > c2)   # Expected Output: True
print(c1 < c2)   # Expected Output: False
print(c1 == c1)  # Expected Output: True
