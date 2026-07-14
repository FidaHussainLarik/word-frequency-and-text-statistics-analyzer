from pathlib import Path
import time
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
    words_count = 0
    content = file_handle.read()
    print(content)
    word_list = content.split()
    print(word_list)
    words_count = len(word_list)
    return words_count


# this will count the total number of sentences in the file
def count_sentences(file):
    sent_count = None
    return sent_count



# count the number of charaters inside the file,with and without spaces.
def count_chars(file):
    char_count = None
    return char_count


# Keep word frequency dictionary/histrogram
def word_freq(file):
    histogram = None
    return histogram


# Count top N most frequent words
def top_most(file):
    top_10 = None
    return top_10

# Summary report generator
def report(file):
    return None

def borders(type_of_b):
    print(f"{type_of_b*70}")

def display_file_content(file_handle):
    borders("-")
    print("                 Displaying file content")
    borders("-")

    for line in file_handle:
        line = line.rstrip()
        print(line)

def main():
    print("\n\n")
    borders("*")
    print("         Word Frequency & Text Statistics Analyzer")
    borders("*")

    file_handle = get_file()

    if not file_handle:
        print(type(file_handle))
        print("🏃Exiting the program",end='')
        for _ in range(5):
            print(".",end='')
            time.sleep(1)
        quit()
    else:
        display_file_content(file_handle)
    
    file_handle.seek(0)
    total_words = count_words(file_handle)
    print("Total Words in the file: ",total_words)










    # End of the main function
    print("\n\n")

if __name__ == "__main__":
    main()