# D25 / original endpoint: exact square transport and second-digit merger of both nonzero seams

2026-10-24 | TASK_RESEARCH portable author proof, exact-arithmetic self-check | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. This is not a Source checkpoint, Result, claimed run, native benchmark or independent review.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; **frozen source pin c47e13e4aba0e006366f989d6334d443f6333ae3**. Authorship/provenance: logical Research lane chatgpt-research-onhour-enterprise-math-20260923; distinct from maintenance lane. Verified global knowledge head bdc4c6b8927afbdf4d031565b3bec53d95936bbc (P000 ACTIVE_LOCKED); source control read head 390d0e89ee9c9327d3c8f1a098b18a3a78945e48. Neither changes the frozen research source pin.

## 1. Preserved original problem

Reuse the original endpoint Gosper/two-seam proof at [070a56781c04](20261024_onhour_d25_original_endpoint_gosper_two_seam_p2.md), *not* as a new result. For m>=1, p=6m+1, use its exact original recurrence

\[
R_0=1,\quad \frac{R_{n+1}}{R_n} =
\frac{(4m+1+2n)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)}
\]

and

\[
K_{p,n}=\frac{(2p+1-3n)(6n+2p+3)}
{(3n+p+2)(3n+2p+1)}.
\]

For prime p, T_2:=R_{2m}/p and T_4:=R_{4m}/p are p-adic units. The old **exact** identity reads

\[
\mathcal K_p=\mathcal U_m+C_2(p)T_2+C_4(p)T_4,\quad
\mathcal U_m:=\sum_{\substack{0\le n<4m\\n\ne2m}}K_{p,n}R_n,
\]

\[
C_2(p)=\frac{(p+2)(4p+1)}{3(2p+1)},\qquad
C_4(p)=\frac{-8p^2+14p-3}{4p-1}.
\]

Importantly, C_4 already contains the original n=4m term **combined with the n=4m+1 terminal**, so neither is omitted or added twice. Previously proved EP/LIFT equivalence remains

\[
S_{4m}(2m)\equiv p(4/3)^{p-1}\pmod{p^3}
\iff \mathcal K_p\equiv G_m\pmod{p^2},\quad
G_m=(-1)^m\frac{((2m)!)^3}{((3m)!)^2}.
\]

## 2. New exact rational all-m factorial and square-transport theorem

**Theorem F/SQ** (no primality required). For all m>=1 and n>=0,

\[
\boxed{R_n=\frac{(4m+2n)!(3n)!((2m)!)^2}
{216^n(n!)^2((2m+n)!)^2(4m+n)!}.}\tag{F}
\]

Therefore

\[
\boxed{R_{2m}=\frac{\binom{8m}{4m}}{216^{2m}},\qquad
\frac{T_4}{T_2}=\frac{R_{4m}}{R_{2m}}
=\left(\frac{\binom{12m}{4m}}{216^m\binom{6m}{2m}}\right)^2.}\tag{SQ}
\]

**Proof:** F is 1 at n=0. Its n+1/n ratio equals the original displayed R ratio: factorial increments yield numerator (4m+2n+1)·2(2m+n+1)·(3n+1)(3n+2)·3(n+1), and denominator 216(n+1)^2(2m+n+1)^2(4m+n+1); cancellation gives the exact defining ratio. Substitute n=2m and 4m, then cancel factorials. SQ is thus an **exact square in Q**. Both distinct seam branch identities are retained.

## 3. New, full mod-p² *two-seam merger*

Assume p=6m+1 is prime >=7. Put

\[
H_k=\sum_{j=1}^k1/j,\quad q_p(6)=\frac{6^{p-1}-1}{p}\in\mathbb Z,\quad
B_m=\frac{(2m-1)!(2m)!}{(4m)!}
=\frac1{2m\binom{4m}{2m}}\in\mathbb Z_{(p)}^\times.
\]

**Lemma TR (two-seam unit transport)**

\[
\boxed{\frac{T_4}{T_2}
\equiv \frac19\left[1-p(2H_{2m}+4+q_p(6))\right]\pmod{p^2}.}\tag{TR}
\]

Proof: finite products for h=4m (even) give

\[
\binom{2p-2}{h}
\equiv(h+1)\left[1-2p(H_{h+1}-1)\right],\qquad
\binom{p-1}{2m}\equiv1-pH_{2m}\pmod{p^2}.
\]

All harmonic denominators are <p. Substitute these in exact SQ and use 216^{2m}=6^{p-1}\equiv1+pq_p(6). Harmonic reflection gives

\[
H_{4m+1}=H_{p-2m}\equiv H_{2m-1}
=H_{2m}-1/(2m)\equiv H_{2m}+3\pmod p.
\]

Since (4m+1)^2=(2p+1)^2/9\equiv(1+4p)/9 mod p², all terms combine to TR.

**Lemma T2 (explicit first-seam unit)**

\[
\boxed{T_2\equiv
B_m\left[1-p\left(\frac1{2m}+q_p(6)\right)\right]\pmod{p^2}.}\tag{T2}
\]

Proof: R_{2m}=\binom{p+2m-1}{4m}/6^{p-1}. Extract the one numerator factor p. The remaining numerator factors split into p+a (1<=a<=2m-1) and p-b (1<=b<=2m). As 2m is even, the sign is positive; hence the *exact* identity

\[
\frac1p\binom{p+2m-1}{4m}
=B_m\prod_{a=1}^{2m-1}(1+p/a)
\prod_{b=1}^{2m}(1-p/b)
\equiv B_m(1-p/(2m))\pmod{p^2}.
\]

Multiply by 6^{-(p-1)}\equiv1-pq_p(6). No division by a nonunit is used.

