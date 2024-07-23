class Solution:
    def similarPairs(self, words):
        set_of_words = []

        for word in words:
            set_of_words.append(set(list(word)))
        
        cnt = 0
        for i in range(len(set_of_words)-1):
            for j in range(i+1, len(set_of_words)):
                if set_of_words[i] == set_of_words[j]:
                    cnt +=1
        
        return cnt
