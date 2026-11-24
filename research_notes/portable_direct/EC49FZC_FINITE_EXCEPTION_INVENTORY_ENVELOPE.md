# EC49FZC — Finite exceptional inventory envelope and 24 new exact values
2026-11-24. Frozen BRC16943 auxiliary Boolean observer: state (U,H), U in the literal 50-support family F below, H a labeled subset of m columns, |H|<=h<m; noiseless queries W(r,j)=1[r in U]1[j not in H]. Exact joint recovery. No new native X6 attribution. Parent-dependent, author-proved, not independently reviewed. Historical researcher EM-DIRECT-23537B; original registration receipt r4-20261124-0240-ec49fyh-own-session-v1 verified SUCCEEDED, RA-2D7B4AD1AA5CD3F5D9EF1C76. Current client authenticated, private writer binding not established. Current topic query r4-20261124-2330-ec49as-read-v1 SUCCEEDED, NO_CANONICAL_PUBLICATION_DIRECTORY at 974ddf81fb969c271faa91ec3cb92b92e961a733; no CLAIM, protected write or formal Result/Review.

## Main result
Let c=ceil((15h+6)/11), d=h+c-1, m0=28h-19c+10, t=11c-15h-6, z=(h-4-8t)/11, h>=4. FZB established M_h=m0 iff z>=max(1,t-1), leaving 82 exceptional h, including already solved h=4. New exact integer weighted-cover inequalities and finite transport recurrence close 24 additional exceptional values, and narrow every remaining exceptional value to an interval of width at most 3. Of 82 exceptions: {"0":25,"1":37,"2":19,"3":1} (key=width); 57 have strictly improved lower bounds over max(h+1,m0+1). Exact values, including h=4: [[4,9],[36,70],[39,77],[44,85],[47,92],[57,109],[58,115],[60,116],[63,123],[66,130],[77,153],[82,161],[85,168],[96,191],[101,199],[104,206],[115,229],[120,237],[123,244],[134,267],[139,275],[142,282],[153,305],[161,320],[172,343]]. Together with FZB this leaves 57 h>=4 unresolved; h=1..3 not treated here.

## New general prefix certificate
For any nonnegative integer weights w_U on F, integers A>0,q>=0 satisfying sum_{U:S intersects U} w_U <= A+q|S| for every nonempty row mask S, let W=sum w_U and v=max w_U. Then
M_h >= ceil((h W-v-q(h+c_h-1))/A).
Proof: use the FYU/FYX all-zero prefix lemma: stop at depth d or earlier complete saturation. There is a feasible such prefix, and every b(U) (distinct forced hole columns) is >=h except at most one that may equal h-1. For early saturation none is deficient. Thus sum w_U b(U)>=hW-v. Each nonempty column mask contributes at most A+q popcount; summing yields <=A N+q L<=A m+q d. This proves the lower bound for any winning tree at depth m+c_h. This uses distinct physical columns, not the sum of row hits. The observation reduction is only a necessary condition, not a substitute for labeled recovery. Six exact certificates below were found with numerical linear programming (maximize hW-v-qd with A=1, auxiliary v>=w_U), rational reconstruction, then exact integer mask checking; the proof does not rely on LP optimality. In particular the simple A=1,q=3,W=9,v=2 certificate gives M_h>=6h-3c_h+1. The six certificate parameter tuples (A,q,W,v) are [[3,30,77,14],[27,64,198,22],[1,3,9,2],[5,36,95,17],[3,22,58,11],[3,38,96,19]]. Take their maximum together with h+1 and FZB's lower bound (m0+1 on exceptional h).

## Upper construction by residual transport
For each k=1..22, reuse a witnessed packed block with L=ceil(26k/11), physical inventory B(k) below, distinct coverage at least k for every support. No optimality of B(k) is required. If a base has c_{h-k}>=6 and c_h-c_{h-k}=L-k, FYX packed transport gives M_h<=M_{h-k}+B(k). Use induction, initializing with Q4(9)=15 and known FZB exact endpoints in the finite range. At each h choose the minimum available candidate. This recurrence combines different phase jumps rather than simply concatenating period-11 blocks. Exact values arise only where the constructive upper equals the certificate lower. The block observations retain physical labels by FYX's proof. All finite bounds are parent-dependent; no new full adaptive tree search or native BRC implementation execution is claimed.

## Reproduction (Python 3, exact integer checks; no optimizer needed)
The literal data below are sufficient to reproduce the entire finite envelope. In this run a local Python/SciPy LP search generated the six certificates; local Python compared the finite bounds, and an independent JavaScript integer replay checked all six certificates (6138 nonempty mask inequalities), all 22 witnessed blocks (1100 support inequalities), and the 180 integer recurrences h=4..183. All passed. The compact Python checker implements exactly that replay.

