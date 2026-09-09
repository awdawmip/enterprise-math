# JT2: finite UR transport and prior-candidate applicability

Status: `DRIVER_AUTHORED_CANDIDATE / SOURCE_EXPOSED / INDEPENDENT_REVIEW_PENDING`.

Author: `EM-DVR-C777E7`, the delegated JT2 line Driver. This is a new paper argument produced while checking an interface; it is not a metadata-only theorem check, a clean independent discovery, a formal Driver acceptance, or a return under a newly claimed UR task. No mathematical program was run.

The published intake at `7894372ffc0b39513736ea74c607b4d8ea3e82f9` correctly left the transport unproved at that time. Its dossier and ledgers remain unchanged. This candidate supplies the finite arguments below and leaves their non-author review pending. The two parent identities and all existing task/Result bytes remain intact.

## 1. Inputs, coefficient ring, and scope

Let p=6m+1 be prime, p>3, and work in the localization Z_(p). Define the following particular finite polynomials, without silently redefining an incompletely pinned predecessor symbol:

\[
c_k=\frac{(1/6)_k(1/3)_k}{(k!)^2},\quad
b_k=\frac{(1/3)_k(2/3)_k}{(k!)^2},\quad
d_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3},
\]
\[
\mathcal F_p(z)=\sum_{k=0}^{p-1}c_kz^k,\qquad
\mathcal L_p(u)=\sum_{k=0}^{p-1}b_ku^k,\qquad
\mathcal W_p(z)=\sum_{k=0}^{p-1}(6k+1)d_kz^k.
\]

