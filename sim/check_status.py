import sys
import os

if len(sys.argv) < 2:
	print(f"[SYNTAX ERROR] Please provide file name")
	print(f"Usage: python3 check_status.py <file_name>")
	sys.exit(2)

target_file = sys.argv[1]

if os.path.exists(target_file):
	print(f"[PASSED] {target_file} has been found")
	sys.exit(0)
else:
	print(f"[FAILED] {target_file} has not been found")
	sys.exit(1)
