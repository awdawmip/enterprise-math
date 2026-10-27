# D25/LIFT R51–R52 — exceptional high-high Green endpoint poles and an integral two-source repair jet

2026-10-27, Asia/Hong_Kong. Author-derived portable mathematics for the independent TASK_RESEARCH logical conversation `chatgpt-research-hourly-enterprise-math-20260923`, not the maintenance lane. Mother objective D25/LIFT/JT2 remains OPEN. Current formal Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen **scientific** source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`, not moved to a later control HEAD.

Classification: `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY`. The source is the unchanged rational W/S pair, not a new H0/B0, native spectral experiment, Result, authorized Source checkpoint or reviewed theorem.

## Inputs and typed observer

Use R47–R50 (already established, not recredited). At every nonnegative integer rank,
\[
w_k=\frac{(6k+1)(2k)!(3k)!}{(k!)^5 216^k},\quad
s_k=\frac{(8k+1)(4k)!}{(k!)^4 2304^k},\quad d_k=w_k-s_k,
\]
with labelled independent state `(W_k,S_k)`, one-step diagonal updates `W_{k+1}=a_k W_k`, `S_{k+1}=b_k S_k`, and **signed** observer `d_k=W_k-S_k`. The exact rational transitions are
\[
a_k=\frac{(6k+7)(2k+1)(3k+1)(3k+2)}{36(6k+1)(k+1)^3},\quad
b_k=\frac{(8k+9)(2k+1)(4k+1)(4k+3)}{288(8k+1)(k+1)^3}.
\]
R47 supplies
\[
D_k=a_k-b_k=\frac{(2k+1)P(k)}{288(k+1)^3(6k+1)(8k+1)},
\quad P(x)=2688x^4+6160x^3+4456x^2+1166x+85.
\]
R50 gives the rational second-order finite Green identity with two endpoints. Here we explicitly solve its `c_1=1` endpoint problem over `Q_p`, classify its previously unisolated exceptional primes, then repair the integral observer interface.

For **all** primes `p>=13` with `p ≡ 1 (mod 6)`, set `N=floor((3p-1)/4)+1`, `A=∏_{j=1}^{N-1} a_j=w_N/w_1`, `B=∏_{j=1}^{N-1} b_j=s_N/s_1`, and `D=a_N-b_N`. The auxiliary rank index and its rational formulas are *not* a claim about native X6 coordinates or a three-dimensional slice.

## R51 — closed Green endpoint solution and three exceptional primes

**Theorem R51.** For every labelled free initial state `(U,V)=(W_1,S_1)∈Q_p²`, let
\[
d_N=A U-B V,\quad d_{N+1}=a_N A U-b_N B V.
\]
There is a unique exact rational endpoint formula
\[
\boxed{U-V=Q_Nd_N+Q_{N+1}d_{N+1}},\qquad
Q_N=\frac{a_N/B-b_N/A}{D},\quad
Q_{N+1}=\frac{1/A-1/B}{D}.
\tag{51.1}
\]
The source-faithful Green coefficients in R50 for this observer are `-Q_N,-Q_{N+1}`; no independent new model equation is introduced. Both `A,B` have `v_p=3`. Moreover
\[
\boxed{v_p(D)=
\begin{cases}1,&p\in\{139,199,277\},\\0,&\text{all other target primes }p\ge13.\end{cases}}
\tag{51.2}
\]
At ordinary target primes, `v_p(Q_N),v_p(Q_{N+1})>=-3` and their minimum is **exactly** `-3`. At each of the three exceptional primes, **both** endpoint coefficients have valuation **exactly** `-4`. Thus R50's universal **at least third-order** pole lower bound is sharp for every ordinary target prime, but the specified rational endpoint observer has a strictly stronger fourth-order pole at precisely these three exceptional primes.

**Proof.** Subtract `b_N d_N` and `a_N d_N` from `d_{N+1}`, giving `D A U` and `D B V`. Since `P(N)>0` over the integers, `D≠0` rationally; solve both amplitudes to get (51.1). The determinant of the two-endpoint observation matrix is `A B D`, up to ordering sign.

For `p≥13` in the target class, `N<p-1`. Legendre's formula gives `v_p((2N)!)=1`, `v_p((3N)!)=2`, `v_p((4N)!)=3`, while `v_p(N!)=0`; neither `6N+1` nor `8N+1` is divisible by `p`. Thus `v_p(w_N)=v_p(s_N)=3`, and `w_1=7/18`, `s_1=3/32` are units, proving the A/B valuations.

If `p≡1 (mod 4)`, then `N≡1/4 (mod p)`; if `p≡3 (mod 4)`, then `N≡3/4 (mod p)`. Every denominator and the `2N+1` numerator factor in `D` is a unit for this target family. Exactly,
\[
P(1/4)=3047/4=11\cdot277/4,\quad
P(3/4)=27661/4=139\cdot199/4.
\]
The congruence classes remove `p=11`; `139,199,277` are primes and have the required mod-4 and mod-6 residues. At these three exact integer ranks, direct unit denominator arithmetic yields `D/p mod p = 120,189,155`, respectively, so no higher-order degeneracy occurs. Everywhere else `D` is a unit.

Put `\bar A=A/p^3`, `\bar B=B/p^3`. For an ordinary prime, `p^3 Q_N=(a_N/\bar B-b_N/\bar A)/D`, `p^3Q_{N+1}=(1/\bar A-1/\bar B)/D` are integral. If both vanished modulo `p`, the second would force `\bar A=\bar B`, while the first would equal `1/\bar A\ne0`, a contradiction. At each exceptional prime, `a_N,b_N` remain units, `a_N≡b_N (mod p)`, and the exact author-certified pairs `(\bar A,\bar B) mod p` are `(130,8),(99,62),(131,81)`: unequal in each case. Hence **both** numerators of (51.1) have valuation `-3` and division by the order-one `D` makes their valuation `-4`. QED.

For the **unchanged factorial trajectory**, each exceptional prime also has `v_p(d_N)=v_p(d_{N+1})=3`. The following is an exact residue certificate; `Q\)-columns are `p^4Q` residues, `d\)-columns are `d/p^3` residues:

| p | N | D/p | A/p³ | B/p³ | p⁴Q_N | p⁴Q_{N+1} | d_N/p³ | d_{N+1}/p³ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 139 | 105 | 120 | 130 | 8 | 32 | 94 | 100 | 102 |
| 199 | 150 | 189 | 99 | 62 | 148 | 66 | 70 | 36 |
| 277 | 208 | 155 | 131 | 81 | 66 | 195 | 27 | 42 |

In each row the coefficient of the apparent `p^{-1}` term in `Q_Nd_N+Q_{N+1}d_{N+1}` vanishes: `32·100+94·102≡0 (139)`, `148·70+66·36≡0 (199)`, `66·27+195·42≡0 (277)`. This is **labelled signed endpoint cancellation**, not a deletion of either source or a proof of the W/S supercongruence.

## R52 — the lossless integral blow-up coordinate

**Theorem R52.** With the same hypotheses, let `λ=v_p(D)∈{0,1}`, and define the unit factors
\[
A_0=A/p^3,\quad B_0=B/p^3,\quad D_0=D/p^\lambda.
\]
For every `(U,V)∈Z_p²` define the *joint* observer
\[
\boxed{
X=\frac{d_N}{p^3},\qquad
Y=\frac{d_{N+1}-a_N d_N}{p^{3+\lambda}}.
}\tag{52.1}
\]
These expressions are **p-integral**, and the exact map is
\[
\begin{pmatrix}X\\Y\end{pmatrix}=
\begin{pmatrix}A_0&-B_0\\0&D_0 B_0\end{pmatrix}
\begin{pmatrix}U\\V\end{pmatrix}.
\tag{52.2}
\]
Its determinant `A_0 D_0 B_0` is a `p`-adic unit, giving an actual `GL_2(Z_p)` interface. Recovery is explicit:
\[
\boxed{V=Y/(D_0B_0),\qquad U=(X+B_0V)/A_0.}\tag{52.3}
\]
The extra `p` factor at `139,199,277` is a **necessary divided-difference jet** of the two correlated endpoints. It repairs the one-digit integral loss of the unmodified normalized pair `(d_N/p^3,d_{N+1}/p^3)`, whose determinant has valuation `λ`. No extra observation dimension, new axiom, changed W/S input, or automatic native X6 theorem is asserted.

**Proof.** Substitute the two exact W/S transitions into `d_{N+1}-a_Nd_N`: it equals `(a_N-b_N) B V = D B V`. Divide by `p^{3+λ}`, obtaining (52.2); `A_0,B_0,D_0` are units by R51. Exact inverse (52.3) proves the claim. QED.

For the unchanged factorial trajectory, the modulo-`p` observed jets `(X,Y)` are `(100,90)` for `p=139`, `(70,116)` for `p=199` and `(27,95)` for `p=277`. With (52.3) they recover the original `(w_1,s_1)=(7/18,3/32)` modulo each prime.

**BRC / information audit.** Applied `BRC COMPOSE_APPLIED` to a *signed labelled source pair*, independent future observer and valuation-sensitive arithmetic. R51 distinguishes scalar endpoint poles from source rank; R52 retains the joint defect needed to make the observer integral. A positive-mass BRC total, an arbitrary one-port change of original inputs, or a scalar-only quotient would erase the relevant future information. The operation `(U,V)→(X,Y)` is a lossless coordinate change on the stated `Z_p` carrier; it is **not** an arbitrary claim that separate endpoint rounding has the same precision. A sufficient independent-endpoint budget for `U-V mod p^t` is `t+3` digits at ordinary primes and `t+4` at exceptional primes; the joint-jet representation can instead retain the divided cancellation directly. These are typed p-adic claims, not claims about physical time, energy, real-valued continuity or a native six-axis transfer.

**Executed author verification.** A Python standard-library exact `Fraction`/factorial certificate checked all 79 target primes `13≤p<1000` for rank/valuation and polynomial exception classification, then independently verified reconstruction for `p=13,19,37,139,181,199,277,373`; the exceptional pole and cancellation table passed. The R52 exact algebraic inverse and jets were separately checked on all eight primes against the unchanged rational factorial terms. This is author checking, **not** independent replication, Lean or native p=373 H0/B0.

**Frontier / do not repeat.** Completed new portable units: exceptional high-high Green endpoint pole classification (R51) and integral divided-difference jet repair (R52). Inputs R47–R50 retain their original credit. Next exact mathematical unit: determine whether the correlated jet `Y` admits a source-preserving W/S **cross-rank** WZ telescoping representation compatible with R23 low-half `p²` difference, R36 PF Green and R38–R42 high-rank labels, including exceptional `139,199,277` and sample `181,373`. Keep both original endpoint labels and all fixed `z=2` Hasse J/E six-channel plus infinity provenance; a special prime cancellation must not be elevated into the full `W_p=S_p mod p³` proof.

**Native/ownership state at research creation.** Actual recovery Issue for this logical lane `awdawmip/kimi-query-bridge#6622`: `recovery_status SUCCEEDED`, current own session `MCP-06f7ad61a8d841d9ba1ba1ef4d088d94` / Researcher `EM-ENTERPRISE-5298BA`, `runs=[]`, `unopened_claims=[]`, `pending=[]`, `unpublished_uploads=[]`, two **neutral** preserved staging manifests, `execution_authorized=false`, `source_authority_verified=false`. Fresh direct gateway continuation returned `CONTROL_QUOTA`; own exact ordinary-control continuation was queued for read. Historical checkpoint/predecessor conflict remains tracked in Enterprise Math Issue #1558; the Research lane did **not** take a CLAIM/open/publish/freeze/review or rebind past staging. Research Activity new semantic events require their own current authorized write and readback. The mother task and original H0/B0, Frobenius `η/κ`, `[X]U mod p²`, native experiment and independent Driver acceptance remain OPEN.
