from datasets import load_dataset
from normalizer import normalize_sentence

ds = load_dataset("DigitalUmuganda/Text_Normalization_Challenge_Unittests_Eng_Fra")

for item in ds['train']:
    input_text = item['raw']
    expected = item['normalized']

    output = normalize_sentence(input_text)
    assert output == expected, f"FAILED: {input_text} → {output} (expected {expected})"

print("All tests passed!")
