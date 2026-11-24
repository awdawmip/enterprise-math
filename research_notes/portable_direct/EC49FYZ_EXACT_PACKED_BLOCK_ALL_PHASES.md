# EC49FYZ — Exact eventual static packed blocks and one-column onset band in every phase

Date 2026-11-24. Frozen auxiliary observer BRC16943, state (U,H), U in the frozen 50-support family below, |H|<=h<m, W(i,j)=1[i in U]1[j not in H], unit noiseless adaptive queries, exact support and labeled holes. No new native X6 attribution. Parents (author-proved, not independently reviewed): FYX packed transport at 3a42e1a171d3db7c557d136d4256747ef0724aff:research_notes/portable_direct/EC49FYX_PACKED_MULTICOVER_TRANSPORT.md; FYX all-phase dual at 299068854165822c41b3e78d42e8c0bf604cfc47:research_notes/portable_direct/EC49FYX_ALL_PHASE_INVENTORY_DUAL.md; FYW base Q4(9)=15 and c_h=ceil((15h+6)/11) for h>=2, b4b38aaa894b6e6906d6037f92b747a7a0dea182:research_notes/portable_direct/EC49FYW_EXACT_STABLE_HOLE_LAW.md. All conclusions below depend on those parent lemmas.

## Exact packed cover at minimum query cost

For k>=1 let L=ceil(26k/11), t=11L-26k (0<=t<=10). A block is a multiset of nonempty row masks S on distinct physical columns with sum of popcounts L and b(U)=# masks intersecting U >= k for every U. Let B(k) be minimum number N of columns. FYX dual w=(86:4,101:8,123:1,281:2,346:1,394:9,412:1,460:1,602:5,673:9,788:6) sums to 47 and gives w(hit S)<=1+19 popcount(S). Thus N>=47k-19L. 

**Theorem:** equality B(k)=47k-19L holds if and only if k>=19t. At equality the mask multiset is unique (up to physical column permutation).

Proof: equality forces every weighted support to have exactly k distinct hit columns and every used mask to be dual-tight. The tight masks in ascending order are (1,2,3,4,8,16,64,128,144,192,256,512). The 11 weighted-support equations plus the query-count equation form a square integer matrix of determinant 1 (exact check below). Write z=(k-8t)/11, an integer because t=-26k mod 11. Its unique solution is
(3z+2t,2z+t,3z+2t,4z+3t,z+t,z,z,2z,t,t,3z+2t,3z+2t).
N=23z+15t=47k-19L and L=26z+19t. For all 50 supports the distinct-hit surplus b(U)-k is one of
{-t+z,0,2t+3z,2t+4z,2z,3t+4z,3t+5z,4t+6z,5t+8z,6t+9z,t+2z,t+3z,t+z,z}.
In particular masks 211 and 243 require z>=t. Conversely z>=t>=0 guarantees every multiplicity and surplus nonnegative. This is equivalent to k>=19t, finishing both directions. The uniqueness refers to static blocks of fixed minimum query cost only.

Threshold by k mod 11: r=(0,1,2,3,4,5,6,7,8,9,10), t=(0,7,3,10,6,2,9,5,1,8,4), first equality k=(0,133,57,190,114,38,171,95,19,152,76) (r=0 positive starts at 11; k=0 empty block). Last failing k is 179. Thus every k>=180 satisfies exact equality, and B(k+11)=B(k)+23 there. The theorem gives an explicit construction without MILP for unbounded k.

## All-phase adaptive onset reduced to one column

Let M_h=min{m>h: Q_h(m)=m+c_h}. For k=h-4 >=1, L=k+c_h-6 by FYW. Use exact B(k) above and FYX packed block transport with base h=4,m=9,c=6. The transport gives an optimal tree on 9+B(k) columns; if all block probes zero, b(U)>=k holes consumed and base strategy on untouched columns applies; if a positive occurs, FYX's first-positive bound restores all labels within m+c_h. Hence M_h<=9+47k-19L=28h-19c_h+11 whenever k>=19t. FYX all-phase lower is M_h>=28h-19c_h+10. Consequently for EVERY h>=184 (and the earlier phase-specific thresholds above plus 4),

