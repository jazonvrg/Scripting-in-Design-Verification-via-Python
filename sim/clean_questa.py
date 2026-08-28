import os
import shutil

files_to_remove = ["transcript", "vsim.wlf", "i2c_regs.svh"]
dirs_to_remove = ["work"]

print(f"--- START TO CLEAN QUESTA'S ENVIRONMENT ---")

for f in files_to_remove:
	if os.path.exists(f):
		os.remove(f)
		print(f"[REMOVE FILE] {f} has been removed")
	else:
		print(f"[SKIP] {f} is not existed")

for d in dirs_to_remove:
	if os.path.exists(d):
		shutil.rmtree(d)
		print(f"[REMOVE DIR] {d} has been removed")
	else:
		print(f"[SKIP] {d} is not existed")
