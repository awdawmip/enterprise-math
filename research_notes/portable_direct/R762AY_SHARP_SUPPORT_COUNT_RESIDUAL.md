# R762AY — Sharp source-support growth bounds and observer-minimal frame-count BRC residual

2026-11-15 | Task RS-X6-TRIADIC-CLOSURE-DYNAMICS | Researcher EM-X6-44BACF | SID MCP-8b844b9054c94d40aaed0131426d3935 | Activity RA-2BFD679DF2B3D27CAA0CB7D5.

Status: AUTHOR-PROVED / EXACT-FINITELY-TESTED / NOT_INDEPENDENTLY_REVIEWED. Source research model is the conditional sequential directed-cycle token-PASS scheduler of R762AX, not a native signed-force TRIADIC_CLOSURE_E realization. Frozen P000 science input: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Nothing here weakens or changes P000, and no V17/V29/V39 physical interface is claimed.

## 1. Exact population and observed histories

Fix integer m>=2, ports Z/mZ with named directed events e_i:i→i+1. A complete macro uses each e_i exactly once, in an arbitrary permutation word; firing e_i requires a positive source inventory immediately beforehand, transferring one token to the target. For K in N_0^m set S(K)={i:K_i>0} and h=|S|. Every legal complete macro restores K exactly.

For nonempty S={s_1,...,s_h} listed cyclically, let ell_i be the positive clockwise distance in edges from s_i to s_(i+1) (cyclically, so sum ell_i=m). R762AX proves the sharp exact count

\[
q_m(S)=\frac{m!}{\prod_{i=1}^h \ell_i!},\quad h>0,\qquad q_m(\varnothing)=0.
\]

This number counts distinct named legal event-order words, not positive-state support, signed amplitudes, V25 winners, or measured force configurations.

## 2. Sharp extremal theorem at fixed occupied-port count

**Theorem AY1 (all m, all h).** For each m>=2 and h in {1,...,m}, define a=floor(m/h) and b=m-ah, so 0<=b<h. Across all supports S of cardinality h,

\[
\boxed{\frac{m!}{(m-h+1)!}\ \le q_m(S)\ \le\
\frac{m!}{(a!)^{h-b}((a+1)!)^b}}.
\]

Both bounds are attained. The lower extremizers have cyclic gaps (m-h+1,1,...,1) up to permutation of gaps, i.e. all unoccupied vertices occur in one gap. The upper extremizers have b gaps of size a+1 and h-b gaps of size a (distributed in any cyclic order). More precisely, these characterize the extremizers at the multiset-of-gaps level; when the two descriptions coincide, all supports have the same count.

**Proof.** Every positive integer composition ell_1+...+ell_h=m is realized by some occupied support on the labelled cycle, and q=m!/prod ell_i!. If two gaps x>=y+2, replace them by x-1 and y+1. The denominator changes by the exact ratio (y+1)/x <1; hence q strictly increases. Repeating terminates only at balanced gaps, giving the upper bound and its complete gap-multiset equality condition. To minimize q, choose a largest gap x and any other gap y>=2 and replace (x,y) with (x+1,y-1). The factorial denominator is multiplied by (x+1)/y>1, thus q decreases; repeat until every gap except one equals 1. The resulting big gap is m-h+1. The strict exchanges establish minimality and characterize its gap multiset. All steps are exact integer identities for every m,h. QED.

At fixed h, the count is independent of *placement for every support* exactly when h=0,1,m-1,m (with h=0 count defined separately). For 2<=h<=m-2, m>=4, the two extremal gap types differ and the bounds are strict. This makes the precise point at which frame-relative support geometry, rather than occupied-port cardinality alone, becomes a needed count observer input.

Examples: m=4,h=2 has q in {4,6}; m=6,h=2 has min q=6,max q=20; m=6,h=3 has min q=30,max q=90. For m=8,h=3 the exact bounds are 56 and 560. These are not asymptotic approximations.

## 3. A future-safe minimal count residual under fixed frame transport

Fix a **specified** permutation sigma in S_m of the physical port labels. Between complete macros, an external frame transport replaces occupied support S by sigma S (and transports the actual inventory K correspondingly); the physical cycle edges stay fixed. This is a conditional, declared frame rule, **not** an inferred P000/V17 native port-action map. Let d=ord(sigma). Define the length-d *count signature*

\[
R_\sigma(S)=\big(q_m(S),q_m(\sigma S),...,q_m(\sigma^{d-1}S)\big).
\]

Let H_r(S) be the number of full named legal PASS histories consisting of r complete macros, with this inter-macro transport, and H_0(S)=1. R762AX gives

\[
H_r(S)=\prod_{j=0}^{r-1}q_m(\sigma^j S).
\]

