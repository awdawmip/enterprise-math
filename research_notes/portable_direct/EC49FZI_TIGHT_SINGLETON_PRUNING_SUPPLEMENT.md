# EC49FZI supplement — tight singleton feature pruning

2026-11-25. Extends the same-turn saved FZI proof at 9cb706ae5ef8ea8972c6fc3dad1d2338c76680d4, no change to frozen inputs or prior conclusions. New pass, not a replay of already feasible keys.

For x=(U,H), let I be the rows with a compatible same-H single-row toggle, and J the columns with a compatible same-U single-column toggle. The common positive anchor persists in every descendant branch. By the full feature certificate theorem restricted to these singleton competitors, the exact cost is
B(x)=max(|I intersect U|,|J minus H|)+|I minus U|+|J intersect H|.
If B>k prune. If B=k the next probe must reduce this cost by at least one along x's response, because k-1 queries remain and singleton rivals that survive still require their features. More explicitly, for a probe (r,j), write a=|I intersect U|, b=|J minus H| and i=1[r in I], l=1[j in J]. On x, if positive, it removes at most the row and column singletons at r and j; thus require max(a-i,b-l)<max(a,b). If negative with r outside U and j live, require i=1. If negative with r in U and j missing, require l=1. If both features zero it removes no singleton and is forbidden at tight B. These conditions follow directly by evaluating W on each toggle rival; no approximation. When queries have identical full branch response vectors, retain all physical locations and require at least one location compatible with all tight-state constraints before considering that response partition. This is safe for both children; positive replay still evaluates actual W.

## Executed pass 3
Starting from FZI's 270 unknown keys, select all with n<=400 (57 keys). Run the enhanced exact solver with cap 50000 per key. 27 new feasible, 30 capped, zero exhausted negatives, 2272193 calls, 8764 replayed labeled states. New feasible IDs:
62,63,64,69,75,78,82,84,85,88,92,93,94,95,96,97,98,99,100,102,103,104,105,106,107,118,131.

Combined latest outcomes across all three passes: 105 feasible, 243 unresolved, no new negative keys; 27698 replayed labeled states; 133 feasible ordered histories and 287 unresolved. Actual cumulative recursion calls 4620881 across all passes (latest-per-key calls 3553523). By final suffix type feasible/unresolved: (3,1) 25/59; (192,6) 38/96; (320,6) 39/74; (320,8) 31/58. M14 remains [25,27], 35/82 finite exceptions closed. These additional feasible branches may be attributable to both larger search caps and new pruning; no speedup factor claimed.

## Exact reproduction of pass 3
Use search.cpp from FZI proof, and the following Python string transformation (same as executed) to create search_forced.cpp:
```python
s=open('search.cpp').read().replace('loc,nei,sup;','loc,nei,sup,rnei;').replace('nei.resize(st.size());sup.resize(st.size());','nei.resize(st.size());sup.resize(st.size());rnei.resize(st.size());').replace('for(int v=0;v<(int)st.size();v++)if(v!=i','for(int r=0;r<10;r++){auto it=idx.find({u^(1<<r),h});if(it!=idx.end())rnei[i].push_back({r,it->second});}for(int v=0;v<(int)st.size();v++)if(v!=i',1)
s=s.replace('vector<pair<int,int>>tight;','vector<pair<int,int>>tight;vector<array<int,4>>ftight;')
s=s.replace('if(a==k)tight.push_back({st[i].first,J});','if(a==k)tight.push_back({st[i].first,J});int I=0;for(auto[r,v]:rnei[i])if(X[v])I|=1<<r;auto[u,h]=st[i];int cost=max(__builtin_popcount((unsigned)(I&u)),__builtin_popcount((unsigned)(J&~h)))+__builtin_popcount((unsigned)(I&~u))+__builtin_popcount((unsigned)(J&h));if(cost>k)return memo.emplace(key,-1).first->second;if(cost==k)ftight.push_back({u,h,I,J});')
s=s.replace('if(!tight.empty()){bool good=false;','if(!tight.empty()||!ftight.empty()){bool good=false;')
s=s.replace('if(ok){good=true;break;}','if(ok)for(auto[u,h,I,J]:ftight){int a=__builtin_popcount((unsigned)(I&u)),b=__builtin_popcount((unsigned)(J&~h));bool row=u>>r&1,live=!(h>>j&1),ir=I>>r&1,jr=J>>j&1;bool useful=row&&live?(max(a-ir,b-jr)<max(a,b)):(!row&&live?ir:(row&&!live?jr:false));if(!useful){ok=false;break;}}if(ok){good=true;break;}')
open('search_forced.cpp','w').write(s)
r={int(a):int(c) for file in ['results.csv','results2.csv'] for a,b,c,d in map(lambda x:x.strip().split(','),open(file))}
f=open('input.txt');n=int(f.readline());cases=[]
for i in range(n):
 a=list(map(int,f.readline().split()));st=[f.readline() for _ in range(a[1])]
 if r[a[0]]==0 and a[1]<=400:
  a[-1]=50000
  cases.append(' '.join(map(str,a))+'\n'+''.join(st))
with open('input3.txt','w') as g:g.write(str(len(cases))+'\n'+''.join(cases))
```
Compile g++ -O3 -std=c++17 search_forced.cpp -o search_forced; run ./search_forced < input3.txt > results3.csv. Merge latest statuses by key ID, retaining the earlier feasible keys unchanged. Next: resume the 243 unknown keys, use full weighted-feature certificate at selected tight descendants, or extend already feasible ordered suffixes. No formal Result/Review or Activity binding asserted.
