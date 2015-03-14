class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    # http://www.cnblogs.com/zuoyuan/p/3699384.html
    def fourSum(self, num, target):
        n = len(num)
        dict = {}
        res = set()

        if n < 4 : 
        	return []
        num.sort()
        for i in range(n) :
        	for j in range(i + 1, n) :
        		if num[i] + num[j] not in dict :
        			dict[num[i] + num[j]] = [(i, j)]
        		else:
        			dict[num[i] + num[j]].append((i, j))

       	for i in range(n) :
       		for j in range(i + 1, n - 2) :
       			t = target - num[i] - num[j]
       			if t in dict:
       				for k in dict[t] :
       					if k[0] > j:
       						res.add((num[i], num[j], num[k[0]], num[k[1]]))
       	return [list(i) for i in res]