# X6 signed BRC: an exact boundary-state composition law for a declared nonbacktracking path rule

Status: `DRIVER_MATHEMATICAL_AUDIT / PROVED_TYPED_SPECIAL_CASE / NOT_NATIVE_RESULT_ADMISSION`
Date: 2026-11-12 (+08)
Scientific domain: the established full signed X6 Cell-coordinate torsor, `Z^6`; optional explicitly defined path admissibility, not an asserted physical rotation rule.
Authorship/provenance: Driver continuation in the shared F7/X6 research context; not clean-blind independent review. Reuses the signed native step alphabet, Path-formal/N/Weighted-BRC hierarchy and existing contributor results identified below. The local boundary-state construction and its proof are this continuation's scientific increment.

## The precise compositional question

Let `A={+1,-1,...,+6,-6}` denote the **twelve signed native-axis step labels**, with `inv(a)=-a`. A nonempty ordered path word `w=a_1...a_m` starts at a chosen native Cell anchor and ends at displacement
`d(w)=sum_j sign(a_j)e_|a_j| in Z^6`.
For this special-case interface **declare**, rather than infer from P000, the local rule

`NB(w) <=> a_(j+1) != inv(a_j)` at every internal seam.

It forbids immediate inverse-step backtracking. All `NB` words still consist only of the existing primitive signed Cell steps. This rule is a testable *candidate path constraint*; no claim is made that native physical X6 rotations or all BRC paths obey it.

A packet is a finite multiset of internally NB-valid **nonempty** words, with nonnegative integer occurrence counts or multiplicative nonnegative rational letter weights. In `P ⋆ Q`, retain the provenance of the ordered pair `(w_P,w_Q)` and its seam: two different valid splits of the same printed word remain two BRC occurrences. The pair is admitted iff `last(w_P) != inv(first(w_Q))`.

## Theorem A — exact operation-safe two-sided boundary transfer

Over the commutative coefficient semiring `R=N[t,x_1^{±1},...,x_6^{±1}]` (or nonnegative rational coefficients for Weighted-BRC), define the polynomial-valued 12-by-12 matrix of a finite path packet `P` by

`F_P[u,v] = sum_{w in P; first(w)=u, last(w)=v} mult(w) t^|w| x^d(w)`,

where `x^d=prod_i x_i^{d_i}`, counting all occurrences/provenances. Define the fixed seam matrix

`J[v,u]=1 if u != inv(v), else 0`.

Then for any two nonempty NB-valid packets,

`F_(P ⋆ Q) = F_P J F_Q`.

For three such packets the packet composition and matrix law are associative:

`(F_P J F_Q) J F_R = F_P J (F_Q J F_R)`.

**Proof.** Every retained compositional occurrence is uniquely specified by an ordered input occurrence pair and its explicit split. Its terminal labels are `first(w_P)` and `last(w_Q)`, its displacement and event length add, and its multiplicative weight multiplies. The seam is admissible precisely when `J[last(w_P),first(w_Q)]=1`. Matrix multiplication sums each permitted intermediate label pair exactly once per ordered occurrence pair, giving the displayed equality. Associativity follows from associativity of pairwise concatenation with fixed seam predicates and the semiring matrix product. QED.

The resulting exact endpoint-length N-BRC generating series is `sum_(u,v) F_P[u,v]`, and setting all `x_i=1` yields the length mass. Setting `t=1` yields the signed endpoint mass. `F_P` keeps only the first/last signed axis labels **plus** endpoint-length weights, rather than full internal word order; within this declared NB-composition operation, that finite-state quotient is sufficient.

Empty words can be accommodated by a separate START/EMPTY identity component. The theorem itself concerns nonempty packets, for which no such special case enters the matrix formula.

## Theorem B — sharp right-extension memory lower bound

Even if an observer already retains exact signed endpoint `d(w)`, length `|w|`, and the **full histogram of all twelve signed step labels**, a single right-extension interface for arbitrary NB words requires at least twelve distinct nonempty terminal-step states.

**Proof.** Consider the cyclic twelve-letter word

