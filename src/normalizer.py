import re
import pynini
from pynini.lib import rewrite

from cardinal_en import CARDINAL_EN

number_regex = re.compile(r"\b[0-9]{1,4}\b")

def normalize_sentence(sentence: str) -> str:
    def replace_number(match):
        num = match.group()
        try:
            return rewrite.one_top_rewrite(num, CARDINAL_EN)
        except:
            return num

    return number_regex.sub(replace_number, sentence)
