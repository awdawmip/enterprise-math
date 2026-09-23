# BRC exact port-event automaton for endpoint, denominator and cancellation thresholds

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`

Research-Activity-ID: `RA-7173A2B0D2B62B10023DBFFB`

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`

Formal D24/UR ownership and theorem status are unchanged. This note advances only the auxiliary BRC carrier theory while the lawful successor-session path remains blocked by control issue #1511. It does not start LIFT/JT2 and grants no CLAIM, OPEN, Result, review, Working Truth, or mathematical acceptance.

## 1. Consumed exact port carrier

For target primes `p ≡ 13,19 (mod 24)`, keep

`X_j=-((1+4^j)/j) p^(2j) H_{2j}`,

and the exact lower valuation carrier

`beta_p(j)=2j+epsilon_p(j)+eta_p(j)`,

where

`epsilon_p(j)=0 iff (p-1)|2j, else 1`,

`eta_p(j)=v_p((1+4^j)/j)`.

The conservative generic port has weight

`g(j)=2j+1`.

Previous units proved separately:

- harmonic endpoint lowering;
- denominator lowering from `v_p(j)`;
- for class 13, a periodic source-coefficient cancellation progression whose numerator valuation cancels denominator valuation exactly;
- for class 19, no source-coefficient cancellation;
- endpoint and source-cancellation progressions are disjoint.

The present unit composes these facts into one exact event classifier for every single port.

## 2. Event coordinates

Write

`h_p=(p-1)/2`,

`E_p(j)=1` iff `h_p | j`, else `0`,

`a_p(j)=v_p(j)`.

Thus `E_p(j)` records a harmonic endpoint event and `a_p(j)` records the denominator-depth event.

For `p ≡ 13 (mod24)`, write

`ord_p(4)=2s_p`

and

`c_p=v_p(1+4^(s_p))`.

Define the cancellation flag

`C_p(j)=1` iff `j=s_p m` with `m` odd, else `0`.

The established order/LTE theorem gives

`v_p(1+4^j)=c_p+a_p(j)`

on `C_p(j)=1`, and zero off that progression except for no other cases relevant here. Moreover

`E_p(j) C_p(j)=0`.

For `p ≡ 19 (mod24)`, set `C_p(j)=0` identically.

## 3. Exact port-event automaton

### Theorem 3.1 — class 19

For every target prime `p ≡19 (mod24)` and every `j>=1`,

`beta_p(j)=2j+1-E_p(j)-a_p(j)`.

Equivalently, relative to generic weight `g(j)=2j+1`, the branch shift is

`delta_p(j)=-E_p(j)-a_p(j)`.

Hence endpoint lowering and denominator lowering add exactly when they intersect.

### Theorem 3.2 — class 13

For every target prime `p ≡13 (mod24)` and every `j>=1`,

`beta_p(j)=2j+1-E_p(j)-a_p(j)+C_p(j)(a_p(j)+c_p)`.

Because `E_p C_p=0`, this is equivalently the exact piecewise rule

- if `C_p(j)=1`, then `beta_p(j)=2j+1+c_p`;
- if `C_p(j)=0`, then `beta_p(j)=2j+1-E_p(j)-a_p(j)`.

Thus a denominator power at a class-13 cancellation port does **not** lower the port. LTE raises the numerator valuation by the same `a_p(j)` and cancels the denominator contribution exactly; the surviving branch shift is the positive constant `+c_p`.

### Proof

Start from

`beta_p(j)=2j+epsilon_p(j)+v_p(1+4^j)-v_p(j)`.

Since `epsilon_p(j)=1-E_p(j)`, the class-19 result follows from the established fact `v_p(1+4^j)=0` on that residue class.

For class 13, off the cancellation progression the numerator valuation is zero, giving the same formula. On the cancellation progression LTE gives

`v_p(1+4^j)=c_p+a_p(j)`.

The `a_p(j)` term cancels `-v_p(j)` exactly. Cancellation ports are never harmonic endpoints, so `epsilon_p(j)=1`; therefore

`beta_p(j)=2j+1+c_p`.

Combining the two states gives the displayed unified formula.

## 4. Observer-entry windows

For a singleton port `e_j`, define its generic first-visible integer horizon

`N_infty(j)=g(j)+1=2j+2`,

and its exact branch first-visible horizon

`N_p(j)=beta_p(j)+1`.

Put

`delta_p(j)=beta_p(j)-g(j)`.

Then the observer windows are exact:

- if `delta_p(j)=-d<0`, the branch sees `e_j` exactly `d` integer horizons before generic, namely
  `N=N_infty(j)-d,...,N_infty(j)-1`;
- if `delta_p(j)=c>0`, generic sees `e_j` while the branch prunes it for exactly `c` horizons,
  `N=N_infty(j),...,N_infty(j)+c-1`;
- if `delta_p(j)=0`, the singleton enters simultaneously.

This is not a heuristic about asymptotic valuation. It is a direct consequence of the strict observer rule `beta<N`.

## 5. Exact special events

The automaton recovers and extends the earlier threshold theorems without new enumeration.

### Primitive endpoint

At

`j=h_p=(p-1)/2`,

