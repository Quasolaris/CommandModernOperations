#!/usr/bin/env python3
"""

Start Script was generated with Lumo AI and then changed for my use case


Read an input text file line‑by‑line and turn each line into a
Sublime‑completions entry:

    { "trigger": "<line>", "contents": "<line>",
      "annotation": "", "kind": "function", "details": "" },

The result is written to *output_file* (one JSON object per line,
trailing commas are kept so you can paste the whole block into a
`sublime‑completions` file later).
"""

import argparse
import json
import pathlib
import sys


def make_entry(line: str) -> dict:
    """Return the dict that represents one completion entry."""
    # Strip the newline but keep the original text (including leading/trailing spaces)
    text = line.rstrip("\n")
    return {
        "trigger": text,
        "contents": text,
        "annotation": "",
        "kind": "function",
        "details": ""
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a plain‑text list into Sublime completion entries."
    )
    parser.add_argument(
        "input_file",
        type=pathlib.Path,
        help="Path to the file that contains one entry per line."
    )
    parser.add_argument(
        "output_file",
        type=pathlib.Path,
        help="Where to write the generated JSON objects."
    )


    args = parser.parse_args()

    # Ensure the input exists
    if not args.input_file.is_file():
        sys.exit(f"❌ Input file not found: {args.input_file}")

    # Open the output file for writing (UTF‑8)
    with args.output_file.open("w", encoding="utf-8") as out_f:
        with args.input_file.open("r", encoding="utf-8") as in_f:
            for line in in_f:
                # Skip completely empty lines (optional – remove if you want them)
                if line.strip() == "":
                    continue

                entry = make_entry(line)
                # Dump as compact JSON, then add a trailing comma and newline
                json_line = json.dumps(entry, ensure_ascii=False, indent=4)
                out_f.write(json_line + ",\n")

    print(f"✅ Done – {args.output_file} now contains the completions.")


if __name__ == "__main__":
    main()