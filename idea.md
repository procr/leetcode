基础算法复习：
排序。

复习各种数据结构：
堆
BST
红黑树
平衡树
。。




一些临时困惑：
1. 如果classB继承了A的public，那么如果A的public用了A自己的private内容，这时候B是什么状态？
2. 析构函数的时候是先自己还是先父类？
 - 先调用派生类的析构函数，再调用基类析构函数

3. java gc怎么做的，final关键字
4. 项目里碰到最困难的东西，怎么解决的
5. c语言一些考点
6. wait()&notify()怎么用、stream和reader





要熟悉的一些东西：
java c++ python中hashmap，list，set等的常见写法。。。
python对list的一些index操作。比如-1什么的。
python的{}dict

设计模式：单例(多线程如何安全？)，工厂？


448. Find All Numbers Disappeared in an Array
tag：easy，array
题意：一个应该是1，2，3...n的数组，有的元素出现了两次，有的元素没有出现过。找出所有没出现过的元素。O(n)时间和O(1)空间。
解法：遍历一遍数组，然后把元素a[i]作为下标，找到a[a[i]]，并且让其值成为负数（注意两次负数还是要为负数，如果a[i]已经是负数的时候，作为下标之前先取绝对值）。最后再遍历一遍数组，如果发现有元素a[i]是正数，表明i没有出现过。

136. Single Number
tag：easy，hash table, bit manipulation
题意：一个数组，所有元素都出现了两次，除了其中一个元素只出现一次，找出他。
解法：简单就用xor就好了

104. Maximum Depth of Binary Tree
tag：easy，tree，dfs
题意：给一棵二叉树，返回高度。
解法：深搜，h(node) = max(h(left_son), h(right_son)) + 1

[*]371. Sum of Two Integers
tag: easy, bit manipulation
题意：计算a+b，但是不能用 + 以及 -
解法：利用c = a^b记录a和b不同的位，利用d = (a&b) << 1 来记录进位，所以a+b等价于c+d。一直循环直到d等于0（所有的进位都完成）

389. Find the Difference
tag: easy, hash table, bit manipulation
题意：有两个字符串s和t，t是由s随机洗乱之后再加上额外一个字符组成的，例如s=abc，t=baec。找出额外添加的字符，即e
解法：直接用xor，或者用ord和chr先转化成数字，然后在做xor操作。一行python代码：
chr(reduce(operator.xor, map(ord, s + t)))

258. Add Digits
tag: math
题意：给一个数字，不停地把各个位相加，如38 -> 3+8=11 -> 1+1=2, 最后返回2, 不用循环和递归，在time O(1)完成。
解法：digital root。数学题。

12345 =  1 × 10,000 + 2 × 1,000 + 3 × 100 + 4 × 10 + 5，并且还可以写成：
12,345 = 1 × (9,999 + 1) + 2 × (999 + 1) + 3 × (99 + 1) + 4 × (9 + 1) + 5， 即：
12,345 = (1 × 9,999 + 2 × 999 + 3 × 99 + 4 × 9) + (1 + 2 + 3 + 4 + 5).

所以  12345 mod 9 = (1+2+3+4+5) mod 9

所以原题想要的值，就是n mod 9（corner case：当n=0，返回0；当mod 9之后为0，返回9）


226. Invert Binary Tree
tag: 二叉树，homebrew作者被google拒的时候碰到的题目
题意：把二叉树左右儿子交换。
题解：简单递归



492. Construct the Rectangle
tag: 模拟
题意：给一个长方体面积，给出一个长宽的值，使得他们之间的差最小，并且面积刚好等于给定的面积
题解：先求一个中间值。如果能除的尽，就可以算出另一个边。如果除不尽，就减1，然后继续上面步骤。


530. Minimum Absolute Difference in BST
tag: BST
题意：给出一个BST中任意两个节点差最小的值。
题解：inorder traverse. 由于遍历的顺序是先左子树，然后根节点，然后右子树。这样从左子树遍历到右子树的prev一定是左子树最大的那个。同理，从根节点遍历到右子树，一定是从右子树最小的那个开始遍历的。由于BST的特点，按照这个方式遍历实际上就是按照从小到大的顺序。所以用prev记录上一个节点，然后相减看看是不是min就行了。。。
public class Solution {
    int min = Integer.MAX_VALUE;
    Integer prev = null;
    
    public int getMinimumDifference(TreeNode root) {
        if (root == null) return min;
        
        getMinimumDifference(root.left);
        
        if (prev != null) {
            min = Math.min(min, root.val - prev);
        }
        prev = root.val;
        
        getMinimumDifference(root.right);
        
        return min;
    }
    
}




