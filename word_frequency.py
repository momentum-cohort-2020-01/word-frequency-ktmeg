import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


with open('seneca_falls.txt', 'r') as f:
    data = f.read()

translator = str.maketrans("","", string.punctuation)
data = data.translate(translator)
data = data.lower()

words = data.split()
new_data = list(filter(lambda w: w not in STOP_WORDS, words))


def get_word_frequency(new_data):
    for entry in new_data:
        print('Frequency of ', entry, 'is:', new_data.count(entry))


if __name__ == "__main__":
    get_word_frequency(new_data)
    
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
