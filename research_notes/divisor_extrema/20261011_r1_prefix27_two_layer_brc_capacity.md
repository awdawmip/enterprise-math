# Research1 — Prefix-27 two-layer certificate and BRC future residual bit capacity

Date: 2026-10-11 (Asia/Shanghai). **Author-verified computation-assisted research note; UNREVIEWED / NOT_ADMITTED**. Not a formal Task Result, Driver review, P000 theorem, or native BRC execution.

## Fixed source/authority
- Account-level GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge@699c95d89660c2de0650d8c27cc91bc71371be17`, reading both normative entries, EM project router and Task bootstrap, ACTIVE worldview and BRC policy; P000 startup projection's original blob pin `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matched the original P000 Git blob at the same SHA.
- EM research basis: `awdawmip/enterprise-math@4b8b07a68741187ff9095c753b7ea705fa96d8ee`, with portable research, ordinary control, activity and persistence protocols, plus `research_notes/divisor_extrema/20261011_r1_prefix26_global_brc_quotient.md`.
- Native current Site identity is static read-only; `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` and `operation_sent=false`. No native CLAIM, Result or owner takeover. Current task inventory says `execution_authorized=false`. A direct live activity-registration attempt through GitHub was blocked by platform safety checks; no RA publication is claimed.

## A. Prefix-27 unimodality, a conditional computation-assisted all-N theorem

Let `D_k(N)=max{tau(n):n<=N,omega(n)=k}` whenever that layer exists, `D_0(N)=1`, and `K(N)=max_{n<=N}omega(n)`. The previous **author-checked and unreviewed** note states that the prefix through k=26 is unimodal for every positive N, and nondecreasing once

`W25=55770722553751604733453884443535017861155456000`.

**Terminal-dominance extension lemma (exact).** If `A_0(x),...,A_k(x)` is unimodal everywhere, is nondecreasing for x>=W, and a new terminal B(x)<=A_k(x) at all x<W where B is defined, then appending B retains unimodality everywhere. Proof: below W only a terminal descent may be added to an already unimodal prefix; above W any last value extends a nondecreasing prefix with at most one terminal descent. Note that the often-suggested strict-triple criterion `A_(k-1)>A_k<B` alone is NOT valid in the presence of a trailing plateau after an earlier descent: `(3,2,2,3)` is a counterexample.

**Exact finite new certificate.** For each k=25,26,27, sort exponents descending and assign to the first k primes; this transformation does not increase n or change tau/omega. Two independent exact enumerators exhaust all such canonical vectors through W25 (arbitrary precision integers, product-based safe pruning, no floats).

|k|candidate vectors <= W25|inverse-tau first-witness records|D_k(W25)|
|---:|---:|---:|---:|
|25|2301|533|5813305344|
|26|964|284|5813305344|
|27|353|138|5435817984|

The first 27-prime primorial is `23984823528925228172706521638692258396210`. The exact first witness attaining `D27(W25)=5435817984` is `43518063810881933996558712861243233634083424000`. There are exactly 3,618 canonical vectors across the three layers (only **1,317** are needed for the new two-layer comparison), and 955 inverse-tau minima events. The two independent implementations report **zero** events where `D27(N)>D26(N)` for N<=W25. D values are constant between candidate thresholds; inverse minima preserve all increases. C++ enumerates extras atop the primorial, while Python recursively enumerates descending positive exponents; independent totals and maxima agree.

**Conditional conclusion:** For N<W25, D27 is either absent or D27<=D26 by complete finite computation. For N>=W25, the inherited prefix through D26 is nondecreasing. The terminal-dominance lemma gives

`forall N>=1: (D_0(N),...,D_min(27,K(N))(N)) is unimodal.`

This all-N theorem **depends on the previous author-verified but still unreviewed prefix-26 assertions**. This note does NOT determine the permanent nondecrease threshold W26 or claim `D27<=D26` after W25. Its finite certificate, a new unit, can be independently reproduced without repeating the previous 29-million-row scan.

## B. BRC finite-horizon residual information theorem