506. Relative Ranks
tag：数组
题意：给一个数组（没有重复的值）。然后返回一个数组，里面的值是原始数组的排序后的下标（即排在第几位）。
题解：可以直接两重循环，对每一个a[i]，算出数组中有几个数是比他大的，这样他就排第几。
map(dict(zip(sort, rank)).get, nums)

map的构造：
{v : k for k, v in enumerate(sorted(nums, reverse=True))}




283. Move Zeroes
tag: array,  tow pointers
题意：一个数组，把所有的0提出来放到最后，别的元素相对位置不变，in place修改。
题解：两个指针，一个指向当前最前面的0，一个指向最前面的非0，然后交换。然后重复。有点像对所有0做bubble up操作。


167. Two Sum II - Input array is sorted
tag：array，two pointers，binary search
题意：给一个排好序的上升数组，给一个和数，然后返回数组中两个下标，对应的值加起来等于这个和。
题解：先让两个指针在头和尾，然后二分搜。


455. Assign Cookies
tag：greedy
题意：小孩分饼干。两个数组，第一个数组是小孩的需求，第二个是饼干的大小。每个小孩只能给一个，但是大小必须要大于他的需求。问最多能满足几个小孩。
题解：两个数组各一个指针，当能分配，就都往后移动。不能分配，就把饼干的指针往后移动。直到两个数组其中一个指针出界。

453. Minimum Moves to Equal Array Elements
tag：math
题意：一个数组，长度为n。每一次move可以往n-1个位置做一次加一操作，问多少次能使得所有的元素变得一样大
题解：往n-1位置做加一，和往n个位置都做加一，然后对某一个元素做减一是等价的。并且对所有元素都加一，并不会改变他们之间的相对高度差，所以直接做减一就行。减去的次数，就是最底层的高度与别的元素的差值的和。

383. Ransom Note
tag：string
题意：给两个string，第一个是ransom note，是要被重构的。第二个是magazine，字符的来源。magazine的每个字符只能被用一次。问能否构造出ransom note？
题解：用一个map或者长度为26的数组来存magazine每个字符出现几次，然后在循环一下ransom note，没用一次就减掉一，如果某个字符变成负数就返回false。如果构造出来就返回true。

404. Sum of Left Leaves
tag：tree
题意：求二叉树中所有左叶子的和。
题解：递归：如果左子树已经到头，则等于该值加上右子树应用上sub probelm。否则就是左子树的sub + 右子树的sub。

349. Intersection of Two Arrays
tag：binary search，hash table，two pointers，sort
题意：找两个数组的交集，出现两次也只取一次。
题解：
解法一：先排序，然后选择比较短的一个数组循环，用二分法找另一个数组是否存在相同的值。
解法二：把一个数组放入hash table，然后循环第二个数组，如果碰撞则加入返回数组。


350. Intersection of Two Arrays II
tag：binary search，hash table，two pointers，sort
题意：找两个数组交集，exactly的次数。
题解：字典存次数，碰撞减去一并且加入ans数组。看看java的hashmap和arraylist用法。。。

public int[] intersect(int[] nums1, int[] nums2) {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    ArrayList<Integer> result = new ArrayList<Integer>();
    for(int i = 0; i < nums1.length; i++)
    {
        if(map.containsKey(nums1[i])) map.put(nums1[i], map.get(nums1[i])+1);
        else map.put(nums1[i], 1);
    }

    for(int i = 0; i < nums2.length; i++)
    {
        if(map.containsKey(nums2[i]) && map.get(nums2[i]) > 0)
        {
            result.add(nums2[i]);
            map.put(nums2[i], map.get(nums2[i])-1);
        }
    }

   int[] r = new int[result.size()];
   for(int i = 0; i < result.size(); i++)
   {
       r[i] = result.get(i);
   }

   return r;
}





504. Base 7
tag：进制转化
题意：把数字转化成7进制的字符串
解法：除以7 mod7

387. First Unique Character in a String
tag：数组
题意：找出字符串中第一个在整个字符串中只出现一次的字符的下标
题解：先遍历一遍找到所有出现的次数，放入26长度的数组。然后在遍历一次，如果有次数是1的就返回。
def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.Counter(s)
        ans = -1
        for x, c in enumerate(s):
            if d[c] == 1:
                ans = x
                break
        return ans



