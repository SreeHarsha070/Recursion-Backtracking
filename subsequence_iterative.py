# // In len of array is 'n':
# // number os subarrays :: "n(n+1)/2"
# //[1,2,3,4]
# // [1],[1,2].[1,2,3],[1,2,3,4],[2,3,4],[2],[2,3],[3,4],[3],[4]
# // all subarrays are subseqences
# // subsequences are :: [1,2],[1,3,4],[1,3],[2,3] etc== "2^n subsequences"
# // It is hard to generate all subsequences.
# // DP could be best possible approach.

# // 		Iterative approach for Subsequences:

# // 				Powerset Algorithm 

# // 		[1,2,3]
# //       0 1 2
# // 2^3
# // 0 - 000 - {}
# // 1 - 001 - [1]
# // 2 - 010 - [2]
# // 3 - 011 - [1,2]
# // 4 - 100 - [3]
# // 5 - 101 - [1,3]
# // 6 - 110 - [2,3]
# // 7 - 111 - [1,2,3]

# // Pseudo Code:
# // for(int i=0;i<2^n;i++){
# // 	for(int j=0;j<n;j++){
# // 		if (i&(1<<j)){
# // 			ds.push_back(arr[i]);
# // 		}
# // 	}
# // }


a=[1,2,3,4]
n=len(a)
l=[]
for i in range(2**n):
    res=[]
    for j in range(n):
        if(i & (1<<j)):
            res.append(a[j]);
    l.append(res)
print(l)












