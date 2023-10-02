import os
import argparse
import string
import pandas as pd
from collections import defaultdict
import re
# ------------------------------------------------------------------------------------------------------


def main(input_file):

    with open(input_file, 'r') as file:
        text_file = file.read()

    sentences = text_file.split('.')

    sen_len = [len(sentence.split()) for sentence in sentences]

    data = {
        'sent': sentences,
        'wrd_cnt': sen_len
    }

    df = pd.DataFrame(data)

    os.makedirs("Text Feature")

    output_file = os.path.join("Text Feature", "word.csv")
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()
    main(args.input_file)
