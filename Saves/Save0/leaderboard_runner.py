from __builtins__ import *

_PROGRAMS = {
    Leaderboards.Fastest_Reset: "l_reset",

    Leaderboards.Hay: "l_hay",  # 04:16.888
    Leaderboards.Hay_Single: "l_hay_single",  # submitted 04:32.809
    Leaderboards.Wood: "l_wood",
    Leaderboards.Wood_Single: "l_wood_single",  # submitted 48:41.783
    Leaderboards.Cactus: "l_cactus", # submitted 00:50:945
}


def run(leaderboard: Leaderboard):
    global _PROGRAMS
    leaderboard_run(leaderboard, _PROGRAMS[leaderboard], 128)

run(Leaderboards.Fastest_Reset)
