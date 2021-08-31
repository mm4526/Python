# Name: Taylor Brent and Meghan McClaskey       Date Assigned: 11.7.17
# Course: CSE 1284 Sec 7                        Date Due: 11.7.17
# Program Description: User enters url and the program returns the reading
# diffiulty and stats about the webpage.
def main():
        # import website
        import urllib.request
        # acess website
        url = str(input('Enter exact url: '))
        # open url
        web_handle = urllib.request.urlopen(url)
        # read & create list of words 
        web_text = web_handle.read().decode("utf8")
        word_list = web_text.split()

        # Import math and initialize lists and counters
        import math
        index = 0
        syl_list = []
        total_syl = 0
        position = 0
        sentence = 0
        # Iterate through words
        for words in word_list:
                # SYLLABLES PER WORD
                
                # Find number of characters in word
                num_char = len(word_list[index]) 
                # Determine number of syllables and add value to list
                syl = math.ceil(num_char/4)
                syl_list.append(syl)
                # Find total number of syllables
                total_syl += syl_list[index]
                
                # WORDS PER SENTENCE

                # Find position of period
                position = word_list[index].find('.')
                if position >= 0:
                        # Accumulate number of sentences
                        sentence += 1
                index += 1
        # Calculate average syllables and words
        avg_syl = total_syl / len(word_list)
        avg_sent_len = len(word_list) /sentence
        # Print results
        print("Average syllables per word: ",avg_syl)
        print("Average sentence length: ",avg_sent_len)

        # READING LEVEL FORMULA & output
        rl = (.39*avg_sent_len) + (11.8*avg_syl) - 15.59
        print("Reading level: ",rl)
       
main()
