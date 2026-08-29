import argparse

parser = argparse.ArgumentParser(description="EDA Tool operate QuestaSim for I2C Project")

parser.add_argument("-t", "--testname", required=True, help="Testname you want to run (Ex: i2c_base_test)")
parser.add_argument("-s", "--seed", type=int, default=1, help="Random seed value for SystemVerilog (Default: 1)")
parser.add_argument("-c", "--coverage", action="store_true", help="Turn on coverage-collected setting")

args = parser.parse_args()

print(f"=== CONFIGURED SIMULATION ===")
print(f"Testcase : {args.testname}")
print(f"Seed     : {args.seed}")
print(f"Coverage : {'ON' if args.coverage else 'OFF'}")