**28h-19c_h+10 <= M_h <= 28h-19c_h+11.**

For each residue of h modulo 11, the lower endpoint increases by 23 per period; each phase has only two adjacent possible offsets. The earlier FYX one-column gap for r=0 is now extended to every residue, not just the phase-5 family. No resolution of M15=31 vs 32 here. The FYY monotone transport argument gives M_(h+11)<=M_h+23, so each of the eleven binary offsets can drop at most once after its own threshold and then stabilize. This does not supply the actual drop points.

## Exact reproduction, executed with Python/SymPy

```python
import sympy as sp
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
S=[1,2,3,4,8,16,64,128,144,192,256,512]
w={86:4,101:8,123:1,281:2,346:1,394:9,412:1,460:1,602:5,673:9,788:6}
assert [s for s in range(1,1024) if sum(v for u,v in w.items() if s&u)==1+19*s.bit_count()]==S
assert all(sum(v for u,v in w.items() if s&u)<=1+19*s.bit_count() for s in range(1,1024))
z,t=sp.symbols('z t');k=11*z+8*t
n=[3*z+2*t,2*z+t,3*z+2*t,4*z+3*t,z+t,z,z,2*z,t,t,3*z+2*t,3*z+2*t]
slacks={u:sp.expand(sum(v for s,v in zip(S,n) if s&u)-k) for u in F}
print('z-t supports',[u for u,v in slacks.items() if v==z-t])
assert all(v.coeff(z)>=0 and v.coeff(t)+v.coeff(z)>=0 for v in slacks.values())
A=sp.Matrix([[int(bool(u&s)) for s in S] for u in w]+[[s.bit_count() for s in S]])
assert A.det()==1
assert A*sp.Matrix(n)==sp.Matrix([k]*11+[26*z+19*t])
print('det',A.det(),'slacks',sorted(map(str,set(slacks.values()))))
print('thresholds',[(r,(-26*r)%11, min(k for k in range(r,250,11) if k>=19*((-26*r)%11))) for r in range(11)])
print('last failure',max(k for k in range(250) if k<19*((-26*k)%11)))
print('all checked')
```
Actual output:
```
z-t supports [211, 243]
det 1 slacks ['-t + z', '0', '2*t + 3*z', '2*t + 4*z', '2*z', '3*t + 4*z', '3*t + 5*z', '4*t + 6*z', '5*t + 8*z', '6*t + 9*z', 't + 2*z', 't + 3*z', 't + z', 'z']
thresholds [(0, 0, 0), (1, 7, 133), (2, 3, 57), (3, 10, 190), (4, 6, 114), (5, 2, 38), (6, 9, 171), (7, 5, 95), (8, 1, 19), (9, 8, 152), (10, 4, 76)]
last failure 179
all checked
```

## FYY continuation preservation and new small-block experiments

FYY prior local evidence pack.py, pack.out, terminal.py, last.py remains in conversation attachment custody. Its eventual onset periodicity proof is the integer monotonicity argument above. Earlier small-block integer optimization reported feasible counts B=(0,1,4,4,6,9,9,12,16,15,18,23) for k=0..11; not all had independently verified optimality. New MILP search for k=12..22, minimum query cost, exact integer witness validation on all 50 supports, reported feasible column counts (21,24,24,27,31,30,33,38,36,40,46). Optimizer reported optimal for each; exact global optimality beyond the dual-equality theorem not asserted. This improves the earlier disjoint-period packing in multiple cases. FYY terminal M15=31 compatible-state replay was reported complete, but earlier positive branches and overall tree remain unfinished; prior logs are historical, not rerun in this turn. Exact preservation of those files still needed if absent remotely.

Control: historical author EM-DIRECT-23537B / TASK_RESEARCH; current Sites identity-only check succeeded but original registration/owner receipt lookup encountered BACKEND_IDENTITY_CHECK_UNAVAILABLE with operation_sent=false; no shared CLAIM, no protected Activity write. Independent research file only. Status AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED. Next: classify equality at adaptive lower endpoint by exploiting the same tight-mask matrix with exactly one deficient support (394 or 673); then solve positive branches including M15.