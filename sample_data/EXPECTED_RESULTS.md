# Expected Results — Sample Data Answer Key

This file is the verification reference required by SRS Acceptance Criteria #2 and #3 ("a sample file with a manually-verified word count..." / "...manually-verified word-frequency list"). Run your program against each file below and check the output matches.

**Recommendation:** hand-count `sample_short.txt` yourself before checking it against this key — the manual verification is the actual skill the SRS is asking for. Use the rest of these as a shortcut once you trust your own counting process.

---

## sample_short.txt
Clean happy-path text, no edge cases. Good first test.

- **Total words:** 21
- **Total sentences:** 3
- **Characters (with spaces, including the file's own newlines if any):** 130
- **Characters (without whitespace):** 110
- **Unique words:** 17
- **Top words:** `python` (3), `is` (3), then 15 words tied at 1 each

**Note on the tie at the top:** `python` and `is` are tied at 3. Your SRS doesn't specify a tie-breaking rule for equal-frequency words. `sorted()` is stable, so ties will come out in whatever order you built the dictionary in (first-appearance order, if you're inserting as you go). That's a reasonable default — just be aware it's a decision, not an accident, and worth a one-line comment in your code explaining it.

---

## sample_empty.txt
Zero bytes. This is your empty-file error-handling test — your program should detect this explicitly and show the SRS's "file has no content" message, not print a report full of zeros.

---

## sample_edge_cases.txt
Deliberately exercises every Business Rule in your SRS at once:

| Rule being tested | Where in the file |
|---|---|
| Case-insensitive counting | `Python`, `PYTHON`, `python` — all should collapse into one `python` entry with count 3 |
| Punctuation stripped from word edges | `language.`, `fun.`, `old!` |
| Hyphenated words kept as one word | `state-of-the-art` |
| Contractions kept as one word | `don't`, `It's` |
| Standalone numbers counted in total but excluded from top-words by default | `2024` |
| Blank lines skipped entirely | the two empty lines between paragraphs |
| Repeated terminal punctuation = one sentence boundary | `Wait, really?!` counts as **one** sentence ending, not two |

- **Total words:** 39
- **Total sentences:** 7
- **Characters (with spaces, including newlines):** 238
- **Characters (without whitespace):** 198
- **Unique words:** 36
- **Top words:** `python` (3), `is` (2), then everything else tied at 1

If your program's word count on this file is off, it's almost always one of: hyphen-splitting, contraction-splitting, or not skipping the blank lines. Check those three first.

---

## sample_frequency_test.txt
> "The cat sat on the mat. The cat ran to the door. The dog barked at the cat."

Built so you can verify the frequency ranking by eye, no script needed:

- **Total words:** 18
- **Total sentences:** 3
- **Unique words:** 11
- **Top words:** `the` (6), `cat` (3), then `sat`, `on`, `mat`, `ran`, `to`, `door`, `dog`, `barked`, `at` — all tied at 1

This is the file to use for Acceptance Criteria #3 specifically — the top-2 ranking (`the`, then `cat`) is unambiguous, no ties to worry about at the top.

---

## sample_bad_encoding.txt
Contains raw invalid-UTF-8 bytes (`0xFF 0xFE`) in the middle of otherwise normal text. Opening this with `open(path, "r", encoding="utf-8")` will raise:

```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 32: invalid start byte
```

This is your test case for the SRS's "file cannot be read" error path — confirm your `try/except` catches this specific failure and shows a plain-English message instead of letting the traceback through.

---

## A note on characters "with spaces"

Your SRS doesn't specify whether newline characters count toward "characters with spaces" or get treated like whitespace for "characters without spaces." The numbers above assume:
- **With spaces** = every character in the file, including newlines, exactly as read.
- **Without spaces** = every character *except* whitespace of any kind (spaces, tabs, newlines) — not just literal space characters.

This is a reasonable interpretation, but it's genuinely ambiguous in the SRS as written. Pick a convention, document it in a comment or your README, and stay consistent — that's the actual expectation here, not guessing the "right" answer.
