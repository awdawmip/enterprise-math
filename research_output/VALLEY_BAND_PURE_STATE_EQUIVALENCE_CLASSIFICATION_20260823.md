# Valley Band Pure-State Equivalence Classification

## Decision

- Researcher-ID: `EM-VBSEQ-7021BF`
- Task-ID: `RS-VALLEY-BAND-PURE-STATE-EQUIVALENCE-CLASSIFICATION`
- Date: 2026-08-23
- Hard target: `VALLEY_STATE_RECURRENCE_CFRAC_EQUIVALENCE_AND_BAND_ROOT_SEMANTICS_CLASSIFIED`
- Final classification: **`EQUIVALENT_ONLY_AFTER_HYPOTHESIS_OR_SIGN_REPAIR`**
- Proof status: closed. The classification follows from symbolic maps and counterexamples; finite checking is corroboration, not a substitute for proof.

The packet recurrence is exactly a signed presentation of the ordinary complete-quotient recurrence for `sqrt(T)` and of the neighboring-form step for the indefinite form `[A,2C,B]`, once the canonical initialization and the forward orientation are imposed. The packet's stated weak domain

`C^2-AB=T`, `AB<0`, `|C|<sqrt(T)`, `A!=0`

does not impose that orientation and is not forward invariant under the packet's absolute-value digit. The smallest odd nonsquare counterexample is `T=3`, `(A,B,C)=(-2,1,-1)`. Consequently an unconditional exact-equivalence classification is false.

The polynomial band is not a different orbit. Within `0 <= t <= a_n`, it is the standard intermediate/semiconvergent column of the same unimodular continued-fraction transform. Outside that interval it is an algebraically valid extrapolation, but not a standard intermediate convergent. The closed state alone supports the local relation

`(At+C)^2 == A D(t) (mod N)`,

not generally `(At+C)^2 == D(t) (mod N)`. To obtain the usual CFRAC relation `X_t^2 == D(t) (mod N)`, one must retain or replay the accumulated transform. This distinction repairs the relation semantics without changing the orbit classification.

## Frozen scope and source firewall

The only task inputs used were:

- project TASK_RESEARCH router from canonical Global Knowledge `main@506eb72c7d409dafda4763403a0bba7c5cc28287`;
- remote `AGENTS.md` at project ref `12725505c636449df7dd913ac06e581bf418b89c`;
- `research_tasks/VALLEY_BAND_PURE_STATE_EQUIVALENCE_CLASSIFICATION_20260823.md` at the same ref, blob `4af7c823...`;
- `research_inputs/VALLEY_BAND_PURE_STATE_AND_BENCHMARK_PACKET_20260823.md` at locked ref `f341b1347939e004e6d55c96e119c53337c0c9a0`, blob `ba3b033d8dab89e26347a8feaa699d6a3c153396`;
- primary or authoritative public prior art listed in the separate prior-art map.

No source prototype, source conversation, withheld checkpoint, Valley source script, or other research branch was read. The execution node was reused only after an unrelated Lane 3 task had completed; that prior lane contained no Valley source, prototype, or context, and none of its mathematics, code, or outputs was read, referenced, or copied.

## 1. Definitions

Let `N` be odd, `M>0`, `T=MN`, and assume `T` is not a square. Put `s=floor(sqrt(T))`.

The candidate state and digit are

```
V_n = (A_n,B_n,C_n),        C_n^2-A_n B_n=T,
a_n^V = floor((s+|C_n|)/|A_n|),
V_{n+1} = (A_n a_n^2+2C_n a_n+B_n, A_n, A_n a_n+C_n).
```

The independent standard complete-quotient recurrence is

```
m_0=0, d_0=1, a_0=s,
m_{n+1}=d_n a_n-m_n,
d_{n+1}=(T-m_{n+1}^2)/d_n,
a_{n+1}=floor((s+m_{n+1})/d_{n+1}).
```

Its quadratic irrational is `xi_n=(sqrt(T)+m_n)/d_n`.

