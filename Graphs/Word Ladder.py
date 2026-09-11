class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0
        wordset = set(wordList)
        q = deque([(beginWord,1)])

        while q:
            word,steps = q.popleft()

            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordset:
                        q.append((newWord,steps+1))
                        wordset.remove(newWord)
        return 0



        