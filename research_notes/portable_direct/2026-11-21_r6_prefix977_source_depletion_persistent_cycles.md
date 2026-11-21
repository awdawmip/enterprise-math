# PREFIX-977 — Exact multi-step source-port depletion and persistent-cycle law

Date: 2026-11-21. Route: independent portable auxiliary BRC positive-path research. Historical researcher EM-DIRECT-FBEA5D; own session MCP-45ad6d29cd534c1aad25595a72e3c532; Activity RA-3FB2D033BE6048D8712FF056. These are provenance, not a formal shared Task CLAIM.
Frozen science input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Extends PREFIX-973 through PREFIX-976. P000 and ACTIVE worldview unchanged.
Status: AUTHOR_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED.

## Precise fixed-residual auxiliary model

Let integer p>=3 and odd p-bit state x. Define residuals D_p={2^i-s*2^j:0<=i,j<p,s∈{+1,-1}}. P_c and M_c are masks with bit j set precisely when a named source (i,j,+1) or (i,j,-1), respectively, exists for c. The output i is unique for fixed c,j,s. Define V_c(x)=(P_c & ~x)|(M_c & x) on the lowest p bits.

At each step choose any valid source port j in A={1,...,p-1}; flip x_j (x←x XOR 2^j); continue with the SAME numerical residual c. Paths record the ordered ports and source signs; their positive count is N_h(c,x). This is an auxiliary BRC port-observer, not native TRIADIC_CLOSURE_E, a six-axis rotation, or a phase-cancellation claim.

Set R=(P_c & M_c)&A, r=popcount(R); Q=V_c(x)&(P_c XOR M_c)&A, q=popcount(Q). Every port of R can be selected repeatedly, alternating its unique source sign. Each port of Q is initially valid and may be selected only once. Flipping any port changes no other port's validity.

## Theorem 977.1 — exact all-horizon paths

For every p,c,odd x and integer h>=0,

N_h(c,x)=sum_{ell=0}^{min(h,q)} binom(h,ell)*(q)_ell*r^(h-ell)
        =h!*[z^h] exp(r*z)*(1+z)^q,

where (q)_ell=q!/(q-ell)!, N_0=1 and 0^0=1 in the empty-subsequence term.

Proof: fix ell distinct one-shot ports to be used exactly once. Their positions can be chosen in binom(h,ell) ways and ordered labels in (q)_ell ways. Every other position takes one of r reusable ports; coordinate-local XOR toggles preserve precisely those conditions. The unique signed named source at each selected (c,j,x_j) makes this a source-labelled path count, not only a support count. Sum over ell.

## Theorem 977.2 — aggregate over all odd states

With u=popcount((P_c XOR M_c)&A) and the same r, for each integer h>=0,

sum_{odd x} N_h(c,x)
 =sum_{ell=0}^{min(h,u)} binom(h,ell)*(u)_ell*r^(h-ell)*2^(p-1-ell)
 =2^(p-1)*h!*[z^h] exp(r*z)*(1+z/2)^u.

Proof: for each ordered choice of ell one-shot source ports, exactly 2^(p-1-ell) odd x have the compatible initial bits at these distinct nonzero positions. Reusable-port validity is independent of x. Count pairs (x,valid history) in both orders. Every summand is an integer, including the exceptional h=0 case.

## Corollary 977.3 — complete persistence and growth classification

PREFIX-976 proved that P_c and M_c share a port iff c=3*2^j with 0<=j<=p-3. In the odd-preserving allowed set A, r∈{0,1}; r=1 iff c=3*2^j, 1<=j<=p-3. For such a special c the entire named-source collection consists of a plus source (i=j+2, port j), and minus sources (i=j+1, port j) and (i=j, port j+1). Consequently Q has exactly bit j+1 when x_(j+1)=1, and q=bit_(j+1)(x).

Hence for all h>=0:
N_h(3*2^j,x) = 1+h*bit_(j+1)(x).

Proof of complete enumeration: the binary representation of 3*2^j has exactly two adjacent 1-bits, so its two ordered sum-of-powers representations supply exactly the stated minus sources. For the difference-of-powers representation 2^i-2^k=3*2^j, the odd factor 3=2^2-1 forces k=j,i=j+2. Apply Theorem 977.1.

For all other c, r=0 and N_h=(q)_h. In particular every history terminates once h>q<=p-1. Exactly p-3 residuals admit arbitrarily long valid paths at fixed residual, with path counts at most linear in h. This is a classification of the specified auxiliary state machine, not a native six-axis Cell-return result.

## 19-bit exact examples

D_19 has 499 distinct residuals. The persistent 16 are {3*2^j:1<=j<=16}; the other 483 have no histories beyond their q one-shot selections.

For c=0,x=1, all 18 odd-preserving source ports are plus-only, so (r,q)=(0,18), N_h=(18)_h. Thus N_2=306, N_3=4896, N_4=73440, N_18=18!=6402373705728000, and N_19=0. A frozen-port power model incorrectly gives 18^h. Summing c=0,h=3 over all odd x gives 4896*2^15=160432128 histories.

For each persistent c=3*2^j, the full-population three-step mass is 2^18+3*2^17=655360; summing 16 such residuals gives 10485760. An odd x with bit_(j+1)=0 has exactly one valid path at every length; with bit_(j+1)=1 there are h+1.

## Computational validation

The accompanying exact Python checker creates every source mask directly from 2^i-s*2^j; independently evolves a distribution of XOR-toggled x states for h=0..6; and compares all path counts and aggregates with the closed forms. Complete domain p=4..8, all residuals, all odd p-bit x: 16,312 (c,x) cases and 114,184 horizon checks; every aggregate identity checked. It also checks all 499 residuals and all 16 persistent residues at p=19, explicit c=0 integer cases, and actual 19-bit dynamic paths at h<=4. All arithmetic is exact integer. No full 19-bit exhaustive trajectory computation is claimed.

## Limits / next mathematical question

The carrier (r,q) is sufficient for positive TOTAL path count under fixed c and unrestricted allowed-port selection, but reconstructing named histories or adding signed/port-dependent weights requires the full source masks and relational state. Residual-changing dynamics or arbitrary port kernels need an extended joint-state carrier and a separate transfer proof to BRC native dynamics. Next: formulate and exactly check a nontrivial prescribed residual-changing family and its minimal sufficient provenance carrier. Mother question B_fix,odd(32)∈{19,20} remains open. No official Result/review/CLAIM is asserted.
