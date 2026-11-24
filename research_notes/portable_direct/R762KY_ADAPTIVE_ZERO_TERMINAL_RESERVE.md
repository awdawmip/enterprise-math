# R762KY — Exact adaptive zero-terminal reserve atlas

2026-11-24. AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED. Portable continuation of R762KX at 12c5d3af04cec46e8922f84785ac7eb04ba7164a:research_notes/portable_direct/R762KX_TEN_EVENT_CYCLE_OBSTRUCTION.md, blob c791bcb45ab6c443fc3e3423a3de337a8e45482f. Frozen P000 and joint observer companion at a72226e2430ffa4786321ac86e7f0c599d5f0389; ACTIVE worldview read. Original registration r3-20261124-0124-own-research-registration-v1 SUCCEEDED; EM-DIRECT-82A007, RA-708BCC309CE076D8BB599B91. Own recovery r3-20261124-1020-own-recovery-read-v1 shows no RUN, execution_authorized=false. Previous inventory r3-20261124-0920-owner-read-v1 SUCCEEDED, nonauthorizing; new inventory r3-20261124-1020-owner-read-v1 QUEUED at initial submission. No shared task adopted.

## 1. Exact scoped observer and truncation theorem

In the unsigned auxiliary cube model of KX, each support s has three event masks M_s, the nonzero vectors of a 2-dimensional binary space H_s. For any fixed prefix support schedule with inventory p, let P(p) be the XOR set of all its ordered words, ignoring mixedness of the prefix itself. A fixed suffix support schedule of inventory t compensates EVERY prefix word to specified final boundary b if and only if b XOR P(p) is contained in P(t). The suffix word may depend on the actual prefix word, but the suffix schedule must be chosen independently of that word. The two schedules can have arbitrary order; XOR is commutative, and the actual words are not identified with each other.

For each support, the 0-fold sum is {0}, 1-fold sum is M_s, 2-fold sum is H_s (equal choices give zero, distinct choices give the third), and H_s+M_s=H_s. Thus clipping p and t componentwise at 2 leaves P unchanged. For raw universal compensation to any fixed b, the minimum over all suffix inventories is attained among 3^8=6561 clipped inventories. For b=0, t=clip(p) always works, and KX supplies another universal upper bound 11. The exact cost is
k(p)=min { sum(t) : t in {0,1,2}^8, P(p) subset P(t) }.
This is a sufficient and necessary reachability criterion for this observer, not a quotient of source histories, counts, signs, or ordered BRC operations.

## 2. Full zero-terminal atlas

Independent exact Python bitset enumeration of every clipped prefix against all suffix candidates in nondecreasing event cost gives the following complete histogram (prefix clipped cost, minimum suffix cost, number):
(0,0,1), (1,1,8), (2,2,36), (3,3,112), (4,4,266), (5,5,504), (6,6,784), (7,7,1016), (8,7,6), (8,8,1101), (9,8,24), (9,9,992), (10,9,60), (10,10,724), (11,10,120), (11,11,384), (12,10,12), (12,11,254), (13,11,112), (14,11,36), (15,11,8), (16,11,1).

All 6561 are covered, 633 need strictly fewer suffix events than their clipped prefix cost. In particular among the 784 cost-ten prefixes, 60 can be universally returned to zero with nine events; among 504 cost-eleven prefixes, 120 need only ten. These are exact minima, not just constructions. For arbitrary unbounded prefix inventories the raw minimum is precisely the corresponding clipped atlas entry.

For each of the 633 strict reductions an optimal suffix with a doubled support exists (executed additional assertion). It also suffices for mixedness of the entire prefix+suffix word: if a chosen return word is monochromatic, replace the two equal events of a doubled suffix support with two equal events of another color. The XOR is unchanged, and the nonempty prefix retains the original color. Hence the same exact minimal costs hold on these 633 types for the observer requiring the joint word to be mixed, also for all original inventories with these clipped types. We do NOT assert the same equality for the unreduced types, or when the suffix itself must be mixed.

## 3. Subspace-prefix structure

