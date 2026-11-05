class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append([value,timestamp])        

    def get(self, key: str, timestamp: int) -> str:
        time_val_pair = self.hmap[key]

        l = 0
        r = len(time_val_pair)-1
        res = ""

        while l <= r:
            m = (l+r)//2

            if time_val_pair[m][1] <= timestamp:
                res = time_val_pair[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
        

        
