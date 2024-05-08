from ramMapConstants import *


# Given the starting RAM location, a pokemon is structured off of the following offsets from the start position:
# Info found here: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_II)
# ------------------------------------------------------
# Offset    Contents                            Size
# ------------------------------------------------------
# 0x00 	    Index number of the species 	    1 byte
# 0x01 	    Index number of held item 	        1 byte
# 0x02 	    Index number of move 1 	            1 byte
# 0x03 	    Index number of move 2 	            1 byte
# 0x04 	    Index number of move 3 	            1 byte
# 0x05 	    Index number of move 4 	            1 byte
# 0x06 	    Original Trainer ID number 	        2 bytes
# 0x08 	    Experience points 	                3 bytes
# 0x0B 	    HP EV data 	                        2 bytes
# 0x0D 	    Attack EV data 	                    2 bytes
# 0x0F 	    Defense EV data 	                2 bytes
# 0x11 	    Speed EV data 	                    2 bytes
# 0x13 	    Special EV data 	                2 bytes
# 0x15 	    IV data 	                        2 bytes
# 0x17 	    Move 1's PP values 	                1 byte
# 0x18 	    Move 2's PP values 	                1 byte
# 0x19 	    Move 3's PP values 	                1 byte
# 0x1A 	    Move 4's PP values 	                1 byte
# 0x1B 	    Friendship/Remaining Egg cycles 	1 byte
# 0x1C 	    Pokérus 	                        1 byte
# 0x1D 	    Caught data 	                    2 bytes
# 0x1F 	    Level 	                            1 byte
# 0x20 	    Status condition 	                1 byte
# 0x21 	    Unused byte 	                    1 byte
# 0x22 	    Current HP 	                        2 bytes
# 0x24 	    Maximum HP 	                        2 bytes
# 0x26 	    Attack 	                            2 bytes
# 0x28 	    Defense 	                        2 bytes
# 0x2A 	    Speed 	                            2 bytes
# 0x2C 	    Special Attack 	                    2 bytes
# 0x2E 	    Special Defense 	                2 bytes
# ------------------------------------------------------

