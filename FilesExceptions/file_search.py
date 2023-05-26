import word_count as wc
import write_to_file
files = ['texts/metamorphosis.txt', 'texts/siddartha.txt']

for file in files:
    wc.count_words(file)
for file in files:
    wc.find_words(file)