class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        neiMap = defaultdict(list)
        visited = set()
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                neiMap[pat].append(word)
        
        q = collections.deque()
        q.append(beginWord)
        visited.add
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pat = word[:i] + "*" + word[i+1:]
                    for nei in neiMap[pat]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res+=1
        
        return 0
            




        