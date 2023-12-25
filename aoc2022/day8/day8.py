def day8():
    tree_array = []
    part1 = 0
    part2 = 0
    with open('day8/inputDay8.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line_to_list = [*line.rstrip()]
            tree_array.append(line_to_list)

        for r in range(len(tree_array)):
            for c in range(len(tree_array[r])):
                k = tree_array[r][c]
                if all(tree_array[r][x] < k for x in range(c)) or all(tree_array[r][x] < k for x in range(c + 1, len(tree_array[r]))) or all(tree_array[x][c] < k for x in range(r)) or all(tree_array[x][c] < k for x in range(r + 1, len(tree_array))):
                    part1 += 1

        for r in range(len(tree_array)):
            for c in range(len(tree_array[r])):
                k = tree_array[r][c]
                L = R = U = D = 0
                for x in range(c - 1, -1, -1):
                    L += 1
                    if tree_array[r][x] >= k:
                        break
                for x in range(c + 1, len(tree_array[r])):
                    R += 1
                    if tree_array[r][x] >= k:
                        break
                for x in range(r - 1, -1, -1):
                    U += 1
                    if tree_array[x][c] >= k:
                        break
                for x in range(r + 1, len(tree_array)):
                    D += 1
                    if tree_array[x][c] >= k:
                        break
                part2 = max(part2, U * D * L * R)



                        
    print(part1)
    print(part2)

day8()