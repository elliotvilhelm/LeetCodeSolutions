class HitCounter:

    def __init__(self):
        self.hits = [(0, 0)] * 300
        

    def hit(self, timestamp: int) -> None:
        index = (timestamp-1) % 300
        t, c = self.hits[index]
        
        if timestamp - t < 300:  # within 5 min
            self.hits[index] = (timestamp, c+1)
        else:
            self.hits[index] = (timestamp, 1)
            
    def getHits(self, timestamp: int) -> int:
        hits = 0
        for t,c in self.hits:
            if timestamp - t < 300:
                hits += c
        return hits
            
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)