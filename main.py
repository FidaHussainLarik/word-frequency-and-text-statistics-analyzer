from pathlib import Path
import time
import re
DATA_FILE_PATH = Path(__file__).resolve().parent/"sample_data"


# function to take user input (file name) and fetch that specific file and return file-handle back
def get_file():

    while True:
        file_name = input("Enter the file you want to analysis(format shoul be .txt): ")
        try:
            # Edge case handled
            if file_name.endswith('.txt'):
                file_handle = open(DATA_FILE_PATH/file_name)
                print("Opening the file.....")
                print("File opened successfully!")

                #Check if file is empty or not before returning it to main
                content = file_handle.read()
                if content:
                    return file_handle
                else:
                    print("File is empty 📪")
                    print("File has no content to analyze.")
                    answer = input("Press enter to re-enter the correct file format OR enter 'exit' to end the program: ").strip().lower()
                    if answer == 'exit': 
                        break
                    else:
                        continue
            else:
                print("Unsupported file format ⚠")
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
def count_words(file_handle):
    # Reset the pointer to the first line of the file
    file_handle.seek(0)
    content = file_handle.read()
    # .split() function convert entire file content (which is a long string of words) into a list of words
    # list elements will be seperated by space ' '.
    word_list = content.split()
    return len(word_list)


# this will count the total number of sentences in the file
def count_sentences(file_handle):
    # Reset the pointer to the first line of the file
    file_handle.seek(0)

    content = file_handle.read()
    sent_list = re.split('[.!?]',content)
    return len(sent_list)-1



# count the number of charaters inside the file,with and without spaces.
def count_chars(file_handle):

    file_handle.seek(0)
    content = file_handle.read()
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
def word_freq(file_handle):
    #file pointer shifted to first line
    file_handle.seek(0)
    # read() transfer the entire content of file as a string in content
    content = file_handle.read()

    # split() creates a list of words
    word_list = content.split()
    histogram = dict()

    # count the frequency of each word using dictionary
    for word in word_list:
        word = word.lower()
        
        #get(word,0) will check the dictionary for the current word. If the word is present it return its value(a numeric value) if not it retrun 0 by default
        histogram[word] = histogram.get(word,0) + 1    
    return histogram

def count_unique_words(histogram):   
    # return a list of unique word in form of a dictionary
    return len(histogram)

# Count top N most frequent words
def top_most(histogram):

    top_10_list = list()

    for (key,value) in histogram.items():
        key.strip()
        top_10_list.append((value,key))
    # sorting the list of tuples of (value,key) pair in descending order
    top_10_list.sort(reverse= True)
    return top_10_list

# Summary report generator
def report(file_handle):
    total_words = count_words(file_handle)
    total_sentences = count_sentences(file_handle)
    total_chars = count_chars(file_handle)
    word_frequency = word_freq(file_handle)
    unique_word_count = count_unique_words(word_frequency)
    top_most_word = top_most( word_freq(file_handle))
    


    print("Total Words                      :",total_words)
    print("Total sentences                  :",total_sentences)

    for key,value in total_chars.items():
        print(f"Total chracters ({key})      : {value} ")
    
    print("Unique words                     :",unique_word_count)
   
    print("     --- Top 10 Words ---")
    for index, (key,value) in enumerate(top_most_word):
        print( print(f"{index} {key} {value}"))

    
    

def borders(type_of_b):
    print(f"{type_of_b*70}")

def display_file_content(file_handle):
    borders("-")
    print("                 Displaying file content")
    borders("-")

    for line in file_handle:
        line = line.strip()
        print(line)

def main():
    print("\n\n")
    borders("*")
    print("         Word Frequency & Text Statistics Analyzer")
    borders("*")


    # for debuging purpose choose a static file not ask one on run time
     # 1st feature
    # file_handle = get_file()
    file_handle = open(DATA_FILE_PATH/"sample_short.txt")

    if not file_handle:
        print(type(file_handle))
        print("🏃Exiting the program",end='')
        for _ in range(5):
            print(".",end='')
            time.sleep(1)
        quit() 
    
    # # This is added just for debuging purpose
    # # display_file_content(file_handle)
    # total_words = count_words(file_handle)
    # total_sentences = count_sentences(file_handle)
    # total_characters = count_chars(file_handle)



    # # 2nd feature (Total Words in the file)
    # print("Total Words in the file    : ",total_words)
    
    # # 3rd feature (Total sentences in the file)
    # print("Total sentences in the file: ",total_sentences)

    # # 4th feature (Total chracters)
    # # A dictionary return (key:value) tuple for number of chars with and without spaces
    # for key,value in total_characters.items():
    #     print(f"Total chracters ({key}): {value} ")

    # # 5th feature (counting frequency of words)
    # print("Listing down the frequency of each word")
    # word_frequency = word_freq(file_handle)
    # for index, (key, value) in enumerate(word_frequency.items(),1):
    #     #this will remove the '.' attached to words in the dictionary's values
    #     key = key.strip('.')
    #     if index <= 9:
    #         print(f"{index}  {key.strip()}: {value} ")
    #     print(f"{index} {key}: {value} ")
    # frequency_histogram = word_freq(file_handle)
   

    # # 6th feature (Number of unique words)
    # unique_count = count_unique_words(frequency_histogram)
    # print("Number of unique words: ",unique_count)


    # # 7th feature (finding 10 top most words)
    # top_most_words = top_most(frequency_histogram)
    # print("top most words in a list of tuple")

    # for index,(value,key) in enumerate(top_most_words):
    #     print(f"{index} {key} {value}")

    # Print the summary report
    report(file_handle)



    print("Analyze another file? (y/n):")
    print("Done ✅✅✅✅✅✅✅✅✅")
    # End of the main function
    print("\n\n")

if __name__ == "__main__":
    main()