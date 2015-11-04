from collections import Counter

class Solution(object):

    # window
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # init
        ans = list()
        dic = Counter(words)
        c = len(words)
        l = len(words[0])
        for idx, word in enumerate(words):
            dic[word] = idx + 1

        targetSum = 0
        for word in words:
            targetSum += dic[word]

        
        # main loop
        length = len(s)
        window_len = c * l
        end = length - window_len + 1
        for i in range(l):
            totalSum = 0
            head = i
            tail = head
            cur_c = 0
            while head <+ end:
                if cur_c < c:
                    ss = s[tail: tail + l]
                    val = dic.get(ss, 0)
                    tail += l
                    if val > 0:
                        totalSum += val
                        cur_c += 1
                    else:
                        totalSum = 0
                        cur_c = 0
                        head = tail
                else:
                    ss = s[head: head + l]
                    val = dic.get(ss, 0) # it must be greater than 0
                    totalSum -= val
                    cur_c -= 1
                    head += l

                if cur_c == c and totalSum == targetSum:
                    ans.append(head)

        return ans



    def findSubstring_bf2(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # init
        ans = list()
        dic = Counter(words)
        c = len(words)
        l = len(words[0])
        for idx, word in enumerate(words):
            dic[word] = idx + 1

        targetSum = 0
        for word in words:
            targetSum += dic[word]

        
        # main loop
        length = len(s)
        end = length - c * l + 1
        for i in range(end):
            # search
            totalSum = 0
            for j in range(c):
                pos = i + j * l
                ss = s[pos: pos + l]
                val = dic.get(ss, 0)
                if val > 0:
                    totalSum += val
                else:
                    break
                if j == c - 1 and totalSum == targetSum:
                    ans.append(i)

        return ans



    def getHash(self, s, c, l):
        primes = [36151, 36161, 36187, 36191, 36209, 36217, 36229, 36241, 36251, 36263, 36269, 36277, 36293, 36299, 36307, 36313, 36319, 36341, 36343, 36353, 36373, 36383, 36389, 36433, 36451, 36457, 36467, 36469, 36473, 36479]
        sum = 0
        for i in range(c):
            u = 1
            for j in range(l):
                u *= ord(s[i * l + j]) * primes[j]
            sum += u

        return sum

    
    def findSubstring_hash(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        # init
        ans = list()
        length = len(s)
        c = len(words)
        l = len(words[0])
        s_words = ""
        for word in words:
            s_words += word
        targetHash = self.getHash(s_words, c, l)

        # search
        for i in range(length - c * l + 1):
            curHash = self.getHash(s[i: i + c * l], c, l)
            if curHash == targetHash:
                ans.append(i)

        return ans

        





    #brute force
    def findSubstring_bf1(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # init
        ans = list()
        dictionary = dict()
        #assert len(words) >= 1
        c = len(words)
        l = len(words[0])
        for word in words:
            dictionary[word] = dictionary.get(word, 0) + 1
        
        # main loop
        length = len(s)
        for i in range(length):
            if i + c * l >= length:
                break
            # refresh
            dic = dictionary.copy()
            # search
            for j in range(c):
                pos = i + j * l
                if pos < length:
                    if dic.get(s[pos: pos + l], 0) > 0:
                        dic[s[pos: pos + l]] -= 1
                        #print dic[s[i: l]]
                    else:
                        break
                else:
                    break
                if j == c - 1:
                    ans.append(i)

        return ans


#s = "barfoothefoobarman"
#words = ["foo", "bar"]
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
sol = Solution()
print sol.findSubstring(s, words)