## 2. Initialization, invariant, and indexed state map

### Theorem 1: canonical initialization and exact forward map

Set

`V_0=(1,-T,0)`.

Then the candidate digit at `n=0` is `s=a_0`. For every `n>=1`, with `sigma_n=(-1)^n`,

```
A_n =  sigma_n d_n,
B_n = -sigma_n d_{n-1},
C_n = -sigma_n m_n.                         (1)
```

In particular,

```
|A_n|=d_n, |B_n|=d_{n-1}, |C_n|=m_n,
a_n^V=(s+m_n)//d_n=a_n.
```

#### Proof

At initialization, `a_0=s`, so

```
V_1=(s^2-T,1,s)=(-d_1,d_0,m_1),
```

which is (1) for `sigma_1=-1`.

Assume (1) at `n` and write `sigma=sigma_n`, `d=d_n`, `e=d_{n-1}`, `m=m_n`, and `a=a_n`. The standard invariant is

`T=m^2+de`.

The candidate update gives

```
B' = sigma d = -sigma_{n+1} d_n,
C' = sigma(da-m) = -sigma_{n+1}m_{n+1}.
```

Furthermore,

```
d_{n+1}
 = (T-(da-m)^2)/d
 = e-da^2+2am,
```

so

```
A' = sigma(da^2-2am-e) = -sigma d_{n+1}
   = sigma_{n+1}d_{n+1}.
```

This proves the state and digit identities by induction. No numerical sampling is used in the proof. ∎

### Theorem 2: symbolic preservation of the packet invariant

For every integer `a`, not only for the selected digit,

```
(Aa+C)^2 - A(Aa^2+2Ca+B) = C^2-AB.
```

Since `B'=A`, the update preserves `C^2-AB=T`. For nonsquare `T`, `A'=0` would force `(C')^2=T`; hence no canonical nonsquare orbit has a zero leading coefficient. The same argument one step earlier keeps `B` nonzero. Zero is therefore not a hidden normal terminator.

## 3. The necessary hypothesis/sign repair

For `n>=1`, the exact forward-oriented reduced domain is

```
C^2-AB=T,
AB<0,
|C|<sqrt(T),
AC<0,
sqrt(T)-|C| < |A| < sqrt(T)+|C|.             (2)
```

The last two inequalities are exactly the standard reduced-complete-quotient conditions

```
xi=(sqrt(T)+m)/d > 1,
-1 < xi_conjugate=(m-sqrt(T))/d < 0,
```

under `m=|C|`, `d=|A|`. The direction condition `AC<0` makes `C=-sigma m` when `A=sigma d`; without it the absolute-value digit can select the neighbor in the wrong direction.

These conditions are forward invariant, not merely descriptive. For a reduced `xi`, nonsquareness makes `0<xi-floor(xi)<1`, and the recurrence gives

`xi_next=1/(xi-floor(xi))>1`.

Its conjugate is `1/(xi_conjugate-floor(xi))`, whose denominator is less than `-1`; hence the next conjugate again lies strictly between `-1` and zero. Also

`floor((sqrt(T)+m)/d)=floor((s+m)/d)`:

the discarded numerator part is in `(0,1)`, and division by the positive integer `d` cannot cross the next integer boundary. Thus the packet integer digit is exactly the standard floor throughout (2).

The canonical initialization `V_0=(1,-T,0)` is a declared exception to (2), because `C=0`. Its first step enters (2).

### Smallest weak-domain counterexample

Take

```
T=3, V=(-2,1,-1).
```

Then `C^2-AB=3`, `AB<0`, `|C|<sqrt(3)`, and `A!=0`, so every weak packet condition holds. But `AC>0`. The absolute-value digit is `a=1`, and

```
V'=(-3,-2,-3),
```

which has `A'B'>0` and `|C'|>sqrt(3)`. The weak domain is therefore not forward invariant. `T=3` is the smallest positive odd nonsquare, so no smaller odd nonsquare counterexample exists. Replacing `C` by `-C` selects the forward-oriented inverse-form representative, or equivalently one may restrict to (2).

