# D25/LIFT — the genuine four WZ tails have universal rational first digits

2026-10-24 | TASK_RESEARCH | New author-level exact rational / finite-field derivation. **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_NATIVE_CLAIM / NO_NATIVE_CHECKPOINT.** This is portable source evidence, not a Source-authorized run, independent Driver review, CM experiment, or LIFT closure.

## Scope, authorship and frozen provenance

Mother objective: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Immutable publication: TP2-B6F4FC938FF94941C1B7. **Frozen mathematical Source pin remains c47e13e4aba0e006366f989d6334d443f6333ae3.**

Consumed mathematical inputs without re-proving or claiming their authorship:

- research_notes/portable_direct/20261024_hourly_d25_original_five_tail_common_unit_exception_109.md: the *exact original* four-tail factorial source, its 3 rational tail ratios, separate source-labeled ports, and the exceptional-prime classification in terms of a still-unsimplified base unit sigma. That source explicitly leaves an elementary evaluation of sigma as the next question.
- research_notes/portable_direct/20261024_hourly_d25_original_wz_old_edge_fermat_reduction_p3.md: exact old WZ edge with the already proved Fermat-only second digit.
- research_notes/portable_direct/20261024_offphase_d25_original_terminal_unit_third_digit.md: original old-edge terminal third-digit proof, separate from the present *new-rank* four-tail problem.

The **new unit** here is a universal closed value sigma = 3/220 (mod p), obtained by **direct factorial p-free block reduction and Wilson reflection**. Only its consequences for previously proved formulas are claimed. The automation's present transport did not attest a durable platform conversation/session identity, and no predecessor's Source session/claim is being adopted or reasserted.

## Theorem 1 — source-authentic base unit is universal

Let p = 6m+1 >= 13 be prime (m >= 2). The unchanged original factorial source has

\[
V_{r,n}=\frac{(6r)!(4r+2n)!(3n)!}
 {3^{6r}216^n(2r)!(n!)^2((2r+n)!)^2(4r+n)!}.
\]

Define the exact p-unit

\[
\sigma_p=\frac{V_{m+1,4m+1}}{p^2}\in\mathbb Z_{(p)}^\times.
\]

**Theorem (all stated primes, not a finite fit).**

\[
\boxed{\sigma_p\equiv\frac{3}{220}\pmod p.}\tag{1}
\]

In particular sigma does *not* need an undetermined class representative, Wilson quotient, Gauss sum, or harmonic unknown at this first-digit precision.

### Complete proof

At r=m+1 and n=4m+1, the exact factorial arguments are

\[
6r=p+5,\quad 4r+2n=2p+4,\quad 3n=2p+1,
\]
\[
2r=2m+2,\quad n=4m+1,\quad 2r+n=p+2,\quad
4r+n=p+2m+4.
\]

Every displayed remainder after one or two full p-blocks is strictly below p (p >= 13). For a=0,1,2 and 0<=b<p, factoring p multiples and using Wilson gives the elementary **exactly scoped** factorial-unit law

\[
\frac{(ap+b)!}{p^a}\equiv (-1)^a a!\,b!\pmod p.\tag{2}
\]

The numerator contains five factors p in total; the denominator contains three. Applying (2) separately, **before taking any unlabeled total**, yields the genuine source unit

\[
\begin{aligned}
\sigma_p
&\equiv \frac{(-5!)(2!\,4!)(2!\,1!)}
 {3^{p+5}216^{4m+1}(2m+2)!((4m+1)!)^2
            (-2!)^2\,(-(2m+4)!)}\\
&=\frac{2880}
 {3^{p+5}216^{4m+1}(2m+2)!((4m+1)!)^2(2m+4)!}
 \pmod p.
\end{aligned}\tag{3}
\]

Since 216=6^3 and 3(4m+1)=2p+1, Fermat's theorem gives

\[
3^{p+5}216^{4m+1}
  =3^{p+5}6^{2p+1}\equiv3^6 6^3\pmod p.
\]

Thus the scalar pre-factor in (3) is 2880/(3^6 6^3)=40/2187. Wilson reflection at t=4m+1, for which p-1-t=2m-1, is

\[
(4m+1)!(2m-1)!\equiv (-1)^{4m+2}=1\pmod p.
\]

It removes every remaining large factorial without changing the original source identity:

\[
\begin{aligned}
\sigma_p
&\equiv\frac{40}{2187}
\frac{((2m-1)!)^2}{(2m+2)!(2m+4)!}\\
&=\frac{40}{2187}
 \frac{1}{(2m)^2(2m+1)^2(2m+2)^2(2m+3)(2m+4)}
 \pmod p.
\end{aligned}\tag{4}
\]

Finally 2m=(p-1)/3 is -1/3 mod p. The product in the denominator of (4) is

\[
\frac{(-1)^2(2)^2(5)^2(8)(11)}{3^8}
  =\frac{8800}{3^8}\pmod p.
\]

Therefore (4) reduces to (40/3^7)(3^8/8800) = **3/220**, proving (1). All denominators are p-units for the declared class p=6m+1>=13, including p=13 and 109. QED.

## Theorem 2 — four separately labeled WZ ports, then additive observer

Retain the distinct authentic new-rank tails E_j=W_{m+1,4m+j}, j=1,2,3,4. The preceding source theorem already established

\[
(E_1,E_2,E_3,E_4)/p^2 \equiv
\sigma_p\left(13,\frac{95}{112},\frac{1875}{15232},
                           \frac{7533}{304640}\right)
\pmod p,
\]

