from datasets import load_dataset
from normalizer import normalize_sentence

# Load the local text file as a dataset with a single split
ds = load_dataset(
    "text",
    data_files="tests/test_cases_cardinal_en.txt",
    split="train"
)

# Example: expected outputs (replace with correct ones for your data)
expected_outputs = [
    "one", "two", "three", "ten", "fifteen", "twenty-one", "one hundred five", "nine hundred ninety-nine", "one thousand", "two thousand five hundred"
]

for i, item in enumerate(ds):
    input_text = item["text"].strip()
    expected = expected_outputs[i]
    output = normalize_sentence(input_text)
    assert output == expected, f"FAILED: {input_text} → {output} (expected {expected})"

print("All tests passed!")
