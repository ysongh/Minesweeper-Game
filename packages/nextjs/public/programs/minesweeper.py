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

    outputs: list[Output] = []

    for i in range(3):
        for j in range(3):
            outputs.append(Output(grid[i][j], "my_output" + str(i) + str(j), miner))
    
    return outputs