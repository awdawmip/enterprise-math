# Prime Coordinate Blind p-adic-to-GCD Bridge — Research Return

Task: `RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE`  
Publication: `TP2-7B0534E09E4286CB5B6E`  
Claim: `chatgpt-pcf4-20260827-1714`  
Researcher-ID: `EM-PCF4-AED70E`  
Execution record: `ER-CB5BCA1809671D892B42`

## Frozen verdict

`BRIDGE_NOT_CLOSED`

Hard target `BLIND_PADIC_GCD_BRIDGE_PROVED_REFUTED_OR_EXACTLY_OBSTRUCTED` is **exactly obstructed for the canonical public-prefix lift**, but not closed for every possible N-dependent second observable.

The new exact obstruction is:

`PUBLIC_PREFIX_FIXED_INTEGER_SUPPORT_NO_GO`.

The p-specific half-coupling fingerprint cannot be turned into a factor-blind asymmetry merely by replacing the hidden prime truncation with an independent public prefix length. After denominator clearing, every such candidate is just gcd against one precommitted integer.

No generic factorization speedup is claimed.

## 1. N-only constructor audited

Let

\[
A_n=\frac{(2n)!(3n)!}{(n!)^5}
=\binom{2n}{n}^2\binom{3n}{n}.
\]

For an odd input `N` with `gcd(N,6)=1` and a public seed/prefix length `L>=1`, define

\[
G_N(L)=\sum_{n=0}^{L-1}
(6n+1)A_n\,216^{-n}\pmod N.
\tag{1}
\]

The seed `L` is independent of the hidden factors. The candidate side reads only `(N,L)` and public constants.

Define the denominator-cleared integer

\[
F_L=
\sum_{n=0}^{L-1}
(6n+1)A_n\,216^{L-1-n}
\in\mathbb Z.
\tag{2}
\]

The exact recurrence used by Checker A is

\[
A_0=1,\qquad
A_{n+1}
=
A_n\,
\frac{6(2n+1)(3n+1)(3n+2)}{(n+1)^3},
\tag{3}
\]

with the division performed in `Z` and asserted exact. This avoids every illegal division modulo a composite.

Stopping rule for this audited lift: compute one prefix `L`, then compute `gcd(G_N(L),N)`.

## 2. Exact fixed-support theorem

### Theorem 1 — denominator-clearing equivalence

For every `N` with `gcd(N,6)=1` and every `L>=1`,

\[
\boxed{
216^{L-1}G_N(L)\equiv F_L\pmod N.
}
\tag{4}
\]

Since `216^(L-1)` is a unit modulo `N`,

\[
\boxed{
\gcd(G_N(L),N)=\gcd(F_L,N).
}
\tag{5}
\]

**Proof.** Multiply (1) by `216^(L-1)` term by term. The result is exactly (2) modulo `N`. Multiplication by a unit modulo `N` preserves the gcd with `N`. ∎

### Corollary 1 — complete CRT/failure classification

Let `N=pq` with distinct primes `p,q>3`. Then:

- `gcd(G_N(L),N)=1` iff neither `p` nor `q` divides `F_L`;
- `gcd(G_N(L),N)=p` iff `p|F_L` and `q∤F_L`;
- `gcd(G_N(L),N)=q` iff `q|F_L` and `p∤F_L`;
- `gcd(G_N(L),N)=N` iff both divide `F_L`.

Thus the reduction modulo `N` creates **no new local asymmetry**. All asymmetry was already present in the prime support of the fixed integer `F_L`.

For any public seed distribution `mu`, the exact success probability is therefore

\[
\Pr(\text{split})
=
\mu\{L:p\mid F_L,\ q\nmid F_L\}
+
\mu\{L:q\mid F_L,\ p\nmid F_L\}.
\tag{6}
\]

No hidden-factor quantity appears on the candidate side.

## 3. Finite public-seed no-go

### Theorem 2 — finite support obstruction

Let `S` be any fixed finite set of public prefix lengths and put

\[
P_S=\prod_{L\in S}F_L.
\]

Only prime divisors of `P_S` can ever be exposed by the family
`{G_N(L):L in S}`.

