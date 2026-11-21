# PREFIX-975 — Minimal signed-source carrier under residual changes; exact odd-slice rank census

Date: 2026-11-21 (Asia/Shanghai). Research author/source: current session `EM-DIRECT-FBEA5D` / `MCP-45ad6d29cd534c1aad25595a72e3c532`, registered on Source by original request `r6-20261121-0807-prefix974-own-research-session-v1` (SUCCEEDED). Historical `EM-DIRECT-58C410` is cited only as predecessor provenance. Scientific status: `AUTHOR_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED`.

## Frozen scientific scope and sources

Frozen input pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; this run does not rebase it. Source predecessor: `research_notes/portable_direct/2026-11-21_r6_prefix974_affine_port_brc_kernel.md` (immutable GitHub commit `4f348faeb98d92490e3bdbda768a5b6965a92eca`). This is the independent **auxiliary odd-gap XOR observer**, not native signed-X6, Heartbeat or physical evolution. P000, ACTIVE discrete worldview and joint-observer preservation remain the project ontology and information-reduction constraints.

For `p>=4`, let `0<=i,j<p`, `s in {+1,-1}`, and numeric residual `c=2^i-s*2^j`. For each c, define `P_c` as the bitset of ports j realized by `s=+1`, and `M_c` for `s=-1`. At an integer source product x, the **signed valid-source carrier** is

    S_c(x) = (S_c^+(x),S_c^-(x))
    S_c^+(x)=P_c & ~x,       S_c^-(x)=M_c & x,

truncated to the lowest p bits. A port j in S+ uniquely fixes i by `2^i=c+2^j`, and a port j in S- uniquely fixes i by `2^i=c-2^j`. Thus S preserves every actual (i,j,s) with residual c. The older port-only mask is their disjoint union `V_c=S_c^+ | S_c^-`.

## Theorem 975.1 — signed exactness and affine fixed-residual transport

For every p,c,x and any p-bit XOR flip F,

    S_c^+(x XOR F) = S_c^+(x) XOR (P_c & F),
    S_c^-(x XOR F) = S_c^-(x) XOR (M_c & F).

This is a closed exact update of the two signed masks, provided c and its static P/M dictionary remain fixed. Proof: on each port j, the plus validity is `P_j*(1-x_j)` and minus validity `M_j*x_j`; toggling x_j toggles exactly those allowed bits. Uniqueness of i follows because a positive power of two has at most one exponent. QED.

**Scope:** This is an arithmetic observer update for a declared XOR flip. It does not claim that any F is a native X6/Heartbeat event.

## Theorem 975.2 — necessary/sufficient residual-change descent, and minimal repair

Put `T_c=P_c|M_c`. Restrict for the following statements to odd input products x and odd-preserving externally supplied XOR flips F (F_0=0), as in the auxiliary odd-core model. For two residuals c,C:

**(a)** Equality of signed carriers `S_c(x)=S_c(y)` for odd x,y is equivalent to equality of the bits of x,y on `T_c \ {0}`. At every j in T_c, at least one of P_j or M_j equals 1, and the corresponding valid/invalid signed bit determines x_j.

**(b)** There exists a deterministic function `G_{c,C,F}` with `S_C(x XOR F)=G_{c,C,F}(S_c(x))` for every odd x **if and only if**

    (T_C \ {0}) subseteq (T_c \ {0}).

For sufficiency reconstruct those x_j that C can query using (a), apply the known flip bits, and compute the target signed pair. For necessity, if some j>=1 is in T_C but absent from T_c, choose x=1 and y=1+2^j: S_c(x)=S_c(y), while S_C(x XOR F) differs from S_C(y XOR F). QED.

**(c)** More generally, fix any declared family of possible next residuals `R`. Among odd inputs, the complete family of signed queries `{S_C(x):C in R}` has precisely

    2 ^ | ((union over C in R of T_C) \ {0}) |

distinguishable states. Its **minimal sufficient bit-coordinate projection** is `x` restricted to that union, with x_0=1 known. Each retained bit is necessary, since some signed singleton query detects it; the projection suffices for every query and any known odd-preserving XOR flip. This is observer-relative minimality for an externally declared residual-query family, not a universal bound for arbitrary native dynamics.

In particular `c=0` has `P_0=2^p-1`, `M_0=0`, so allowing any residual including zero among future queries makes the exact odd-slice state require all p-1 free bits. Merely keeping the currently valid signed ports is then insufficient for unrestricted future residual changes.

**Smallest displayed obstruction:** p=4, c=-7, C=-3, x=1, y=5, F=0. Both old carriers are `S_{-7}=(0b1000,0)`, while `S_{-3}(1)=(0b0100,0)` and `S_{-3}(5)=(0,0)`. The missing input bit j=2 is exactly the repair coordinate.

