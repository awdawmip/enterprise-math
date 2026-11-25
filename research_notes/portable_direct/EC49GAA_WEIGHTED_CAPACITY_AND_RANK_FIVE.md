# EC49GAA — Weighted short-leaf capacity and genuine rank-five frozen obstructions
2026-11-25. Informed portable continuation of EC49FZZ at 96fbe6611af95be186ec08859f8b9c6fd3768046:research_notes/portable_direct/EC49FZZ_BOUNDED_OBSTRUCTION_ANTICHAIN.md. All inherited archive files checked against SHA256SUMS. Frozen BRC16943 fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923. Exact binary support-hole observation model W(r,j)=1_{r in U}1_{j notin H}, 10 rows, 25 columns, h=14. No physical dynamics or alteration of P000. Current topic receipt r4-20261125-2328-ec49as-read SUCCEEDED, source b1b39590cc72fa0a98ef10fb56cd8db9dca3a563, NO_CANONICAL_PUBLICATION_DIRECTORY; no live owner projection or shared execution authority. Historical EM-DIRECT-23537B provenance, private current binding unconfirmed; Activity pending. Independent scientific preservation only.

## 1. Weighted short-leaf capacity and obstruction rank
Let S be a nonempty finite set of states distinguishable by a fixed finite family Q of binary unit-cost queries, k>=0 integer, weights a_x>=0. Define V_k(S;a) as maximum total weight of states identified at depth <=k by any complete identifying decision tree (other states have no depth bound). V_0(S;a)=a_x if S={x}, else 0. For |S|>1 and k>=1:
V_k(S;a)=max_{q nonconstant on S} [ V_{k-1}(S_0(q);a)+V_{k-1}(S_1(q);a) ].
For singleton S use V_k=a_x. Proof: constant queries are removable, informative root splits into disjoint conditional state sets; objective is additive, and optimum child trees may be glued. At depth k unresolved leaves can be completed later because Q separates S. Nonnegative weights allow refining without loss. With a=1_T, V_k(S;1_T)=|T| iff FZY's D(S,T)<=k. With all weights 1, v=V_k(S;1) is the exact greatest number of simultaneously budget-feasible targets. Thus every target set of size v+1 is an obstruction, and every inclusion-minimal obstruction has size <=v+1. This is an exact value oracle, not a claim of efficient solution for arbitrary large nodes.

Omission lemma: D(S,S\{x})=D(S,S) for every x in S if |S|>=2. Indeed in a tree identifying all other states by depth k, an unresolved population at depth k would contain at least two states and therefore at least one designated state, a contradiction. The last remaining state must already be identified by depth k. Thus if full recovery fails, v<=|S|-2. If |S|>2^k, at most 2^k-1 singleton leaves can be present at depth <=k, because at least one leaf of the truncated tree must contain at least two states. Consequently every minimal obstruction has rank <=min(|S|-1,2^k), more precisely <=v+1. This exponential bound is sharp even in the class of anchored support-hole models with variable row count: take N=2^k+1 states, include for each unordered pair of states k bit queries coding the N-1 equivalence classes obtained by merging just that pair bijectively into {0,1}^k. For k>=1 these queries jointly separate all states. For any target set of size <=N-2, choose an omitted pair, execute its k bit queries and identify all designated states, then separate the omitted pair later. Any target set of size N-1 fails by leaf capacity. For k=0, take two separable states and rank-one failure. Realize the query family as rows of a one-normal-column support model with a common all-one anchor row and arbitrary prescribed supports; take H=empty and h=0. This construction uses a variable support family/row count, not the fixed BRC16943. Hence no universal fixed rank cutoff independent of k holds even for this anchored model class.

A monotone deletion oracle extracts an inclusion-minimal obstruction without generating all antichain members: start from a failing T and test T\{x} using the weighted value oracle; delete x iff failure persists. A single pass suffices: when deletion succeeds in producing a feasible set, all future subsets of that feasible set are feasible. FZZ antichain still supplies exact minimum-rank and all-witness information; deletion alone need not find minimum rank.

