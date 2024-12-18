import os
import argparse
import json
from tqdm import tqdm

from rdkit.Chem import AllChem as Chem


def get_charset_from_xyz(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    atom_count = int(lines[0])

    smiles = lines[atom_count + 3].split()[1]

    try:
        smiles = Chem.MolToSmiles(Chem.MolFromSmiles(smiles), isomericSmiles=True, canonical=True)
    except Exception:
        smiles = ""

    if len(smiles) > 34:
        smiles = ""

    out = set(smiles)
    if "." in out:
        out.remove(".")
    return out


def main():
    parser = argparse.ArgumentParser(description="Create json file containing all the characters used in SMILES in .xyz files")
    parser.add_argument("--dir", type=str, help="Directory containing xyz files.")
    parser.add_argument("--out", default="qm9.json", type=str, help="Output json file")

    args = parser.parse_args()

    out_json_filename = args.out

    char_set = set(" ")

    directory = os.fsencode(args.dir)
    for file in tqdm(os.listdir(directory)):
        filename = os.fsdecode(file)
        if filename.endswith(".xyz"):
            filepath = os.path.join(args.dir, filename)
            char_set = char_set.union(get_charset_from_xyz(filepath))

    json_str = json.dumps(list(char_set))
    with open(out_json_filename, "w") as outfile:
        outfile.write(json_str)

    print(f"Wrote {len(char_set)} chars to {out_json_filename}.")


if __name__ == "__main__":
    main()
