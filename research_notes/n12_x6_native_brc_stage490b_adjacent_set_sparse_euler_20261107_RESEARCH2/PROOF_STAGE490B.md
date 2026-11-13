# Stage490-B — Adjacent fixed-index edits and exact signed Euler–BRC class calculus

Status: AUTHOR-SIDE PROOF + EXECUTED FINITE CHECKS; NOT AN ADMITTED NATIVE RESULT.
Scientific frozen pins inherited unchanged from Stage489-B: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral rules were read separately from canonical global main. Parent: PR #1736, Stage489-B `PROOF_STAGE489B.md`, and `NEXT_TASK_PACKET_490B.md`. This finite ordered-word model uses all twelve signed primitive X6 directions; its mathematics is conditional on the declared observer/operator grammar and does not claim unproved physical dynamics.

## 1. Exact two-site edit lift

Let `D={A,...,L}` denote `+E1,...,+E6,-E1,...,-E6`. Two compared initial histories `(P,Q1)`, `(P,Q2)` have the same initial complete observer: word lengths, six-component signed native displacements, all 144 directed edge counts separately for P and Q, and overlap-position match count `K(P,Q)`.

Basic operations POP (remove last letter while nonempty), APPEND(z) with public `z∈D` have fixed finite budgets and are applied as identical labeled operation traces to both histories. Write `~0` for equality of *all* legal base-operation observation traces, without assuming the unreviewed Stage486-B proposed closed key.

Add at most one `Q_SET(j,x)` and at most one `Q_SET(l,y)`, where `1<j<l<|Q|` are fixed original one-based absolute positions; each guard checks that the selected position remains internal. Edits retain length and may interleave arbitrarily with base operations. Both replacement symbols range over all twelve signed directions. Let `~{j,l}` denote equality of all legal enlarged traces.

**Theorem 490.1 (exact relative lift):**
```
(P,Q1) ~{j,l} (P,Q2)
iff
(P,Q1) ~0 (P,Q2)
and (Q1[j-1],Q1[j],Q1[j+1])=(Q2[j-1],Q2[j],Q2[j+1])
and (Q1[l-1],Q1[l],Q1[l+1])=(Q2[l-1],Q2[l],Q2[l+1]).
```
The triples here use one-based indices. This is an exact equivalence *partition*, not a claim of coordinatewise irredundancy in every initial fiber.

**Necessity.** The no-edit sublanguage gives `~0`. The one-edit-at-j and one-edit-at-l sublanguages are individually legal, and the one-site identification argument of Stage489-B applies to each: immediate signed-displacement response identifies the overwritten direction, and, choosing a replacement symbol different from the finite local alternatives, the 144 directed-edge response identifies the two neighbors. Thus both original triples must agree.

**Sufficiency.** For any identical operation trace, construct its unedited reference trace by omitting both SETs but keeping POP/APPEND operations. The two unedited observers agree by `~0`. At time t, the edited word differs from its unedited reference only at the subset of `{j,l}` edited and still present; if an index was popped and later reconstructed by APPEND, its reference letter and any new editor replacement are public. The letters of the unedited reference adjacent to an edited original index belong to its initial triple or are publicly appended. Adjacent edits have an overlapping edge, accounted for once by the joint local correction below. Therefore the displacement, all ordered edge counts and overlap-match correction against the reference are identical for both histories. Public length and P corrections are identical. The enlarged observers agree at every step. This proves the theorem for all finite POP/APPEND budgets, all twelve replacement directions and all legal interleavings.

The same argument extends to a finite set of distinct, original fixed interior edit indices, taking the original triple at every such site; overlapping neighborhoods are handled jointly. It does not directly cover changing-relative addresses, insert/delete in the interior, or repeated edits under a new grammar.

## 2. Adjacent-edit interaction is a typed residual

For consecutive sites with original quadruple `(a,b,c,d)` and replacements `b→x,c→y`, write `[uv]` for the basis vector of the ordered directed edge `u→v`. The **exact** two-edit edge change is

`ΔE_joint = -[ab]-[bc]-[cd]+[ax]+[xy]+[yd]`.

If `δ_b` and `δ_c` are the isolated single-edit changes computed against the *original* quadruple, then

`ΔE_joint = δ_b+δ_c+I`,

`I=[xy]-[xc]-[by]+[bc]`.

The signed six-component displacement has no corresponding two-site cross term: `ΔV=v(x)-v(b)+v(y)-v(c)`. The nonzero `I` is a structural overlap residual, not a failure of the triple key. Example `a=b=c=d=A, x=y=B`: `I=[AA]-[AB]-[BA]+[BB]` is nonzero. A method adding separate edge-deltas without `I` loses information about the joint edge.

