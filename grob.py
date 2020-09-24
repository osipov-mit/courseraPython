def GetResult(villages: list, shelters: list):
    result = list(range(len(villages)))
    indexShelter = 0
    for i in villages:
        dist = abs(i[1] - shelters[indexShelter][1])
        while indexShelter < len(shelters) - 1:
            if abs(shelters[indexShelter + 1][1] - i[1]) >= dist:
                result[i[0] - 1] = shelters[indexShelter][0]
                break
            else:
                indexShelter += 1
                dist = abs(i[1] - shelters[indexShelter][1])
        if indexShelter == len(shelters) - 1:
            result[i[0] - 1] = shelters[indexShelter][0]
    return result


def GetSortedListTuples(a: list):
    result = []
    for i in range(len(a)):
        result.append((i + 1, a[i]))
    return sorted(result, key=lambda dist: dist[1])


n = int(input())
villages = GetSortedListTuples(list(map(int, input().split())))
m = int(input())
shelters = GetSortedListTuples(list(map(int, input().split())))
print(*GetResult(villages, shelters))
