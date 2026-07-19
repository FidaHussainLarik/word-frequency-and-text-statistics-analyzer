# Word Frequency & Text Statistics Analyzer

A simple command-line tool that reads a text file and shows useful facts about it, like word count, sentence count, and the most common words.

---

## About This Project

Writers, students, and content creators often want quick facts about a piece of text. For example: How many words are in this file? What are the most common words? Is the text easy or hard to read?

This tool answers these questions. It reads a plain text file (`.txt`) and prints a clear, organized report. You do not need to install any extra software — it uses only core Python.

This is my first portfolio project. I built it to practice real Python skills and a professional Git workflow, as part of my path to become a Full Stack AI Engineer.

---

## Features

### Completed Features
These features work in the current version:
- Reads a `.txt` file and checks that it exists
- Counts the total number of words
- Counts the total number of sentences
- Counts the total number of characters, with and without spaces
- Builds a word-frequency dictionary (not case-sensitive)
- Shows the top 10 most common words
- Shows a clear message if the file does not exist
- Shows a clear message if the file is empty
- Lets the user check more than one file, without restarting the program

### Planned Features (Not Built Yet)
These features are not built yet, but are planned for a future version:
- Remove common stop words (like "the," "is," "and") from the top-word list
- Show the average word length and average sentence length
- Show the longest and shortest word in the file
- Let the user choose how many top words to see
- Save the report to a new text file

---

## How to Run This Project

### Requirements
- Python 3 (no extra libraries needed)

### Steps
1. Clone this repository:
   ```
   git clone <your-repo-url>
   ```
2. Go to the project folder:
   ```
   cd word-frequency-and-text-statistics-analyzer
   ```
3. Run the program:
   ```
   python main.py
   ```
4. When the program asks for a file, type the name of a `.txt` file from the `sample_data` folder. For example:
   ```
   sample_frequency_test.txt
   ```

---

## Example Usage

Input file (`sample_data/sample_frequency_test.txt`):
```
The cat sat on the mat. The cat ran to the door. The dog barked at the cat.
```

Program output:
```
Enter the file you want to analysis(format shoul be .txt): sample_frequency_test.txt

--- Text Statistics ---
Total Words                      : 18
Total sentences                  : 3
Total chracters (w/ spaces)      : 75
Total chracters (no spaces)      : 58
Unique words                     : 11

--- Top 10 Words ---
Rank   Word            Count
----   -------------   -----
1       the       6
2       cat       3
3       to       1
4       sat       1
5       ran       1
6       on        1
7       mat       1
8       door      1
9       dog       1
10      barked    1
```

---

## Project Structure

```
word-frequency-and-text-statistics-analyzer/
├── main.py
├── README.md
├── LICENSE
├── .gitignore
└── sample_data/
    ├── sample_short.txt
    ├── sample_empty.txt
    ├── sample_edge_cases.txt
    ├── sample_frequency_test.txt
    ├── sample_bad_encoding.txt
    └── EXPECTED_RESULTS.md
```

The `sample_data/` folder holds test files with known, checked results. Use `EXPECTED_RESULTS.md` to compare the program's output against verified numbers.

---

## Known Limitations

This project is still a work in progress. The following issues are known, and I plan to fix them soon:

- **Wrong file name in the report.** The report does not correctly show the name of the file you analyzed. A fix is planned.
- **Crash on unreadable files.** If a file has an unusual or broken encoding, the program crashes instead of showing an error message. This will be fixed next.
- **Sentence-counting issue.** If a sentence ends with more than one punctuation mark (like "Really?!"), the program may count it as two sentences instead of one.
- **Incomplete punctuation cleaning.** The program removes periods from the edges of words, but not other marks like commas or question marks. Because of this, a word like `wait,` can appear in the results with the comma still attached.

These issues were found through direct testing against the sample files in `sample_data/`, not just by reading the code. I am fixing them one at a time.

---

## Planned Improvements
- Fix the four known issues listed above
- Add all planned features listed above
- Add a save-to-file option for the report
- Add automated tests

---

## License
This project uses the MIT License. See the `LICENSE` file for details.

## Author
Built by Fida Hussain, as the first project in a Full Stack AI Engineer learning roadmap, following the Python for Everybody Specialization (Courses 1 and 2).
