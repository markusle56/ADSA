
NEVER_USED = 0
TOMBSTONE = 1
OCCUPIED = 2

class HashTable:
    def __init__(self):
        self.table = [(NEVER_USED, "") for _ in range(26)]

    def _idx(self, ch: str):
        return ord(ch) - ord('a')

    def _find_slot(self, key: str):
        start = self._idx(key[-1])
        i = start
        while True:
            status, k = self.table[i]
            if status == NEVER_USED:
                return (False, i)
            if status == OCCUPIED and k == key:
                return (True, i)
            i = (i + 1) % 26
            if i == start:
                return (False, start) 

    def search(self, key: str):
        found, _ = self._find_slot(key)
        return found

    def insert(self, key: str):
        if self.search(key):
            return
        start = self._idx(key[-1])
        i = start
        while True:
            status, _ = self.table[i]
            if status != OCCUPIED:   
                self.table[i] = (OCCUPIED, key)
                return
            i = (i + 1) % 26
            if i == start:
                return
       
    def delete(self, key: str):
        start = self._idx(key[-1])
        i = start
        while True:
            status, k = self.table[i]
            if status == NEVER_USED:
                return
            if status == OCCUPIED and k == key:
                self.table[i] = (TOMBSTONE, "")
                return
            i = (i + 1) % 26
            if i == start:
                return

    def output(self) -> str:
        return " ".join(k for (status, k) in self.table if status == OCCUPIED)

def main():
    prompt = input()
    prompt = prompt.split()
    hashtable = HashTable()
    for action in prompt:
        if action[0] == "A":
            hashtable.insert(action[1:])
        elif action[0] == "D":
            hashtable.delete(action[1:])
    print(hashtable.output())
    return 

if __name__ == "__main__":
    main()