## 2. Actual new frozen evidence
Target actual low-budget failed internal nodes rather than random easy conditioned nodes. Instrumented FZV sat_token.cpp at the final exhaustive return only (does not alter search or memo decisions); after earlier tests and candidate search, record up to 60 nodes per root with n<=16 and k<=4, canonical column ordering. Roots 1852,1865,1869 (ordered capture batches of 60 each), 180 observations, 176 distinct exact (ordered state list,k) records. All 180 have maximum singleton certificate <=k, yet full optimum >k. 141 observations have minimum obstruction rank 2; 39 have minimum obstruction rank exactly 5 (38 distinct recorded populations/budgets). For these 39: exhaustive rank 1..4 found no failure; deletion generated rank-five failed target set and every single deletion verified feasible. Thus rank-four truncation is strictly insufficient in actual frozen nodes, not merely generic examples. Sampling is deliberately failure-conditioned and capped; proportions are not prevalence estimates.

Representative observation index 3 (zero-based, root1852), budget4, 15 states in normalized column labels, (U,H) integer masks in exact order:
[(23,33529344),(23,33512960),(23,33504768),(23,33496576),(86,33552384),(86,33551360),(86,33550848),(86,33550336),(86,33549312),(86,33548800),(86,33548288),(86,33547776),(86,33547264),(86,33546752),(86,33546240)].
Distinct informative physical query masks: 11,13,14,15,21936,26320,30944,32512,32752.
Singleton depths: 2,2,2,3,3,3,3,4,3,3,4,3,4,4,4.
Targets indices (3,7,10,12,13), mask13448. All nine target-separating root queries have exact total designated depth5; deleting any one of these five gives depth4. Every one of sum_{r=1}^4 binom(15,r)=1940 subsets of rank <=4 is feasible at budget4. Full depth5, maximum simultaneous short-leaf count13. In particular |S|=15<=16 so simple binary leaf capacity cannot explain the failure.

Actual exact comparison: 183494 low-rank subset tests of value oracle, independent all-informative-query reference and FZZ dual antichain; 2141 one-omission equalities; 70 weighted powerset tests (50944 enumerated subsets), no assertion failure. The weighted DP and deletion check used integer masks and nonnegative integer weights, never coarsening away the competitors. New oracle not integrated in formal solver; no speed claim.

## 3. Fourth layer
The original solver processed first 3 previously OPEN roots with cap250000; instrumented unchanged-decision solver processed next 3 with cap180000.
```csv
1773,1451,0,250001,7185,193,0
1813,1495,0,250001,3892,183,0
1828,1526,1,245400,8688,44,0
1852,1557,0,180001,1441,100,0
1865,1575,0,180001,6696,160,0
1869,1579,1,22373,213,36,0
```
Two YES, zero new NO, four unresolved, 3105 labelled joint states replayed. Fourth layer 1895 YES /27 NO /471 OPEN of 2393. M14 remains 25<=M14<=27. Never treat a node cap as NO. Next: use actual rank-five examples to derive a structural two-support-fiber obstruction rule and measure a narrowly gated oracle on difficult nodes; continue 471 OPEN roots. Completed roots not repeated. AUTHOR_PROVED / EXACT_FINITE_RANK_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.

