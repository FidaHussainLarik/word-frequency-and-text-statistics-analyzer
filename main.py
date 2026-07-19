from pathlib import Path
import time
import re
DATA_FILE_PATH = Path(__file__).resolve().parent/"sample_data"
# function to take user input (file name) and fetch that specific file and return file-handle back
def get_file():

    while True:
        file_name = input("\nEnter the file you want to analysis(format shoul be .txt): ")
        try:
            # Edge case handled
            if file_name.endswith('.txt'):
                file_handle = open(DATA_FILE_PATH/file_name)
                print("Opening the file.....")
                print("File opened successfully!")
                #Check if file is empty or not before returning it to main
                content = file_handle.read()
                file_handle.seek(0)
                if content:
                    return file_handle
                else:
                    print("File is empty 📪")
                    print("This file is empty — there's no content to analyze. Try a different file.")
                    answer = input("Press enter to re-enter the correct file format OR enter 'exit' to end the program: ").strip().lower()
                    if answer == 'exit': 
                        break
                    else:
                        continue
            else:
                print("""\nThat file couldn't be read as text — it may be corrupted, use an unsupported encoding, or not be a text file at all. Try a different file.\n""")
                
                answer = input("Press enter to re-enter the correct file format OR enter 'exit' to end the program: ").strip().lower()
                if answer == 'exit': 
                    break
                else:
                    continue
                
        # in case file not found the program asks user for re-entering the filename or to quit the execution
        except FileNotFoundError:

            print("File not found ⚠")
            answer = input("Press enter to reenter the correct file name/format OR enter 'exit' to end the program: ").strip().lower()
            if answer == 'exit': 
                break
            else:
                continue
# End of the method

# This function counts words
def count_words(content):
    word_list = content.split()
    return len(word_list)


# this will count the total number of sentences in the file
def count_sentences(content):
    sent_list = re.split('[.!?]',content)
    return len(sent_list)-1


# count the number of charaters inside the file,with and without spaces.
def count_chars(content):

    char_count = dict()

    #Give the lenght of entire file's characters
    char_count['w/ spaces'] = len(content)

    count_without_spaces = 0
    for char in content:
        # count character and skips spaces
        if not char == ' ':
            count_without_spaces = count_without_spaces+1

    char_count['no spaces'] = count_without_spaces

    return char_count


# Keep word frequency dictionary/histrogram
def word_freq(content):
    # split() creates a list of words
    word_list = content.split()
    histogram = dict()

    # count the frequency of each word using dictionary
    for word in word_list:
        word = word.lower().strip('.')
        word = word.strip()
        
        #get(word,0) will check the dictionary for the current word. If the word is present it return its value(a numeric value) if not it retrun 0 by default
        histogram[word] = histogram.get(word,0) + 1    
    return histogram

def count_unique_words(histogram):   
    # return a list of unique word in form of a dictionary
    return len(histogram)

# Count top N most frequent words
def top_10_words(histogram):

    top_10_list = list()

    for (key,value) in histogram.items():
        key.strip()
        top_10_list.append((value,key))
    # sorting the list of tuples of (value,key) pair in descending order
    top_10_list.sort(reverse= True)
    return top_10_list[:10]

# Summary report generator
def file_report(content):
    total_words = count_words(content)
    total_sentences = count_sentences(content)
    total_chars = count_chars(content)
    word_frequency = word_freq(content)
    unique_word_count = count_unique_words(word_frequency)
    top_ten_word = top_10_words( word_frequency)
    

    print("\nAnalyzing 'sample_short.txt'...\n")
    print("--- Text Statistics ---")
    print("File Analyzed                    :")
    print("Total Words                      :",total_words)
    print("Total sentences                  :",total_sentences)

    for key,value in total_chars.items():
        print(f"Total chracters ({key})      : {value} ")
    
    print("Unique words                     :",unique_word_count)
   
    print("\n\n--- Top 10 Words ---")
    print("""Rank   Word            Count\n----   -------------   -----""")
    # print("Rank       Word                Count")
    for index, (value,key) in enumerate(top_ten_word,1):
        if index <=9:
            print(f"{index}       {key}       {value}")
        else:
            print(f"{index}      {key}       {value}")

    
def borders(type_of_b):
    print(f"{type_of_b*80}")

def main():
    print("\n\n")
    borders("*")
    print("         Word Frequency & Text Statistics Analyzer")
    borders("*")

    # for debuging purpose choose a static file not ask one on run time
     # 1st feature

    while True: 
        file_handle = get_file()
        # file_handle = open(DATA_FILE_PATH/"sample_short.txt")

        if not file_handle:
            print("🏃Exiting the program",end='')
            for _ in range(5):
                print(".",end='')
                time.sleep(1)
            print("\n\n\n")
            borders('*')
            return 
        
        # Print the summary report
        content = file_handle.read()
        file_report(content)
        borders('*')



        # this while loop is used incase when the user do not enter value yes or not.
        while True:
            print("Analyze another file? (yes/no): ",end='')
            answer = input().strip().lower()
            if answer == 'yes' or answer == 'no':
                if answer == "yes":
                    break
                else:
                    print("Done ✅✅✅✅✅✅✅✅✅")
                    print("Exiting the program......\n\n\n")
                    borders('*')
                    file_handle.close()
                    return
            else:
                continue
    
 

if __name__ == "__main__":
    main()