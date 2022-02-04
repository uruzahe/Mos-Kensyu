import difflib
import csv
import jaconv
import math
import unicodedata
import time


def csv2dict_list(csv_file_path):
    with open(csv_file_path, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        return [row for row in csvreader]


def str_similarity(str1, str2):
    return difflib.SequenceMatcher(
        None,
        unicodedata.normalize('NFKC', jaconv.hira2kata(str1)),
        unicodedata.normalize('NFKC', jaconv.hira2kata(str2))
        ).ratio()

def count_down(t):
    while 0 <= t:
        print(f"{t} ... ")
        time.sleep(1)
        t = t - 1

def entropy(list_of_probabilities):
    return sum([-math.log2(p) * p for p in list_of_probabilities])