121. Best Time to Buy and Sell Stock
tag：数组
题意：给每天股票的价格，只能买一次卖一次，卖的时间要在买的时间之后，给出最大差价。
题解：从左往右扫描，并且每次标记一下当前是否是最小价钱min_price。然后每次都算一下当前价钱和min_price的差价是否为max_diff。由于是从左往右，所以保证之前记录的min_price对之后都有效。



122. Best Time to Buy and Sell Stock II
tag: array, greedy
题意：不限次数的买卖股票。求最大收益。
题解：题目即为找到所有的不下降序列的最大值与最小值的差。简单来说，只要当price[i]>price[i-1]就能计入收益当中。



123. Best Time to Buy and Sell Stock III
tag:好像是最难的，maybe next time

&……（&……%￥&*……*&）（&（*&%*……（&……（&……%￥&*……*&）（&（*&%*……（&……（&……%￥&*……*&）（&（*&%*……（&……（&……%￥&*……*&）（&（*&%*……（&……（&……%￥&*……*&）（&（*&%*……（&……（&……%￥&*……*&）（&（*&%*……（&……（&……%￥&*……*&）（&（*&%*……（



168. Excel Sheet Column Title
tag：math
题意：    
	1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
题解：把十进制转化成26进制。。。



171. Excel Sheet Column Number
tag：math
题意：
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
题解：把26进制转成10进制




237. Delete Node in a Linked List
tag：linked list
题意：给一个单向linked list中的一个节点 node，删掉这个node 但是不破坏源list别的node
1 -> 2 -> 3 -> 4 -> 5， 给3，那么1 -> 2 -> 4 -> 5
题解：虽然没有办法拿到node 2，然是可以把4给顶替掉。把3的val改成4的val，把3的next换成5。这样4就被隔空了。。。什么jb。。。


100. Same Tree
tag：tree，dfs
题意：给两个二叉树，判断是否一样。
题解：递归。。。如果当前都为null，则true。如果一个null一个非null，则false。如果当前val一样，则继续递归左右子树。。



169. Majority Element
tag： Array， Divide and Conquer， Bit Manipulation
题意：给一个数组，找出majority element，即more than ⌊ n/2 ⌋ times.
题解：
1. 因为一定会有大于⌊ n/2 ⌋的数。遍历数组，维护一个counter和当前的number，当a[i]等于number，counter加一，否则减一。当counter等于0的时候，number就换成当前新的a[i]。
2. 由于都是32位的数，可以统计每一个bit，用一个长度为32的数组计算每一个bit出现的次数。最后遍历这个32长度的数组，提取出次数大于⌊ n/2 ⌋的bit，然后重构出数字。。。
3. 用hash table统计每个数字出现的次数，然后再遍历一次，取出大于⌊ n/2 ⌋的数字



242. Valid Anagram
tag：hash table, sort
题意：给两个字符串，看看里面的字符构成是否一样。
题解：排序之后比较即可。

409. Longest Palindrome
tag：hash table
题意：给一个字符串，对里面的字符可以重新挑选并且重组，组成最长的回文是多长。
题解：
我一开始以为必须要把所有同一个字符用完，实际上不用。所以可以支取偶数个总数是奇数的字符。然后回文最中间可以插一个奇数的川。
所以答案 = 字符串原始长度 - 某个字符总数是奇数的次数 + 如果出现过奇数就加一

217. Contains Duplicate
tag：array，hash table
题意：找出数组中是否有出现过两次的元素。
题解：len(nums) != len(set(nums))。或者用hash table，看某次插入的时候是否已经存在某个元素。或者排序，看相邻两个元素是否一样。

219. Contains Duplicate II
tag: array, hash table
题意：这次判断在下标长度为k的窗口里面，是否有duplicated number
题解：两个指针维护窗口，移动的时候需要把table中原来的删掉，加入新的。然后一样的判断。

220. Contains Duplicate III
tag: binary search tree
题意：这次判断在下标长度为k的窗口里面，是否有差别度为t的两个数。
题解：利用二叉搜索树，floor(n)是小于n但是最大的值，ceiling(n)是大于n但是最小的值。像上面一题一样，用两个指针维护好窗口，然后往BST里面插入节点（移动的时候删除最旧的节点），然后根据最近插入的那个节点，判断其floor与自己，或者自己与ceiling的差是不是满足t的条件。 Java的 treeset就是用BST实现的。


401. Binary Watch
tag：backtracking
题意:给binary watch中亮灯的个数n，放回所有可能的时间。
题解：回溯所有的combination。。。


