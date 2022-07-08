#!/usr/bin/env python3
"""Crow's Nest"""


import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a Jazz noise here"""

    args = get_args()
    word = args.word

    article = ""
    if word[0].lower() in "aeiouAEIOU":
        article = "an"
    else:
        article = "a"

    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
