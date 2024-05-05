from pyboy import PyBoy
from ramMapConstants import *

pyboy = PyBoy('Pokemon - Gold Version (UE) [C][!].gbc', sound=True)
previousStats = ""
currentStats = ""

while pyboy.tick():
    if pyboy.events:
        print(f"events: {pyboy.events}")

    itemHeldMemory: int = pyboy.memory[0xCB0D]
    movesMemory = pyboy.memory[0xCB0E:0xCB11]
    ppMovesMemory = pyboy.memory[0xCB14:0xCB17]
    statusMemory = pyboy.memory[0xCB1A]
    hpMemory = pyboy.memory[0xCB1C:0xCB1D]
    typeMemory = pyboy.memory[0xCB2A:0xCB2B]
    substituteMemory = pyboy.memory[0xCB49]
    moneyMemory = pyboy.memory[0xCB65:0xCB66]
    expGivenMemory = pyboy.memory[0xCB7E:0xCB7F]
    currAttMemory = pyboy.memory[0xCBC1]
    currentStats = f"Item held memory: {itemHeldMemory} -> {itemConstants[itemHeldMemory]}\nMoves 1-4 memory: {movesMemory}\nPP Moves 1-4 memory: {ppMovesMemory}\nStatus memory: {statusMemory}\nHP in Battle memory: {hpMemory}\nType 1-2 memory: {typeMemory}\nSubstitute memory: {substituteMemory}\nMoney earned memory: {moneyMemory}\nExp Given memory: {expGivenMemory}\nCurrent Attack memory: {currAttMemory}\n\n\n"

    # print(currentStats)

    if currentStats != previousStats: 
        previousStats = currentStats
        print(previousStats)

    # print(f"Item held memory: {pyboy.memory[0xCB0D]}")
    # print(f"Moves 1-4 memory: {pyboy.memory[0xCB0E:0xCB11]}")
    # print(f"PP Moves 1-4 memory: {pyboy.memory[0xCB14:0xCB17]}")
    # print(f"Status memory: {pyboy.memory[0xCB1A]}")
    # # Skip 0XCB1B
    # print(f"HP in Battle memory: {pyboy.memory[0xCB1C:0xCB1D]}")
    # print(f"Type 1-2 memory: {pyboy.memory[0xCB2A:0xCB2B]}")
    # # Skip 0xCB2C:0xCB48
    # print(f"Substitute memory: {pyboy.memory[0xCB49]}")
    # # Skip 0xCB4A:0xCB64
    # print(f"Money earned memory: {pyboy.memory[0xCB65:0xCB66]}")
    # # Skip 0xCB67:0xCB7D
    # print(f"Exp Given memory: {pyboy.memory[0xCB7E:0xCB7F]}")
    # # Skip 0xCB80:0xCBC0
    # print(f"Current Attack memory: {pyboy.memory[0xCBC1]}")
    # print("\n\n")
    # # print(f"memory val: {pyboy.get_memory_value()}")
    pass
pyboy.stop()