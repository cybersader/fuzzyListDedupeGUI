# Fuzzy Bullet List Deduplication
<img src="https://user-images.githubusercontent.com/106132469/222927852-2769f8f7-63b3-4236-a436-dd2ddb9e6528.png" alt="image" width="700">

This Python project provides a simple Graphical User Interface (GUI) that allows users to remove duplicate bullet points from a list of bullet points. The GUI is built using the Tkinter library and fuzzy string matching is performed using the fuzzywuzzy library.

## Installation

To run the project, you will need to have Python 3 and the fuzzywuzzy library installed. You can install the library by running the following command:

```pip install fuzzywuzzy```

Once you have the necessary dependencies installed, you can run the project by executing the following command in the root directory of the project:

```python main.py```

Alternatively, if you are running Windows, you can run the provided exe file in the `Releases` section to the right.

## Usage

### Input
Enter a list of bullet points in the input box and specify a similarity threshold (between 0 and 100). 

### Deduplication
Click the "Deduplicate List Items" button to remove duplicate bullet points from the input list and display the cleaned list in the output box.

## Contributing

Contributions to the project are welcome! If you encounter any bugs or would like to suggest improvements, feel free to open an issue or submit a pull request.

## Potential Development

### Javascript Implementation
I could develop a quick little "io" website to do the same thing and host it feely on Netlify

### Use Different Similarity Algorithm
I think that Jaccard similarity might work better
