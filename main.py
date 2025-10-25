class CountrySystem():
    def __init__(self, data):
        country, build, destroy = data.split(" ")
        country = country.split(",")
        build = build.split(",")
        destroy = destroy.split(",")
        n = len(country)
        self.length = n 
        self.country = [[0 for _ in range(n)] for _ in range(n)]
        self.build = [[None for _ in range(n)] for _ in range(n)]
        self.destroy = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.country[i][j] = int(country[i][j])
                self.build[i][j] = self.interpretCost(build[i][j])
                self.destroy[i][j] = self.interpretCost(destroy[i][j])
    def interpretCost(self, digit):
        num = ord(digit)
        if num >= ord('a') and num <= ord('z'):
            return num - ord('a') + 26
        if num >= ord('A') and num <= ord('Z'):
            return num - ord('A') 
        return -1 
    def optimizeCost(self):
        parent = [i for i in range(self.length)]
        rank = [0 for _ in range(self.length)]
        def find(i):
            return i if parent[i] == i else find(parent[i])
        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x == p_y: 
                return False
            else: 
                if rank[p_x] >= rank[p_y]:
                    rank[p_x] += 1
                    parent[p_y] = p_x
                else:
                    parent[p_x] = p_y
                return True
        def DSU(pairs):
            mst = 0
            for w, i, j in pairs:
                if union(i,j):
                    mst += w
            return mst
        pairs = []
        total_destroy_cost = 0
        for i in range(self.length):
            for j in range(i + 1, self.length):
                if self.country[i][j] == 1:
                    total_destroy_cost += self.destroy[i][j]
                    w = -self.destroy[i][j]
                else:
                    w = self.build[i][j]
                pair = (w, i, j)
                pairs.append(pair)
        pairs.sort(key= lambda x: x[0])
        mst = DSU(pairs)
        return mst + total_destroy_cost

def main():
    data = input()
    country_system = CountrySystem(data)
    cost = country_system.optimizeCost()
    print(cost)
    return 

if __name__ == "__main__":
    main()