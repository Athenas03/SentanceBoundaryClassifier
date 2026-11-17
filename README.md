# Sentence Boundary Classifier

## Overview

This project implements a **Sentence Boundary Detection (SBD) system** using a Decision Tree Classifier from Python's Scikit-learn library.

The purpose of the program is to determine whether a period (`.`) at the end of a token represents the end of a sentence or whether it is being used for another purpose, such as an abbreviation or decimal.

The classifier learns from labeled training data and uses features surrounding each period to predict whether a sentence boundary exists.

## Technologies Used

- Python 3
- Scikit-learn
- Decision Tree Classifier

## How It Works

The program reads both training and testing files containing three values per line:

- **Position:** The position of the token in the dataset.
- **Token:** The word or punctuation being analyzed.
- **Label:** The correct sentence boundary classification.

The program first processes the training data and builds a vocabulary of unique words. It then identifies tokens ending in a period and extracts eight features to help the decision tree make predictions.

### Features

The classifier uses the following eight binary features:

| Feature | Description |
|---|---|
| L_vocab | Checks whether the token before the period is in the training vocabulary. |
| R_vocab | Checks whether the next token is in the training vocabulary. |
| L_len_less_4 | Checks whether the token before the period has fewer than four characters. |
| L_is_num | Checks whether the token before the period is a number. |
| R_capitalized | Checks whether the next token begins with a capital letter. |
| R_contains_num | Checks whether the next token contains a number. |
| L_len_greater_1 | Checks whether the token before the period has more than one character. |
| R_len_greater_1 | Checks whether the next token has more than one character. |

Here, **L** represents the token before the period, and **R** represents the token immediately after it.

## Training the Classifier

After extracting the features, the program trains a `DecisionTreeClassifier` using the training data.

It also uses Scikit-learn's `export_text()` function to display the learned decision tree rules. These rules show how the classifier uses the extracted features to make its predictions.

## Testing and Evaluation

Once training is complete, the program processes the testing data using the same eight features.

The classifier predicts whether each period represents a sentence boundary. These predictions are compared against the actual labels in the testing file to calculate the model's accuracy.

Accuracy is calculated using:

**Accuracy = (Correct Predictions / Total Predictions) × 100**

## Output

The program produces two outputs:

1. **Decision Tree Rules:** Displays the rules learned by the classifier.
2. **SBD.test.out:** A file containing the position, token, and predicted label for each token ending in a period in the testing dataset.

## How to Run

### Requirements

Make sure Python 3 and Scikit-learn are installed.

Install Scikit-learn using:

```bash
pip install scikit-learn
```

### Running the Program

Run the program from the command line and provide the training and testing filenames as arguments:

```bash
python SBD.py SBD.train SBD.test
```

Replace `SBD.py`, `SBD.train`, and `SBD.test` with the actual filenames if they are different.

The program will display the learned decision tree rules and the testing accuracy. It will also generate the `SBD.test.out` output file.

## Project Goal

The goal of this project was to explore how machine learning can be applied to Natural Language Processing, specifically sentence boundary detection. By using a Decision Tree Classifier and surrounding word features, the system learns patterns that help distinguish sentence-ending periods from other uses of periods in text.