12. Integer to Roman
tag：math，string
题意：如题
题解：先列所有的combination，然后再一个个减掉。。
int[] values = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
String[] strs = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};

StringBuilder sb = new StringBuilder();

for(int i=0;i<values.length;i++) {
    while(num >= values[i]) {
        num -= values[i];
        sb.append(strs[i]);
    }
}


13. Roman to Integer
tag：math，string
题意：如题
题解：注意要判断4，400，400，900这样的。就是IV，前面一个比后面一个小，必须先减掉1，才能加上5
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]




206. Reverse Linked List
tag：linked list
题意：反向单项链表
解法：用一个新的表头，然后把旧的表头指向的东西移过去，然后新表头指向移来的node，旧表头指向下一个准备被移动的。
可以用iteration 或者 recursion
public ListNode reverseList(ListNode head) {
    /* iterative solution */
    ListNode newHead = null;
    while (head != null) {
        ListNode next = head.next;
        head.next = newHead;
        newHead = head;
        head = next;
    }
    return newHead;
}

recursion的写法，就要用一个helper。。。参数第一个是旧表头，第二个是新表头，其实原理是一样的
public ListNode reverseList(ListNode head) {
    /* recursive solution */
    return reverseListInt(head, null);
}
private ListNode reverseListInt(ListNode head, ListNode newHead) {
    if (head == null)
        return newHead;
    ListNode next = head.next;
    head.next = newHead;
    return reverseListInt(next, head);
}




268. Missing Number
tag：array，math，bit manipulation
题意：从0 1 2 3 ...n 这n+1个元素中，抽取n个组成数组，找出没有放入的那个元素。
题解：
1. 直观感觉就是448. Find All Numbers Disappeared in an Array的方法来做就行了。就是把数组标记成负数，然后越界的那个元素单独用一个变量来存。。
2. 可以用xor。。。
3. 可以求0..n的和，然后减去数组的和，就知道少了哪个。。








535. Encode and Decode TinyURL
tag：hash table
题意：给一个长url，转换成短url，实现encode和decode两个函数
题解：
1. encode每碰到一个新的url就分配一个新的id给他，然后decode的时候就根据这个id来index数组
class Codec:

    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.urls) - 1)

    def decode(self, shortUrl):
        return self.urls[int(shortUrl.split('/')[-1])]
2. 上面方法有很多缺点，比如用户可以根据当前id直接知道整个库至少有多少个url。所以可以用到随机化。
来了一个新的长url，从a-z A-Z 0-9中任意选出6个字符作为短url，然后加入map中。
class Codec:

    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]





419. Battleships in a Board
tag：二维数组
题意：有一个地图，上面有‘·’和‘x’,其中x连成一个battleship，只能水平或者竖直一条。问一个有几个battleships
题解：以为要宽搜，但是好像不要。直接遍历这个二维数组，判断上面一个和或者左边一个不是墙壁以及不是‘x’，就说明这是一个新的battleship。



338. Counting Bits
tag：动归，bit
题意：给一个n，返回一个数组，表示1-n的二进制中1出现了几次。
题解：二进制中很好理解，像2 4 8 16这样的数组，会导致多一位，然后最高位之后的位和前面出现过的是一样的。
所以遍历，然后当i到达了一个新的2^k, 就把offset*2。
public int[] countBits(int num) {
    int result[] = new int[num + 1];
    int offset = 1;
    for (int index = 1; index < num + 1; ++index){
        if (offset * 2 == index){
            offset *= 2;
        }
        result[index] = result[index - offset] + 1;
    }
    return result;
}


513. Find Bottom Left Tree Value
tag：tree，dfs，bfs
题意：给一棵二叉树，返回深度最深的一层当中，最左边的节点的值。
题解：
bfs的话就一层一层搜，每次保存最左边的当做备选答案。
dfs的话，就一直以左边为第一个深入的节点，当达到最深的时候记录当前备选答案以及当前深度，如果有更深的就把备选答案换掉。



413. Arithmetic Slices
tag：数学题。
题意：问数组中有多少个长度大于二的等差数列。
题解：
1. 把原数组相邻的两两相减，然后得到一个新的数组，其实就是问，新数组中相同连续数字的各个slice中，可以有几种结合方式。用求和公式可以得到答案
public int numberOfArithmeticSlices(int[] A) {
    if(A == null || A.length < 3)
        return 0;
    int sum = 0;
    int len = 2;

    for(int i=2;i<A.length;i++) {

        // keep increasing the splice
        if(A[i] - A[i-1] == A[i-1] - A[i-2]) {
            len++;
        }
        else {
            if(len > 2) {
                sum += calculateSlices(len);
            }
            // reset the length of new slice
            len = 2;
        }
    }
    // add up the slice in the rear
    if(len>2)
        sum += calculateSlices(len);

    return sum;
}