```python
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
D=[[3,30,[[86,6],[91,1],[101,13],[243,1],[281,3],[299,1],[346,1],[394,14],[412,2],[460,2],[602,9],[673,14],[788,10]]],[27,64,[[23,6],[86,14],[101,19],[157,2],[243,9],[281,3],[299,12],[394,21],[412,6],[460,15],[602,22],[646,7],[673,22],[697,6],[788,22],[833,12]]],[1,3,[[86,1],[101,1],[299,1],[394,1],[460,1],[602,1],[673,2],[788,1]]],[5,36,[[23,1],[86,6],[101,16],[243,2],[281,3],[299,2],[346,2],[394,16],[412,3],[460,3],[602,12],[673,17],[788,12]]],[3,22,[[86,5],[101,9],[243,1],[281,2],[299,2],[346,1],[394,9],[412,2],[460,2],[602,7],[673,11],[788,7]]],[3,38,[[86,7],[91,2],[101,17],[243,1],[281,4],[346,1],[394,19],[412,2],[460,2],[602,11],[673,17],[788,13]]]]
P=[[],[[7,1]],[[1,1],[2,1],[256,1],[516,1]],[[3,1],[5,1],[6,1],[520,1]],[[1,1],[3,1],[6,1],[144,1],[256,1],[516,1]],[[1,1],[2,1],[3,1],[4,2],[9,1],[144,1],[256,1],[512,1]],[[1,1],[3,1],[4,1],[6,1],[17,1],[144,1],[192,1],[256,1],[768,1]],[[1,1],[3,2],[4,1],[6,1],[17,1],[64,1],[128,1],[144,1],[256,2],[512,1]],[[1,3],[2,2],[3,1],[4,3],[8,1],[144,1],[192,1],[256,2],[512,2]],[[1,1],[3,2],[4,2],[8,1],[12,1],[17,1],[64,1],[128,1],[144,1],[256,1],[257,1],[512,1],[514,1]],[[1,2],[2,2],[3,2],[4,4],[9,2],[144,2],[256,2],[512,2]],[[1,3],[2,2],[3,3],[4,4],[8,1],[16,1],[64,1],[128,2],[256,3],[512,3]],[[1,2],[2,1],[3,3],[4,3],[6,1],[17,1],[40,1],[64,1],[128,1],[144,2],[256,3],[512,2]],[[1,4],[2,2],[3,2],[4,4],[8,1],[144,2],[192,2],[256,3],[320,1],[512,3]],[[1,2],[3,4],[4,2],[6,2],[48,2],[64,2],[128,2],[144,2],[256,4],[512,2]],[[1,3],[2,3],[3,3],[4,6],[9,3],[144,3],[256,3],[512,3]],[[1,4],[2,2],[3,4],[4,5],[8,2],[16,1],[64,1],[128,1],[132,1],[144,1],[192,1],[256,4],[512,4]],[[1,3],[2,1],[3,5],[4,5],[6,1],[8,1],[9,1],[48,1],[64,1],[128,1],[144,3],[256,4],[512,3]],[[1,3],[2,2],[3,5],[4,6],[8,2],[17,1],[64,1],[128,2],[144,2],[256,3],[257,1],[320,1],[512,4]],[[1,5],[2,3],[3,5],[4,7],[8,2],[16,1],[64,1],[128,2],[144,1],[192,1],[256,5],[512,5]],[[1,4],[2,4],[3,4],[4,8],[9,4],[144,4],[256,4],[512,4]],[[1,5],[2,3],[3,5],[4,7],[8,1],[9,1],[12,1],[16,1],[64,1],[128,2],[144,2],[192,1],[256,5],[512,5]],[[1,6],[2,4],[3,6],[4,8],[8,2],[16,2],[64,2],[128,4],[256,6],[512,6]]]
def ceildiv(x,y): return -((-x)//y)
def C(h): return ceildiv(15*h+6,11)
for A,q,w in D:
    assert A>0 and q>=0 and all(u in F and n>=0 for u,n in w)
    for s in range(1,1024):
        assert sum(n for u,n in w if u&s)<=A+q*s.bit_count()
B=[0]
for k,p in enumerate(P[1:],1):
    assert sum(n*s.bit_count() for s,n in p)==ceildiv(26*k,11)
    assert all(sum(n for s,n in p if s&u)>=k for u in F)
    B.append(sum(n for s,n in p))
hi={}; rows=[]
for h in range(4,184):
    c=C(h); d=h+c-1; t=11*c-15*h-6
    assert (h-4-8*t)%11==0
    z=(h-4-8*t)//11; m0=28*h-19*c+10
    eq=z>=max(1,t-1)
    lo=m0 if eq else max(h+1,m0+1,*[ceildiv(h*sum(n for u,n in w)-max(n for u,n in w)-q*d,A) for A,q,w in D])
    choices=[(m0,0)] if eq else [(9,0)] if h==4 else []
    for k in range(1,min(22,h-4)+1):
        if c-C(h-k)==ceildiv(26*k,11)-k: choices.append((hi[h-k]+B[k],k))
    hi[h],via=min(choices)
    assert lo<=hi[h]
    if not eq: rows.append((h,t,z,m0,lo,hi[h],via))
assert len(rows)==82
assert sum(lo==up for h,t,z,m0,lo,up,k in rows)==25
assert max(up-lo for h,t,z,m0,lo,up,k in rows)==3
for row in rows: print(*row)
```

