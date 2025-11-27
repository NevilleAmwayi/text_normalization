import pynini
from pynini.lib import pynutil

# Load basic number files
ONES = pynini.string_file("/home/neville/text_normalization/src/digits.tsv")
TENS = pynini.string_file("/home/neville/text_normalization/src/tens.tsv")

# Compose numbers 0-99
# 0-9
ONES_FST = ONES

# 10-19
TEENS = TENS @ pynini.cdrewrite(pynini.cross("10", "ten"), "", "", pynini.union("[BOS]", "[EOS]"))

# 20-99
# e.g., twenty-one = twenty + "-" + one
TENS_FST = (
    pynini.union(*[str(i) for i in range(20, 100, 10)]) @ TENS
)
TENS_ONES_FST = TENS_FST + pynutil.insert("-") + ONES
NUM_0_99 = pynini.union(ONES_FST, TENS, TENS_ONES_FST)

# 100-999
HUNDREDS = pynini.union(*[str(i) for i in range(1, 10)]) + "00"
HUNDREDS_FST = ONES + pynutil.insert(" hundred")
NUM_100_999 = HUNDREDS_FST + (pynutil.insert(" ") + NUM_0_99).ques

# 1000
NUM_1000 = pynutil.insert("one thousand")

# Full range 0-1000
CARDINAL_EN = pynini.union(NUM_0_99, NUM_100_999, NUM_1000).optimize()
