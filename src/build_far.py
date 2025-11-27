import pynini
from cardinal_en import CARDINAL_EN

far_path = "grammars/cardinal.far"

with pynini.Far(far_path, mode="wb") as far:
    far["CARDINAL_EN"] = CARDINAL_EN

print("FAR file successfully written to:", far_path)
