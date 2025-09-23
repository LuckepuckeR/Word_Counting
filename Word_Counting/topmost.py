import wordfreq
import sys
import urllib.request

stopwords = [
    ".", "?", "!", ",", "(", ")", "[", "]", "{", "}", "-", "–", "_", '"', "'", "’", "‘", "·", ":", ";",
    "$", "£", "€", "%", "#", "@", "\\", "+", "^", "/", "=", "±", "&", "—", "*",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "the", "a", "an", "and", "or", "nor", "just", "never", "quite",
    "am", "is", "are", "was", "were", "be", "been",
    "do", "did", "does",
    "may", "might", "can", "must", "should", "shall", "could", "would",
    "to", "of", "in", "for", "as", "on", "off", "by", "at", "but", "such", "also",
    "this", "these", "those", "that", "here", "there", "how", "where", "when",
    "no", "upon", "out", "up", "down", "into",
    "i", "me", "my", "myself",
    "you", "your", "yourself",
    "he", "his", "him", "himself",
    "she", "her", "herself",
    "it", "its", "itself",
    "we", "our", "us",
    "they", "their", "them", "themselves",
    "s", "t", "d", "n", "o", "with",
    "all", "not", "from", "so", "now",
    "which", "whose", "like", "self", "most", "one", "once", "first", "two", "twice", "second", "three", "last",
    "have", "has", "had", "then",
    "what", "some", "more", "if", "other", "only", "yet",
    "will", "over", "any", "who", "though", "than", "whom", "very", "about", "still", "before", "after", "again", "while", "away",
    "go", "went", "goes", "come", "comes", "came",
    "say", "says", "said",
    "see", "sees", "saw",
    "let", "give", "gives", "gave",
    "take", "takes", "took",
    "nothing", "something", "gutenberg", "project"]

def main():
    #filename = "C:\\Users\\Administratör\\Desktop\\DAT425\\Word_Counting\\examples\\article7.txt"
    link = "https://www.gutenberg.org/files/15/15-0.txt"

    #inp_file = open(filename, encoding="utf-8")
    #lines = inp_file.readlines()
    #inp_file.close()

    response = urllib.request.urlopen(link)
    lines = response.read().decode("utf-8").splitlines()

    token = wordfreq.tokenize(lines)
    frequencies = wordfreq.countWords(token, stopwords)
    return wordfreq.printTopMost(frequencies, 10)


main()