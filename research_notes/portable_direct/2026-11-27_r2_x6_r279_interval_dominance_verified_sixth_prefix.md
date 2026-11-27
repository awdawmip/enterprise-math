# X6 R279 — exact interval dominance implemented and sixth-pencil continuation

2026-11-27. Same independent informed TASK_RESEARCH as R278, NOT_REVIEWED. Own identity/owner projection unconfirmed; no CLAIM or shared mutation. Topic read r2-20261127-2208-x6-read, Source af81386070eb9079f70af7e52183936a68e5f920, NO_CANONICAL_PUBLICATION_DIRECTORY. Auxiliary coefficient algebra, P000 V5 and joint-relation preservation retained.

## Inputs and theorem
R278@ae39371f60600f89054327a5ef9a8f1470e7ab69:research_notes/portable_direct/2026-11-27_r2_x6_r278_sixth_prefix_and_safe_envelopes.md. Same R277/R276/R275/R247 pinned inputs and complete suffix/necessary wall premises; strict words c=1. Continue [1800,0] only.

Use R278's future-safe dominance: within retained exact open f interval I, discard a lower-bound row if another lower bound is everywhere at least as strong; analogously upper bound. Keep I and all endpoint words/germ masks. Since same-sign denominators multiply to a positive number, for p,r on the same side the numerator of g_p-g_r is (B_r A_p-B_p A_r) f + C_r A_p-C_p A_r. Reverse sign for upper bounds. Finite endpoint tests are nonstrict; infinite endpoints impose the correct slope sign. If two functions coincide on I, keep the earlier row; otherwise strict dominance is acyclic (pointwise partial order), so every removed function is dominated by a retained function through a finite chain. Thus simultaneous filtering is sound. Preserve the seen set: an omitted old row already follows from the retained state and every later intersection, including when a future row repeats it. This is exact joint feasible-set equality, not merely current interval equality.

## Actual computation
Start=1800,size=450, cap 25m suffix checks. Compress the base five-line state once per prefix. For every algebra-tested sixth extension compare compressed and uncompressed R277 grow, including exact f lower/upper bounds for feasible cases, and for the first 100 also compare original R275 full elimination. Count only cross-pairs in sixth-extension grow calls, not base construction or dominance overhead. No runtime acceleration claimed; this verifies the algebra optimization and measures paired comparisons in this finite sample.

```json
{"hist":{"direct":10051,"alg":21008,"recursive":4287,"surv":204,"visits":35550,"checkedAgainstOld":100},"checks":15113956,"next":[2250,0],"stats":{"prefixes":450,"oldRows":25503,"newRows":2418,"domTests":145815,"algebraCompared":25499,"oldPairs":41135141,"newPairs":22565362},"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"partial":false}
```
New classified extensions 35550, new survivors 204, next [2250,0]. Cumulative classified 177750/667787; survivors 1387; unclassified 490037. Necessary-condition survivors only. All classified survivors saved below. If partial, next is first unclassified local index, and earlier survivors are kept.

```text
1813:18060000
1814:8000000
1820:1c
1821:2000000000000000000
1822:1
1825:40000600e
1826:4
1829:418000000002007
1830:6
1833:10
1838:600c
1842:418000000002007
1843:2004
1852:18000000
1855:3c1e008000
1856:8000
1857:200403000000
1858:3000000
1863:18000000
1865:2000000
1866:2000000
1871:18000000
1872:8000000
1877:18000000
1879:18000000
1881:18060000
1882:8000000
1885:18060000
1886:8000000
1888:3000000000
1890:1
1895:80
1897:3800000000
1900:410380000000000
1901:1
1910:400000000000000000
1911:40000000381c000000
1914:10383c06000000
1919:80001000000
1920:1000000
1921:8000000
1924:80000000000
1926:18000000
1927:1c000000
1930:400000000000000000
1931:40000000381c000000
1937:8000000
1942:18000000
1943:18000000
1947:18000000
1950:8000000
1952:8000000
1953:100000000000
1954:8000000
1957:180600c0
1961:603008000000
1962:1c00000000
1964:18000000
1983:600000000000
1987:2000000000
2012:181c000000000
2013:10000000000
2053:1800000000000000
2054:800000000000000
2060:1818000000000
2074:100000000000000
2077:40800000000000
2078:21060c00000000000
2081:800000000000
2102:1
2108:1818000000000
2109:1010000000000
2117:1810000000000
2120:8000000000000000
2145:c000000000000000000
2146:8000000000000000000
2191:400000000000
2222:60000000000
2224:20000000000
2240:404000000000
2243:20404000000000
```

## Reproduction
Use R277 reproduction with four immutable notes and same data/bank. Insert the following immediately before function grow:
```javascript
let pairCalls=0,stats={prefixes:0,oldRows:0,newRows:0,domTests:0,algebraCompared:0,oldPairs:0,newPairs:0};
function prune(st){
function cutOK(b,c){if(st.lo?b*st.lo[0]+c*st.lo[1]<0n:b>0n)return false;if(st.hi?b*st.hi[0]+c*st.hi[1]<0n:b<0n)return false;return true}
function dom(p,r,side){stats.domTests++;return cutOK(side*(r[1]*p[0]-p[1]*r[0]),side*(r[2]*p[0]-p[2]*r[0]))}
function keep(rows,side){return rows.filter((r,i)=>!rows.some((p,j)=>i!==j&&dom(p,r,side)&&(j<i||!dom(r,p,side))))}
let pos=keep(st.pos,1n),neg=keep(st.neg,-1n);stats.prefixes++;stats.oldRows+=st.pos.length+st.neg.length;stats.newRows+=pos.length+neg.length;return {...st,pos,neg};
}
function sameBound(a,b){return a===null||b===null?a===b:a[0]*b[1]===b[0]*a[1]}
function both(st,raw,N){let before=pairCalls,small=grow(st,N);stats.newPairs+=pairCalls-before;before=pairCalls;let full=grow(raw,N);stats.oldPairs+=pairCalls-before;stats.algebraCompared++;if(!!small!==!!full||small&&(!sameBound(small.lo,full.lo)||!sameBound(small.hi,full.hi)))throw Error("prune mismatch");return !!small}

```
In grow's pair function increment pairCalls before return cut. In the outer loop replace the base state construction with:
```javascript
let raw=grow(empty,R);if(!raw)throw Error("old bank infeasible");let st=prune(raw);
```
Replace let good=!!grow(st,N); with let good=both(st,raw,N); and add stats to both return objects. Start=1800,size=450. All arithmetic BigInt (counters ordinary bounded integers). No repeated five-line capacity search.

Next continue exactly from [2250,0], reuse all prior banks. If measured pair savings warrant, further implement complete upper/lower affine envelope pruning; compare actual total cost including dominance tests. Mixed zero words and singleton directions remain open; K6=1–2. Independent review and Activity association pending.
