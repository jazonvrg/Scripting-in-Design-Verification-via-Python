import argparse
import subprocess

parser = argparse.ArgumentParser(description="EDA tool operate QuestaSim for I2C Project")

parser.add_argument("-t", "--testname", required=True, help="Testname you want to run (Ex: i2c_base_test)")
parser.add_argument("-s", "--seed", type=int, default=1, help="Random seed value for SystemVerilog (Default: 1)")
parser.add_argument("-c", "--coverage", action="store_true", help="Turn on coverage-collected setting")

args = parser.parse_args()

print(f"=== CONFIGURED SIMULATION ===")
print(f"Testcase : {args.testname}")
print(f"Seed     : {args.seed}")
print(f"Coverage : {'ON' if args.coverage else 'OFF'}")

cmd = ["make", "run", f"TESTNAME={args.testname}", f"SEED={args.seed}"]

if args.coverage:
	cmd.append("COV=1")

print(f"\n[TRIGGER] Sending command to Linux: {' '.join(cmd)}")

mock_cmd = ["echo"] + cmd

process = subprocess.run(mock_cmd)

if process.returncode == 0:
	print(f"[SAFETY] Simulated process has completed without syntax error.")
else:
	print(f"[CRASH] Simulated process has failed or Makefile is error.")