This counterexample is why the final result is `EQUIVALENT_ONLY_AFTER_HYPOTHESIS_OR_SIGN_REPAIR`, rather than unconditional exact equivalence.

## 4. Two-way state correspondence and reverse recovery

For a standard reduced state `(m,d)` set

`e=(T-m^2)/d`.

For either orientation bit `sigma in {+1,-1}`, define

```
Phi_sigma(m,d)=(sigma d,-sigma e,-sigma m).   (3)
```

Conversely, any state satisfying (2) yields

```
m=|C|, d=|A|, e=|B|, sigma=sign(A).           (4)
```

The invariant proves `e=(T-m^2)/d`, and (3)-(4) are mutually inverse. Global negation changes only `sigma`; consequently candidate states modulo

`(A,B,C) ~ (-A,-B,-C)`

are in bijection with ordinary reduced complete quotients. The candidate transition flips `sigma` and applies exactly the standard transition by Theorem 1. On the canonical principal orbit, `sigma=(-1)^n`.

For a recorded digit `a`, the individual form step is also algebraically reversible. From `V'=(A',B',C')`,

```
A = B',
C = C'-aB',
B = A'-2aC'+a^2 B'.                          (5)
```

Thus no information is lost by one neighboring-form substitution when its digit/path is retained. Equation (4), rather than a finite lookup table, is the direct reverse map checked at every noninitial paired step.

An arbitrary state satisfying (2) belongs to a standard reduced complete-quotient cycle, but need not belong to the principal class reached from `V_0`. The principal-orbit claim therefore always includes canonical initialization; the general claim is equivalence of reduction dynamics within the state's own indefinite-form class.

## 5. Indefinite binary quadratic form equivalence

Associate to a state the form

`F(x,y)=Ax^2+2Cxy+By^2`,

whose discriminant is `4(C^2-AB)=4T`. Let

```
S_a = [[a,1],[1,0]],  det(S_a)=-1.
```

Under the unimodular substitution `(x,y)=(aX+Y,X)`, the transformed form has coefficients

```
[A',2C',B']=[Aa^2+2Ca+B, 2(Aa+C), A].
```

This is exactly the candidate update. It is the ordinary neighboring-form/continued-quotient move in a signed coordinate presentation. Formula (5) is the coefficient form of `S_a^{-1}`.

With `F_0(x,y)=x^2-Ty^2`, define the accumulated transform

```
P_0=I, P_{n+1}=P_n S_{a_n}.
```

Then

`F_n(z)=F_0(P_n z)`

and the coefficients of `F_n` are exactly `V_n`. This supplies both directions of the standard-form orbit identification.

### Periodic and ambiguous states

Reduced nonsquare complete quotients are periodic; periodicity is not termination. Global sign creates a twofold oriented lift. A concrete symmetric case is

```
T=5, V=(1,-1,-2), a=4, V'=(-1,1,2)=-V.
```

It is fixed after quotienting by global sign, but both oriented states have nonzero coefficients and continue indefinitely. More generally, form classes equivalent to their inverse can create such cycle symmetries; they do not create a zero or a special factor by themselves.

If all of `A,B,C` share a prime `p`, then `p^2|T`. Such imprimitive states can arise when the multiplier supplies square content. They remain algebraically valid, but must be separated in modular-root handling and are not primitive class-group representatives.

Square `T` is genuinely exceptional: the standard first denominator `T-s^2` is zero. It is outside this theorem, not an ordinary terminal state of the nonsquare recurrence.

## 6. What the closed state retains—and what it omits

The triple retains the complete quotient, its previous denominator, the next digit, and the local quadratic form. It is therefore sufficient to continue the local orbit.

It does not retain the accumulated matrix `P_n`, hence it does not uniquely retain the growing convergent numerator/denominator. A reduced state can recur after a period while `P_n` has been multiplied by a nontrivial automorphism. The `T=5` example already returns to the same oriented state after two steps while its accumulated matrix has changed. Therefore the growing convergent can be reconstructed by replaying the digit history, but not recovered as a single-valued function of the periodic triple alone.

