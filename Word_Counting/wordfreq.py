

def tokenize(lines):
    words = []
    for line in lines:
        # Counter for current letter
        start = 0

        while start < len(line):

            while start < len(line) and line[start].isspace():
                start = start+1

            if start >= len(line):
                break


            end = start


            while end < len(line) and line[end].isalpha():
                end = end+1
            
            if end > start:
                word = line[start:end]
                lower = word.lower()
                words.append(lower)
                start = end
                continue

            while end < len(line) and line[end].isdigit():
                end = end+1
            
            if end > start:
                words.append(line[start:end])
                start = end
                continue


            while end < len(line) and not line[end].isdigit() and not line[end].isalpha() and not line[end].isspace():
                end = end+1

            if end > start:
                words.append(line[start:end])
                start = end
                continue


            start = end

    return words

def countWords(words, stopWords):
    Counter = 0
    frequencies =  {}
    for word in words:

        if word not in stopWords and word not in frequencies:
            frequencies[word] = 1 
            Counter = Counter + 1
            continue

        if word not in stopWords:
            frequencies[word] = frequencies[word] + 1
            Counter = Counter + 1

        if word in stopWords:
            Counter = Counter + 1
            continue
    return frequencies    

      