private int calculateSlices(int n){
    return (n-1)*(n-2)/2;
}



406. Queue Reconstruction by Height
tag: greedy
题意：一个随机的数组，每个元素是一个pair（h，k），描述了一个人的身高h，以及这个人前面应该要有k个人的身高大于或等于他。让你用这个信息给数组排序。
题解：
第一种方法：n^2
1. 先选出k为0当中，身高最矮的，这个人一定排在第一个。
2. 根据刚刚已经出队列的人，更新之后的人的信息：如果有比他矮或者跟他一样矮的人，k值减去1
3. 在省下的人当中，再做第一步的选择，然后一直重复。

第二种方法：n^2
首先我们给队列先排个序，按照身高高的排前面，如果身高相同，则第二个数小的排前面。
这样排好序之后，排在最前面的身高最大的人一定已经满足了最后的k的约束，并且当后面的人插进来的时候，一定不会违背k的约束，因为他们的身高都比自己矮。
最后，根据每个元素的第二个数字，将其插入到res数组中对应的位置。





515. Find Largest Value in Each Tree Row
tag：tree，dfs，bfs
题意：找到二叉树中每一层最大的点。
题解：
bfs比较容易理解。
dfs的话也一样，用下标表示深度，每一次到一个新的节点就跟那个深度的下标的值比较一下。




442. Find All Duplicates in an Array
tag：array
题意：1 ≤ a[i] ≤ n (n = size of array), 找出所有出现两次的元素。
题解：好像做过，直接把对应的下标是a[i]的元素取相反数就好了


529. Minesweeper
tag：dfs，bfs
题意：完成扫雷点按某个键的模拟、
题解：模拟呗。。。还是看算法实现的完成度，算法上没有什么难的地方。



526. Beautiful Arrangement
tag: backtracking
题意：给一个n，数组元素是从1..n，当一个数组满足所有的i：a[i] % i == 0 or i % a[i] == 0，就成为Beautiful Arrangement，问一共有几种。
题解：递归+剪枝。
定义递归函数：helper(i, X):表示当前要放第i位，剩下的元素数组是X，简单方法就是一个个试就行了。
剪枝：因为当程序回溯回去，然后又回来之后，可能需要面对的helper(i, X)当中i和X可能和之前一模一样，这样就要白算好几次。可以全局放一个hashtable，然后把helper(i, X)中（i，X）作为key，这部分子集次数为value，然后保存下来。
代码：
cache = {}
class Solution(object):
    def countArrangement(self, N):
        def helper(i, X):
            if i == 1:
                return 1
            key = (i, X)
            if key in cache:
                return cache[key]
            total = 0
            for j in xrange(len(X)):
                if X[j] % i == 0 or i % X[j] == 0:
                    total += helper(i - 1, X[:j] + X[j + 1:])
            cache[key] = total
            return total
        return helper(N, tuple(range(1, N + 1)))



495. Teemo Attacking
tag：array
题意：给一些时间点，以及一个duration，表示一个时间点+duration这段时间内，某人属于中毒状态。（可能会有覆盖）。问总的中毒时长。
题解：遍历数组每一个元素，如果当前元素+duration超过了下一个元素，那么ans+=两个元素的差，如果没超过，ans+=duration。




508. Most Frequent Subtree Sum
tag: tree，hashtable
题意：算出一棵树的所有子树的和，然后返回出现最多的几个和。
题解：简单的树遍历和hashtable使用，看看java代码吧：
public class Solution {
    int max = 0;
    public int[] findFrequentTreeSum(TreeNode root) {
        if(root==null) return new int[0];
        Map<Integer, Integer> map = new HashMap<>();
        helper(root, map);
        List<Integer> res = new LinkedList<>();
        for(Map.Entry<Integer, Integer> me: map.entrySet()){
            if(me.getValue()==max) res.add(me.getKey());
        }
        return res.stream().mapToInt(i->i).toArray();
    }
    
    private int helper(TreeNode n, Map<Integer, Integer> map){
        int left = (n.left==null) ? 0 : helper(n.left, map);
        int right = (n.right==null) ? 0 : helper(n.right, map);
        int sum = left + right + n.val;
        map.put(sum, map.getOrDefault(sum,0)+1);
        max = Math.max(max, map.get(sum));
        return sum;
    }
}



