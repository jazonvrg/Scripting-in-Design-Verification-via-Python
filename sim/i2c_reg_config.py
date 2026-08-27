base_addr = "0x2000"
i2c_regs = {
	"PREGlo" : "0x00",
	"PRERhi" : "0x01",
	"CTR" : "0x02",
	"TXR" : "0x03"
}

with open("i2c_regs.svh", "w") as f:
	f.write("// --- AUTOMATED FILE CREATED BY PYTHON ---\n")
	f.write(f"// Base Address: {base_addr}\n\n")
	for reg_name, offset in i2c_regs.items():
		sv_offset = offset.replace("0x", "'h")
		f.write(f"`define {reg_name}_ADDR {sv_offset}\n")
print('[SUCCESS] File "i2c_regs.svh!" has been created')
