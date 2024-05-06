from pyboy import PyBoy
from ramMapConstants import *
from io import BufferedIOBase

pyboy = PyBoy('Pokemon - Gold Version (UE) [C][!].gbc', sound=True, scale=3)
previousStats = ""
currentStats = ""
pyboy.set_emulation_speed(4)
with open("state_file.state", "rb") as f:
    f.seek(0)
    pyboy.load_state(f)

while pyboy.tick():
    if pyboy.events:
        print(f"events: {pyboy.events}")

    itemHeldMemory: int = pyboy.memory[0xCB0D]
    movesMemory: list[:int] = pyboy.memory[0xCB0E:0xCB12]
    ppMovesMemory: list[:int] = pyboy.memory[0xCB14:0xCB18]
    # TODO: Figure out if this actually works
    statusMemory = pyboy.memory[0xCB1A]
    # end TODO
    hpMemory = pyboy.memory[0xCB1D]
    typeMemory: list[:int] = pyboy.memory[0xCB2A:0xCB2C]
    substituteMemory = pyboy.memory[0xCB49]
    # TODO: These aren't working -> need to find the memory locations proper
    moneyMemory = pyboy.memory[0xCB65:0xCB66]
    expGivenMemory = pyboy.memory[0xCB7E:0xCBC0]
    # end TODO
    currAttMemory = pyboy.memory[0xCBC1]

    currentStats = (f"Item held memory: {itemHeldMemory} -> {itemConstants[itemHeldMemory]}\n"
                    f"Moves 1-4 memory: {movesMemory} -> {printMoves(movesMemory)}\n"
                    f"PP Moves 1-4 memory: {ppMovesMemory}\n"
                    f"Status memory: {statusMemory}\n"
                    f"HP in Battle memory: {hpMemory}\n"
                    f"Type 1-2 memory: {typeMemory} -> {printPokeType(typeMemory)}\n"
                    f"Substitute memory: {substituteMemory}\n"
                    f"Money earned memory: {moneyMemory}\n"
                    f"Exp Given memory: {expGivenMemory}\n"
                    f"Current Attack memory: {currAttMemory} -> {printMoves([currAttMemory])}\n\n\n")

    if currentStats != previousStats:
        print(f"Pokemon Struct: {pyboy.memory[0xCB0C:0xCB33]}\n")
        previousStats = currentStats
        print(previousStats)
        with open("state_file.state", "wb") as f:
            pyboy.save_state(f)
pyboy.stop()