`E=1`, `a=0`, `C=0`, so

`beta_p(h_p)=p-1`.

Its branch entry is `N=p`, one horizon before generic. This is the first-entry endpoint singleton.

### First denominator port

At `j=p`, one has `a=1`, `E=0`, and the port is not a class-13 cancellation port. Therefore

`beta_p(p)=2p`,

so it enters at `N=2p+1`, one horizon before generic. This is precisely the denominator-dominance handoff proved in the previous threshold note.

### First endpoint-denominator intersection

At

`j=p h_p=p(p-1)/2`,

one has `E=1`, `a=1`, `C=0`. Hence

`beta_p(p h_p)=2p h_p-1`.

The branch entry is therefore

`N=2p h_p`,

whereas generic entry is `2p h_p+2`. The intersection creates a two-horizon early window. Endpoint and denominator defects add rather than overwrite one another.

### Class-13 p-multiple cancellation

Let `p≡13 (mod24)` and take

`j=s_p p`.

Then `j` lies on the cancellation progression and `a=1`. Nevertheless

`beta_p(s_p p)=2s_p p+1+c_p`.

Thus the target-prime denominator does **not** create an early branch event here. Instead the branch is delayed by `c_p` horizons relative to generic. This is the sharpest illustration that `p|j` alone is not a sufficient event label: denominator provenance must be composed with source-coefficient provenance before quotienting.

For example, at `p=13`, `s_p=3`, `c_p=1`, the port `j=39` has

`beta_13(39)=80`,

while generic weight is `79`. It is pruned for one observer horizon rather than advanced by the denominator.

## 6. Threshold-limited event scheduler

For any fixed observer horizon `N`, only finitely many `j` can satisfy `beta_p(j)<N`. Therefore the exact-per-prime compiler can generate candidate port events by the following typed divisibility data instead of recomputing large powers `4^j+1` at every port:

- endpoint progression `h_p | j`;
- denominator depth `v_p(j)`;
- on class 13 only, cancellation progression `j/s_p` odd and integral, with fixed height `c_p`.

The state retained for a port is therefore

`(j, E_p(j), v_p(j), C_p(j), c_p-if-C, source class)`.

For the `EXACT_PER_PRIME_SUPPORT` observer this tuple is lossless for the port valuation. For the `UNIFORM_SUFFICIENT_MOD_p^N` observer it may be further quotiented only after applying the already-proved large-prime and branch-redundancy results.

This distinction is essential: a singleton event becoming early for one branch does not by itself prove that it is novel in the **uniform union**, because an earlier branch may already cover the same exponent vector.

## 7. Finite falsification / regression

Checker:

`research_checks/check_brc_port_event_automaton_20260924.py`.

The checker independently evaluates the raw formula

`2j+epsilon_p(j)+v_p(1+4^j)-v_p(j)`

against the automaton for every target prime

`p<5000`, `p mod24 in {13,19}`,

and every

`1<=j<=500`.

It also checks the singleton event-window algebra and the special endpoint, denominator, endpoint-denominator-intersection and class-13 p-multiple-cancellation cases.

Exact output:

`{'status': 'PASS', 'target_primes': 166, 'classes': {13: 83, 19: 83}, 'j_range': [1, 500], 'raw_vs_automaton_failures': 0, 'event_window_failures': 0, 'first_intersections': [(13, 78, 156), (19, 171, 342), (37, 666, 1332), (43, 903, 1806)], 'class13_p_multiple_cancellation_examples': [(13, 3, 1, 39, 80), (37, 9, 1, 333, 668), (61, 15, 1, 915, 1832), (109, 9, 1, 981, 1964)]}`.

In the `first_intersections` tuples the third coordinate is the branch first-visible horizon `beta+1`; in the cancellation tuples the last coordinate is `beta` itself.

Finite regression is not the proof. The proof is the exact order/LTE composition above.

## 8. BRC interpretation

This unit separates four local mechanisms without losing their source identity:

- endpoint lowering: `-E`;
- denominator lowering: `-v_p(j)`;
- their additive intersection: `-E-v_p(j)`;
- class-13 coefficient cancellation: replaces denominator lowering on that progression and leaves a positive delay `+c_p`.

Thus the compiler should not store a single Boolean `exceptional_port`. The minimally sufficient exact-per-prime state is the typed event tuple above. Only after the observer is fixed may the state be collapsed.

## 9. Do not repeat / next

Do not rediscover endpoint and denominator thresholds by horizon-by-horizon enumeration. Use this event automaton as the port-level front end, and the valuation-partition compiler as the monomial-level back end.

If formal D24 control remains blocked, the next information-gain auxiliary unit is to lift this port automaton to an exact **uniform-union event automaton**: determine when endpoint multiples, denominator multiples and their decorations are genuinely union-novel versus already covered by earlier target-prime branches. If #1511 gains a deployed lossless rollover/disposition operation, stop auxiliary work and resume the Source-native D24 frontier through lawful successor identity -> native-frontier `continuation_prepare` -> CLAIM -> OPEN -> truthful checkpoint/readback -> UR/JT0 Result/freeze -> independent Driver review.
