# D25/LIFT: composite-cutoff counterexamples to the 216/2304 transport extension

Research date: 2026-10-29 Asia/Hong_Kong.
Classification: **AUTHOR-SIDE / EXACT FINITE FALSIFICATION / EXECUTED INTEGER CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_EXECUTED / SOURCE_CHECKPOINT_PENDING**.

Mother goal: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Frozen task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
**Scientific Source pin stays** `c47e13e4aba0e006366f989d6334d443f6333ae3`. This note is a noncanonical external author artifact, not a Source task mutation.

## Already established inputs, not claimed as new

The prior author-side D25 notes at `66ad9fdaddc4389a5d6f544cb9864fde9a5dacd6` and `7f23e5cb67cd455564317004e377feba60ace1bb` provide the exact complementary-half formulas and the **finite observation**, not proof, of the prime-index bridge for 781 primes. For primes p>3 define

\[
A_p=\sum_{n=0}^{p-1}(6n+1)\binom{2n}{n}^2\binom{3n}{n}216^{-n},
\qquad
B_p=\sum_{n=0}^{p-1}(8n+1)\binom{2n}{n}^2\binom{4n}{2n}2304^{-n}.
\]

The genuine prime conjecture `A_p = B_p mod p^3` is still open. The published Guo–Zudilin supercongruence for the B-model is an external prior theorem; this note does not reprove or promote it.

## New exact negative result: primality cannot be removed

For **any** integer N≥5 with gcd(N,6)=1, define the same two *complete original-length* sums `A_N` and `B_N`, interpreted in `Z/N^3 Z`. The denominator powers are well-defined because gcd(N,216·2304)=1; both binomial numerators are integral. The seemingly stronger statement

\[
A_N\stackrel{?}=B_N\pmod{N^3}\qquad(N\equiv1\pmod6)
\tag{false-composite-extension}
\]

is **false**, including for prime powers and squarefree composite N. Two rigorous finite witnesses:

\[
\begin{array}{c|c|r|r|r}
N & N^3 & A_N\bmod N^3 & B_N\bmod N^3 &
(A_N-B_N)\bmod N^3\\
25&15625&3150&9400&9375=15\cdot25^2\\
85&614125&416500&144500&272000
\end{array}
\]

For N=25, the bridge does hold mod N² but **fails exactly at its third N-adic digit**: the residual has 5-adic valuation 5, below the required valuation 6. For N=85, it fails **already modulo N²**, since `272000 mod 7225 = 4675`; in fact its 17-adic valuation is 1 (versus 2 needed for N²). These are exact modular facts, not approximations. Extra independent-length witnesses: N=49 has difference `43218=18·49²` mod `49³=117649`; N=55 has difference `48400=16·55²` mod `166375`; N=115 has difference `1101125` mod `1520875`, nonzero already mod `115²`.

**Sharp inference.** Any uniform proof of the actual prime-index bridge must either explicitly exploit primality/finite-field structure or impose some other hypothesis that excludes these composite witnesses. A purely formal argument that claims the full `N^3` divisibility for every `N=6m+1` from the displayed summands alone is refuted. This does **not** prove or refute the still-open prime theorem, and does not constitute the native H0/B0 benchmark.

## Exact certificate and branch/observer semantics

Executed a Python standard-library-only script with **two independently implemented coefficient evaluation routes**: (i) original binomial products and modular inverses, (ii) exact integral factorial quotients before modular reduction, using the identities
\[
\binom{2n}{n}^2\binom{3n}{n}=\frac{(2n)!(3n)!}{(n!)^5},
\qquad
\binom{2n}{n}^2\binom{4n}{2n}=\frac{(4n)!}{(n!)^4}.
\]
Both produce the same modulus-N³ residues for all five composites. Six previously observed prime examples (7, 13, 19, 37, 43, 373) are *regression checks only*. All assertions passed.

Exact test output:

```text
COMPOSITE_WITNESS length=25 modulus=15625 A=3150 B=9400 delta=9375 delta_mod_length2=0
COMPOSITE_WITNESS length=49 modulus=117649 A=86485 B=43267 delta=43218 delta_mod_length2=0
COMPOSITE_WITNESS length=55 modulus=166375 A=96800 B=48400 delta=48400 delta_mod_length2=0
COMPOSITE_WITNESS length=85 modulus=614125 A=416500 B=144500 delta=272000 delta_mod_length2=4675
COMPOSITE_WITNESS length=115 modulus=1520875 A=51750 B=471500 delta=1101125 delta_mod_length2=3450
PASS_D25_COMPOSITE_CUTOFF_FALSIFIER 5 exact composite witnesses; 2 independent integer evaluators; 6 prime regressions
```