## 4. Reproduction
Use inherited FZZ archive beside fourth.json, gen.py, retry_z.py, sat_token.cpp, multi_target.py, obstruction_antichain.py and their existing dependencies. Exact input generation:
```sh
sed "s/'y2.csv'/'y2.csv','z.csv'/;s/==476/==473/" retry_z.py > retry_ga.py
python retry_ga.py 0 3 250000 > ga.in
g++ -O3 -std=c++17 sat_token.cpp -o sat_token
./sat_token < ga.in > ga.csv
python build_ga.py
python retry_ga.py 3 6 180000 > ga2.in
g++ -O3 -std=c++17 ga_capture.cpp -o ga_capture
./ga_capture < ga2.in > ga2.csv 2> ga_nodes.txt
python capacity_rank.py > capacity_rank.out
```
build_ga.py:
```python
from pathlib import Path
s=Path('sat_token.cpp').read_text()
s=s.replace('int cap,calls=0','int captured=0;int cap,calls=0',1)
old='return mem.emplace(key,o.q).first->second;}return mem.emplace(key,-1).first->second;}'
new='''return mem.emplace(key,o.q).first->second;}
 if(k<=4&&n<=16&&captured<60){++captured;cerr<<k<<" "<<n;for(int i=0;i<(int)ids.size();i++){int f=A[i]^B[i];for(int z=f;;z=(z-1)&f){if(pc(B[i]|z)<=H)cerr<<" "<<F[ids[i]]<<" "<<(B[i]|z);if(!z)break;}}cerr<<endl;}
 return mem.emplace(key,-1).first->second;}'''
assert s.count(old)==1
s=s.replace(old,new)
Path('ga_capture.cpp').write_text(s)
```
capacity_rank.py:
```python
from functools import lru_cache
from itertools import combinations
from collections import Counter
from random import Random
import json
from multi_target import model,physical
from obstruction_antichain import dual

def capacity(n,qs,weights):
    full=(1<<n)-1
    @lru_cache(None)
    def val(s,k,t):
        t &= s
        if not t:return 0
        if s.bit_count()==1:return weights[s.bit_length()-1]
        if k==0:return 0
        return max(val(s&q,k-1,t&q)+val(s&~q,k-1,t&~q) for q in qs if s&q and s&~q)
    return full,val

def main():
    rng=Random(16943); c=Counter(); evidence=[]
    rows=[tuple(map(int,l.split())) for l in open('ga_nodes.txt')]
    for index,line in enumerate(rows):
        k,n,*pairs=line;st=list(zip(pairs[::2],pairs[1::2]));assert len(st)==len(set(st))==n
        full,qs,cert,split,ref,allowed=model(n,physical(st,10,25))
        _,score=capacity(n,qs,[1]*n)
        v=score(full,k,full); assert v<n and ref(full,full)>k
        assert v<=min(n-2,(1<<k)-int(n>(1<<k)))
        # Every n-1 target set has exactly the same optimum as the full set.
        for i in range(n):assert ref(full,full^(1<<i))==ref(full,full);c['one_omission_checks']+=1
        t=full
        for i in range(n):
            a=t&~(1<<i)
            if score(full,k,a)<a.bit_count():t=a
        assert ref(full,t)>k
        assert all(ref(full,t^(1<<i))<=k for i in range(n) if t>>i&1)
        c['nodes']+=1;c['deletion_minimal_rank_'+str(t.bit_count())]+=1
        singleton=max(cert(full,1<<i) for i in range(n)); c['singleton_pass']+=singleton<=k
        # Exhaust rank <=4 and compare with independent designated recurrence.
        _,bad,_=dual(n,qs,4); fam=bad(full,k)
        for r in range(1,min(n,4)+1):
            for ids in combinations(range(n),r):
                a=sum(1<<i for i in ids); fail=ref(full,a)>k
                assert (score(full,k,a)<r)==fail==any(a&b==b for b in fam)
                c['subset_checks']+=1
        minrank=min((b.bit_count() for b in fam),default=None)
        c['minimum_rank_'+str(minrank)]+=1
        if n<=10:
            weights=[rng.randrange(0,8) for _ in range(n)]; _,weighted=capacity(n,qs,weights)
            feasible=[a for a in range(1<<n) if ref(full,a)<=k]
            assert weighted(full,k,full)==max(sum(weights[i] for i in range(n) if a>>i&1) for a in feasible)
            c['weighted_full_powerset_checks']+=1;c['weighted_subsets']+=1<<n
        evidence.append(dict(index=index,k=k,n=n,score=v,singleton=singleton,minimum_rank_le4=minrank,greedy_witness=t,antichain=list(fam)))
    print(json.dumps(dict(counts=dict(c),nodes=evidence),sort_keys=True))
if __name__=='__main__':main()
```
SHA256 actual files:
```
93182f6e0a4d99872d59098ad370f0885b2d48f8039ddeba83a40542d7021b86  build_ga.py
2f7487a95deb63ca579e924d6c1f8eca109ea3c486473f071b9adf6b167a87f8  retry_ga.py
54cdb7b02e8d8940f8055508e461b6c5ad9f287b16a822daea536363b5f92e72  ga.in
cf7bd114ecba626cee98f1c913cadeef855b6d73faddfafa7b63f30335ac88f4  ga.csv
fd1b4f8173c8a2db539436ce36e3862911e3d67d85a752a282b9f7736ed1be50  ga2.in
1baa21c3ce6f3dc830b5643cb7c2a27dfe08d42e3cf12fea7848daf14cf51429  ga2.csv
c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0  ga_nodes.txt
86f84b1d128f1c12bf023f21af660ca2f25e0e7bb3094e9d0697b2238640201f  capacity_rank.py
351da71f87e96fb5405b8d23903e86f21e8996084cb46cdfa1d62183d4f15adb  capacity_rank.out
```
Full raw captured nodes and result encoded below; decode each single line using zlib.decompress(base64.b64decode(line)).
ga_nodes.txt (28368 bytes):
```text
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
```
capacity_rank.out (23843 bytes):
```text
eNrNXNtu2zAMfd9XFHneg0hRt33EfmAYgizxWqOpMzQpuqHYv09ud3GMdJO9MEdPrS07h6QoiqJ0/LRY7x66w37x7uppsWm2zaHddcu7tmvvVtvl/aq7XXJuI6G3V6+0u9xuU25+vvtwN37r6Pb7Xdf8er7bbZoemKLJV7lhubtr9/seYH3TrG/7Nn75jX3bXWfs3PJltf/zzv7h0745/HmaopUkueGxaa9vDs1m+flhu11+2T0290cPBjN86OVn+vvOJJHvA9k+PC1W3aFd36zarr8k699eEefXybqP+cHr+6bZfFs+toeueZGsf2LRdpvma77qcW57hceG2DbSq9dD5b+xV2a9u+9t44f69q9meUZSOI4nsfP9ATb9xJa/Y5MZgMcRuMwFZx3wV0wuMsS2f8fusk/8gncDeLLnUl4KlacBejqT8q5ceT9R+dP4gVkG+F7P+EX4QU//ss6POp4/NfIkZOQxddiACGkEZAgkeAwkQarvwFGI0GGQgp4Ak4dhRA7DBE2DzCVHwcgHmOrxAWagD7CF+gAyErJDTwTsocYPaujZ9b2YfgT4mPzp3uhbhtKUJodu2sqAjJjTAuSGIX7SWZmQca8YIDcMV2ZGB7/MFyypoc/wBcszfIFITRxblziiJM7Uics64MRlfR0LKRuQRojIWlKCF5OgMVOqiplSGjOPSjusJo7VE6ekbwTqGQ5Y5RSvWuab4wuhLteMSuKUpnpSmmryUABzPgGcQQtASgKUjU/HyOjgLBRdacld3PUOu85yHowf9Fx/RjB0sarY7BI0bfBKCeXURYVH7s54RlalvAWWhb3MzJ3kfIUorxYgC/E9cnryoY5lvUduzPhUhxEC8oxOIGBtI7Di/lDhQAz2gqtI9jEeGUAxEpYdVrn4PvXYBXw9W4QBWWQMETgjB3iRMUKLjJHqyEgjcpM6InPCqJkTTu0F5I5L9MAJOQa9XihUP16yqDt2woRWPxlg7yeCq8/A3k8Wrr7UMQ0lZABMHjgNpXDphHw8BiPcCRN014AMNBMkQ+BdGzIMl8Biq/d5iQ43gYNL4NGdEOAmiNhQkKDwaiSWwsoYkV4oLJWA4RJYuASCnY/JYUeBR4+CAPeACJdA7SzNVCYPQwnNTJXwCqFsFtKisxT7I2vFRH7OQCj2i5D8/+m+4FGawm7OcQoNnttvqgvGLQLySANxxE6UXMl+MllojLQEpR0zmvdq8cxnC6U+W4c3gK8lX4ESV8jGWkIS9GsQgtxVISF0SBKuiIv/m7OCcQWpZESIg5oBuclCUtO3IQT6cQhJyI74F0XlP6fqGUfTqZi0chkaMDlVlrTl0J98sZbj6ZXvc8uRPLYqKgE5qay/XGX95aFcCypmwuiUb10EkjTJJfDxVvKmoqkOSnghLOOFoJQXmsJ50fcDaO7pobmnD9WlPD7WNYUWE2OmylMWMoNBB+1A1flI4Eo+R0MBun4PAp1EgkNWkjTJMnP9MtQVu0KsZpycpeT58fubH1Cb+84=
```
