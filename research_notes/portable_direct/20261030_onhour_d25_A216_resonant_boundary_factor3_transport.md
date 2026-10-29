# D25 / SECOND-DIGIT-LIFT — factor-three residue transport at the A216 resonant endpoint

Date: 2026-10-30 Asia/Hong_Kong. Evidence status: AUTHOR-SIDE / PROVED p-ADIC LEMMA / EXACT FINITE REGRESSION EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
Research lane: chatgpt-research-onhour-enterprise-math-20260923, NOT maintenance. Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Original scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.

## Domain, exact objects and new theorem

Let p=6m+1 >=7 be PRIME and N=3m=(p-1)/2. The ORIGINAL model is

\[
a_n=\frac{(2n)!(3n)!}{(n!)^5 216^n},\qquad w_n=(6n+1)a_n.
\]

Reuse the prior derived A216 valuation-two reflected kernel and universal 4F3 term:

\[
C_m=3\cdot216^{2m}\frac{((2m)!)^5}{(4m+1)!},\quad
h_s=(2s+1)2^s\frac{(2/3)_s^3}{(7/6)_s(4/3)_s s!},
\]

\[
g_s=(12m+6s+5)216^{2m+s}
\frac{((2m+s)!)^5}{(4m+2s+1)!(3s+1)!}.
\]

For 0<=s<=m-1, the prior reflection lemma establishes g_s=C_m h_s mod p with p-unit denominators. At s=m the *rational* h_m and g_m have valuation -1, so only p h_m and p g_m have valid reductions mod p. Write chi_p=(6/p) for the Legendre symbol.

**THEOREM (algebraically proved for every stated prime):**

\[
\boxed{C_m\,p h_m\equiv3p g_m
\equiv-3\frac{w_N}{p}\equiv-12\chi_p\pmod p.}
\tag{RB1}
\]

Hence the following genuinely cross-source rational regularization is p-integral:

\[
\boxed{E_p=C_mh_m+3w_N/p^2\in\mathbb Z_{(p)}.}\tag{RB2}
\]

The object g_m is a formal continuation of the *middle-port reflected expression*, whereas w_N is the actual original valuation-one low-end coefficient. The congruence compares *scaled pole residues* and does not identify these as one physical or native H0/B0 operator.

For the frozen target classes p=13 mod24 and p=19 mod24, chi_p is respectively -1 and +1, so C_m p h_m is 12 and -12 mod p while w_N/p is -4 and 4 mod p.

## Proof: cancel the actual p before reducing

1. By the previous middle-port proof, g_(m-1)≡C_m h_(m-1) mod p; its denominators are p-units.

2. Use the exact ratio, without substituting residues in a denominator that may later vanish:

\[
\frac{g_{s+1}}{g_s}=
\frac{12m+6s+11}{12m+6s+5}
\frac{216(2m+s+1)^5}
{(4m+2s+2)(4m+2s+3)(3s+2)(3s+3)(3s+4)}.
\]

At s=m-1 the exact factor (4m+2s+3)=p. Multiplying by p first and only then reducing the other p-units with 6m=p-1 gives

\[
p\,g_m/g_{m-1}\equiv-9\pmod p.\tag{RB3}
\]

3. The universal ratio is

\[
\frac{h_{s+1}}{h_s}=
\frac{4(2s+3)(3s+2)^3}
{3(2s+1)(6s+7)(3s+4)(s+1)}.
\]

At s=m-1 the exact factor (6s+7)=p. Multiplication by p followed by reduction gives

\[
p\,h_m/h_{m-1}\equiv-27\pmod p.\tag{RB4}
\]

The ratio of the two scaled steps is THREE, not one. The interior substitution 4m+2s+3 ≡ 2(s+7/6) mod p replaces the *exact* pole p by p/3 at the boundary; it cannot be used as a division-preserving relation there. Using step 1 and (RB3)-(RB4), C_m p h_m≡3p g_m.

4. The p from (6m+1)!=p! can be cancelled explicitly:

\[
p g_m=(18m+5)216^{3m}\frac{((3m)!)^5}{(6m)!(3m+1)!}.
\]

Here 18m+5=3p+2, (6m)!=(p-1)!≡-1, (3m+1)≡1/2. Wilson reflection gives ((3m)!)^4≡1 mod p, and Euler's criterion gives 216^{3m}≡(216/p)=(6/p)=chi_p. Hence p g_m≡-4 chi_p mod p.

