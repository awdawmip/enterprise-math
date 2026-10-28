# D25/LIFT — universal original-216 complement reflection and exact p-adic cutoff

Date: 2026-10-28, Asia/Hong_Kong.
Status: **AUTHOR-SIDE / EXACT NEW ALL-PRIME EXTENSION / EXECUTED INTEGER CHECK / UNREVIEWED / NOT_ADMITTED / NATIVE_NOT_EXECUTED / SOURCE_CHECKPOINT_PENDING**.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged.
Research ordinary-control routing label: chatgpt-research-onhour-enterprise-math-20260923, not a current service session/CLAIM attestation. The CONTROL_PLANE_MAINTENANCE lane is separate and unused.

## Prior verified mathematical input (not recredited)

Define, for primes p>3,

$$
t_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
=\frac{(2n)!(3n)!}{(n!)^5\,216^n},
\qquad
s_n=\frac{\binom{2n}{n}^{2}\binom{4n}{2n}}{2304^n}.
$$

The frozen original 216 observable is $A_p=\sum_{n=0}^{p-1}(6n+1)t_n$; the comparator is $B_p=\sum_{n=0}^{p-1}(8n+1)s_n$. The predecessor note at Enterprise Math commit c9bef64b788c7b0eb70067a839c55326b0b65059 proved the 216 inverse reflection for p=6m+1, and the 2304 inverse reflection for all primes p>3, giving the still-open complete half-cut transport obstruction (T1). The full-cutoff congruence A_p=B_p mod p³ was previously checked at 781 primes under commit 7f23e5cb67cd455564317004e377feba60ace1bb but has not been proved. The original p=373 data are inherited validation checks.

The new contribution here is the exact extension of the original 216 reciprocal theorem and the corresponding complete cutoff formula to the disjoint p=6m+5 prime class. It is a supplementary adversarial control for the original frozen p=13,19 mod24 bridge; it does not expand or replace its hard target.

## New exact theorem: both prime classes without a 6m+1 assumption

**A-all.** For every prime p>3 and integer j satisfying

$$
L:=\left\lceil\frac p3\right\rceil\le j\le h:=\frac{p-1}{2},
$$

the valuations are $v_p(t_j)=1$, $v_p(t_{p-j})=2$, and both normalized coefficients are nonzero mod p. Moreover

$$
\boxed{
\left(\frac{t_j}{p}\right)\left(\frac{t_{p-j}}{p^2}\right)
\equiv \frac1{36j^3}\pmod p.}
\tag{A-all}
$$

**Proof.** The Legendre factorial formula, with j strictly between p/3 and p/2, gives valuations 0,1,1,1 for $(2j)!$, $(3j)!$, $(2p-2j)!$, $(3p-3j)!$, respectively, and all $(j!)$, $((p-j)!)$ and 216 are p-units. Put

$$
a=3j-p,\quad b=2p-3j=p-a,\quad c=p-2j,
$$

all in 1,...,p-1. Wilson gives $(p+r)!/p\equiv-r!\pmod p$ whenever 0≤r<p. Thus the normalized factorial product in the numerator of the reflected coefficient pair is

$$
-(2j)!\,a!\,c!\,b!\pmod p.
$$

Wilson reflection $k!(p-k)!\equiv(-1)^k k\pmod p$ gives

$$
(2j)!\,c!\equiv2j,\qquad
a!\,b!\equiv(-1)^a a=-(-1)^j\,3j\pmod p,
$$

because p is odd and a=3j-p. Hence the numerator is $6(-1)^j j^2$. The denominator is

$$
[j!(p-j)!]^5\,216^p\equiv(-1)^j\,j^5\,216\pmod p.
$$

The quotient is $6/(216j^3)=1/(36j^3)$, as claimed. There is no use of p=6m+1 anywhere in the derivation. QED.

## Original full-to-half complement theorem

For 0≤n<p,

$$
v_p(t_n)=\left\lfloor\frac{2n}{p}\right\rfloor+
\left\lfloor\frac{3n}{p}\right\rfloor.
$$

Consequently the original upper half has valuation exactly 2 for h+1≤n≤p-L and at least 3 for p-L<n<p. Put $u_j=(t_j/p)\bmod p\in\mathbb F_p^\times$. Theorem A-all and the unchanged original weight (6n+1) imply

$$
\boxed{
H_A:=\sum_{n=h+1}^{p-1}(6n+1)t_n
\equiv \frac{p^2}{36}\sum_{j=L}^{h}
\frac{1-6j}{j^3u_j}\pmod{p^3}.}
\tag{HA-all}
$$

This holds for every p>3. For p=6m+1 it specializes exactly to the previously proved original interval j=2m+1,...,3m; for p=6m+5 the interval is j=2m+2,...,3m+2, giving a new exact complete-cutoff formula.