This identity follows by expanding the three replaced adjacent edges and holds for all 12^6 local symbol combinations algebraically.

## 3. BRC Boolean support, positive population, exact rank/unrank

On any fixed observed directed edge multiset `e` with first symbol s and final symbol t, define integer Euler completion count:

`N(c,r)=1[c=t]` when all edge counts `r` are zero, otherwise
`N(c,r)=Σ_{v:r[c,v]>0} N(v,r-[c,v])`.

The recurrence counts *distinct raw direction strings*, not artificial permutations of identical edges; every nonnegative summand preserves positive source population. For a chosen observer key equal to the first k directions after s, its raw-history mass is `N(last(key), remaining(key))`. Its Boolean support equals 1 iff this mass is positive. Memoized Boolean support on `(last,remaining,depth)` gives exact lexicographic rank and unrank by summing smaller-branch support. This is a typed BRC application: positive population and Boolean support remain separate.

A complete **signed 12-direction** star instance contains once each of the 22 directed edges `A→z,z→A` for the eleven other symbols z. Every Euler trail from A to A consists of the eleven two-edge excursions in some order. For the key of the first three complete excursions (six steps):
`raw=11!=39,916,800`; `classes=11·10·9=990`; each key has `8!=40,320` raw histories. This is a complete closed-form independent check of the dynamic program and does not require enumerating 39,916,800 strings.

The implementation uses dense 144-entry tuples, a tuple of actual active directed edges (s=22), and a row-keyed sparse tuple-of-tuples. All three use the same exact recurrence and output identical counts/ranks. The bound on state enumeration is `O((n+1)^s)` at fixed s, with integer bit costs additional. There is no claim of polynomial complexity when s grows with input size or of uniform performance dominance.

## 4. Real executed checks (Python standard library, exact integer arithmetic)

- Adjacent-edge identity: 36,864 configurations (`a,b,c,d∈{A,B,G,H}`, `x,y∈D`); interaction nonzero on 30,976.
- Initial-fiber enumeration for `T=ABGABA,W=GH`, H over `{A,B,G,H}` with lengths u=2,3,4,6: respective original histories 16/64/256/4096; fibers 13/46/148/1202. For u≤4 there were 0 nonidentical same-triple pairs (a finite vacuity); for u=6, 720 same-initial-and-same-quadruple pairs.
- Nontrivial u=6 pair `H1=AAAABA,H2=AAABAA` has same full initial observer and same original edit neighborhoods at j=10,l=11. The entire Q-operation graph with at most one Q POP, one Q APPEND and one SET at each site, *all twelve parameters*, was exhausted: 4,394 reachable coupled states, all observations equal. In this concrete family P has length ≤7 with one POP and APPEND, while edits are at indices 10,11: P operations cannot expose a new K distinction; they preserve the pair equality.
- Signed star Euler experiment: all three implementations returned `raw=39,916,800`, `classes=990`, 14,160 DP states and 22,528 recursive transitions; checked ranks 0,330,495,989 with equal key and mass 40,320.
- Independent exhaustive five-excursion check enumerated all 120 raw words, all 20 prefix keys (mass 6 each), and full rank/unrank in each representation.
- Single-run end-to-end Python tracemalloc peaks: dense 18,414,098 bytes, active 5,494,976 bytes, row-keyed 4,613,904 bytes; respective time 0.131/0.091/0.126 seconds in this run. Includes word-to-edge input construction, memoized DP, rank/unrank checks; not a hardware-independent speed claim.

Full author-run source: `REPRO_STAGE490B.py` (local plain copy; corresponding compressed source retained as an extra artifact when published). Complete executed JSON: `STAGE490B_EXECUTED.json` (full local record), with `REPRO_STAGE490B_PORTABLE.py` independently runnable. Code and evidence are published without credentials.

## 5. Scope and continuation

Theorem 490.1 is hand-proved under the stated grammar, not formally verified or independently Driver-admitted. The arithmetic is exact; state counts reflect the declared finite experiment only. The earlier global Stage486 repair key remains unreviewed and is not used as an axiom here. The next question is a moving-address or interior INSERT/DELETE grammar where original neighborhood triples need not suffice, along with faster exact Euler-BRC rank/unrank for growing active edge support.

Native Enterprise Math status/session call in this run returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`: no authenticated CLAIM, Owner observation, Native Result, or independent Driver review is asserted.
