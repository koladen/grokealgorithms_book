# ПОИСК В ШИРИНУ

from collections import deque

# Формируем граф
graph = dict()
graph ["you"] = [("alice", 0), ("bob", 0), ("claire", 0)] # цифра ы тапле - уровень в графе
graph["bob"] = [("anuj", 1),  ("peggy", 1)]
graph["alice"] = [("peggy", 1)]
graph["claire"] = [("thom", 1),  ("jonny", 1)]
graph["anuj"] = [("zal", 2)]
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
graph["zal"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name] # Добавляем в очередь всех, начиная с name
    searched = [] # Тут сохраняем тех кого уже искали
    while search_queue:
        item = search_queue.popleft() # выталкиваем первого из очереди
        person = item[0]
        level = item[1]
        if person not in searched:
            if person_is_seller(person): # если узел удовлетворяет условию
                print(person + " is а mango seller! Level = " + str(level))
                path = [person]
                path = get_path(item[0], path) # тут строим полный путь в графе от корня, до того, кот удовлетворяет
                print(list(reversed(path)))    #  условию
                return True
            else:
                search_queue += graph[person] # если не удовлетворяет, тогда добавляем в очередь всех потомков узла
                searched.append(person) # добавляем в список тех, кого искали
    return False


def person_is_seller(person):
    return 'zzz' in person


def get_path(item, path):
    my_list = ''
    for key, value in graph.items():
        if value:
            for j in value:
                if item in j[0]:
                    my_list = key
                    break
    if not my_list:
        return path
    else:
        path.append(my_list)
        return get_path(my_list, path)


# search('you')

# АЛГОРИТМ ДЕЙКСТРЫ

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost_node = None
    # for node in costs:
    #     cost = costs[node]
    #     if cost < lowest_cost and node not in processed:
    #         lowest_cost = cost
    #         lowest_cost_node = node
    items = [key for key, value in costs.items() if key not in processed]
    if items:
        lowest_cost_node = min(items, key=lambda x: costs[x])

    return lowest_cost_node


def find_path(node, path):
    if parents[node] == 'start':
        path.append(parents[node])
        return path
    path.append(parents[node])
    return find_path(parents[node], path)


node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

path = ['fin']
print(list(reversed(find_path('fin', path))))
