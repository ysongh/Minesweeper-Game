from nada_dsl import *

def nada_main():
    miner = Party(name="Miner")
    # minesweeper = Party(name="Minesweeper")
    my_int1 = SecretInteger(Input(name="my_int1", party=miner))
    my_int2 = SecretInteger(Input(name="my_int2", party=miner))

    grid = []
    sweeperGrid = []
    minerIndex = Integer(1)
    sweeperIndex = Integer(1)

    for r in range(3):
        temp = []
        for c in range(3):
            res = (my_int1 >= minerIndex).if_else((my_int1 <= minerIndex).if_else(Integer(99), Integer(0)), Integer(0))
            temp.append(res)
            minerIndex += Integer(1)
            
        grid.append(temp)

    for r in range(3):
        temp = []
        for c in range(3):
            res = (my_int2 >= sweeperIndex).if_else((my_int2 <= sweeperIndex).if_else(Integer(77), Integer(0)), Integer(0))
            temp.append(res)
            sweeperIndex += Integer(1)
            
        sweeperGrid.append(temp)

    for r in range(3):
        for c in range(3):
            sweeperGrid[r][c] += (sweeperGrid[r][c] == Integer(77)).if_else(Integer(100),
                (grid[r][c] == sweeperGrid[r][c]).if_else(Integer(0), Integer(0)))

    outputs: list[Output] = []

    for i in range(3):
        for j in range(3):
            outputs.append(Output(grid[i][j], "miner_output" + str(i) + str(j), miner))

    for i in range(3):
        for j in range(3):
            outputs.append(Output(sweeperGrid[i][j], "minesweeper_output" + str(i) + str(j), miner))
    
    return outputs