class PokemonRAM:
    def __init__(self, ramHex, PY_BOY):
        self.ramStartHex = ramHex
        self.pokeNumberRamHex = PY_BOY.memory[self.ramStartHex + 0x00]
        self.pokeItemRamHex = PY_BOY.memory[self.ramStartHex + 0x01]
        self.pokeMove1RamHex = PY_BOY.memory[self.ramStartHex + 0x02]
        self.pokeMove2RamHex = PY_BOY.memory[self.ramStartHex + 0x03]
        self.pokeMove3RamHex = PY_BOY.memory[self.ramStartHex + 0x04]
        self.pokeMove4RamHex = PY_BOY.memory[self.ramStartHex + 0x05]
        self.ogTrainerIDRamHex = PY_BOY.memory[(self.ramStartHex + 0x06):(self.ramStartHex + 0x08)]
        self.expRamHex = PY_BOY.memory[(self.ramStartHex + 0x08):(self.ramStartHex + 0x0B)]
        self.hpEVDataRamHex = PY_BOY.memory[(self.ramStartHex + 0x0B):(self.ramStartHex + 0x0D)]
        self.attEVDataRamHex = PY_BOY.memory[(self.ramStartHex + 0x0D):(self.ramStartHex + 0x0F)]
        self.defEVDataRamHex = PY_BOY.memory[(self.ramStartHex + 0x0F):(self.ramStartHex + 0x11)]
        self.speedEVDataRamHex = PY_BOY.memory[(self.ramStartHex + 0x11):(self.ramStartHex + 0x13)]
        self.specialEVDataRamHex = PY_BOY.memory[(self.ramStartHex + 0x13):(self.ramStartHex + 0x15)]
        self.ivDataRamHex = PY_BOY.memory[(self.ramStartHex + 0x15):(self.ramStartHex + 0x17)]
        self.pokeMove1PPRamHex = PY_BOY.memory[self.ramStartHex + 0x17]
        self.pokeMove2PPRamHex = PY_BOY.memory[self.ramStartHex + 0x18]
        self.pokeMove3PPRamHex = PY_BOY.memory[self.ramStartHex + 0x19]
        self.pokeMove4PPRamHex = PY_BOY.memory[self.ramStartHex + 0x1A]
        self.friendEggCyclesRamHex = PY_BOY.memory[self.ramStartHex + 0x1B]
        self.pokerusInfectionRamHex = PY_BOY.memory[self.ramStartHex + 0x1C]
        self.caughtDataRamHex = PY_BOY.memory[(self.ramStartHex + 0x1D):(self.ramStartHex + 0x1F)]
        self.levelRamHex = PY_BOY.memory[self.ramStartHex + 0x1F]
        self.statusRamHex = PY_BOY.memory[self.ramStartHex + 0x20]
        self.unusedByteRamHex = PY_BOY.memory[self.ramStartHex + 0x21]
        self.currHPRamHex = PY_BOY.memory[(self.ramStartHex + 0x22):(self.ramStartHex + 0x24)]
        self.maxHPRamHex = PY_BOY.memory[(self.ramStartHex + 0x24):(self.ramStartHex + 0x26)]
        self.attStatRamHex = PY_BOY.memory[(self.ramStartHex + 0x26):(self.ramStartHex + 0x28)]
        self.defStatRamHex = PY_BOY.memory[(self.ramStartHex + 0x28):(self.ramStartHex + 0x2A)]
        self.speedStatRamHex = PY_BOY.memory[(self.ramStartHex + 0x2A):(self.ramStartHex + 0x2C)]
        self.spAttStatRamHex = PY_BOY.memory[(self.ramStartHex + 0x2C):(self.ramStartHex + 0x2E)]
        self.spDefStatRamHex = PY_BOY.memory[(self.ramStartHex + 0x2E):(self.ramStartHex + 0x30)]

    def printPokemonRAM(self):
        print(f"ramStartHex: {self.ramStartHex}\n"
              f"pokeNumberRamHex: {self.pokeNumberRamHex}\n"
              f"pokeItemRamHex: {self.pokeItemRamHex}\n"
              f"pokeMove1RamHex: {self.pokeMove1RamHex}\n"
              f"pokeMove2RamHex: {self.pokeMove2RamHex}\n"
              f"pokeMove3RamHex: {self.pokeMove3RamHex}\n"
              f"pokeMove4RamHex: {self.pokeMove4RamHex}\n"
              f"ogTrainerIDRamHex: {self.ogTrainerIDRamHex}\n"
              f"expRamHex: {self.expRamHex}\n"
              f"hpEVDataRamHex: {self.hpEVDataRamHex}\n"
              f"attEVDataRamHex: {self.attEVDataRamHex}\n"
              f"defEVDataRamHex: {self.defEVDataRamHex}\n"
              f"speedEVDataRamHex: {self.speedEVDataRamHex}\n"
              f"specialEVDataRamHex: {self.specialEVDataRamHex}\n"
              f"ivDataRamHex: {self.ivDataRamHex}\n"
              f"pokeMove1PPRamHex: {self.pokeMove1PPRamHex}\n"
              f"pokeMove2PPRamHex: {self.pokeMove2PPRamHex}\n"
              f"pokeMove3PPRamHex: {self.pokeMove3PPRamHex}\n"
              f"pokeMove4PPRamHex: {self.pokeMove4PPRamHex}\n"
              f"friendEggCyclesRamHex: {self.friendEggCyclesRamHex}\n"
              f"pokerusInfectionRamHex: {self.pokerusInfectionRamHex}\n"
              f"caughtDataRamHex: {self.caughtDataRamHex}\n"
              f"levelRamHex: {self.levelRamHex}\n"
              f"statusRamHex: {self.statusRamHex}\n"
              f"unusedByteRamHex: {self.unusedByteRamHex}\n"
              f"currHPRamHex: {self.currHPRamHex}\n"
              f"maxHPRamHex: {self.maxHPRamHex}\n"
              f"attStatRamHex: {self.attStatRamHex}\n"
              f"defStatRamHex: {self.defStatRamHex}\n"
              f"speedStatRamHex: {self.speedStatRamHex}\n"
              f"spAttStatRamHex: {self.spAttStatRamHex}\n"
              f"spDefStatRamHex: {self.spDefStatRamHex}\n")

    def printPokemonInfo(self):
        pokeMovesList = [self.pokeMove1RamHex, self.pokeMove2RamHex, self.pokeMove3RamHex, self.pokeMove4RamHex]
        pokeMovesPPList = [self.pokeMove1PPRamHex, self.pokeMove2PPRamHex, self.pokeMove3PPRamHex,
                           self.pokeMove4PPRamHex]
        print(f"Item held memory: {self.pokeItemRamHex} -> {itemConstants[self.pokeItemRamHex]}\n"
              f"Moves 1-4 memory: {pokeMovesList} -> {printMoves(pokeMovesList)}\n"
              f"PP Moves 1-4 memory: {pokeMovesPPList}\n"
              f"Status memory: {self.statusRamHex}\n"
              f"HP in Battle memory: {self.currHPRamHex}/{self.maxHPRamHex}\n")
        # f"Type 1-2 memory: {typeMemory} -> {printPokeType(typeMemory)}\n"
        # f"Substitute memory: {substituteMemory}\n"
        # f"Money earned memory: {moneyMemory}\n"
        # f"Exp Given memory: {expGivenMemory}\n"
        # f"Current Attack memory: {currAttMemory} -> {printMoves([currAttMemory])}\n\n\n")
