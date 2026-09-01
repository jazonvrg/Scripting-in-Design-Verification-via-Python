import subprocess
import re

passed_tests = []
failed_tests = []

print(f"=== REGRESSION SYMTEM IS ALREADY OPERATING ===")

try:
	with open("testlist.txt", "r") as f:
		tests = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
	print(f"[ERROR] File testlist.txt is not existed in this folder.")
	exit(1)

error_pattern = re.compile(r'(Error:|Fatal:|UVM_ERROR|UVM_FALTAL)', re.IGNORECASE)

for test in tests:
	print(f"\n---> Executing: {test}...")
	
	cmd = ["make", "run", f"TESTNAME={test}"]
	mock_cmd = ["echo"] + cmd + ["&&", "sleep", "1"]
	subprocess.run(" ".join(mock_cmd), shell = True)

	with open("transcript", "w") as f:
		f.write(f"UVM_INFO: Starting {test}...\n")
		if test == "i2c_read":
			f.write(f"UVM_ERROR: Data mismatch detected!\n")
		f.write("UVM_INFO: Test finished.\n")

	error_count = 0
	with open("transcript", "r") as log_file:
		for line in log_file:
			if error_pattern.search(line):
				error_count += 1
	
	if error_count == 0:
		print(f"[RESULT] PASSED")
		passed_tests.append(test)
	else:
		print(f"[RESULT] FAILED ({error_count} error)")
		failed_tests.append(test)

print("\n" + "=" * 50)
print(f"		REGRESSION REPORT		")
print("=" * 50)
print(f"Total testcases have been scanned : {len(tests)}")
print(f"Total PASSED testcases		  : {len(passed_tests)}")
print(f"Total FAILED testcases		  : {len(failed_tests)}")

if failed_tests:
	print(f"\n[LISTS OF TESTCASES NEED TO DEBUG]")
	for failed_test in failed_tests:
		print(f" - {failed_test}")
print("=" * 50)
