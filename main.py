class HashTable():
    def __init__(self):
        alphabet = list("abcdefghijklmnopqrtsuvwxyz")
        self.words = {key : "" for key in alphabet}
        self.status = {key: "never used" for key in alphabet}
        
    def insert(self, word: str):
        last = word[-1]
        if self.status[last] == "occupied":
            return 
        else:
            self.words[last] = word
            self.status[last] = "occupied"
        return 
    def deletion(self, word: str):
        last = word[-1]
        if self.words[last] == word:
            self.status[last] = "tombstone"
    def search(self, word: str):
        for key, value in self.words.items():
            if value == word:
                if self.status[key] == "occupied":
                    return True
        return False
            
    def print(self):
        data = []
        for key, status in self.status.items():
            if status == "occupied":
                data.append(self.words[key])
        print(" ".join(data))
        return 
def main():
    prompt = input()
    prompt = prompt.split()
    hashtable = HashTable()
    for action in prompt:
        if action[0] == "A":
            hashtable.insert(action[1:])
        elif action[0] == "D":
            hashtable.deletion(action[1:])
    hashtable.print()
    return 

if __name__ == "__main__":
    main()