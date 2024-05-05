from pyboy import PyBoy

pyboy = PyBoy('Pokemon - Gold Version (UE) [C][!].gbc', sound=True)
while pyboy.tick():
    print(f"events: {pyboy.events}")
    print(f"memory: {pyboy.memory[0xCB0D:0xCBC1]}")
    print(f"memory val: {pyboy.get_memory_value()}")
    pass
pyboy.stop()