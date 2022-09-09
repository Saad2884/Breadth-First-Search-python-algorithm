
# graph = {
#     'F' : ['B' , 'G'],
#     'B' : ['A' , 'D'],
#     'G' : ['I'],
#     'A' : [],
#     'D' : ['C' , 'E'],
#     'I' : ['H'],
#     'C' : [],
#     'E' : [],
#     'H' : []
# }

# visited = [0]
# queue = [0]

# def bfs(visited, graph, node):
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         current = queue.pop(0)
#         print (current, end = " ")

#         for neighbour in graph[current]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)

# bfs(visited, graph, 'F')




graph = {
    'S' : ['Q','W','T'],
    'Q' : ['W','R'],
    'W' : ['T','G'],
    'T' : ['G'],
    'R' : ['W','G'],
    'G' : []
}
 
visited = []
queue = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        current = queue.pop(0)
        print (current, end =" ")
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited, graph, 'S')


# graph = {
#     'F' : ['B' , 'G'],
#     'B' : ['A' , 'D'],
#     'G' : ['I'],
#     'A' : [],
#     'D' : ['C' , 'E'],
#     'I' : ['H'],
#     'C' : [],
#     'E' : [],
#     'H' : []
# }
# visited = []
# def dfs(visited, graph, node):
#     if node not in visited:
#         print(node, end=" ")
#         visited.append(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)

# dfs(visited, graph, 'F')


# graph = {
#     'F' : ['B' , 'G'],
#     'B' : ['A' , 'D'],
#     'G' : ['I'],
#     'A' : [],
#     'D' : ['C' , 'E'],
#     'I' : ['H'],
#     'C' : [],
#     'E' : [],
#     'H' : []
# }
# visited = []
# n = input('Enter the number of levels : ')
# def dfs(visited, graph, node, level):
#     if node not in visited:
#             print(node, end=" ")
#             visited.append(node)
#             level += 1
#             for level in n:
#                 for neighbour in graph[node]:
#                     dfs(visited, graph, neighbour, level)

# dfs(visited, graph, 'F', n)