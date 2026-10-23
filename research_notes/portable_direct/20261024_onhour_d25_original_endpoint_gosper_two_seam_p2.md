# D25/SECOND-DIGIT-LIFT — Original endpoint: exact Gosper deformation and two indispensable p-adic seams

2026-10-24 | TASK_RESEARCH portable author evidence | AUTHOR-PROVED EXACT RATIONAL IDENTITY / EXACT AUTHOR SELF-CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. This is not native benchmark, formal Source checkpoint/CLAIM/Result, mathematical admission or independent review.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; canonical publication TP2-B6F4FC938FF94941C1B7; **frozen Source pin c47e13e4aba0e006366f989d6334d443f6333ae3**, unchanged. Logical Research lane provenance: chatgpt-research-onhour-enterprise-math-20260923; not CONTROL_PLANE_MAINTENANCE. Global-knowledge read head main@b8bb96dfb7e40cee5c70197be3d0ddc2a355fbe1, P000 ACTIVE_LOCKED. Exact external rational/p-adic arithmetic; no change to native X6 physics/worldview. Reuses prior WZ/first digit, LOW/Beta JOINT-P2 and Morley-port notes; no old theorem or native experiment is marked complete by this paper.

## 1. A direct, termwise telescoper for the **same original endpoint**, not another LOW jet

For integer m>=1, put p=6m+1 (primality is NOT needed for this section), and set

$$
R_0=1,\quad
\frac{R_{n+1}}{R_n}=
\frac{(4m+1+2n)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)}.
$$

The original endpoint is exactly

$$
S_{4m}(2m)=\mathcal A_m\sum_{n=0}^{4m}(6n+2p-1)R_n,\qquad
\mathcal A_m=\frac{(p-1)!}{3^{p-1}((2m)!)^3}.
$$

Equivalently, retaining all original summands,

$$
\frac{R_{n+1}}{R_n}=
\frac{(6n+2p+1)(3n+1)(3n+2)}
{12(n+1)(3n+p+2)(3n+2p+1)}.
$$

Define the explicit potential and its rational forcing

$$
G_n^{\rm Gos}=-12nR_n,\qquad
K_{p,n}=\frac{(2p+1-3n)(6n+2p+3)}
{(3n+p+2)(3n+2p+1)}.
$$

**New all-m exact termwise identity**:

$$
\boxed{(6n+2p-1)R_n =
G_{n+1}^{\rm Gos}-G_n^{\rm Gos}+pK_{p,n}R_n.}\tag{TG}
$$

Proof: divide by R_n, substitute the displayed ratio, and bring to a common denominator. The resulting numerator is identically

$$
(2p+1-3n)(6n+2p+3)p.
$$

This is an equality in Q for EVERY m>=1,n>=0, not a modular guess. At p=0 the source kernel vanishes and G_n=-12n(1/6)_n/(2^n n!) is the exact Gosper antidifference for (6n-1)(1/6)_n/(2^n n!). Thus TG is a genuine deformation of a **closed base telescope**; the remaining forcing is explicitly proportional to p and is not set to zero.

Sum (TG) through the original terminal n=4m:

$$
\boxed{\sum_{n=0}^{4m}(6n+2p-1)R_n
=-12(4m+1)R_{4m+1}
+p\sum_{n=0}^{4m}K_{p,n}R_n.}\tag{T}
$$

No term of the original truncation was discarded.

## 2. The two poles and the terminal exactly combine into a p-integral certificate

Now let p=6m+1 be prime. Directly counting p factors in the **original exact ratio** yields

$$
v_p(R_n)=
\begin{cases}0,&0\le n\le m,\\1,&m<n\le4m+1.\end{cases}
$$

The only p-bearing ratio events before n=4m+1 are: n=m (first numerator factor contributes p), n=2m (second numerator factor and last denominator factor each contribute p), and n=4m (third numerator factor and penultimate denominator factor each contribute p). In particular T_2:=R_{2m}/p and T_4:=R_{4m}/p are p-units. Within 0<=n<=4m the denominator of K_{p,n} contains a p factor **only at n=2m and n=4m**, not at generic n.

At those two indices the exact values are

$$
K_{p,2m}R_{2m}
=\frac{(p+2)(4p+1)}{3(2p+1)}T_2,\qquad
K_{p,4m}R_{4m}
=\frac{6p-1}{4p-1}T_4.
$$

The one-step ratio at the upper terminal is exactly

$$
\frac{R_{4m+1}}{R_{4m}}=
\frac{(2p-1)^2}{6(4m+1)(4p-1)}.
$$

Hence the terminal from (T), after division by p, combines **without approximation** with the n=4m pole into

$$
\left[\frac{6p-1}{4p-1}
-\frac{2(2p-1)^2}{4p-1}\right]T_4
=\frac{-8p^2+14p-3}{4p-1}T_4.
$$

Define the fully explicit original-endpoint divided certificate