462. Minimum Moves to Equal Array Elements II
tag：math
题意：给定非空整数数组，求使得数组中的所有元素均相等的最小移动次数，一次移动是指将某个元素加1或者减1。
题解：之前的I，是对n-1个做减一，和这题不一样。这题实际上就是求：数组各元素与中位数差的绝对值之和。
所以先排序，然后在算头尾两个数相减就好了（相减的结果就是这两个数都一起到中位数的距离）




296. Best Meeting Point （locked）
tag：array
题意：给一个地图，上面有1和0，1表示有人0表示没人，问地图上某个点到所有人的距离最短之和是多少。
题解：
这道题和上面这题有点类似，考虑二维的直线的话，当点处于两个点之间，距离值和最短（等于两个点的距离），如果是很多点都在直线上，到所有点距离最短，也就是在中位数那个点上。
然后因为在这个地图上求和是曼哈顿距离（只能走水平或者竖直），所以可以把所有点投射到水平二维和竖直二维上，分别求最短和，然后再把两个和相加。




451. Sort Characters By Frequency
tag：hash table
题意：根据字符出现的频率排序
题解：python的写法还是简便的一笔啊：
from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c1, c2 = Counter(s), {}
        for k,v in c1.items():
            c2.setdefault(v, []).append(k*v)
        return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])



137. Single Number II
tag：bit manipulation
题意：有一个数字只出现一次，别的出现三次，找出这个出现一次的。
题解：因为是int，所以是32位，用长度为32的数组，对于每一位，都记录出现的次数，然后取mod 3，最后的结果就是数组里的数重构一下。
这道题可以扩展为一个数只出现一次，别的出现k次。


260. Single Number III
tag：bit manipulation
题意：有2个数字出现一次，别的都出现2次，找出出现一次的两个数。
题解：对所有的数先xor，得到的结果去第一个非零位，bit = all_xor & -all_xor = all_xor & (~all_xor + 1)。
假设最后的两个数结果是a和b，对所有的数进行遍历，如果对应的那个bit是1就与a进行xor，如果bit是0就与b进行xor，那么别的数字出现两次一定都会一起在某一个组里面，然后两两抵消，最后只剩下出现一次的那个数。



238. Product of Array Except Self
tag：array
题意：给出一个数组的乘积，第i个数不参与结果的第i个输出。
题解：从两个方向分别算到最远的地方到当前的乘积是多少，然后最后左右两个方向相乘就好了。



347. Top K Frequent Elements
tag：hash，heap
题意：找出数组中出现频率最高的前k个元素
题解：
1.自己写的类似于hash + bucket sort。。。
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        c1, c2 = Counter(nums), {}
        for key, val in c1.items():
            c2.setdefault(val,[]).append(key)
        for i in range(len(nums), -1, -1):
            if i in c2:
                ans += c2[i]
                k -= len(c2[i])
                if k < 0:
                    ans = ans[:k]
                    return ans
                elif k == 0:
                    return ans

        return ans

2. 用堆：先用hashmap记录counter，然后维护一个大小为k的最小堆，超过之后就把第一个扔掉。然后最后整个堆就是答案。
public List<Integer> topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> counterMap = new HashMap<>();
    for(int num : nums) {
        int count = counterMap.getOrDefault(num, 0);
        counterMap.put(num, count+1);
    }
    
    PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> a.getValue()-b.getValue());
    for(Map.Entry<Integer, Integer> entry : counterMap.entrySet()) {
        pq.offer(entry);
        if(pq.size() > k) pq.poll();
    }
    
    List<Integer> res = new LinkedList<>();
    while(!pq.isEmpty()) {
        res.add(0, pq.poll().getKey());
    }
    return res;
}
如果用python就是这么短：

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = collections.Counter(nums)
        return [x[0] for x in c.most_common(k)]

后记：听石培涛说的一道面试题：问给1M内存，怎么找出1G的数组中前100个最大数字。答案就是也用一个最小堆来维护100个数。



139. Word Break
tag：dp，字典树（trie）
题意：给一个源字符串，给一个字典，问字符串能否切割成字典中若干个子串。
题解：用动态规划。f[i]表示从i到结尾是否是满足可切分的条件。初始化的时候，从最后往前遍历，表示i到末尾是否满足。之后二重循环，从后往前进行状态叠加。
当然，判断一个子串是否在一个字符串数组里面，可以用字典树来优化




503. Next Greater Element II

















        