Verifier: `research_notes/portable_direct/d25_crosskernel_composite_cutoff_falsifier_20261029.py`, immutable project commit `37c60f1c5d360f557b3ccb730d9e0a799fb9845f` (readback required separately). No actual H0/B0, Frobenius, or native CM calculation was run.

**BRC/observer applied:** carrier is the signed and source-labeled finite family of pairs `(N,n,A-term,B-term)` with integer coefficient, denominator/unit, cutoff and modulus; the observer is `A_N-B_N mod N^3`, with future operation changing the cutoff between prime N and composite N. Compression to one scalar congruence without source/cutoff typing would erase precisely the failure mode. This is external finite-ring arithmetic, **not** a new X6 native geometric operation, balance axiom or BRC foundation theorem.

## Second exact unit: preserve the comparator's signed high-half port

The published B high-half vanishing result is a **prime-only** input in T1, not a formal property of the original summands for every cutoff. Our new counterexamples have separately computed original four source-labeled half-cut ports, using h=(N−1)/2 and no replacement cutoff:

| N | A_low | A_high | B_low | B_high | B_high mod N² |
|---:|---:|---:|---:|---:|---:|
| 25 | 4525 | 14250 | 10650 | 14375 | 0 |
| 85 | 80750 | 335750 | 310250 | 448375 | 425 |

All entries are residues mod N³ and recombine to the already reported A_N and B_N. At N=25 the comparator B high half is **nonzero modulo N³**, though zero modulo N². At N=85 it is **nonzero even modulo N²** (residue 425). Thus a formal attempt to carry over the Guo–Zudilin B half-cut vanishing to all N would already fail, independently of the original A high-tail correction. The full bridge defect is

\[
D_N=(A_{\le h}-B_{\le h})+(A_{>h}-B_{>h})\pmod{N^3},
\]

and the second signed pair cannot be replaced by only the A high half outside the proved prime setting.

This pinpoints the hypothesis boundary for a prospective uniform prime-sensitive WZ or CM argument: preserve both original high-half ports until prime-specific vanishing is actually proved. **Status:** exact finite four-port certificates for N=25,85; no universal theorem. Checked by the updated verifier at project commit `893389bdcc3afefe1d439387e3286027018590a7`.

## Continuation, current owner separation, and exact next step

No mathematical claim of uniform `A_p=B_p mod p³` was made; no full prime theorem and no new native experiment. The immediate *portable* proof task remains the original **T1** prime-index bridge, for frozen classes p≡13,19 mod24: construct a prime-sensitive finite-field/CM/nonlocal-WZ identity for the half-cut difference plus nonvanishing 216 high-tail; any candidate transformation must fail or explicitly become undefined for N=25 and N=85, as its scope prescribes. Do not repeat earlier 781-prime observations as proof or re-prove the completed 216 reflection.

The **highest hard-target evidence gap** is unchanged: existing `awdawmip/enterprise-math#1559` original p=373 H0/B0 divided-power native `[X]U mod 139129`, actual module rank, Frobenius direction/eta, odd signed Green/Hesse, κ and Delta_p–R_p, with source-versioned execution and independent review; owner pending as of latest Issue read. This scalar falsifier cannot satisfy that acceptance criterion.

Research lane routing label: `chatgpt-research-onhour-enterprise-math-20260923`; maintenance lane `chatgpt-hourly-enterprise-math-20260921` was not used. Previously retrieved own #6575 recovery status carries an historical session pointer but no verified Source claim/run; #6576 dispatch receipt was FAILED/TimeoutExpired. Current Site gateway `research_authority_granted=false`, `write_relay_enabled=false`, and native job quota full 5/5; do not reissue or impersonate role-bound writes. Preserve prior staging as neutral independent provenance. The author-side GitHub research artifact and mirror journal are **not** a formal Research-Activity registration, CLAIM/open/checkpoint/Result/review. Keep `REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING` and existing task OPEN until lawful Source continuation and native completion.

Next exact authorized action: consume any current original-request receipt/Source continuation on a genuinely permitted Researcher path, bind this unreviewed external author evidence without altering task ownership, and advance the prime-sensitive halfcut bridge. In parallel, the actual native authorized executor must complete #1559 as specified.
