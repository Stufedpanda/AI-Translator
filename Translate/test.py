class forbes:
    def __init__(self, param):
        pass

    def __getitem__(self, key):
        return key + 2
    
    def __len__(self):
        return 10
    
if __name__ == "__main__":
    f = forbes("asdf")
    print(f[3.5])
    print(len(f))