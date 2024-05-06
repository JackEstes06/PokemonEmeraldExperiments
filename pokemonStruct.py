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

class Pokemon:
    # TODO stub out structed class
    pass