This is the exact sense in which convergents are unnecessary for local recurrence but still necessary, directly or by replay, for the conventional global CFRAC residue.

## 7. Band semantics

Let

`D_n(t)=A_n t^2+2C_n t+B_n=F_n(t,1)`.

If

`P_n(t,1)^T=(X_t,Y_t)^T`,

then

```
D_n(t)=X_t^2-TY_t^2,                          (6)
X_t^2 == D_n(t) (mod N).                      (7)
```

The first column of `P_{n+1}` is `a_n` times the first column of `P_n` plus its second column. Hence:

- `t=a_n` is the next principal convergent/form step and `D_n(a_n)=A_{n+1}`;
- integers `0<t<a_n` are the standard intermediate/semiconvergent columns;
- `t=0` is the previous column endpoint;
- values outside `0<=t<=a_n` still satisfy (6), but are extrapolated form values, not standard intermediate convergents.

There is also a path-free local identity:

```
(A_nt+C_n)^2-A_nD_n(t)=T=MN.                 (8)
```

Thus a closed-state-only implementation has the valid congruence

`(A_nt+C_n)^2 == A_nD_n(t) (mod N)`.

It may factor and combine the signed values `A_nD_n(t)`. It may instead use `D_n(t)` only if it retains/replays `P_n` and uses the witness `X_t` from (6). Treating smoothness of `D_n(t)` alone as sufficient while discarding `P_n` is not justified by the triple.

## 8. Complete modular-root classification

The identity

`A D(t)=(At+C)^2-T`

gives the roots without heuristic assumptions.

### Odd prime `p`

1. If `p` does not divide `A`, then

   `t=(-C +/- sqrt(T)) A^{-1} (mod p)`.

   There are zero roots when `T` is a nonresidue, two distinct roots when `T` is a nonzero residue, and one double root when `p|T`.

2. If `p|A` but `p` does not divide `C`, then `D` is linear modulo `p` and has exactly one root

   `t=-B(2C)^{-1} (mod p)`.

   Here the invariant forces `T==C^2 (mod p)`, so this is a nonramified linear degeneration of the coefficient presentation.

3. If `p|A` and `p|C`, then `D(t)==B (mod p)` and `p|T`:

   - if `p` does not divide `B`, there are no roots;
   - if `p|B`, the polynomial is zero modulo `p` and all `p` residues are roots. In the latter case `p^2|T`.

### `p=2`

Since `2Ct` vanishes modulo two, `D(t)==At+B (mod 2)`:

- `A` odd: exactly one root, `t==B (mod 2)`;
- `A,B` even: both residues are roots;
- `A` even and `B` odd: no root.

The same classification applies to small and large factor-base primes; size changes cost, not algebra. If a declared factor-base prime has `gcd(p,N)>1`, that gcd is already an immediate factor and the root need not enter ordinary sieving. For prime powers, every simple root (`2At+2C` nonzero modulo `p`) lifts uniquely by Hensel's lemma. Ramified double roots and zero-polynomial cases can have zero, several, or all lifts depending on valuations and must be recomputed rather than assigned the simple-root rule.

## 9. Square-congruence relation semantics

Each accepted relation must declare which of the two valid witnesses it uses:

- accumulated form: `(X_t, D_n(t))` from (6)-(7); or
- closed-state local form: `(A_nt+C_n, A_nD_n(t))` from (8).

For either form, factor the entire signed right-hand side. Include `-1` as a parity coordinate. A collection `I` is a square dependency only when every signed prime exponent in

`product_{i in I} R_i`

is even. Then

```
X = product X_i (mod N),
Y = product p^(sum_i e_{i,p}/2) (mod N),
X^2 == Y^2 (mod N),
gcd(X-Y,N), gcd(X+Y,N)
```