$$
\boxed{
\mathcal K_p=
\sum_{\substack{0\le n<4m\\n\ne2m}}K_{p,n}R_n+
\frac{(p+2)(4p+1)}{3(2p+1)}\frac{R_{2m}}p+
\frac{-8p^2+14p-3}{4p-1}\frac{R_{4m}}p.
}\tag{2S}
$$

**Exact all-target-prime theorem**: every term of (2S) belongs to Z_(p), and

$$
\boxed{\frac{S_{4m}(2m)}p=\mathcal A_m\mathcal K_p\quad\text{in Q}.}\tag{EXACT}
$$

The proof is just (T) and the two seam substitutions above, but its scientific consequence is stronger than a presentation change: it proves directly from the original R_n that the first p factor can be extracted without ever inverting the zero divisors at the two seams. It gives a p-integral finite-difference forcing with a **specific rational Gosper potential and terminal**, not an unspecified LOW/Beta equality.

Both normalized seam corrections are individually nonzero modulo p for every p>=7 in this family:

$$
\frac{(p+2)(4p+1)}{3(2p+1)}T_2\equiv\frac23T_2\not\equiv0\pmod p,
\qquad
\frac{-8p^2+14p-3}{4p-1}T_4\equiv3T_4\not\equiv0\pmod p.
$$

Thus any proof dropping the n=2m pole or the joint n=4m/terminal contribution **without an additional proved compensation** loses the original scalar. The signs/cancellations are signed rational amplitudes, not positive BRC mass conservation.

## 3. Exactly equivalent second-digit target with no illegal modular division

The original unfrozen hard endpoint obligation remains

$$
S_{4m}(2m)\stackrel{?}{\equiv}p(4/3)^{p-1}\pmod{p^3}.
$$

Because A_m is a p-unit and (EXACT) already establishes S/p in Z_(p), this is exactly equivalent to

$$
\mathcal K_p\stackrel{?}{\equiv}
\mathcal A_m^{-1}(4/3)^{p-1}
=\frac{4^{p-1}((2m)!)^3}{(p-1)!}
\pmod{p^2}.
$$

Reuse (do not re-prove as a new result) the earlier all-target-prime Morley-port congruence

$$
\frac{4^{p-1}((2m)!)^3}{(p-1)!}
\equiv G_m:=(-1)^m\frac{((2m)!)^3}{((3m)!)^2}\pmod{p^2}.
$$

Therefore **same, still-open LIFT, now an exact two-seam Gosper forcing target**:

$$
\boxed{ {\rm EP/LIFT}\quad\Longleftrightarrow\quad
\mathcal K_p\equiv G_m\pmod{p^2}. }\tag{2S-P2}
$$

The identity (TG), valuation proof, seam units, and equivalence (2S-P2) are proved for all target primes. The right-hand p^2 congruence in (2S-P2) is **not** proved for all target primes, so this paper does NOT claim the LIFT supercongruence.

This is a parallel exact input interface to the existing LOW/Beta JOINT-P2, NOT an unreviewed replacement of Source, native benchmark, current selector, or the frozen m/source pin. Next research must match the **regular forcing sum plus BOTH normalized seams** to G_m modulo p^2 with a genuine terminating contiguous/WZ-Gosper primitive, or exhibit an exact nonzero obstruction. In particular, matching only generic n terms is mathematically insufficient.

## 4. Executed independent-arithmetic author checks

[Companion exact Python checker](./20261024_onhour_d25_original_endpoint_gosper_two_seam_p2_check.py) verifies each individual (TG) and the exact finite sum (T),(EXACT) for m=1,...,12 (including m with composite 6m+1). An independent p-factor-stripped modular stream checks the same ORIGINAL endpoint and (2S) for all 25 primes 7<=p<=241 with p=6m+1. All pass the **identity and exact two-seam reductions**. For these same 25 primes, the *unproved* target second-digit residual also happens to vanish; that check is limited finite author evidence and does not extend the previously reported 611-case scope or finish the theorem. No native benchmark was executed.

Finite witnesses (all residues taken with their stated prime modulus):
| p | R_(2m)/p mod p | R_(4m)/p mod p | regular forcing mod p | n=2m seam mod p | n=4m+terminal mod p | K_p mod p^2 | G_m mod p^2 |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 13 | 2 | 6 | 6 | 10 | 5 | 151 | 151 |
| 19 | 14 | 10 | 13 | 3 | 11 | 141 | 141 |
| 31 | 24 | 13 | 30 | 16 | 8 | 209 | 209 |

The nonzero seam residues are exact consequences of the p-unit valuation lemma, not extrapolations from the table. The finite target-congruence matches are author checks only.

## 5. BRC / next mandatory original objective / operational continuation

BRC REUSE_APPLIED / COMPOSE_APPLIED: signed hypergeometric carrier n; exact v_p+unit R_n; p-adic first/second-digit observer, original 4m terminal and both 2m/4m seams. Compression from original weighted terms to (TG) is an **exact telescoping identity for the full scalar**, with every future operation requiring individual term provenance retaining original R_n. Moving to mod p^2 assumes exactly the declared second-digit observer; it does not apply automatically to a future p^3/p^4 observer.

