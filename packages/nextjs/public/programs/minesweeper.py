from nada_dsl import *

def nada_main():
    miner = Party(name="Miner")
    my_int1 = SecretInteger(Input(name="my_int1", party=miner))
    my_int2 = SecretInteger(Input(name="my_int2", party=miner))

    grid: list[SecretInteger] = []
    grid.append(my_int1 - my_int2)

    return [Output(grid[0], "my_output", miner)]