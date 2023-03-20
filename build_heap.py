# python3
import os

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    abc=len(data) 
    for i in range (abc//2,-1,-1):
     maz(data, i, swaps)
    return swaps

    def maz(data, i, swaps):
    abc = len(data)
    min_inde = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < abc and data[left] < data[min_inde]:
        min_inde = left
    if right < abc and data[right] < data[min_inde]:
        min_inde = right
    if min_inde != i:
        swaps.append((i, min_inde))
        data[i], data[min_inde] = data[min_inde], data[i]
        maz(data, min_inde, swaps) 
    


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    inp = input()
    if "I" in inp:

    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    
    elif "F" in inp
    file = input()
        find = './tests/'
        file2 = os.path.join(find, file)
        with open(file2, mode="r") as file:
         n = int(file.readline())
            data = list(map(int, file.readline().split()))
    swaps = build_heap(data)

    

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
