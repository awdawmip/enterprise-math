# Enterprise Math Research1 — Prefix-26 divisor extrema and global finite-horizon BRC quotient

Date: 2026-10-11 (Asia/Shanghai). Status: **AUTHOR_VERIFIED / COMPUTATION_ASSISTED / UNREVIEWED / NOT_ADMITTED**. This is a typed classical arithmetic application, NOT a theorem about P000 native X6 dynamics.

## Immutable starting points and authority

- GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge@46de0b0d4865d9e7410df30d96b07ee4167d1fbe`, where the bootstrap, operating manual, project router, verified P000 projection (original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`), ACTIVE worldview and BRC contract were loaded.
- Enterprise Math source before this work: `awdawmip/enterprise-math@dbfea83c5039ce555364d4c4d83c81cfd49789b9`; exact portable/ordinary-control protocol and prior `research_notes/divisor_extrema/20261011_r1_prefix25_finite_horizon_brc.md` were read.
- Previous prefix-25 global unimodality and permanent nondecrease threshold `W24=552185371819322819143107766767673444169856000` are **author-checked but unreviewed** inherited premises, not independent acceptance.
- Canonical tasks read through real gateway: `execution_authorized=false` at source commit `dbfea83c`. Native session-start actually failed with `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. GitHub identity `awdawmip` has repository push permission. No live CLAIM, owner takeover, formal Result or independent Driver review is claimed.

## A. Global unimodality of the first 26 nonzero omega layers

Write `D_k(N)=max{tau(n): 1<=n<=N, omega(n)=k}`, `D_0(N)=1`, `K(N)=max_{n<=N}omega(n)`. Canonical exponents on the first k primes, descending, preserve tau and omega without increasing n, so exhaustive normalized enumeration determines every layer maximum.

**One-step extension lemma (exact).** If `A_0(N)<=...<=A_k(N)` for all `N>=W` and the sequence with one additional last element `A_{k+1}` is unimodal for all `N<W`, then the extended sequence is unimodal for every N. For `N>=W`, appending any last value can create only a terminal fall, never a valley.

Two independently implemented **full** normalized scans through `C=10^49 > W24` verified every extremal refresh event for the first 26 nonzero layers. Each program enumerated 29,102,164 canonical candidate integers and 873,663 inverse-threshold states, found 14,741 strict record refreshes, and found **zero** unimodality valleys. Different event merge algorithms agreed on the last adjacent-layer failure boundaries. Between events all D values are constant.

For `N>C`, the inherited prefix-25 `D_0,...,D_25` is nondecreasing, so the extension lemma applies regardless of the value of `D_26`. Therefore, *conditional on the previously author-validated prefix-25 premise*, the following is a computation-assisted **all-positive-integer** conclusion:

`forall N>=1: (D_0(N),...,D_min(26,K(N))(N)) is unimodal.`

This argument removes the unnecessary requirement to enumerate every layer as far as the new exchange-tail threshold.

## B. Exact earliest **permanent nondecrease** threshold

Here k=25 and `q=p_26=101`. Set `b_i=min{b>=2:p_i^b>=101}`, `j0=#{i<=25:2*p_i<101}=15`. A canonical 25-prime n admitting neither a single-donor nor two-donor non-increasing-size exchange satisfies

`tau(n)<=B25=max(3^25,2^(25-j0)*prod_{i<=j0}(2*b_i-1))`

`=max(847288609443,530590694400)=847288609443.`

**Exchange proof.** When `a_i>=2*b_i-1`, `m=n*101/p_i^(b_i)` has `m<=n`, `omega(m)=26`, and `tau(m)/tau(n)=2*(a_i-b_i+1)/(a_i+1)>=1`. Alternatively, for distinct i,j with `p_i*p_j>=101`, `a_i,a_j>=2`, and `(a_i-1)*(a_j-1)>=2`, take `m=n*101/(p_i*p_j)`; its ratio is `2*a_i*a_j/((a_i+1)*(a_j+1))>=1`. Without either exchange, either every exponent is <=2, giving the first branch of B25, or every `j>j0` has exponent 1 and each head exponent is <=`2*b_i-2`, giving the second branch.

Two independent **targeted** complete scans of the canonical k=25 and 26 layers through

`E25=109228534586917317858960440646934443377007454501784224989081600000`

found the first canonical 25-prime integer with tau above B25:

`T25=71301960077571026935710287644526650537768755021998035756761600000`,
`tau(T25)=848945111040>B25`,
with 25 exponents `[12,8,5,4,3]+[2]*10+[1]*10`.

Thus for every `N>=T25`, the 25th layer maximizer has tau>B25 and admits a nonincreasing-size exchange to the 26th layer. Hence `D25(N)<=D26(N)` on the **infinite tail**.