**Theorem AY2 (unbounded-horizon exact observer quotient).** For any supports S,T and the fixed specified sigma, the following are equivalent:

1. For every integer r>=0, H_r(S)=H_r(T).
2. For every r in {0,1,...,d}, H_r(S)=H_r(T).
3. R_sigma(S)=R_sigma(T).

Moreover, the transition S→sigma S descends to the quotient by equality of R_sigma, and the resulting quotient is the coarsest exact deterministic state description sufficient to predict all future *history-count* observations H_r for every r>=0, with phase anchored at the current frame. It is not the coarsest quotient for the named-word language.

**Proof.** (3) immediately gives (1) by the product formula and periodicity sigma^d=id; (1) implies (2). For nonempty S all q_m(sigma^j S)>0, so each q_j is recovered exactly as H_(j+1)/H_j for j=0,...,d-1. Equality in (2) thus forces equality of all signature components. The empty support has H_1=0, while every nonempty support has H_1>0, so it forms its own count-equivalence class. Therefore (2) implies (3) in every case. If two supports have the same signature, shifting both one step rotates their signatures; hence sigma preserves equivalence classes and the quotient supports iteration. Any deterministic abstraction preserving all H_r must distinguish supports with unequal H_r, which by the equivalence is exactly unequal signatures; hence the equivalence is the maximal allowed collapse and its partition the minimal sufficient quotient. QED.

A shorter, state-dependent period may replace d if the complete q sequence repeats earlier; d is a universal finite observation certificate, not an asserted irreducible signature length. This quotient is exact only for scalar positive BRC *counts* and the declared sigma transition. It does NOT justify deleting named port positions, event-word provenance, full conditional V25 state-branch multiplicities, signed phase or future operations not in this observer contract.

**Strictly different observers.** AX2 already showed that the complete named first-event language distinguishes every support: the possible initial events are exactly {e_i : i in S}. For the count-only observer, the smaller R_sigma quotient is sometimes safe. For m=4 and sigma=(1 2), take S_1={0,1}, S_2={1,2}, S_3={2,3}. Their signatures are (4,6),(4,4),(4,6), respectively. Hence S_1 and S_2 have identical one-macro counts but are distinguished at the second macro (24 versus 16 histories). In contrast S_1 and S_3 have the same H_r for every r, but different named first-event languages. This gives both an insufficient one-step coarse observer and a certified proper all-horizon count quotient.

## 4. Exact universal growth bounds and tightness

Let 1<=h<=m, and write q_min(m,h) and q_max(m,h) for AY1. Since a port permutation preserves h, every sigma-orbit factor lies between them. Thus for all S of size h, all sigma and r>=0,

\[
\boxed{q_{\min}(m,h)^r\le H_r(S)\le q_{\max}(m,h)^r}.
\]

Both are globally sharp at every r: choose sigma=id and respectively a lower-/upper-extremal support. The per-macro geometric growth factor over a complete sigma orbit of support period p is exactly (prod_{j=0}^{p-1}q_m(sigma^j S))^(1/p) (an algebraic positive real); no numeric approximation, long-horizon extrapolation or physical entropy interpretation is needed. The upper and lower bounds concern complete-macro named token-PASS words. V25 positive-BRC winner multiplicities may add separate factors, so these bounds do not silently apply to full V25 histories before conditioning on that interface.

## 5. Verification, source provenance and actual next research obligation

The companion standalone JS checker performs two independent exact tests: all named permutations of all m-cycle supports for m=2,...,7 (252 support cases, 695480 examined words), simultaneously checking the R762AX q formula and AY1 extrema; and every sigma in S_m, every support, and every support-pair for m=2,...,5 (152 permutations, 4280 frame-support orbits, 66860 support-pair signature/count-horizon comparisons), including a concrete witness test. Factorials are exact JS integers in the tested range, and products of counts use BigInt. The checker and its complete summary JSON are saved alongside this proof. The universal assertions AY1/AY2 have independent symbolic proofs, not finite extrapolations.

Mathematical antecedent: R762AX Draft PR #2462@9dc6cef905642fbc044c10d67d6574ad4a17ba5b, especially AX1/AX2/AX6. Protected source: P000 frozen enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389; present general and task research protocols were read from current canonical main, not used to alter frozen scientific inputs.

**Unfinished native question.** Read actual admitted P000 TRIADIC_CLOSURE_E signed Cell/Link/Port events, how microstep enabling/pre-reservation works, actual V17 frame-to-port map beta, and the V39 based-loop observer. Test whether an exact homomorphism from native signed event histories to this token scheduler exists and whether the count-only residual R_sigma factors through the native observer. If not, preserve the mismatch and compute the truly sufficient native typed residual; never infer the bridge from the comparator's exact proof.

**Admission:** author proof and finite self-check only; no independent Driver proof review, native Result, or P000 update established by this document.
