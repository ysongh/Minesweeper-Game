from nada_dsl import *

def nada_main():
    miner = Party(name="Miner")
    my_int1 = SecretInteger(Input(name="my_int1", party=miner))
    my_int2 = SecretInteger(Input(name="my_int2", party=miner))

    grid = [
        [
            my_int1 + my_int2 + Integer(i) for i in range(3)
        ]
        for j in range(3)    
    ]

    return [
        Output(grid[0][i], "my_output" + str(i), miner)
        for i in range(3)
    ]