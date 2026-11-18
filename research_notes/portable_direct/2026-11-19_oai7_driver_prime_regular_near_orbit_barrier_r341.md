# OAI7 r341 — Exact regular near-orbit obstruction: zero auxiliary seed, perfect terminal marginals, but maximal small-list tail

Date: 2026-11-19. Status: author-side mathematical construction, exact proof and a finite exhaustive crosscheck; **not** an independent Native Driver review, frozen Result, Activity/Source acceptance, Task completion, or native X6/Port/Link realization. This builds on the source-pinned external finite cyclic model of r307, r330, r336–r340. Historical OAI7 researcher **EM-EMF6D046-5A2844** and all previous mathematical contributors retain their actual attribution. The present Driver context shares earlier author-side derivations and must not be counted as a clean independent review.

## 1. A quantitative near-orbit obstruction

Let p be prime, 1 <= u,n < p, n+u-1 < p, and let W={0,1,...,n-1}, K={0,1,...,u-1} in F_p. Fix any nonnegative integer threshold h and any p labeled n-element sets C_t, t in F_p. Put
```
V_C(K) := #{ x in F_p : |(x+C) intersect K| <= h },
r_t := |C_t \ (W+t)| = |(W+t) \ C_t|,
B := p-(n+u-1),
D := [B-p^(3/4)]/(2u).
```
Assume D>0. Under the uniform row distribution t~Unif(F_p), its worst deterministic-test-set tail satisfies
```
q := max_{|K'|=u} Pr_t{V_{C_t}(K')>p^(3/4)}
  >= #{t : r_t<D}/p.                            (341.1)
```
In particular, if q<=zeta<1, then at least (1-zeta)p rows require r_t>=D and
```
sum_t r_t >= (1-zeta)pD.                       (341.2)
```
The claim holds even if the C_t are p distinct rows of an exactly n-regular incidence design. No randomness/independence across its rows is assumed.

**Proof.** The set of x for which (x+W) meets K is K-W={-(n-1),...,u-1}, of size n+u-1 (no wrap collision under the stated assumption). All other x have intersection count zero, hence V_W(K)>=B. Translation of W merely translates the starts, so V_(W+t)(K)=V_W(K). Exchanging one removed shift a for one inserted shift b can change the overlap count only at starts x with x+a in K or x+b in K, at most 2u starts. Exchanging r_t shifts changes the threshold indicator at at most 2ur_t starts, so
```
V_(C_t)(K) >= B-2u r_t.
```
If r_t<D, this is strictly above p^(3/4), giving (341.1). The number of bad rows must be <=zeta p if q<=zeta; every remaining row has r_t>=D, giving (341.2). QED.

For the sharp second-order OAI7 length n=ceil(c_* sqrt(p)[log p-2log log p+d]), u=ceil(sqrt p), any fixed d, and large primes,
```
D = (1/2+o(1))*sqrt(p).
```
Thus any q=o(1) p-row design made by editing the interval-translation orbit must alter **at least (1-o(1))p rows by Omega(sqrt p) swaps each**. Sparse row substitutions or O(1)-edit local switches cannot solve this particular all-K tail obstruction. This is an orbit-relative obstruction, **not** a universal nonexistence theorem for all p-row regular codebooks.

## 2. An explicit p-row n-regular non-orbit family with q=1

Let 2<=n, p>2n+u+1, and start from all p translates R_t=W+t, t in F_p. Modify only rows 0 and n by an incidence-preserving 2-switch:
```
C_0 = (R_0 \ {n-1}) union {n},
C_n = (R_n \ {n}) union {n-1},
C_t = R_t for all other t.
```
The swapped elements belong exclusively to their original row within this pair. Each row still has n elements, and every field element still appears in **exactly n rows**, since the global multiset of incidences is unchanged. The two altered sets are nonconsecutive, so neither equals any original interval translate; they are distinct from each other, and the p codebook sets are pairwise distinct. The codebook is therefore a genuine non-orbit, n-regular p-row example, outside the synchronized two-shape selection class excluded by r340.

By the finite n-regular bipartite matching decomposition (r337), there is a **deterministic permutation ordering** for each row so every one of the n columns contains each field element exactly once among the p ordered rows. Choose one of these p ordered schedules uniformly, with **no auxiliary seed**. Each position shift is uniform over F_p, and the joint vector is supported on p distinct rows, so
```
H(H)=log p,  L(H_l)=Uniform(F_p) for every l.   (341.3)
```
The exact same property holds for diagonal integer representatives h_l=([v_l]_p,...,[v_l]_p) in Z^k. For any independent finite integer-valued Y, the complete Z^k-valued marginal laws L(Y+h_l) agree. For independent Y_j uniform on the standard representatives of F_p\B_0, the signed terminal residues ±(Y_j+v_l) are actually **uniform on F_p**: convolution with an independent uniform shift is uniform. Hence all signed terminal coordinates satisfy every ordinary (tau,beta)-coverage assertion with tau<1.

Nevertheless, all r_t are 0 except r_0=r_n=1, so for sufficiently large p, D>1. By (341.1), for the single fixed interval test K,
```
V_(C_t)(K)>p^(3/4) for every t; therefore q_c=1
```
for every positive signed coordinate; for negative coordinates use -K. Thus the r307 **small-list tail sufficient condition fails maximally**, while equal full-lattice sample marginals, H(H)=log p, and *perfect terminal signed coverage* all hold. This is not a counterexample to r307's transfer theorem: its hypothesis (IT) is absent. It is an exact witness that (IT) is not necessary for terminal coverage, including in the entropy-minimal p-row regular class.