`c=(+1,+2,+3,+4,+5,+6,-1,-2,-3,-4,-5,-6)`.

It is NB even across its cyclic closing seam. Its twelve cyclic rotations `c_k` are valid paths with the *same* endpoint zero, length 12, and histogram having exactly one occurrence of every signed label. Their final labels range over all twelve members `a in A`. For any two different final labels `a != b`, append the one-step word `inv(a)`: the extension of the path ending in `a` is forbidden, while the extension of the path ending in `b` is allowed. Thus all twelve share identical retained endpoint/length/histogram data yet have pairwise distinguishable future admissibility. Any universally correct deterministic right-extension state interface must distinguish all twelve. Storing `last(w) in A` suffices, so the bound is exact. QED.

For the three-axis signed slice the same argument with
`(+1,+2,+3,-1,-2,-3)` gives a sharp **six-state** terminal memory bound. If an empty prefix must also be represented in this one-step extension automaton, it needs a distinct START state (all twelve next letters allowed).

An elementary two-word discriminator is
`w_1=(+1,+2)`, `w_2=(+2,+1)`: they have the same endpoint `(1,1,0,...,0)`, length 2 and signed histogram, yet appending `-1` succeeds after `w_1` and fails after `w_2`.

## Exact finite check, not used as the universal proof

Enumerate all nonempty three-axis signed words of lengths 1–2 for packet P (36 valid words), and lengths 1–3 for Q (186 valid words), each with unit occurrence weight. Directly filter the `36*186` ordered pairs for NB-valid concatenation and compare their indexed endpoint/length/first/last counts with the polynomial-matrix law. Result: **5,580 admissible pairs; zero coefficient discrepancies**. Independently verify the twelve cyclic rotations above have zero native displacement, identical signed histogram and all twelve distinct terminal labels. These are exact integer enumerations; Theorems A and B are proved algebraically.

Reproducible pseudocode for the core check:

```python
from itertools import product
A = (1,-1,2,-2,3,-3)
valid = lambda w: all(v != -u for u,v in zip(w,w[1:]))
P = [w for n in (1,2) for w in product(A,repeat=n) if valid(w)]
Q = [w for n in (1,2,3) for w in product(A,repeat=n) if valid(w)]
assert (len(P),len(Q)) == (36,186)
assert sum(valid(p+q) for p in P for q in Q) == 5580
# Index by (first,last,length,signed_endpoint), then compare
# packet-pair filtered counts to F_P @ J @ F_Q coefficientwise.
```

## Relation to the current X6 upper-structure task

This is a **constructive operation-safe BRC path quotient for one declared seam-local relation**. It gives a reusable finite-state composition tool and a sharp boundary-memory lower bound. The stronger current task `RS-X6-NATIVE-ROTATION-DYNAMICS` still asks for a native physical C6 rotation generator on arbitrary triads, its globally generated group, and the actual admissibility/weight law governing rotation path fibers. Those dynamics must be specified and proved before this interface can be identified with native physical rotation.

Previously verified sources retained without reassigning authorship:
- `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` (signed twelve-step Cell adjacency; Path-formal and N-BRC remain distinct; immutable Source Git blob `e266c103cae02550c8bbaa794958f3423b41d151`).
- `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` (Path-formal → N-BRC → Boolean-BRC, blob `97ab1403ab04b4fa80034625fb1b2e3ed115e59b`).
- `research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md` (full signed endpoint kernel, blob `aa005cd62c45d7f4105632257db9186b115c5b29`).
- `research_notes/driver/2026-11-12_x6_diagonal_quotient_minimal_native_lift_energy.md` (separate endpoint reconstruction, blob `92e8547e856a273cc33621b7dbea8644c5ce768e`).
- Task `RS-X6-NATIVE-ROTATION-DYNAMICS`, immutable publication `TP2-6A1F9D8C2047E3B51C01`, parent `PO-X6-UPPER-STRUCTURE-20260906` under actual frozen signed-X6 source, with existing authorship and task ownership preserved.

Review/admission: Driver-authored scoped theorem note, not a clean-independent reference pass, formal native review/Result admission, new Task, CLAIM, physical-rotation identification or mother-objective closure.

