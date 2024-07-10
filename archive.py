import sys
import subprocess

def archive(output, objects):
    command = ["ar", "rcs", output] + objects
    result = subprocess.run(command, capture_output=True)
    if result.returncode != 0:
        print("Error archiving objects:")
        print(result.stderr.decode())
        sys.exit(1)

if __name__ == "__main__":
    output = sys.argv[1]
    objects = sys.argv[2:]
    print("+", *sys.argv)
    archive(output, objects)