Across the complete finite region through E25, a separate C++ targeted search and an independently coded Python search agreed exactly: 537,136 canonical k=25 and 334,736 canonical k=26 candidates; 23,754 and 17,170 inverse-threshold states respectively; nine k25>k26 failure intervals; last failure endpoint

`55770722553751604733453884443535017861155455999`.

**Sharp threshold:**

`W25=55770722553751604733453884443535017861155456000.`

`(D25,D26)(W25-1)=(5813305344,5662310400)` while `(D25,D26)(W25)=(5813305344,5813305344)`.

A third independent **direct** Python boundary scan enumerated 2,301 canonical k=25 integers at both boundaries, 963 k=26 below W25 and 964 at W25. The new k=26 witness is W25 itself with exponents `[10,6,3,2,2]+[1]*21` and tau 5,813,305,344.

The old prefix through 25 layers is nondecreasing for `N>=W24<W25`; the new k25/k26 pair is nondecreasing on `[W25,E25]` by exact exhaustive enumeration and on `[T25,infinity)` by exchange. Thus

`forall N>=W25: D0(N)<=D1(N)<=...<=D26(N)`.

The failure at W25−1 establishes the **earliest permanent** bound, not merely one passing sample.

## C. New exact global BRC future-observer quotient (no fixed initial fiber)

Let S be finite nonempty primes, H>=1, and L>=1. Allowed actions: multiply by any p in S, or divide exactly when legal. After each prefix of at most L actions, observe `(tau(n),omega(n),[n<=H])` and legality. Write `n=r*prod_{p in S}p^(a_p)`, with r coprime to S. Define

`R_L(a)={b in N^S: sum|b_p-a_p|<=L}`;
`F_L(r;a)=max({0} union {prod p^(b_p):b in R_L(a), r*prod p^(b_p)<=H})`.

**Theorem (exact, globally coarsest observational equivalence):**

`Q_L(n)=((a_p)_{p in S}, tau(r), omega(r), F_L(r;a))`

determines every future observation tree through depth L, and two initial integers have identical such trees **iff** they have identical Q_L. No previously fixed base fiber is needed.

*Necessity:* from the root tau and the length-one multiplication branch for p one recovers `a_p+1=tau(n)/(tau(p*n)-tau(n))`. Then root tau and omega recover `tau(r)` and `omega(r)`. Identical a determines all legal words, and their threshold bits recover F_L as the maximal threshold-satisfying reachable factor.

*Sufficiency:* a decides exact division legality; at any reachable b, the counts are `tau(r)*prod(b_p+1)` and `omega(r)+#{p:b_p>0}`. For a reachable integer factor s, the threshold bit is 1 **iff** `s<=F_L`: if F_L>0 its definition gives r*F_L<=H; larger reachable factors fail by maximality. Therefore Q_L exactly describes all declared observations and is the coarsest partition. At L=0 the correct quotient is only `(tau(n),omega(n),[n<=H])`.

This strengthens the prior note's fixed-fiber theorem. It is a literal application of BRC positive branch multiplicity to divisor counts (`REUSE_APPLIED`), not native BRC engine execution, not a physical X6 assertion.

An independently written Python full-tree checker passed 72 parameter instances, 11,520 starting states, 211,200 word nodes, and 915,840 pairwise equivalence checks.

## Evidence, limits, next unit

Local independently verified handoff package: `EnterpriseMath_Research1_Prefix26_GlobalBRC_20261011.zip`, SHA256 `0c4d3060cf05166375884c957ebae62a125b35ef951feb39ce5f6d552ce45a91`. Its full report SHA256 is `8e78f43759110ec939c3edda45ad5a2210c7b0faedf1a28d2e211eefe432594d`. Package includes two full C++ scans (bounded at 10^49), targeted C++/Python full pair scans (bounded at E25), independent boundary checker, BRC future-tree checker, machine-readable numerical reports, logs and per-file SHA256 manifest. **The separate package has not been synchronized to Source merely by this note.** The attempted full all-layer run to E25 exceeded its process limit; it is *not* used in the finished proof, which uses the extension lemma and targeted tail proof instead.

**Status:** Source research note when readback-verified, mathematical candidate only; formal research activity checkpoint, native CLAIM, Source code/log sync, independent review and admission remain separate. Prior premises retain their actual unreviewed status.

**Next:** develop a reusable exact certificate for adjacent k/k+1 targeted inverse minima plus a machine-checkable version of the one-step unimodality extension. For BRC, quantify the bit complexity of Q_L against full labeled observation-tree size as L, H and |S| vary; preserve integer valuations/provenance and observer scope.