## Corollary C — exact C6 two-branch microtrace population under the declared NB rule

The earlier restricted local native C6 construction (original researcher `EM-FREE-7D3C9A`, `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md`, pinned task-source Git blob `e8185ae28bef4d55c50622848b225c0b5e3125aa`) has six unit-shell phases `a_r` (indices mod 6), with `a_(r+3)=-a_r`, adjacent phases on different signed axes, and two shortest primitive microtraces for each macrotransition `a_r -> a_(r+1)`:

- `I_r=(-a_r,+a_(r+1))`: INNER, through the pivot Cell `0`;
- `O_r=(+a_(r+1),-a_r)`: OUTER, through native Cell `a_r+a_(r+1)`.

All these are legal signed unit-axis steps and each two-step word is internally NB. For consecutive macrosteps `r,r+1`, the NB seam is forbidden **if and only if** the branch pair is `(I_r,I_(r+1))`. Indeed `I_r` ends `+a_(r+1)` and `I_(r+1)` begins `-a_(r+1)`. The other three seam types are legal by the distinct signed-axis labels at neighboring phases and the antipodal relation at a three-phase offset. Hence the exact NB condition on a sequence of local C6 macrobranches is simply **no two consecutive INNER choices**.

Let `f_n` count split-provenance-preserving legal choices along an open sequence of `n` forward C6 macrosteps. With `F_0=0, F_1=1` denoting Fibonacci numbers,

`f_n=F_(n+2)`.

For a cyclic sequence of `n` C6 macrosteps, when the closing last-to-first primitive seam is also required NB (a repeatable closed path), the count is

`g_n=tr([[1,1],[1,0]]^n)=F_(n-1)+F_(n+1)=L_n`,

where `L_n` is the Lucas number. This follows from the two-state transfer on branch choices `{O,I}`: `O` may be followed by `O` or `I`, whereas `I` must be followed by `O`. For one complete C6 phase circuit (`n=6`), all `2^6=64` shortest two-step branch sequences return to the start unit-shell Cell after twelve primitive steps, but precisely

- **21** have no immediate inverse turn along the 12-step *open* word;
- **18** also satisfy the cyclic closing seam and can be repeated without immediate inverse at the joining point.

These counts are native Cell-path **occurrence counts for the declared NB refinement**, with all branch choices retained as provenance. They do not claim a selection law for the physical rotation. Requiring all intermediate microphase directions to remain nonzero selects the unique all-OUTER loop, a different (stronger) rule already justified at its restricted scope in the original C12 source.

Exact integer verification uses the legitimate carrier-phase ordering
`a=(+1,-3,+2,-1,+3,-2)` as signed native-axis labels, enumerates all 64 six-branch strings, expands each branch by the two words above, and checks internal and closing seams separately:

```python
from itertools import product
a = (1,-3,2,-1,3,-2)
word = lambda r,b: (a[(r+1)%6],-a[r]) if b=="O" else (-a[r],a[(r+1)%6])
ok = lambda w: all(v != -u for u,v in zip(w,w[1:]))
seq = [(b,tuple(x for r,s in enumerate(b) for x in word(r,s)))
       for b in product("OI",repeat=6)]
open_ok = [(b,w) for b,w in seq if ok(w)]
cyclic_ok = [(b,w) for b,w in open_ok if w[-1] != -w[0]]
assert (len(seq),len(open_ok),len(cyclic_ok)) == (64,21,18)
assert all(sum((1 if x==j else -1 if x==-j else 0) for x in w)==0
           for b,w in seq for j in (1,2,3))
assert all(all(not (b[r]=="I" and b[(r+1)%6]=="I") for r in range(6))
           for b,w in cyclic_ok)
```

**Scientific use:** this provides a concrete exact `C6`-macrostep instance of the operation-safe matrix transfer theorem, identifies the local seam-memory variable, and computes the branch-population effect of a precise candidate microtrace constraint. The remaining dynamical selection question is whether the actual X6 native physical rotation grammar adopts NB, nonzero-phase refinement, another path constraint, or a typed combination.