Guo and Zudilin, *A q-microscope for supercongruences*, *Advances in Mathematics* 346 (2019) 329–358, arXiv:1803.01830, prove the comparator high half $H_B=B_p-B_{\le h}\equiv0\pmod{p^3}$ for all p>3. This external theorem and HA-all yield the **equivalence** for every p>3,

$$
\boxed{
A_p\equiv B_p\pmod{p^3}
\quad\Longleftrightarrow\quad
A_{\le h}-B_{\le h}
+\frac{p^2}{36}\sum_{j=L}^{h}
\frac{1-6j}{j^3u_j}\equiv0\pmod{p^3}.}
\tag{T-all}
$$

The right-hand congruence is an **open mathematical obligation**; the equivalence is proved. In the frozen target classes p=13,19 mod24, T-all is exactly the earlier T1, not a new claim of its proof.

## Executed exact evidence, scope, and BRC observer

Source code: research_notes/portable_direct/d25_allprime_216_complement_guard_20261028.py at immutable Git commit 5cc7a4736a92d08bac9d0f7ce37111edf1f4cb8e (Git blob 0d62991ffba3758fc3d3d09eb2ba931a432aaf1e). Executed locally with the standard Python integer ring; no machine-native H0/B0 operator or surrogate Frobenius was evaluated. All modular divisions use p-units. For selected indices an independent binomial factorial definition checks the recurrence.

Actual output:

    PASS_D25_A216_UNIVERSAL_REFLECTION 209 primes <1300; 20918 paired indices
    FROZEN_CLASS_COUNT 55
    NEW_P_MOD_6_EQ_5_EXTENSION 107 primes

The script also confirmed the full weighted complement and the **observed**, unproved A_p=B_p mod p³ on those 209 primes, without counting the already-known 781-prime observations as a new theorem. Exact labeled witnesses (p, (A_half-B_half)/p² mod p, H_A/p² mod p, H_B/p² mod p):

    (5,4,1,0) (7,2,5,0) (11,10,1,0)
    (13,3,10,0) (19,10,9,0)
    (37,17,20,0) (43,8,35,0)
    (211,9,202,0) (373,107,266,0).

The two nonzero ports cancel mod p in every listed finite witness. This does not prove their universal cancellation. In particular the p=373 ports 107 and 266 are **previously known** and are included only for exact-source regression.

BRC resolution **COMPOSE_APPLIED**: indexed signed pairs $(p,j,p-j,t_j,t_{p-j})$ with separate p-valuations, weights, original denominator, source and half-cut identities. Observer: full weighted sum modulo p³; future operation: complement the half-cut and compare without quotienting away the high-tail source. The high tail of A is generally nonzero; that of B vanishes at this precision by the published theorem. The external auxiliary scalar carrier is not an X6 native-geometry or P000 transfer.

## Durable frontier, authority boundary and next exact actions

Scientific current obligation: prove or refute T1 uniformly for the **frozen** p≡13,19 mod24 via finite p³ transformation/CM/WZ that retains the original A high-tail. The newly covered p≡5 mod6 primes provide negative controls for any proposed universal bridge theorem. Avoid re-proving the old p≡1 mod6 reflection and re-running finite 781-prime observations as new claims.

Native hard target remains existing Issue #1559 (https://github.com/awdawmip/enterprise-math/issues/1559): original same-class H0/B0 divided-power [X]U mod139129 at p=373, native module rank, actual semilinear Frobenius direction and eta, odd signed Green/Hesse, original κ and Delta_p-R_p, source-versioned execution and independent Source review. It is separate from this scalar theorem. As read 2026-10-28, Issue #1559 is OPEN and unassigned.

As checked 2026-10-28, Sites reported research_authority_granted=false and write_relay_enabled=false; Site checkpoint_list reported ACCESS_DENIED. The older Research-lane recovery Issue #6575 attests a historical subject-scoped session pointer, not current Source CLAIM; #6576 was an earlier dispatch request, not new ownership. No native Researcher session/CLAIM/open, Source checkpoint, formal Result, independent review, or mathematical acceptance is claimed here. AUTHOR-SIDE Source file only; REGISTER_PENDING and SOURCE_CHECKPOINT_PENDING are retained. Old staging remains separately sourced. P000 ACTIVE, all existing scientific source and owner pins, and Research/maintenance identity separation remain unchanged.

Next authorized recovery: check exact Research-lane Source authority, original-request receipts and canonical continuation; if a valid current claim exists, bind this as independent **unreviewed external author evidence** while preserving previous contributions, then advance the frozen T1 proof. In parallel, the actual authorized native executor must run original H0/B0 per #1559. Without Site write permission, do not replay a forbidden control mutation through another lane.