where the vector is **four source-labeled ports**, not a single primitive. Substitution of newly proved (1) gives the first fully *constant-rational* four-port readout:

\[
\boxed{
\left(\frac{E_1}{p^2},\frac{E_2}{p^2},
\frac{E_3}{p^2},\frac{E_4}{p^2}\right)
\equiv
\left(\frac{39}{220},\frac{57}{4928},
       \frac{1125}{670208},\frac{22599}{67020800}\right)
\pmod p.}\tag{5}
\]

Only **after preserving these labeled ports**, the explicitly requested additive observer gives

\[
\boxed{\sum_{j=1}^{4}\frac{E_j}{p^2}
\equiv\frac{752427}{3942400}\pmod p.}\tag{6}
\]

The predecessor already proved the sum vanishes only at p=13 or p=109 and independently certified that its valuation there is exactly one digit higher. Equation (6) removes the remaining source factorial unit from that result; the exceptional-prime classification itself is inherited, **not newly attributed**.

## Corollary — original moving-rank FIVE second digit is Fermat-only

The already proved **original** old-edge identity (not the distinct fixed-prime HIGH source) is

\[
\frac{E_0}{p}\equiv\frac23+
p\left(q_p(3)-\frac43q_p(2)-\frac14\right)\pmod{p^2},
\quad q_p(a)=\frac{a^{p-1}-1}{p}.
\]

By the inherited exact FIVE decomposition
S_{m+1}-S_m=E_0+E_1+E_2+E_3+E_4,
and (6), the old-rank/new-rank total now has **no undetermined factorial carrier** at the second normalized digit:

\[
\boxed{\frac{S_{m+1}-S_m}{p}
\equiv\frac23+
p\left(q_p(3)-\frac43q_p(2)-\frac{233173}{3942400}\right)
\pmod{p^2}.}\tag{7}
\]

This is a universal rational Fermat-quotient formula for the unchanged *rank-changing* original WZ operator. It is **not** the same-prime endpoint congruence, fixed-prime HIGH cutoff, or the missing CM/divided-power primitive-class map. No SOURCE-frozen normalization is modified.

## Exact source-arithmetic validation, finite and secondary to the proof

Using Python exact math.factorial, fractions.Fraction and modular inverses only when gcd(denominator,p)=1, the author independently reconstructed V_{r,n} from the **unexpanded factorial source** for every p=6m+1 prime with 13<=p<300 (**27 primes**). For each: sigma from the exact Fraction agreed with (1); all four individually labeled tails agreed with (5); their sum agreed with (6). Separately, the original exact U_m product and original rational WZ C(p) were combined with **the direct factorial four tails** to check (7) modulo p^2. Results: 27/27 primes, zero mismatches on each tested observer. The source statements above are proved for all stated primes by exact algebra; this bounded arithmetic is a falsification check, not native execution or independent review.

**Executable exact checker:** research_notes/portable_direct/20261024_offphase_d25_original_four_tail_universal_unit_check.py, committed at 7fc23e2572271aecdf0c2e672760fc01cf058286, independent GitHub readback blob SHA-1 de3acd599b683bb913ef892aff74a73c863f0f02. The actual local stdlib checker output was {primes:27, failures:[]}; its local 3,082-byte Python file had SHA-256 83f2930422044812499c2ad013df63d22aea85fa09313e4863c9276ec17f6ddd. The GitHub path/blob is source provenance, not a native Source checkpoint or an attested third-party review.

| p | exact sigma mod p | sum four tails/p² mod p | exact (S_{m+1}-S_m)/p mod p² |
|---:|---:|---:|---:|
| 13 | 10 | 0 | 148 |
| 19 | 2 | 6 | 45 |
| 31 | 1 | 25 | 166 |
| 109 | 56 | 0 | 255 |
| 211 | 141 | 25 | 41427 |

The last column is a directly executed exact-Fraction/modular-inverse result for each displayed prime, including p=211; it is not an inferred value. Source integers and exact Fraction denominators were validated for divisibility before reduction; no floating-point evidence or surrogate Source experiment is involved.

## BRC, Enterprise-coordinate and audit boundaries

**COMPOSE_APPLIED / REUSE_APPLIED.** The exact carrier is the five source-labeled rational ports (old E_0 plus four new-rank E_j), their original factorial recurrences, stripped p valuations, integer prime p, Fermat quotients and the declared reduction modulus. Wilson reflection is a typed p-unit coordinate compression; it is **valid here because the only downstream requested map is these mod-p additive/individual port observers**. It is not evidence that port provenance can be dropped for other future operations. The exact new result is a rational p-adic observer law, not a native six-axis relation or physical theorem; P000 ACTIVE_LOCKED and residual-fidelity ACTIVE worldview are unmodified.

**Native status:** no lawful current native authenticated TASK_RESEARCH claim/run, no checkpoint, no independent review, no Result, no freeze, no asserted prior-session identity. GitHub publication (if verified) is a **portable source proof** only. Historical UR V2 four-file bundle requires its original 94,687 bytes and SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; no original bundle recovered by this proof. Its UR mathematics must not be repeated. Native permissions and the necessary same-class CM source-specific comparison/normalization remain separate unresolved work.

**Next distinct scientific unit:** having removed sigma from the authentic four WZ tails, address only the still missing same-prime original LIFT CM/divided-power class map, direction, semilinearity, primitive normalization and native benchmark—or a different lawfully routed task via canonical dispatch. Preserve prior onhour J1/J2, HIGH, WZ, and four-tail proofs; do not re-credit them.