5. Independently evaluate the original coefficient at n=N=3m. Since 3N=p+N-1<2p, the original (3N)! has exactly one p factor with (3N)!/p≡-(N-1)! mod p, while (2N)!=(p-1)!≡-1. Therefore

\[
a_N/p\equiv[N(N!)^4\,216^N]^{-1}
\equiv-2\chi_p\pmod p.
\]

The original signed weight 6N+1=3p-2 is -2 mod p, so w_N/p≡4 chi_p mod p. Together with steps 1-4 this proves (RB1) and the p-integrality (RB2). Another equivalent local interface is g_(m-1)≡4chi_p/9 and w_N/p≡9g_(m-1), both mod p.

## What the boundary theorem does and does not settle

The exact p-integral finite part E_p mod p requires *one further p-adic digit*. It is computed by obtaining p E_p modulo p², checking its divisibility by p, and then dividing, NOT by reducing a 1/p expression directly in F_p. Let J_p=(A_low-p)/p² mod p, Q_p=C_m*sum_(s=0)^(m-1) h_s mod p, where A_low=sum_(n=0)^N w_n is the ORIGINAL A216 lower port. The prior D24 first digit ensures integrality of J_p for frozen target primes. The still-open original LIFT proof obligation is J_p+Q_p=0 for ALL p=13 or 19 mod24. The new theorem supplies a necessary WZ *boundary compatibility* law, not this bulk cancellation.

Independent exact computations (all values reduced to [0,p)):

| p | w_N/p | C_m p h_m | E_p | J_p | Q_p |
|---:|---:|---:|---:|---:|---:|
| 13 | 9 | 12 | 4 | 3 | 10 |
| 19 | 4 | 7 | 2 | 10 | 9 |
| 373 | 369 | 12 | 141 | 107 | 266 |

In each row C_m p h_m+3 w_N/p=0 mod p. The proposal E_p=Q_p fails even at p=13,19,373: a paired WZ certificate must also carry original low-port *interior* contributions and first jets. The p373 scalar target J+Q=107+266=373 is a prior finite observation, not proof of all-prime LIFT.

## Executed evidence, BRC scope, next action

Companion executable: research_notes/portable_direct/d25_resonant_boundary_transport_20261030.py (Python standard library). Actually executed this turn for **115 primes** p<1500, p=1 mod6, including **60** frozen-class primes: all RB1 component congruences passed. Independent original raw factorial/binomial coefficient checks at p=7,13,19,31,37,373. The program also computes p² first jets of E_p and original signed A_low modulo p³ at p=13,19,373, preserving exact division. This supports the *execution evidence*; the five-step argument is the proof.

BRC COMPOSE_APPLIED: preserve original index n=N and valuation-one w_N, the separate formal reflected g_s and original valuation-two middle source, transported index s, pole multiplicity and signed residue before quotient. Observer is the p-local rational scalar after specified p-multiplication, then reduction to F_p. The associated finite-field scalar formula is NOT a native X6/spatial/H0/B0 transfer.

As read on 2026-10-30 this Site connection reported research_authority_granted=false and write_relay_enabled=false; own checkpoint list returned ACCESS_DENIED. No native recovery_status/Source session/claim/run/checkpoint/Result/review is asserted. The existing native support issue #1559 was OPEN and without assignee: original same-class p=373 H0/B0 divided-power [X]U mod139129, native module rank, semilinear Frobenius/eta, signed Green/Hesse, kappa and independent reproduction remain to be run by an authorized evaluator. Portable mathematics does not replace these requirements.

**Next smallest mathematical action:** construct and check a *paired* finite WZ/contiguous relation whose boundary contributes -27 times the hypergeometric last interior term and +9 times the adjacent original low endpoint (forcing the coefficient three); show the interior bulk exactly supplies J_p+Q_p for all frozen target primes, or give a genuine counterexample. Track first jets of the regularized E_p and do not set E_p=Q_p. The native experiment follows #1559 under its own legitimate executor.

Scientific Source pin, owner, P000/worldview, Research-vs-maintenance lane boundary, scheduler and notifications are unchanged. This file is durable author-side evidence, not Source admission.