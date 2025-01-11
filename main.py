from pycatan import Game
from pycatan.board import RandomBoard

import random

game = Game(RandomBoard())

pOne = game.players[0]
settlement_coords = game.board.get_valid_settlement_coords(player = pOne, ensure_connected = False)
game.build_settlement(player = pOne, coords = random.choice(list(settlement_coords)), cost_resources = False, ensure_connected = False)
print(game.board)