All denominators here are p-units. The exact old objects are
\(g=\mathcal F_p(1/2)\), \(h=(\mathcal F_p+12z\mathcal F_p')(1/2)\), and \(W_p=\mathcal W_p(1/2)\). Sun's definition gives \(B(t)=P_{p-1}(-1/3,t)=\mathcal L_p((1-t)/2)\).

Substitution is permitted in A=Z_(p)[t]/(2t²-1); no choice of a complex square-root branch is needed for a polynomial congruence. The involution t↦-t preserves both labeled ports. In characteristic p, t^p=t(2/p); hence the exchanged-Frobenius condition means (2/p)=-1. Together with p=3n+1 and p>3, this gives n=2m and exactly p≡13 or 19 mod24. This statement uses Frobenius modulo p, not an unproved equality t^p=-t modulo p².

The inherited CM0/SIMPLE input is retained separately: \(H_m(z)=Q_m(1-z)\), \(\mathcal F_p\equiv H_m\pmod p\), \(H_m(1/2)=0\pmod p\), \(Q_m'(1/2)\) a unit, and \(P_n'(t)=2tQ_m'(1/2)\). Their complete prior return is source `EBP6JT_RETURN` in the companion manifest. Its original proof and historical numerical checks are not rerun here.

## 2. Candidate finite quadratic transport

**Claim.** In Z_(p)[u],
\[
\mathcal L_p(u)\equiv\mathcal F_p(4u(1-u))\pmod {p^2}.
\tag{Q2}
\]

Use the normalized formal power-series identity
\[
{}_2F_1(1/3,2/3;1;u)
={}_2F_1(1/6,1/3;1;4u(1-u)).
\]
This is the specialization of [DLMF 15.8.18](https://dlmf.nist.gov/15.8.E18), interpreted at u=0 where both constant terms are 1. It is an exact formal identity over Q, not an assumed congruence at a CM value.

For 2m+1≤k≤p-1, (1/6)_k contains p/6, from index m, and (1/3)_k contains p/3, from index 2m. Thus c_k belongs to p² Z_(p). A coefficient of u^j with j<p in the composite infinite series uses only k≤j; consequently the two finite sides of (Q2) have exactly equal coefficients in those degrees, before reduction. For j≥p, a contributing term (4u(1-u))^k must have k≥ceil(j/2)≥3m+1>2m. Its coefficient c_k is divisible by p². The left side has degree p-1. This proves (Q2) in every degree. No inference is made about the infinite series' coefficients at indices k≥p, where factorial denominators would need separate treatment.

At u=(1-t)/2, 4u(1-u)=1-t²=1/2. Therefore
\[
\boxed{B(t)\equiv g\pmod {p^2}}
\tag{B2}
\]
holds in A, and also at -t. This proof only uses p≡1 mod6; the additional inert/exchanged conditions enter the UR application. It neither proves nor assumes the QTF3 fixed-point congruence modulo p³.

## 3. Candidate finite weighted first-digit bridge

**Claim.** In Z_(p)[z],
\[
\mathcal W_p(z)\equiv
\mathcal F_p(z)\bigl(\mathcal F_p(z)+12z\mathcal F_p'(z)\bigr)
\pmod {p^2}.
\tag{C2}
\]

The exact Clausen identity F(z)²=sum d_k z^k, for F(z)={}_2F_1(1/6,1/3;1;z), is the specialization of equation (3.4) in [Chisholm et al.](https://www.mdpi.com/2227-7390/1/1/9). Apply 1+6z d/dz to obtain F(F+12zF'). In degrees j<p, the corresponding finite coefficients still agree exactly. In any remaining degree i+k≥p, at least one of i,k exceeds 2m, since 4m<p. That factor c_i or c_k is divisible by p². Differentiation here only multiplies by the integer 12k; it introduces no denominator. All high terms therefore vanish modulo p², proving (C2).

Evaluating gives W_p≡gh mod p². The inherited CM0 implies p divides g. Also h≡H_m(1/2)+6H_m'(1/2)≡-6Q_m'(1/2) mod p. Dividing gh-p by p is now justified, and yields the exact equivalence
\[
W_p\equiv p\pmod {p^2}
\quad\Longleftrightarrow\quad
(g/p)(-6Q_m'(1/2))\equiv1\pmod p.
\tag{W2-UR}
\]

Using (B2), the unit t, and P_n'=2tQ_m', the same condition is equivalent to
\[
3B(t)P_n'(t)\equiv-pt\pmod {p^2}.
\tag{UR-SLOPE}
\]
The frozen barycentric lift then gives (P_(2n)(t)+2P_n(t))P_n'(t)≡-pt mod p². SIMPLE remains a required inherited input when these formulas are interpreted as a reciprocal/unit certificate; it is not silently discarded.

Only a first-digit bridge was checked. High terms proved divisible by p² above can contribute at p³. The reflected R_p, G_p modulo p², and the second-digit LIFT obligation are preserved.

## 4. PR1383: theorem applicability and the recovered normalization

The exact candidate is `9a1d0b374564abfcc888458b79c1030d52da924c`, file `ur_chisholm_closure_lift_frontier_20260908.md`, SHA256 `1f4e8207a969a5ccf151e9f60d5eece93249d655b46c78a23a8c71e77ce1e6e6`. It was observed open/unmerged; its own theorem labels are predecessor claims, not this Driver's verdict.

The primary [Chisholm–Deines–Long–Nebe–Swisher Theorem 1](https://www.mdpi.com/2227-7390/1/1/9) uses a CM-determined Ramanujan coefficient a, appropriate unit/unramified/good-reduction hypotheses, and the signed factor sgn·((1-λ)/p)p modulo p². Its d=3 model is y²+xy+(u/27)y=x³, with λ=4u(1-u). The paper's stronger p³ statement is identified there as conjectural, not supplied by Theorem 1.

The following is this author's explicit applicability calculation, using the inherited CM identification. Put u=(1-t)/2, t²=1/2. The displayed Weierstrass model has
\[
\Delta=\frac{u^3(1-u)}{3^9},\quad
j=\frac{27(9-8u)^3}{u^3(1-u)}
=1728(1399+1976t).
\]
Thus its two j-values are exactly 2417472±1707264√2, matching the prior return's discriminant -24 pair. Since u(1-u)=1/8, the displayed discriminant is a unit for p>3. Q(√2) is unramified there. The inherited CM field is Q(√-6); for p≡13,19 mod24 both (-6/p) and (2/p) are -1, so supersingularity gives sgn=-1 and the two signs cancel. λ=1/2 is rational and satisfies the real/size/unit conditions. These comparisons do not enlarge the residue scope or redo the CM class-polynomial theorem.

**Primary normalization recovered.** The weight is not arbitrary. In Jonathan and Peter Borwein, [*Pi and the AGM*, §5.5](https://carmamaths.org/jon/Preprints/Papers/Submitted%20Papers/Elliptic%20moments/pi-agm.pdf), printed p.186, (5.5.33) has coefficients
\[
\bigl(a_s(N)+k b_s(N)\bigr)
\frac{(1/2-s)_k(1/2+s)_k(1/2)_k}{(k!)^3}
G_s(N)^{-24k}.
\]
The convention \(G_s(N)^{-12}=2\lambda_s^*(N)\lambda_s^{*\prime}(N)\), together with (5.5.28i) on p.185, identifies \(G_{1/6}(N)\) with the \(H_N\) used in Exercise 19(b). On p.190, Exercise 19(b)(ii) gives \(H_2^{24}=2\), and Exercise 20(b)(i) supplies
\[
a_{1/6}(2)+k b_{1/6}(2)=\frac{6k+1}{3\sqrt3}.
\]
Consequently the series address is \(G_{1/6}(2)^{-24}=1/2\), its three parameters are \((1/3,2/3,1/2)\), and normalizing the constant coefficient to 1 gives the Chisholm weight \(a=b_{1/6}(2)/a_{1/6}(2)=6\). The corresponding analytic constant is \(3\sqrt3/\pi\); it is not an extra factor in the finite congruence. This argument consumes the book's published exact parameter values and formula; it does not claim a fresh proof of its elliptic-integral exercises.

These pages were actually rendered and visually read after the initial image-only text extraction returned no hits. The observed PDF SHA256 is `2ea662124501c5a1604c96c705da10049e0dd81824562f3b48853672bb53ca71`; PDF page indices 99, 100 and 102 contain printed pp.184–185, 186–187 and 190–191. The companion read receipt preserves the failed locator steps and subsequent visual recovery. Neither a search snippet nor an unread citation is substituted for that recovery.

Combining this normalization, the stated CM/good-reduction scope, Theorem 1 and §3 gives the candidate conclusion \(W_p\equiv p\pmod{p^2}\), and hence (UR-SLOPE), for the matched primes \(p\equiv13,19\pmod{24}\). This is a source-exposed paper deduction using the explicitly retained prior CM0/CM identification and SIMPLE inputs. Its non-author review remains pending; no independent theorem acceptance, new canonical UR Result, or stronger p³ conclusion is asserted.

## 5. Current Sun task: six outputs remain separate

The controlling book is `RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT`, gen2 `TP2-22F5729C777040ECA121`; its exact pin is in the manifest.

| Required output | Evidence now available | Unmet boundary |
| --- | --- | --- |
| 1. Uniform B(t) slope-value congruence | Candidate (B2)/(W2-UR) transfers the source-matched W2 conclusion; §4 now pins the a=6 normalization. | Non-author review remains; no canonical UR acceptance. |
| 2. p² parity-defect definitions and balance | The published W59A definition and Sun recurrence specialize consistently, as below. | This source check is not a new full UR execution. |
| 3. Differentiate and eliminate adjacent values with defects retained | Sun's differentiated recurrence is a valid input. | PR1383 and the finite bridges above contain no such elimination. An external W2 theorem is not this output. |
| 4. Ordinary-Legendre deduction | Multiplication of the frozen barycentric lift gives it conditional on output 1. | No replacement of the barycentric input or precision. |
| 5. Original UR bridge with legal division | Section 3 gives the explicit first-digit transport; p divides g before division. | The old CM0/SIMPLE hypotheses and all second-digit data remain. |
| 6. Exact obstruction if the Sun route is insufficient | A missing derivation has been identified. | Absence of that derivation is not a proof that the recurrence is insufficient, nor a certified minimal obstruction. |

For the source consistency check, [Sun, arXiv:1101.5386v5, Theorem 2.1, Corollary 2.1 and Theorem 2.2](https://arxiv.org/html/1101.5386v5) provide the finite recurrence, its derivative congruence, and reflection modulo p². With A=P_(p-1)(2/3,x), B=P_(p-1)(-1/3,x), C=P_(p-1)(-4/3,x), their specialization gives
\[
2A-xB-C\equiv-2p^2((x-1)/2)^p\pmod {p^3},\qquad
2A'-xB'-B-C'\equiv0\pmod {p^2}.
\]
Keep A(t)+A(-t)=p²α, B(t)-B(-t)=p²β, C(t)+C(-t)=p²γ, with the quotients interpreted modulo p using precision p³. At the exchanged ports the sum of the two right-hand powers is -1 modulo p; hence 2α-tβ-γ≡2 modulo p. These are congruence defects, not exact odd/even polynomial identities. This reproduces the declared balance, not an elimination of all adjacent jets.

## 6. Line decision and next evidence action

Keep both original parent objectives and their task/result states. No duplicate UR, QTF3, audit or integration task is created. No shared bridge task is currently needed merely to express (B2)/(W2-UR); the next action is non-author review of this candidate, including the recovered a=6 convention. The current Sun task still owns its unmet jet/obstruction outputs. Any later change to its hard contract must be explicit.

QTF3's displayed fixed point uses u=1/2 and quadratic address 1; B(t) above uses u=(1-t)/2 and address 1/2. The polynomial proof (Q2) justifies its own p² substitutions, not p³ transport or the QTF3-to-LIFT reflected-tail identification. The full residual-space normalization and exact R_p chain remain separately recorded source obligations. No value of them is invented here.

BRC information boundary: the population remains the labeled prime/Frobenius branches; unit/valuation data are retained before quotients, and p² rather than p³ is the observation horizon of the new finite argument. This is a paper certificate candidate, not a new native executable, API, tool family, Foundation result, formal Result or Working Truth. Historical exact-rational programs were not called or described as migrated. Wallis/sine issue-1159 is outside this line.

Driver-ID: EM-DVR-C777E7 / CONTROL_PLANE

Global-Knowledge-Sync: main@5f14819 / GLOBAL_KNOWLEDGE_V1
