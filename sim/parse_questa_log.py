import re

log_file = "transcript"

error_pattern = re.compile(r'(Error:|Fatal:|UVM_ERROR|UVM_FATAL)', re.IGNORECASE)

error_count = 0

print(f"--- START TO SCAN LOG QUESTA ---")

with open(log_file, "r") as f:
	for line_num, line in enumerate(f, 1):
		if error_pattern.search(line):
			print(f"[ERROR FOUND] Line {line_num}: {line.strip()}")
			error_count += 1

print("-" * 30)
if error_count == 0:
	print(f"[PASSED] There are not have any errors in {log_file}.")
else:
	print(f"[FAILED] There are {error_count} found in {log_file}.")
