def find_ways(graph, start, end, way=[]):
    way = way + [start]
    if start == end:
        return [way]
    if start not in graph:
        return []
    all_ways = []
    for neighbor in graph[start]:
        if neighbor not in way:
            ways = find_ways(graph, neighbor, end, way)
            for new_way in ways:
                all_ways.append(new_way)
    return all_ways
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
all_ways = find_ways(graph, start, end)
print("Все найденные пути:")
for way in all_ways:
    print(way)