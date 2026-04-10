import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--extra-args")
try:
    args = parser.parse_args(["--extra-args=--use-tns"])
    print(f"Success: {args}")
except SystemExit:
    print("Failed")