Because `P_S` has finite prime support and there are infinitely many primes, there exist infinitely many distinct prime pairs `p,q>3` with

\[
p\nmid P_S,\qquad q\nmid P_S.
\]

For every corresponding semiprime `N=pq` and every `L in S`,

\[
\boxed{\gcd(G_N(L),N)=1.}
\tag{7}
\]

Therefore no fixed finite public-prefix seed family is a generic semiprime splitter.

This is an exact no-go, not a density heuristic.

## 4. Exact support-size bound

Elementary binomial bounds give

\[
A_n
=
\binom{2n}{n}^2\binom{3n}{n}
\le 4^n\,4^n\,8^n
=128^n
\le216^n.
\]

Hence every term of `F_L` is less than `(6L)216^(L-1)`, so

\[
\boxed{
0<F_L<6L^2\,216^{L-1}.
}
\tag{8}
\]

Writing `omega(m)` for the number of distinct prime divisors,

\[
\boxed{
\omega(F_L)
<
\log_2(6L^2)+(L-1)\log_2 216.
}
\tag{9}
\]

Thus even before any finer arithmetic is used, each public prefix has only `O(L)` distinct prime support. A finite seed family accumulates only the union of those fixed supports.

## 5. Why the p-specific fingerprint does not survive blind substitution

The predecessor p-adic object uses a **factor-labelled truncation length** `p`:

\[
S_p=
\sum_{n=0}^{p-1}
(6n+1)A_n216^{-n}.
\]

That `p` is not an admissible constructor input under PCF1.

Replacing it by an independent public `L` yields Theorems 1–2 and therefore a fixed-integer gcd probe. The prime fingerprint has not been transformed into an N-only asymmetry generator; the factor-labelled stopping boundary has simply been removed.

This precisely separates:

`FINGERPRINT_CONGRUENCE != FACTOR_ASYMMETRY`.

## 6. Composite-length lift and synchronization frontier

A second natural blind lift is to replace the hidden truncation by the input itself:

\[
L=N.
\]

For a prime `p>3`, all `a>=0`, and `0<=b<p`, Lucas' theorem gives the exact block law

\[
\boxed{
A_{ap+b}\equiv A_aA_b\pmod p.
}
\tag{10}
\]

Reason: if `b>p/3`, a low base-`p` carry makes the relevant binomial factor and `A_b` vanish modulo `p`; if `b<=p/3`, there is no low carry and Lucas factors the two binomial coefficients into the high-digit and low-digit pieces.

Also, Fermat gives `216^(-ap) == 216^(-a) (mod p)`, and the weight satisfies
`6(ap+b)+1 == 6b+1 (mod p)`.

For `N=pq`, splitting the `pq` terms into `q` blocks of length `p` therefore yields

\[
G_{pq}(pq)
\equiv
S_p
\sum_{a=0}^{q-1}A_a216^{-a}
\pmod p.
\tag{11}
\]

The analogous statement holds modulo `q`.

Consequently:

> If the weak prime shadow
> \[
> S_r\equiv0\pmod r
> \tag{W}
> \]
> holds for both hidden primes `r=p,q`, then
> \[
> \boxed{G_{pq}(pq)\equiv0\pmod{pq}}
> \]
> and the gcd is `N`, not a factor.

This is an exact **conditional synchronization theorem**.

Current repository state does **not** contain an all-prime proof even of the stronger mod-`p^3` target; Sun A14(ii) remains a prior conjecture, and the dedicated all-prime proof task returned `PROOF_NOT_CLOSED`. Therefore `(W)` is not silently promoted here.

## 7. Independent exact checkers

Two candidate-side checkers were implemented. Both candidate functions receive only `(N,L)` and public constants.

### Checker A — exact recurrence

`scripts/check_prime_coord_factor_blind_padic_gcd_bridge.py`

Load-bearing construction: exact integer recurrence (3), with exact divisibility asserted before division.

Frozen result:

`PCF4_CHECK_A_PASS gcd_cases=204 weak_primes=93 composite_sync=66 d_pattern=100`

### Checker B — direct binomial construction