For prefixes with every occupied support used at least twice, P is a binary subspace. With a occupied supports the complete counts (a, minimum, number) are:
(0,0,1),(1,2,8),(2,4,28),(3,6,56),(4,7,6),(4,8,64),(5,9,24),(5,10,32),(6,10,12),(6,11,16),(7,11,8),(8,11,1).
For a fixed occupied set A and suffix restricted to the same A, a relaxed representation of a target is a coset of the cycle space of Q3[A] (KW). At singleton vertices the forbidden fiber is the local projection equal to the corresponding relaxed triple. Since the prefix ranges over the whole relaxed image, all choices of forbidden values are possible. Therefore saturation is equivalent to the absence of any covering by one forbidden local fiber per singleton. If Q3[A] is a forest, the kernel is trivial: every support must be doubled, so restricted minimum 2a. If Q3[A] has exactly one cycle, the kernel has two elements. A singleton off that cycle forbids the entire kernel for some target; two singletons on the cycle can forbid its two elements; one singleton on the cycle always leaves a solution. Thus restricted minimum 2a-1 in the unicyclic case. (This argument is not a lower bound for suffixes with extra outside supports; global minima above are obtained by exhaustive classification.)

Example: prefix (0,0,0,0,2,2,2,2) occupies a cube face; suffix (0,0,0,0,1,2,2,2) of cost 7 works for all prefix words. Example: prefix (0,0,2,2,2,2,2,2), suffix (0,0,1,2,1,2,2,2) of cost 10 works. These are globally optimal in the exact atlas. The universal 11-event reserve from KX is unnecessary for these specified prefix populations.

## 4. Reproducible exact Python computation (executed)

Bit index r denotes boundary r. XOR translation by 2^j swaps pairs of bits in each block of length 2^(j+1). OR is union; AND equality is subset inclusion. Every stock has a predecessor obtained by lowering its first nonzero coordinate; lexicographic order guarantees it is already computed. Sorting all suffix stocks by total cost proves the first feasible cost is minimal. All arithmetic is exact Python integer arithmetic. No floating point, Monte Carlo, or assumption of symmetry is used.

```python
from itertools import product
from collections import Counter,defaultdict
D=4096
ALL=(1<<D)-1
lo=[sum(1<<i for i in range(D) if not(i>>j&1)) for j in range(12)]
def tr(x,e):
    while e:
        q=e&-e;j=q.bit_length()-1;l=lo[j]
        x=((x&l)<<q)|((x&(ALL^l))>>q);e^=q
    return x
masks=[]
for i,j,k in product(range(2),repeat=3):
    a=1<<(2*i+j); b=1<<(4+2*i+k); c=1<<(8+2*j+k)
    masks.append((a|b,a|c,b|c))
def step(x,s):
    return tr(x,masks[s][0])|tr(x,masks[s][1])|tr(x,masks[s][2])
R={(0,)*8:1}
for t in product(range(3),repeat=8):
    if not any(t):continue
    j=next(i for i,n in enumerate(t) if n)
    u=list(t);u[j]-=1
    R[t]=step(R[tuple(u)],j)
bycost=sorted(R,key=sum)
res=Counter(); reduced=Counter(); stable=Counter(); witness={}
for p,P in R.items():
    m=next(s for s in bycost if (P & R[s])==P)
    a=sum(p);b=sum(m)
    res[a,b]+=1
    if b<a:reduced[a,b]+=1;witness.setdefault((a,b),(p,m))
    if 1 not in p: stable[sum(x>0 for x in p),b]+=1
print('all prefix counts',sum(res.values()),'reduced',sum(reduced.values()))
print('histogram', sorted(res.items()))
print('subspace', sorted(stable.items()))
print('witness',witness)
for p,P in R.items():
    k=next(sum(s) for s in bycost if P&R[s]==P)
    if k<sum(p):
        assert any(sum(s)==k and 2 in s and P&R[s]==P for s in bycost)
print('all 633 reduced prefixes have double-containing optimal suffixes')
```

Observed outputs: total 6561, reduced 633, full histograms as in sections 2 and 3; all double assertions passed. The witness inventory pairs in section 3 use the same lexicographic support order as KX. This is an author exact finite proof plus arbitrary-stock clipping argument; independent review pending.

## Next

Extend the atlas to b!=0 (coset-dependent reserve) and determine which zero-terminal minima admit an analytic classification without the finite census. In particular seek a structural lower bound for suffixes that use support vertices absent from the prefix. For unreduced prefixes, classify the mixedness penalty separately; for native signed, time-sensitive BRC and three-axis slice common-depth observers, establish the actual operation/observation mapping before discarding any source distinction.