are verified in that order. An odd `-1` exponent is not discardable. Pre-existing square factors contribute half their exponent to `Y`; they are not merely removed from the audit trail.

A single-large-prime partial becomes a usable relation only after the large prime has even total exponent, normally by pairing the same large prime. Double-large-prime partials form graph edges; only an edge cycle gives even incidence for every large prime. The checker verifies both a single-prime pair (`31`) and a two-edge double-prime cycle (`19*41`) using actual band values for `T=N=5`, then rechecks the resulting congruences. This establishes semantics, not a yield or speed claim.

Before sieving, `gcd(M,N)>1` is already a factor and must be reported. Otherwise `T=MN` vanishes modulo `N`, which is why (7)-(8) remain valid. The multiplier still changes the integer discriminant, orbit, coefficient sizes, and root characters. Replacing `M` by `Mr^2` preserves Legendre/Kronecker characters away from primes dividing `rMN`, but does not produce the same canonical form orbit. Scaling a state scales its invariant by `r^2`; it does not turn `(1,-T,0)` into `(1,-r^2T,0)`.

## 10. Independent validation record

Command:

`python experiments/valley_band_pure_state_equivalence_checker.py`

Formal full-run results:

- deterministic corpus: 20 balanced exact 80-bit semiprimes, SHA-256 seed rule recorded in the checker summary;
- paired candidate/reference steps: `100000` (`20*5000`);
- direct state-map round trips: `99980` (all noninitial steps);
- paired stream SHA-256: `cdfc900c1daaeaf21cd353795c72a5569cc0500e8403c0e1e2dd28e969ad607c`;
- root exhaustion cases: `13602`, comprising `2848992` tested residues, including primes through 257 and selected primes `1009,1013,4099,65537`;
- simple Hensel roots: `38/38` had exactly one lift modulo `p^2`; ramified profiles were separately recorded;
- matrix/band identities: `2732`; principal endpoints: `144`;
- fully factored signed band relations: `2448`; even-exponent dependencies checked: `256`; dependencies yielding a nontrivial factor in the small controlled corpus: `180`;
- recurrence sign perturbations rejected: all `6/6`; wrong quotient direction rejected;
- required weak-domain counterexample and symmetric nonterminal state confirmed;
- mismatch count: `0`.

The candidate and reference recurrence functions share no transition helper. Analytic modular roots are compared against an independent all-residue evaluator. Negative controls change each recurrence sign, change the quotient direction, mutate a relation witness and value, omit the required factor `A`, omit signed parity, and inject nonroots. The mismatch log is emitted even when empty.

These checks establish reproducibility and catch implementation errors. The equivalence, counterexample, root cases, and relation rules are proved in Sections 2-9 independently of the finite corpus.

## 11. Prior-art and novelty boundary

The neighboring-form map, standard complete quotients, accumulated convergents, CFRAC square dependencies, multiplier characters, intermediate columns, and polynomial modular-root sieving all have classical or established antecedents. The separate prior-art map cites Gauss's original form reduction, Lehmer-Powers, Morrison-Brillhart, Pomerance-Wagstaff, Pomerance's quadratic sieve, and Gower-Wagstaff's square-form factorization, plus authoritative monographs for the standard algebra.

The packet's closed signed triple and its band are therefore best classified as a coordinate presentation and synthesis of established components. This report finds no evidence for a new orbit. It makes no performance, yield, or superiority claim. A claim that this exact full-band packaging appeared previously would require a more targeted historical search; none is asserted here.

## 12. Final closure statement

The hard target is met with the exact result:

**`EQUIVALENT_ONLY_AFTER_HYPOTHESIS_OR_SIGN_REPAIR`**.

After canonical initialization and repair (2), the candidate recurrence, standard complete-quotient recurrence, and neighboring indefinite-form orbit are bijectively the same dynamics, modulo the explicit global-sign lift. Without that repair, the `T=3` counterexample refutes equivalence. Band roots and square-congruence semantics are completely classified, including degenerate primes, multiplier/square-content effects, signs, square factors, and large-prime recombination.
