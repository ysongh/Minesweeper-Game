from nada_dsl import *

def nada_main():
    miner = Party(name="Miner")
    my_int1 = SecretInteger(Input(name="my_int1", party=miner))
    my_int2 = SecretInteger(Input(name="my_int2", party=miner))

    grid = []
    index = Integer(1)

    for r in range(3):
        temp = []
        for c in range(3):
            res = (my_int1 == index).if_else((my_int2 == index).if_else(Integer(99), Integer(99)), Integer(0))
            temp.append(res)
            index += Integer(1)
            
        grid.append(temp)

    outputs: list[Output] = []

    for i in range(3):
        for j in range(3):
            outputs.append(Output(grid[i][j], "my_output" + str(i) + str(j), miner))
    
    return outputs