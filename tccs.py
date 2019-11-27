from chess import isvalid
def main():
    grid=readasolution()
    if isvalid(grid):
        print("Valid solution")
    else:
        print("you failed")
def readasolution():
    print("enter a sudoku solution")
    grid=[]
    for i in range(9):
        line=input( ).strip( ).split( )
        grid.append([eval(x) for x in line])
    return grid
main()