Next **discriminating original mathematical unit**: over Z_(p)/p^2, solve the induced finite Gosper co-boundary for the regular K_{p,n}R_n sum while keeping the two isolated nonzero seam values; compare its true endpoint and seam against G_m. A candidate must show algebraic n-dependence, complete rational denominators, exact terminal/seam and rigorous p^2 cancellation for all target primes (or an explicit counterexample). Coordinate with prior LOW/Beta JOINT-P2 but do not claim that a renaming has discharged either. Original native benchmark: unchanged scientific object/input/validation and STILL NOT EXECUTED.

Source/recovery status: existing control support issue #1539 remains OPEN; most recent static-readonly Sites service reports version 0.6.11, research_authority_granted=false, executor_binding_configured=false. No own verified Researcher session or Source claim/run/checkpoint was created by this note. Original Research lane history #6186/#6187/#6188 are bridge Issue identifiers, not new native request_ids; they have prior remote dispositions and are not replayed as fresh writes. Three historical staging items remain separate archival sources. Site read-only cannot be silently promoted to execution authority. A future genuinely authorized owner must first read actual Source exact continuation and its original receipts, then follow current selector/session/claim/open. Native benchmark and independent Driver review remain explicit missing evidence, with #1539 as the actual control support path. Existing TASK_RESEARCH timer configuration and notification behavior were not changed.

References:
- prior author JOINT-P2: research_notes/portable_direct/20261024_onhour_d25_joint_morley_p2_normalization_certificate.md @ bea1356f2d058231db5fa5a2cda6dd6a0f6aa393
- original endpoint streaming/611 finite checks: research_notes/portable_direct/20261023_onhour_d25_endpoint_padic_stream_611.md @ 4fe67f915d52a563825757c8d6e9e199f2eb4b64
- original endpoint/band proof sources remain frozen at c47e13e4aba0e006366f989d6334d443f6333ae3.


## 6. Further exact unit: obstruction to a one-term **exact rational** Gosper primitive

After durable publication of (TG)/(2S), a second symbolic proof isolates what remains impossible for the **original** full weighted hypergeometric term, without replacing the original finite question. Fix ANY integer m>=1 and let

$$t_n=(6n+12m+1)R_n.$$

Define three exact rational polynomials

$$
A(n)=\frac{(3n+1)(3n+2)(4m+2n+1)}{36},\quad
B(n)=(n+1)(n+2m+1)(n+4m+1),\quad
C(n)=n+2m+\frac16.
$$

The full original term ratio factors as

$$
\frac{t_{n+1}}{t_n}
=\frac{A(n)}{B(n)}\frac{C(n+1)}{C(n)}.
$$

**Negative theorem (all fixed positive integer m):** There is **no rational function** f(n) in C(n) with

$$
t_n=t_{n+1}f(n+1)-t_nf(n)
$$

as an identity in n. Thus the original weighted summand does NOT possess a universal **one-term exact rational same-kernel Gosper primitive**. This theorem does NOT forbid a modulo-p^2 finite-interval antidifference, a higher-order WZ pair, a multi-term creative telescope, or a finite polynomial of degree growing with the terminal; it does not disprove EP.

**Elementary proof (no black-box failure-as-proof):** If rational f existed, put
\(X(n)=C(n)f(n)/B(n-1)\). The ratio identity rearranges into

$$
\boxed{A(n)X(n+1)-B(n-1)X(n)=C(n),}
\qquad B(n-1)=n(n+2m)(n+4m).
\tag{G}
$$

Suppose X has a pole and choose one pole \(\alpha\) of maximal real part. Since X(n+1) has no pole at n=alpha (a pole there would require X at alpha+1), (G) forces \(B(\alpha-1)=0\); hence alpha is one of the **integers** \(0,-2m,-4m\). But A(n) has roots only \(-1/3,-2/3,-2m-1/2\), NONE an integer. At n=alpha-1 the term \(A(n)X(n+1)\) therefore has a pole, so cancellation in (G) forces X to have a pole also at alpha-1. Iterate: X must have poles at alpha-k for every positive integer k, contradicting rationality. Therefore X is a polynomial.

If X has degree d>=0 with leading coefficient x_d, the leading term of the left side of (G) is
\((1/2-1)x_dn^{d+3}=-x_dn^{d+3}/2\), because A has leading coefficient 1/2 while B(n-1) has leading coefficient 1. This cannot equal C(n), of degree 1. X=0 also fails. Contradiction; theorem proved for every m>=1.

**Interpretation:** The exact one-term potential \(G_n^{\rm Gos}=-12nR_n\) from (TG) correctly leaves a nonzero \(pK_{p,n}R_n\) forcing. There is no other rational multiple of the same full weighted term that removes this forcing **exactly at all n**. A valid next proof must exploit the arithmetic modulus and the two nonzero seams (or a genuinely different multi-term/parameter WZ identity), not repeatedly search for a universally exact one-term rational antidifference. This is a mathematically proved choice-of-method obstruction, not a claim that no p-adic supercongruence proof exists. No additional Source/task ownership or native experiment is claimed.
