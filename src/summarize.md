# XLNet-based Text Summarizer

This script provides a command-line interface (CLI) for summarizing text using the XLNet transformer model.

## Overview

The `SummarizerCLI` class implements a text summarization tool using the XLNet model from the `summarizer` library. It can take input text and generate a concise summary.

## Dependencies

- summarizer

## Class: SummarizerCLI

### Initialization

```python
summarizer = SummarizerCLI(text=None)
```

## Methods

- summarize_text()

Generates a summary of the provided text.
Returns the generated summary.
Prints the summary to the console.


- run()

Executes the summarization process.
Returns the result of summarize_text().
