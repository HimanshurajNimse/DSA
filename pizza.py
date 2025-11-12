
def nearest_neighbor(dist, start=0):
    n = len(dist)
    visited = [False]*n
    route = [start]
    visited[start] = True
    total = 0.0
    cur = start

    for _ in range(n-1):
        nxt = None
        best = float('inf')
        for v in range(n):
            if not visited[v] and dist[cur][v] < best:
                best = dist[cur][v]
                nxt = v
        if nxt is None:  # no unvisited reachable node
            break
        route.append(nxt)
        visited[nxt] = True
        total += best
        cur = nxt

    return total, route

def read_matrix(n):
    print(f"Enter the {n}x{n} distance matrix (rows of {n} numbers, space separated).")
    mat = []
    for i in range(n):
        while True:
            row = input(f"Row {i} : ").strip().split()
            if len(row) != n:
                print(f"Please enter exactly {n} numbers.")
                continue
            try:
                mat.append([float(x) for x in row])
                break
            except:
                print("Invalid numbers — try again.")
    return mat

def main():
    n = int(input("Number of locations (including shop as node 0): ").strip())
    dist = read_matrix(n)
    cost, route = nearest_neighbor(dist, start=0)
    print("\nRoute visited (in order):", " -> ".join(map(str, route)))
    print("Total travel time (approx):", cost)
    print("\nNote: This uses nearest-neighbor heuristic. For small n an exact solver exists but is more complex.")

if __name__ == "__main__":
    
    dist = [
        [0, 10, 15, 20],   # 0 = shop
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    cost, route = nearest_neighbor(dist, start=0)
    print("Route:", route)
    print("Cost:", cost)

