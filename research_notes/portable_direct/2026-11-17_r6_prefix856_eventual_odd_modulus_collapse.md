# PREFIX-856 — Eventual elimination of multiplier-prime observation channels under bounded modular readout

Date: 2026-11-17. Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (unchanged).
Direct predecessor: [PREFIX-855](2026-11-17_r6_prefix855_adaptive_feedback_coldstart_game.md). Preserve its precise 1,944-belief-state odd-modulus feedback certificate.

## Exact model and observation scope

We retain the positive-integer **named-source BRC scalar carrier**, not a native X6 Cell/Link/Port event. The full source identity, transition relation, background, joint state and provenance remain available. For a known integer baseline \`S\`, at heartbeat \`t>=1\` the raw observed residue is

\`R_t(m,U)=c_t(S+U) mod m, c_t=a^{floor(t/2)}b^{floor((t-1)/2)}\`,

where \`a,b\` are positive integers. An arbitrary history-dependent controller may choose a *raw* modulus \`1<=m<=2^B\`, know \`t,a,b,S,m\`, and retain unlimited private memory. Each sample's raw modulus uses at most \`B\` register bits. This paper concerns **observer-response equivalence for this declared future language**, not a global deletion of composite/joint BRC directions or native information.

## Theorem 856-A — Exact effective modulus, including feedback

Let \`g=gcd(m,c_t)\` and \`q_t=m/g\`. At a fixed known heartbeat and raw modulus, the map \`U -> R_t(m,U)\` has precisely the same fibers as \`U -> U mod q_t\`:

\`R_t(m,U)=R_t(m,V) iff U ≡ V (mod q_t).\`

The two attainable residues are explicitly invertibly recoded. Write \`m=gq\` and \`c_t=gc'\`. Then \`gcd(c',q)=1\` and the raw residue \`r\` is divisible by \`g\`. For \`q>1\`,

\`U mod q = ((r/g)*(c')^{-1} - S) mod q\`.

For \`q=1\` both observations carry no distinguishing information. Conversely, from \`u=U mod q\` reconstruct \`r=c_t(S+u) mod m\`, because \`m|c_t q\`. The two transformations are exact inverses on their attainable images. QED.

These response maps can be applied **after each feedback-dependent choice**, so a raw-modulus strategy can be simulated at every step using its effective modulus and the same state dynamics.

## Theorem 856-B — Uniform eventual prime-support collapse

Fix \`B>=1\` and let \`C=ab\`. For each prime \`ell|C\` define

\`E_ell(B)=max{e>=0: ell^e<=2^B}\`.

Let \`T_B(a,b)\` be the smallest \`T>=1\` such that \`v_ell(c_T)>=E_ell(B)\` for all primes \`ell|C\`; take \`T_B=1\` when \`C=1\`. This time exists because every such prime divides at least one of \`a,b\`, and \`v_ell(c_t)\` is nondecreasing and unbounded.

For **every** \`t>=T_B(a,b)\` and **every** raw modulus \`1<=m<=2^B\`, the exact effective modulus \`q_t=m/gcd(m,c_t)\` is coprime to \`C\`. Conversely, every \`q<=2^B\` coprime to \`C\` can be used as raw \`m=q\`, because \`gcd(q,c_t)=1\`.

**Proof.** If \`ell|C\` and \`ell^e||m\`, then \`e<=E_ell(B)<=v_ell(c_t)\`. Thus no such prime survives in \`m/gcd(m,c_t)\`. Theorem 856-A is a bijection of raw and normalized observation responses, valid adaptively at every step. Choosing a coprime raw modulus realizes the reverse direction. Hence the *entire family* of bounded-modulus observation partitions and feedback-strategy response trees after \`T_B\` equals the family built from coprime moduli. QED.

This is an exact asymptotic restriction on the **accessible readout direction**, not a claim that the underlying multiplier-prime factors or composite/joint structure disappear from the full BRC source carrier.

## Corollary 856-C — Sharp even-modulus threshold and five-bit late-start optimum

Take PREFIX-855's five named binary sources, \`U(x)=sum_{i=0}^4 2^i x_i\`, \`x_i in {0,1}\`, allowing no change or one named bit flip between samples, and \`a=2,b=1\`. Here \`c_t=2^{floor(t/2)}\`. For raw \`m<=2^B\` all effective moduli are odd, **uniformly over raw modulus choices**, exactly when \`t>=2B\`. Sharpness: for \`m=2^B,t=2B-1\`, \`q_t=2\`, whereas at \`t=2B\`, \`q_t=1\`.

For \`B=4\` and each late cold-start time \`t>=8\`, all allowed raw moduli \`m<=16\` — even, odd, mixed or varying adaptively — normalize to an element of \`{1,3,5,7,9,11,13,15}\`. Modulus 1 adds no information: an odd-modulus controller can simulate a modulus-1 step by choosing modulus 3 and ignoring its observation. PREFIX-855's complete odd-modulus information-game certificate has 1,944 reachable belief states and 13,608 action rows, with winning attractor cardinalities \`[32,48]\`, leaving 1,896 losing states closed under all seven odd actions. The full 32-state cold-start belief is losing. Therefore **no four-bit raw-modulus strategy, even with arbitrary adaptive choices, unlimited time or memory, can guarantee late cold-start synchronization**.

A five-bit ordered schedule of raw moduli \`(17,31)\` always works: both remain invertible against \`c_t\`, and the exact two-step test over all valid transitions has no distinct-terminal-state collision. After synchronization, raw modulus 11 tracks every single-source/no-op update using four bits. A single five-bit late-start sample cannot distinguish 32 initial states: every effective modulus is an odd integer at most 31. Consequently the exact maximum raw-modulus width for guaranteed late cold start is **five bits**, achieved in **two samples**, followed by four-bit warm tracking. QED.

## Exact arithmetic reproduction

Run \`python3 research_notes/portable_direct/PREFIX856_R6_ASYMPTOTIC_MODULUS_ERASURE_CHECK.py\` using Python 3 standard library only. The script writes \`PREFIX856_R6_ASYMPTOTIC_MODULUS_ERASURE_RESULTS.json\`. In the author-side 2026-11-17 run:

- 262,144 raw/normalized exact residue forward-and-inverse checks over \`(a,b)=(2,1),(2,3),(6,5),(1,1)\`, \`t=1..16\`, \`m=1..64\`, \`S=0,7\`, \`U=0..31\`;
- 630 saturation checks over \`B=1..6\`, \`t=2B..2B+4\`, all \`m<=2^B\`, plus each sharp threshold witness at \`2B-1\`;
- independent Python regeneration of the 1,944-state odd-only feedback game, all 13,608 action rows, \`[32,48]\` winning layers and the 1,896 losing-state closure witnesses;
- the ordered pair \`(17,31)\` has zero off-diagonal terminal collisions, while \`(31,17)\` has 32; the warm modulus 11 covers all 32 old states.

All assertions returned \`ALL_EXACT_ASSERTIONS_PASSED\`. General Theorems 856-A/B and the time threshold have symbolic proofs above; finite enumeration supplies an exact author-side regression and a finite certificate for the five-source corollary.

## Provenance, limitations and next scientific problem

This new theorem generalizes PREFIX-855's **odd-only** four-bit impossibility to **all raw modular readouts** at sufficiently late heartbeats, while preserving frozen source inputs. The general saturation theorem applies for all positive \`a,b\` and finite port width independently of the state-transition law, provided the stated scalar observer is used. The five-source cold-start lower bound depends on the precise no-op/one-named-flip transition relation and the existing exhaustive feedback certificate. No native X6 physics, triadic event admissibility, source-to-port mapping or independent theorem acceptance is claimed.

Next: compute the \`1<=t<8\` early-even-modulus feedback game exactly to determine whether a four-bit transient cold start is possible; quantify multi-prime multiplier saturation; test an independently source-authorized native X6 Cell/Link/Port observer bridge. Preserve full joint/provenance information outside the declared scalar observation.