**New theorem MERGE (two individually nonzero seam contributions have one full second-digit normal form):**

\[
\boxed{\mathcal S_m:=C_2(p)T_2+C_4(p)T_4
\equiv B_m\left[1+\frac p9
\bigl(28-6H_{2m}-12q_p(6)\bigr)\right]\pmod{p^2}.}\tag{MERGE}
\]

Proof: C_2\equiv(2+5p)/3 and C_4\equiv3-2p mod p². By TR,

\[
\boxed{C_2+C_4T_4/T_2
\equiv1+\frac p9(1-6H_{2m}-3q_p(6))\pmod{p^2}.}\tag{COEFF}
\]

Multiply by T2, apply T2 and -1/(2m)\equiv3 (mod p). That gives MERGE exactly. The two seam terms **do not vanish**: \(\mathcal S_m\equiv T_2\equiv B_m\ne0\pmod p\). The p² correction is explicitly retained.

## 4. Original LIFT now reduces to one regular-forcing p² problem

Substitute MERGE into the inherited exact Gosper-to-EP equivalence:

\[
\boxed{\mathrm{EP/LIFT}\iff
\mathcal U_m\stackrel{?}{\equiv}
G_m-B_m\left[1+\frac p9(28-6H_{2m}-12q_p(6))\right]
\pmod{p^2}.}\tag{REG-P2}
\]

This is an exact equivalence, **not an all-prime proof of the right side**. Split U=U^{lo}+U^{hi}, with lo over 0<=n<=m and hi over m<n<4m, n!=2m. Existing valuations give U^{hi} in p Z_(p). Previously proved first digit of this original endpoint, together with MERGE mod p, implies U^{lo}-G+B in p Z_(p). Thus (REG-P2) is the strictly equivalent **single open divided regular obstruction**

\[
\boxed{\Delta_m^{reg}:=
\frac{\mathcal U_m^{lo}-G_m+B_m}{p}
+\frac{\mathcal U_m^{hi}}p
+\frac{B_m}{9}(28-6H_{2m}-12q_p(6))
\stackrel{?}{\equiv}0\pmod p.}\tag{D-REG}
\]

Both displayed divisions are p-integral by the cited existing laws; they are not illegal modular inversions. The previous independent seam units have been fully removed from the next second-digit proof obligation. The *ordinary regular forcing*, not the native experiment, remains unsolved.

## 5. Reproducible author exact computations

Two representations were actually executed: an exact rational Fraction recurrence at m=1,...,10 checks the seam values and SQ, and an independent valuation/p-unit recurrence modulo p³ checks TR, T2, COEFF, MERGE and the original U+MERGE versus G for all **80 primes p<=1000, p=1 mod6**, 45 of which lie in target residue classes 13 or 19 (mod24). These last endpoint checks are finite author observations only. Reproducible Python3 stdlib checker, now committed as [two-seam exact checker](20261024_onhour_d25_two_seam_exact_square_second_digit_merge_check.py), SHA256 9a3f793fceb09b33fe1072d9e94213f614c625e6ed55005b8947111b49ff4275 (Git blob dba3f6c0561a9ec0de5a9bd78672d8552c037321). Arbitrary-n formula F is separately proved by the displayed ratio, not by finite testing.

Selected actual residues (each modulus p²):

| p | T2 | T4/T2 | U_low | U_high | MERGE | G | divided-low + high/p + MERGE correction (mod p) |
|--:|--:|--:|--:|--:|--:|--:|:--|
| 13 | 28 | 107 | 162 | 52 | 106 | 151 | 6+4+3=0 |
| 19 | 280 | 302 | 203 | 152 | 147 | 141 | 4+8+7=0 |
| 31 | 86 | 937 | 929 | 496 | 706 | 209 | 10+16+5=0 |
| 37 | 511 | 736 | 1218 | 592 | 807 | 1248 | 12+16+9=0 |
| 61 | 3114 | 1559 | 118 | 915 | 1284 | 2317 | 31+15+15=0 |

Finite agreement does not prove D-REG globally or replace the unchanged native benchmark.

## 6. BRC, provenance, permissions, and mandatory next unit

BRC=COMPOSE_APPLIED / REUSE_APPLIED (no native BRC executable invoked). Exact signed term carrier R_n, branch identity n, p-valuation and unit, seam labels n=2m and 4m, original terminal n=4m+1, and precision observer modulo p² after division by p are retained. MERGE licenses a single-scalar representation for **this declared total-second-digit observer only**; it does not assert branch equality, positive mass cancellation, or higher-digit preservation.

Highest new author frontier: all-m exact F/SQ; all target primes proved TR/T2/MERGE; original EP reduced to D-REG. **Unreviewed, not admitted**. D24 frozen UR result remains consumed, not reopened. Next discriminating unit: find a genuine terminating weighted telescope or an exact first-order-in-p formula for U_low *together with* U_high/p, matching the explicit B(28-6H-12q)/9 in D-REG. Preserve the n=m+1 valuation onset, n=2m discontinuity, full high tail and terminal; prove all-prime cancellation or give a strict obstruction. No further seam factorial replay or larger prime scan substitutes for it. Original native benchmark and independent Driver review remain NOT EXECUTED.

Control: Issue #1539 continues native Researcher/Source authorization repair. This connected Sites gateway reports 0.6.11, research_authority_granted=false and executor_binding_configured=false; subject-local recovery_status is not exposed as a direct action here. Prior request IDs/old staged UR material are not replayed or adopted. No CLAIM/run/checkpoint/freeze is claimed. Future formally authorized continuation must first read real per-subject recovery/receipt and exact canonical Source, then use real Researcher session/claim/open and native writer. The original hourly task schedule and notification configuration were not changed.