## Theorem 975.3 — closed-form census of signed-carrier ranks

Let `D_p={2^i-2^j, 2^i+2^j:0<=i,j<p}` be the distinct numeric residual population. The number of independent odd-slice input bits discernible by S_c is `r_c=popcount(T_c & ~1)`. For every integer p>=4, the exact distribution is

| Rank r_c | Number of distinct c |
|---:|---:|
| 0 | p-2 |
| 1 | p^2-3p+8 |
| 2 | p(p-1)/2 - 2 |
| p-1 | 1 |

and `|D_p|=(3p^2-5p+10)/2`.

**Proof.** Negative differences `2^i-2^j<0` (i<j) each give one positive-sign port j. Positive differences (i>j) each give one plus port j; positive sums (i<=j) give one minus port for i=j and two for i<j. Within positive numbers, difference and sum overlap precisely for one-bit powers `2^j` with `1<=j<=p-2`, and two-adjacent-bit powers `3*2^j` with `0<=j<=p-3`—a total of `2(p-2)` overlaps. Subtracting these from 1 zero residue, two sets of `binom(p,2)` signed differences, and `binom(p+1,2)` sums proves |D_p|.

A zero-rank residue is either c=1 (plus port j=0), or a positive difference `2^i-1` with i=3,...,p-1 (a run of at least three ones, no matching sum and only port j=0); total p-2. A rank-two residue is either a positive sum with two distinct set bits at positions at least 1 (`binom(p-1,2)`), or the overlapping one-bit residue `2^j` with j=2,...,p-2 (p-3 more). Their total is `binom(p,2)-2`. Residual zero has all p ports and rank p-1; every remaining residual has rank one. QED.

**19-bit consequence:** 499 distinct residuals; ranks `{0:17,1:312,2:169,18:1}`. Current signed-port state for 498 of 499 residuals sees at most two of the 18 free odd-source bits. This quantifies the information loss when a later residual may change. It does not assert an 18-bit optimal encoding for the entire two-core arithmetic history, which has additional constraints.

## Proposition 975.4 — endpoint marginal masks do not encode multi-step correlation

At p=4,c=0,x=1, the plus-source labels for j=1 and j=2 are individually valid. Consider two explicitly declared positive two-step path populations on those port labels:

    H_diag={(1,1),(2,2)},   H_cross={(1,2),(2,1)}.

Both have the same source and target one-port marginals, each {1,2}, and each has total mass 2. But the later equality-path query `sum_{(j,J) in H} [j=J]` gives 2 versus 0. A serial branch quotient that retains only endpoint signed masks, marginals or total mass can therefore lose path correlation. Preserve the joint incidence matrix/history carrier, or prove factorization for the intended composite queries. This construction is a declared positive path observer, not a claim that both populations arise from the same fixed original two-core equation.

## Reproducible evidence and limits

The companion `PREFIX975_R6_SIGNED_TRANSITION.py` computes every numeric residual and source mask from integer powers. It compares reconstructed signed (i,j,s) labels with direct enumeration for all odd x at p=4..8, checks each single-bit odd-preserving F, and tests the residual-change descent by the constructive counterexample or complete reconstruction for all ordered (c,C). It also checks the analytic rank distribution for all p=4..19. Companion JSON records the exact counts:

- p=4..8: 16,312 signed endpoint states, 105,416 single-bit updates, 13,479 ordered residual-pair cases (10,424 non-factoring).
- p=19: rank distribution exactly (17,312,169,1), `P_0=524287`.
- Constructive signed-residual-change and two-step correlation counterexamples confirmed using the displayed integer ports.

Proof applies to all p>=4, while exhaustive computations are limited to the stated finite domains. No new full p=19 two-core witness enumeration or native X6 event integration was run; inherited 1,903 named histories remain predecessor evidence, not a newly rerun check.

## Continuation and status

Next discriminating direction: for a **specified** source-dependent BRC transition family, compute its actual reachable residual-support union and test whether the union-coordinate carrier is closed under every branch. For signed output indices / histories with correlations, carry the joint edge-label incidence or provide an exact Markov/sufficient-statistic factorization. Compare storage plus transition and history-recovery costs on the frozen p=19, k=21, m in {1,3,5} population only after identifying the intended transition kernel.

Scientific result is an independent Source note, not a native X6 CLAIM, Result/Review or Working Truth. Current session activity: `RA-3FB2D033BE6048D8712FF056` (read from Source); source association is a separate CAS/bookkeeping operation. Any pending original control read remains on its original request ID.
