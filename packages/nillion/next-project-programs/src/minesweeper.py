from nada_dsl import *

def nada_main():
    miner = Party(name="Miner")
    # minesweeper = Party(name="Minesweeper")
    my_int1 = SecretInteger(Input(name="my_int1", party=miner))
    my_int2 = SecretInteger(Input(name="my_int2", party=miner))

    grid = []
    index = Integer(1)

    for r in range(3):
        temp = []
        for c in range(3):
            res = (my_int1 >= index).if_else((my_int1 <= index).if_else(Integer(99), Integer(0)), Integer(0))
            res += (my_int2 >= index).if_else((my_int2 <= index).if_else(Integer(99), Integer(0)), Integer(0))
            temp.append(res)
            index += Integer(1)
            
        grid.append(temp)


    targetR = 1
    targetC = 1

    count = Integer(0)

    ## Up
    count += (grid[targetR - 1][targetC] >= Integer(99)).if_else((grid[targetR - 1][targetC] <= Integer(99)).if_else(Integer(1), Integer(0)), Integer(0))
    ## Down
    count += (grid[targetR + 1][targetC] >= Integer(99)).if_else((grid[targetR + 1][targetC] <= Integer(99)).if_else(Integer(1), Integer(0)), Integer(0))
    ## Left
    count += (grid[targetR][targetC - 1] >= Integer(99)).if_else((grid[targetR][targetC - 1] <= Integer(99)).if_else(Integer(1), Integer(0)), Integer(0))
    ## Right
    count += (grid[targetR][targetC + 1] >= Integer(99)).if_else((grid[targetR][targetC + 1] <= Integer(99)).if_else(Integer(1), Integer(0)), Integer(0))

    grid[targetR][targetC] = count

    outputs: list[Output] = []

    for i in range(3):
        for j in range(3):
            outputs.append(Output(grid[i][j], "my_output" + str(i) + str(j), miner))
    
    return outputs