`scripts/check_prime_coord_factor_blind_padic_gcd_bridge_independent.py`

Load-bearing construction:

\[
A_n=\binom{2n}{n}^2\binom{3n}{n}
\]

using direct exact binomial integers, not recurrence (3).

Frozen result:

`PCF4_CHECK_B_PASS gcd_cases=112 weak_primes=53 composite_sync=36`

SHA256:

- Checker A: `sha256:2f287d5e9ab5ca929b95f9a96a5447818f6de25d9951f269d07812d92839e390`
- Checker B: `sha256:b216d073c5e61eb55f08cfbe9c4c000cdd77507c4938a89455e230983e710b8f`

Both verify the exact gcd-equivalence theorem independently.

## 8. Regression-only observations

These are **not proofs**:

1. weak shadow `(W)` passes every prime `5<=p<=499` in Checker A and every prime `5<=p<=257` in Checker B;
2. `G_(pq)(pq)=0 mod pq` passes all tested distinct prime pairs through `43` (Checker A) and through `31` (Checker B);
3. for `1<=L<=100`, both calculations are consistent with
   \[
   d_L\mid F_L,\qquad
   d_L=
   \begin{cases}
   3L-2,&L\text{ odd},\\
   3L-1,&L\text{ even}.
   \end{cases}
   \]
   This pattern is deliberately left as a conjectural finite observation.

No finite range is promoted to an infinite theorem.

## 9. Complexity

For the recurrence implementation through prefix `L`:

- `O(L)` recurrence/gcd-stage arithmetic steps;
- exact `A_n` intermediates have `O(L)` bits up to constants from the exponential growth;
- `F_L` has `O(L+log L)` bits by (8);
- a conservative bit bound is polynomial in `L+log N`, e.g. `O(L M(L+log N))` for standard fast-integer multiplication cost `M`;
- streaming memory is `O(L+log N)` bits.

For a fixed public `L`, this is polynomial in `log N`, but Theorem 1 shows that it is only a fixed-integer gcd probe. Increasing `L` enlarges support but does not create N-dependent dynamics.

No sub-square-root generic factoring theorem is claimed.

## 10. Smallest unresolved unit

The direct fingerprint-to-gcd bridge now has a sharp interface requirement:

`N_DEPENDENT_SECOND_OBSERVABLE_NOT_FIXED_INTEGER_REDUCTION`.

A successor would need an integer observable whose value genuinely depends on `N` **before** the final modular reduction and whose CRT projections can be proved asymmetric on a nontrivial infinite semiprime family.

Merely choosing more public prefix lengths, or reducing the same rational sequence modulo `N`, stays inside the fixed-support no-go class.

A secondary theorem frontier for the `L=N` lift is the weaker all-prime statement `(W)`. Proving `(W)` would certify synchronization, not extraction.

## 11. Claim boundary

Established:

- exact N-only public-prefix construction;
- exact denominator clearing;
- exact gcd/CRT success and failure set;
- exact finite-public-seed no-go;
- exact support-size bound;
- exact Lucas block decomposition;
- exact conditional synchronization theorem for `L=N`;
- two independent exact-integer checker implementations.

Not established:

- a generic or balanced-semiprime extractor;
- an N-dependent asymmetric second observable;
- the all-prime weak shadow `(W)`;
- the all-prime mod-`p^3` Sun congruence;
- any factorization speedup theorem.

Artifact:

`research_artifacts/PRIME_COORD_FACTOR_BLIND_PADIC_GCD_BRIDGE_20260827/evidence.json`

## Driver recommendation

Accept this task at `BRIDGE_NOT_CLOSED / EXACT_OBSTRUCTION` strength if the scope is read exactly:

- close the naive public-prefix lift as `PUBLIC_PREFIX_FIXED_INTEGER_SUPPORT_NO_GO`;
- do not relabel the finite synchronization evidence as an all-prime theorem;
- do not issue another task that only extends prime bounds;
- if continuing PCF4, require a genuinely N-dependent second observable outside the fixed-integer reduction class.

Research state after result freeze: `AWAITING_DRIVER_REVIEW`. The researcher does not self-issue `DONE`.
