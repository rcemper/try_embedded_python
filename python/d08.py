def p1():
    with open('../stream/input08.txt', 'r') as f:
        code = [(op, int(n)) for op, n in (line.split(' ') for line in f)]

        accumulator = 0
        index = 0
        visited = set()
        while index not in visited:
            visited.add(index)
            if code[index][0] == 'acc':
                accumulator += code[index][1]
                index += 1
            elif code[index][0] == 'jmp':
                index += code[index][1]
            elif code[index][0] == 'nop':
                index += 1
            else:
                raise Exception(f'Unknown code: {code[index][0]} at index {index}')
 #       print(f'Part 1: {accumulator}')
        return accumulator

def p2():
    with open('../stream/input08.txt', 'r') as f:
        code = [(op, int(n)) for op, n in (line.split(' ') for line in f)]

        # Init graph
        graph = {}  # log the preceding node(s) for each node
        for i in range(len(code) + 1):  # + 1, because we're interested in the node after the code
            graph[i] = []

        # Collect links
        for i in range(len(code)):
            if code[i][0] == 'acc' or code[i][0] == 'nop':
                graph[i+1].append(i)
            elif code[i][0] == 'jmp':
                graph[i + code[i][1]].append(i)
            else:
                raise Exception(f'Unknown code: {code[i][0]} at index {i}')

        # Collect all the nodes connected to the endpoint
        visited = set()
        connected_to_end = [len(code)]
        for node in connected_to_end:
            if node not in visited:
                visited.add(node)
                connected_to_end.extend(graph[node])

        # Run the code. For each nop or jmp, check if changing would land us on a node connected to the end.
        accumulator = 0
        index = 0
        connected = False
        while index != len(code):
            if code[index][0] == 'acc':
                accumulator += code[index][1]
                index += 1
            elif code[index][0] == 'jmp':
                if not connected and (index + 1) in connected_to_end:
                    if __name__ == '__main__': 
                        print(f'\t\tChange line {index} jmp -> nop')
                    index += 1
                    connected = True
                else:
                    index += code[index][1]
            elif code[index][0] == 'nop':
                if not connected and (index + code[index][1]) in connected_to_end:
                    print(f'\t\tChange line {index} nop -> jmp')
                    index += code[index][1]
                    connected = True
                else:
                    index += 1
            else:
                raise Exception(f'Unknown code: {code[index][0]} at index {index}')
#        print(f'Part 2: {accumulator}')
        return accumulator

if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()       