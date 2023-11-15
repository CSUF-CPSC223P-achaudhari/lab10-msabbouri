# Mahdi Sabbouri
# 11/15
# main.py

"""main driver file"""

import bots

if __name__ == "__main__":
    print("INPUT  :", [])
    print("OUTPUT :", bots.bot_clerk([]))
    
    print("\nINPUT  :", ['104'])
    print("OUTPUT :", bots.bot_clerk(['104']))
    
    print("\nINPUT  :", ['106', '109', '102'])
    print("OUTPUT :", bots.bot_clerk(['106', '109', '102']))
    
    print("\nINPUT  :", ['103', '108', '102', '110', '106'])
    print("OUTPUT :", bots.bot_clerk(['103', '108', '102', '110', '106']))
    
    print("\nINPUT  :", ['106', '102', '108', '109', '103', '101', '110', '104', '107', '105'])
    print("OUTPUT :", bots.bot_clerk(['106', '102', '108', '109', '103', '101', '110', '104', '107', '105']))