For k=s=4097, the r307 entropy budget is also satisfied eventually: H(H)=log p, and
```
H(H)+k[-log(1-u/p)] = log p+o(1) < (k/4096)log p.
```
Only the tail hypothesis fails. At the displayed sharp n-scale there is no native Gaussian-prime/X6 inference.

## 3. Complete small-instance crosscheck

Take p=101, n=8, u=11, threshold h=floor((17/64)nu/p)=0, t1=0, t2=8. Enumerate all 101 field starts for every one of the 101 rows above. The computed multiset of V_(C_t)(K) is **99 copies of 83 and 2 copies of 82**; the comparison threshold p^(3/4)=31.8596521910... . All 101 unordered rows are distinct, and every symbol has incidence degree 8. Thus q=1 for this K. This checks the finite witness; the universal/asymptotic statements follow from the exact proofs above, not from the enumeration.

Reproducer (Python 3; exhaustive in all 101 rows and starts):
```python
from collections import Counter
from math import floor
p,n,u=101,8,11
K=set(range(u)); W=set(range(n))
rows=[{(a+t)%p for a in W} for t in range(p)]
rows[0]=(rows[0]-{n-1})|{n}
rows[n]=(rows[n]-{n})|{n-1}
h=floor((17/64)*n*u/p)
def V(C):
    return sum(sum((x+a)%p in K for a in C)<=h for x in range(p))
assert len({frozenset(C) for C in rows})==p
assert all(sum(a in C for C in rows)==n for a in range(p))
assert Counter(map(V,rows))==Counter({83:99,82:2})
assert min(map(V,rows))>p**.75
```

## 4. Relation to existing results and frontier

- r307 [@baaaabaacaf8](https://github.com/awdawmip/enterprise-math/blob/baaaabaacaf8543f62a45a00cdfcf03e95389075/research_notes/driver/2026-11-18_oai7_integrated_list_tail_transfer_r307.md): sufficient integrated-tail criterion, not necessity.
- r330 [@67f57ab66249](https://github.com/awdawmip/enterprise-math/blob/67f57ab662493b6744df560c8358a293a08d1165/research_notes/portable_direct/2026-11-18_oai7_driver_fixed_index_nonuniform_codebook_sharp_loglog_r330.md): existential all-K codebook at the sharp n-scale, not necessarily n-regular.
- r336 [@e56f4a1ad634](https://github.com/awdawmip/enterprise-math/blob/e56f4a1ad63405c30c392a2c22c1f57cea194128/research_notes/portable_direct/2026-11-18_oai7_driver_sharp_entropy_lowtail_failure_ap_robustness_r336.md): individual arithmetic-progression Hamming barrier; the present note lifts it to quantitative **whole-codebook** edit mass with exact regularity.
- r337–r339 [@cf352564](https://github.com/awdawmip/enterprise-math/blob/cf352564a8f985fbc3151783fa0ee74f1a0b2a7f/research_notes/portable_direct/2026-11-18_oai7_driver_zero_overhead_equal_marginal_codebook_criterion_r337.md): exact zero-seed matching, uniform-capacity and prime-p saturation tools.
- r340 [@3199143e](https://github.com/awdawmip/enterprise-math/blob/3199143e838bb495dd9d9b7bb1047fefddfc1511/research_notes/portable_direct/2026-11-18_oai7_driver_prime_translation_two_shape_switching_r340.md): synchronous two-shape orbit switching no-go; the 2-switch here is not of that prohibited form.
- Original published task: `RS-OAI7-028-C-20261007-6F2A81` / `TP2-96FAC49786245691AE19`; parent `OBJ-OAI7-RESEARCH-TRANSFER-20261007`. Neither this note nor its failed tail certificate completes the parent, and no Native Result/Source/Activity review authority is inferred.

**Next discriminating question:** characterize regular p-row incidence designs far (at least Omega(sqrt p) row edits on a 1-o(1) fraction) from every *obstructed* interval-like translation orbit, and test whether a genuinely different design can simultaneously realize the sharp all-K certificate and deterministic equal-marginal ordering. A separately verified Native reviewer is still needed for official admission of any of these author-side results.


## Later exact sharpening (r342, 2026-11-19)

The preceding estimates with `2ur_t` and cutoff `D=(B-p^(3/4))/(2u)` remain correct as conservative bounds. The subsequent [r342 one-sided threshold-list edit lemma](https://github.com/awdawmip/enterprise-math/blob/b8790284f7e1ee102b5de27d2060004518e52912/research_notes/portable_direct/2026-11-19_oai7_driver_monotone_shift_edit_bound_r342.md) proves the sharper general inequality `|V_C(K;h)-V_W(K;h)|<=u*r_t` for equal-size shift sets. Accordingly, all r341 near-orbit assertions strengthen by replacing the cutoff with `D_sharp=(B-p^(3/4))/u=(1+o(1))*sqrt(p)` at the second-order OAI7 length. The r341 2-switch witness and its computed `q_c=1` are unchanged. This is an author-side mathematical correction/strengthening, with original author/contribution and Native review boundaries preserved.
