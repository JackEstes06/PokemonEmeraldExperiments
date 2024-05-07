from pyboy import PyBoy
from ramMapConstants import *
from pokemonStruct import PokemonRAM
from io import BufferedIOBase

PY_BOY = PyBoy('Pokemon - Gold Version (UE) [C][!].gbc', sound=True, scale=3)
previousStats = ""
currentStats = ""
PY_BOY.set_emulation_speed(4)
with open("state_file.state", "rb") as f:
    f.seek(0)
    PY_BOY.load_state(f)

while PY_BOY.tick():
    if PY_BOY.events:
        print(f"events: {PY_BOY.events}")

    itemHeldMemory: int = PY_BOY.memory[0xCB0D]
    movesMemory: list[:int] = PY_BOY.memory[0xCB0E:0xCB12]
    ppMovesMemory: list[:int] = PY_BOY.memory[0xCB14:0xCB18]
    # TODO: Figure out if this actually works
    statusMemory = PY_BOY.memory[0xCB1A]
    # end TODO
    hpMemory = PY_BOY.memory[0xCB1D]
    typeMemory: list[:int] = PY_BOY.memory[0xCB2A:0xCB2C]
    substituteMemory = PY_BOY.memory[0xCB49]
    # TODO: These aren't working -> need to find the memory locations proper
    moneyMemory = PY_BOY.memory[0xCB65:0xCB66]
    expGivenMemory = PY_BOY.memory[0xCB7E:0xCBC0]
    # end TODO
    currAttMemory = PY_BOY.memory[0xCBC1]

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
        pokemon = PokemonRAM(0xCB0C)
        pokemon.printPokemoneRAM()
        pokemon.printPokemonInfo()

        previousStats = currentStats
        print(previousStats)
        with open("state_file.state", "wb") as f:
            PY_BOY.save_state(f)
PY_BOY.stop()