## Actual exact replay output
B=[0,1,4,4,6,9,9,12,16,15,18,23,21,24,24,27,31,30,33,38,36,40,46].
Columns h,t,z,m0,lower,upper,chosen increment k (0=known base):
```
4 0 0 8 9 9 0
5 7 -5 -2 8 10 1
6 3 -2 7 10 13 2
7 10 -7 -3 11 13 3
8 6 -4 6 13 15 4
9 2 -1 15 17 18 5
10 9 -6 5 16 18 6
11 5 -3 14 19 21 7
12 1 0 23 24 25 8
13 8 -5 13 22 24 4
14 4 -2 22 25 27 5
16 7 -4 21 28 30 5
17 3 -1 30 32 33 13
18 10 -6 20 31 33 4
19 6 -3 29 34 36 5
20 2 0 38 39 40 5
21 9 -5 28 37 39 4
22 5 -2 37 41 42 5
24 8 -4 36 43 45 5
25 4 -1 45 47 49 5
27 7 -3 44 49 51 5
28 3 0 53 54 55 5
29 10 -5 43 52 54 5
30 6 -2 52 56 57 13
32 9 -4 51 58 60 5
33 5 -1 60 63 64 5
35 8 -3 59 65 66 5
36 4 0 68 70 70 5
38 7 -2 67 71 73 5
39 3 1 76 77 77 8
40 10 -4 66 73 75 5
41 6 -1 75 78 79 5
43 9 -3 74 80 81 13
44 5 0 83 85 85 13
46 8 -2 82 87 88 5
47 4 1 91 92 92 16
49 7 -1 90 93 94 5
51 10 -3 89 95 97 5
52 6 0 98 100 101 5
54 9 -2 97 102 103 5
55 5 1 106 107 108 5
57 8 -1 105 109 109 13
58 4 2 114 115 115 8
60 7 0 113 116 116 13
62 10 -2 112 117 118 5
63 6 1 121 123 123 13
65 9 -1 120 124 125 5
66 5 2 129 130 130 16
68 8 0 128 131 132 5
71 7 1 136 138 139 5
73 10 -1 135 139 140 13
74 6 2 144 145 146 5
76 9 0 143 146 147 13
77 5 3 152 153 153 8
79 8 1 151 153 154 13
82 7 2 159 161 161 13
84 10 0 158 162 163 5
85 6 3 167 168 168 16
87 9 1 166 169 170 5
90 8 2 174 176 177 5
93 7 3 182 183 184 5
95 10 1 181 184 185 13
96 6 4 190 191 191 8
98 9 2 189 191 192 13
101 8 3 197 199 199 13
104 7 4 205 206 206 16
106 10 2 204 207 208 5
109 9 3 212 214 215 5
112 8 4 220 221 222 5
115 7 5 228 229 229 8
117 10 3 227 229 230 13
120 9 4 235 237 237 13
123 8 5 243 244 244 16
128 10 4 250 252 253 5
131 9 5 258 259 260 5
134 8 6 266 267 267 8
139 10 5 273 275 275 13
142 9 6 281 282 282 16
150 10 6 296 297 298 5
153 9 7 304 305 305 8
161 10 7 319 320 320 16
172 10 8 342 343 343 8
```

## Frozen sources and next
- FZB: a90a1888fe19b895b59a1877ce744c083bfa8e02:research_notes/portable_direct/EC49FZB_SHARP_PHASE_ONSETS.md (sharp lower endpoint onset).
- FYX: 299068854165822c41b3e78d42e8c0bf604cfc47:research_notes/portable_direct/EC49FYX_ALL_PHASE_INVENTORY_DUAL.md (zero prefix lemma and original inventory certificate).
- FYX: 3a42e1a171d3db7c557d136d4256747ef0724aff:research_notes/portable_direct/EC49FYX_PACKED_MULTICOVER_TRANSPORT.md (labeled recovery and transport).
- FYY: 3c1f6b95ce10dec1e3dbb5889689073149bb8228:research_notes/portable_direct/EC49FYY_pack.out (blocks k=1..11, exact replay in this turn).
- FYZ: dce2ea422bf8cc45823046a966e0050b25fb8b3d:research_notes/portable_direct/EC49FYZ_ADAPTIVE_LOWER_ENDPOINT_RIGIDITY.md (blocks k=12..22, exact replay in this turn).
Next: sharpen remaining 57 intervals, especially h=6 (width 3) and small h=5..14. Split the sole deficient support in the prefix lemma and derive stronger conditional duals or construct exact strategies on the lower endpoint. Preserve all closed values rather than repeat searches. AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