Let S consist of s allowed primes, a be the initial valuation vector, and L>=1 the maximum number of legal multiply/divide actions by S. Observe tau, omega, threshold `[n<=H]` and action legality after each action. Write `n=r*prod p_i^(a_i)` with gcd(r,prod S)=1. Put

`R_L(a)={b in N^s:sum_i |b_i-a_i|<=L}`,
`F_L(r;a)=max({0} union {prod p_i^(b_i):b in R_L(a),r*prod p_i^(b_i)<=H})`.

Fix `a,tau(r),omega(r)`. Every length-L future observation tree is determined by the integer F_L: operation legality depends on a, future divisor counts equal `tau(r)*prod(b_i+1)`, and thresholds are `[prod p_i^(b_i)<=F_L]`. Conversely distinct F_L values give a differing reachable threshold test. Therefore the exact minimal fixed-length residual-code bit count on a baseline fiber is `ceil(log2 C)`, where C is the number of attainable F_L values on that fiber.

Let `M=|R_L(a)|`. Unique factorization shows F_L has at most M+1 values, so at most `ceil(log2(M+1))` residual bits suffice. Moreover

`M <= B_s(L)=sum_{j=0}^{min(s,L)} 2^j binom(s,j) binom(L,j)`.

Proof: choose j nonzero difference coordinates, signs, and positive magnitudes summing at most L. Equality holds if all `a_i>=L`. If all `a_i=0`, `M=binom(L+s,s)`. For fixed s, the required extra threshold-state bits are `O(s log(L+1))`, compared with potentially exponentially many explicit action-word nodes. This is scoped bit complexity, not total unbounded state entropy.

**Sharp 3-bit certificate:** Take S={2,3}, a=(0,0), L=2, H=100. Reachable factors are exactly {1,2,3,4,6,9}. The seven *prime* residual integers `r=(5,13,17,29,37,53,101)` share `tau(r)=2,omega(r)=1`, but give `F_L=(9,6,4,3,2,1,0)`. Their complete future observation trees are pairwise distinct. Thus seven lossless residual states, i.e. exactly **3 worst-case bits**, are necessary and sufficient; the M+1 upper bound is attained in one fixed baseline fiber.

More generally, for sorted reachable t_1<...<t_M, F=t_j for 1<=j<M iff `floor(H/t_(j+1))<r<=floor(H/t_j)`; F=t_M iff `1<=r<=floor(H/t_M)`; F=0 iff `r>floor(H/t_1)`. Intersect these explicit integer intervals with the admitted coprime residual set of fixed tau and omega to obtain the exact class count C. This supplies a finite arithmetic capacity certificate rather than merely a cardinality upper bound.

## Evidence, limits, next
- Local report SHA256: `ad7ac3094d7e2c381d7385e2c7eba55463f741045d5f991d69f37064a20cb698`. Complete companion evidence ZIP SHA256: `56de5ae12601cc19db5a0c0bbe0c4960785896460fe092bb00e6c2751f007f76`; local package `EnterpriseMath_Research1_Prefix27_BRC_Capacity_20261011.zip`. This Source note does NOT imply the ZIP/programs are uploaded.
- Independent C++ and Python exact canonical enumeration: 3,618 candidate vectors; 955 inverse-minima records; zero D27>D26 failures for N<=W25. Python BRC checker: 7 prime witnesses, 20 lattice-count cases, 18 global observer/tree partition cases, 72,090 pair comparisons, all passing. Full checksums and runnable sources are in the companion package.
- Pending: Source upload of complete programs/logs if permitted; live activity registration/checkpoint, formal native CLAIM and independent review. All theorem strengths remain candidate/unreviewed.
- Next divisor question: exact k=26 to 27 donor-exchange tail and first permanent nondecrease W26 using a small inverse-minima proof certificate, without replaying the 29-million-row old prefix check.
- Next BRC question: evaluate exact attainable class count C as H varies for fixed tau/omega, in particular prime-fiber interval counts; distinguish lattice capacity from arithmetically attained capacity.
