# Enterprise BRC Half-Coupling Inert-Minus Second-Order CM/Jacobi Lift — Research Return

Status: `FINAL_FROZEN / PROOF_NOT_CLOSED / STRICT_EXACT_CLAUSEN_REDUCTION / SINGLE_FINITE_TRANSFORMATION_RESIDUE`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-SECOND-ORDER-CM-JACOBI-LIFT`  
Publication: `TP2-05DB03EAF4E1DDCDBDF2`  
Claim: `chatgpt-ebp5m2-20260828-1411-d74849`  
Researcher-ID: `EM-EBP5M2-D74849`  
Execution: `ER-69F4296978826B9EBFA6`

## Frozen verdict

`PRIMARY_VERDICT = PROOF_NOT_CLOSED_WITH_STRICT_EXACT_REDUCTION`.

The requested all-prime proofs of `(R0-)` and `(R1-)` were **not** closed in this execution. They were, however, reduced exactly and substantially farther than the six-quantity second-order deformation interface.

For every prime
\[
p\equiv17,23\pmod{24},
\]
the conjunction `(R0-) + (R1-)` is equivalent to the single Ramanujan-type supercongruence
\[
\boxed{
W_p:=\sum_{n=0}^{p-1}(6n+1)
\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
\equiv-p\pmod{p^3}.
}
\tag{W-}
\]

This is not merely a numerical reformulation: there is an exact finite identity
\[
\boxed{S_p=G_pH_p-T_p=W_p}
\tag{FC}
\]
obtained by symmetrization followed by Clausen's coefficient formula. Thus the entire remaining second-order BRC residue is a classical one-variable truncated hypergeometric supercongruence.

Moreover `(W-)` is exactly the `a=1`, `p\equiv2\pmod3` specialization of Zhi-Wei Sun's Conjecture A14(ii) in *Open Conjectures on Congruences* (arXiv:0911.5665v41). A targeted literature check found the exact conjectural statement, the known zero-order/unweighted CM results, and Swisher's adjacent E.2 theorem, but did **not** locate a verifiable published all-prime proof of this exact weighted `216^{-n}` congruence. Therefore this return does not promote it to a theorem by citation.

The smallest exact successor certificate found here is a finite transformation bridge from `(W-)` to a theorem of Swisher:
\[
\boxed{C_p\equiv0\pmod{p^3}},
\tag{Bridge-}
\]
where for \(M=(2p-1)/3\),
\[
C_p=
2\sum_{k=0}^{M}(6k+1)
\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3 2^k}
-
\sum_{k=0}^{M}(-1)^k(6k+1)\frac{(1/3)_k^3}{(k!)^3}.
\]
Swisher proved the second sum is \(-2p\pmod{p^3}\) for every prime \(p\equiv2\pmod3\). Hence `(Bridge-)` is equivalent to `(W-)` on the target classes. The bridge passed bounded regression but remains unproved here.

## 1. Frozen parent interface

The predecessor return is accepted as frozen. In its notation,
\[
S_p=G_pH_p-T_p,
\]
and it proved the complete first cancellation layer
\[
p\mid T_{00},\quad p\mid T_{01},\quad p^2\mid T_{02},\quad p^2\mid T_{11},\quad p\mid G_p.
\]
It then introduced
\[
g_0,g_1,\tau_0,\tau_1,J_0,J_1
\]
and proved that the original inert-minus target is equivalent to
\[
g_0J_0-\tau_0\equiv-1\pmod p
\tag{R0-}
\]
and
\[
\frac{g_0J_0-\tau_0+1}{p}+g_0J_1+g_1J_0-\tau_1\equiv0\pmod p.
\tag{R1-}
\]
Equivalently, if
\[
A=g_0J_0-\tau_0,
\qquad
B=g_0J_1+g_1J_0-\tau_1,
\]
then the pair says exactly
\[
A+pB\equiv-1\pmod{p^2},
\]
which is the frozen expansion of \(S_p/p\). No parent cancellation layer is reopened below.

## 2. Exact symmetrization removes the derivative asymmetry

Recall
\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2}2^{-k},
\quad
G_p=\sum_{k=0}^{p-1}B_k,
\quad
H_p=\sum_{k=0}^{p-1}(12k+1)B_k.
\]
Then
\[
G_pH_p
=\sum_{0\le i,j<p}(12j+1)B_iB_j.
\]
Interchanging \(i\) and \(j\) and averaging gives the exact identity
\[
\boxed{
G_pH_p
=\sum_{0\le i,j<p}(1+6(i+j))B_iB_j.
}
\tag{S1}
\]
The tail \(T_p\) is exactly the part of this symmetric double sum with \(i+j\ge p\). Therefore
\[
\boxed{
S_p=G_pH_p-T_p
=\sum_{\substack{0\le i,j<p\\i+j<p}}
(1+6(i+j))B_iB_j.
}
\tag{S2}
\]
This step is exact over \(\mathbb Q\); no congruence and no CM input has been used.

## 3. Finite Clausen collapse

Set
\[
F(x)=\sum_{k\ge0}B_kx^k
={}_2F_1\!\left(\frac16,\frac13;1;\frac{x}{2}\right).
\]
Because
\[
1=\frac16+\frac13+\frac12,
\]
Clausen's formula gives
\[
F(x)^2
={}_3F_2\!\left(
\frac12,\frac13,\frac23;1,1;\frac{x}{2}
\right).
\]
Thus for every \(n\ge0\), coefficient comparison yields
\[
\sum_{i=0}^{n}B_iB_{n-i}
=
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3 2^n}.
\tag{C1}
\]
Using
\[
\frac{(1/2)_n}{n!}=\frac{\binom{2n}{n}}{4^n},
\qquad
\frac{(1/3)_n(2/3)_n}{(n!)^2}
=\frac{\binom{2n}{n}\binom{3n}{n}}{27^n},
\]
we obtain
\[
\boxed{
\sum_{i=0}^{n}B_iB_{n-i}
=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}.
}
\tag{C2}
\]
Since the triangle in `(S2)` has \(n=i+j=0,\ldots,p-1\), grouping by \(n\) gives the exact finite identity
\[
\boxed{
S_p=
\sum_{n=0}^{p-1}(6n+1)
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
=W_p.
}
\tag{FC}
\]
There is no infinite-series truncation argument in `(FC)`.

## 4. Exact valuation control of the high tail

For \(0\le n<p\), Legendre/Kummer counting gives
\[
\begin{aligned}
v_p\!\left(\binom{2n}{n}^2\binom{3n}{n}\right)
&=2\Big\lfloor\frac{2n}{p}\Big\rfloor
+\Big\lfloor\frac{3n}{p}\Big\rfloor
-\Big\lfloor\frac{2n}{p}\Big\rfloor\\
&=\boxed{\Big\lfloor\frac{2n}{p}\Big\rfloor+\Big\lfloor\frac{3n}{p}\Big\rfloor}.
\end{aligned}
\tag{V}
\]
For the target classes \(p=6m+5\), put
\[
M=\frac{2p-1}{3}=4m+3.
\]
If \(n>M\), then \(n>2p/3\), so `(V)` is at least \(1+2=3\). Since \(p\nmid216\),
\[
W_p\equiv
\sum_{n=0}^{M}(6n+1)
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
\pmod{p^3}.
\tag{T}
\]
This is the exact finite endpoint needed for comparison with Swisher's \((2p-1)/3\) truncation.

## 5. Equivalence to `(R0-) + (R1-)`

The predecessor expansion has
\[
\frac{S_p}{p}\equiv A+pB\pmod{p^2},
\]
with
\[
A=g_0J_0-\tau_0,
\qquad
B=g_0J_1+g_1J_0-\tau_1.
\]
Therefore
\[
S_p\equiv-p\pmod{p^3}
\]
is equivalent to
\[
A+pB\equiv-1\pmod{p^2}.
\]
Splitting this single congruence into its zeroth and first base-\(p\) digits gives exactly `(R0-)` and `(R1-)`. Combining with `(FC)` proves
\[
\boxed{
(R0-)\ \&\ (R1-)
\iff
W_p\equiv-p\pmod{p^3}.
}
\tag{EQ}
\]
Thus the six deformation quantities are no longer the minimal unresolved interface.

## 6. Exact match with Sun's Conjecture A14(ii)

Zhi-Wei Sun's *Open Conjectures on Congruences*, arXiv:0911.5665v41, Conjecture A14(ii), states in particular that for every prime \(p>3\) and positive integer \(a\),
\[
\frac1{p^a}\sum_{k=0}^{p^a-1}
\frac{6k+1}{6^{3k}}
\binom{2k}{k}^2\binom{3k}{k}
\equiv
\left(\frac{p^a}{3}\right)
\pmod{p^2}.
\tag{Sun-A14}
\]
Taking \(a=1\) gives exactly
\[
W_p\equiv p\left(\frac p3\right)\pmod{p^3}.
\tag{Sun-W}
\]
For
\[
p\equiv17,23\pmod{24},
\]
we have \(p\equiv2\pmod3\), hence
\[
\left(\frac p3\right)=-1,
\]
and `(Sun-W)` is exactly `(W-)`.

### Literature boundary

The targeted search performed in this execution located:

1. the exact A14(ii) conjectural statement above;
2. Zhi-Hong Sun's 2013 proof of the corresponding unweighted/CM-level congruences used upstream, not the weighted mod-\(p^3\) statement `(Sun-W)`;
3. later literature explicitly recording Guo-Zudilin's proof of the sibling `8k+1`, quartic-binomial, `48^{-2k}` mod-\(p^3\) congruence;
4. Swisher's adjacent \((1/3)^3\) supercongruence below.

No source inspected in this execution supplied a verifiable proof of `(Sun-W)` itself. Absence from a later conjecture list is not treated as proof. Hence `(Sun-W)` remains an imported **conjectural target**, not an imported theorem, in this return.

## 7. Swisher finite-transformation bridge

For \(p\equiv2\pmod3\), define
\[
E_p=\sum_{k=0}^{M}(-1)^k(6k+1)\frac{(1/3)_k^3}{(k!)^3},
\qquad M=\frac{2p-1}{3}.
\]
Holly Swisher, *On the supercongruence conjectures of van Hamme*, Research in the Mathematical Sciences 2:18 (2015), proved
\[
\boxed{E_p\equiv-2p\pmod{p^3}}.
\tag{Sw}
\]
By `(T)`, `(W-)` is therefore equivalent to the single finite bridge
\[
\boxed{
2W_p-E_p\equiv0\pmod{p^3},
}
\tag{Bridge-raw}
\]
where the \(W_p\)-side may be truncated at \(M\). In pure Pochhammer form:
\[
\boxed{
\begin{aligned}
C_p={}&2\sum_{k=0}^{M}(6k+1)
\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3 2^k}\\
&-\sum_{k=0}^{M}(-1)^k(6k+1)
\frac{(1/3)_k^3}{(k!)^3}
\equiv0\pmod{p^3}.
\end{aligned}}
\tag{Bridge-}
\]
This is the smallest explicit residue found in this execution: a single finite cubic/Clausen-to-E.2 transformation congruence with matching truncation endpoint.

Bounded regression found `(Bridge-)` for every prime \(p\equiv2\pmod3\), \(5\le p\le1000\) (`86` primes). This is falsification evidence only.

## 8. Why the ordinary analytic transformation is insufficient

The corresponding infinite Ramanujan values satisfy
\[
W_\infty=\frac{3\sqrt3}{\pi},
\qquad
E_\infty=\frac{3\sqrt3}{2\pi},
\]
so
\[
W_\infty=2E_\infty.
\]
But the finite \(p\)-adic bridge required above is
\[
E_p\equiv2W_p\pmod{p^3}.
\]
The factor is reversed. Consequently, a proof cannot take an ordinary analytic cubic transformation and silently truncate it: the finite boundary/tail carries a leading \(p\)-adic correction. Any successful hypergeometric proof must include an explicit terminating deformation, WZ certificate, creative-microscoping certificate, or equivalent tail calculation.

This is a route-specific no-go for the naive `analytic identity -> truncate -> congruence` move; it is not a no-go against a genuine terminating cubic transformation.

## 9. Independent Domb/Apéry route

The Clausen sum also sits on the classical Domb pullback. Let
\[
D_n=\sum_{k=0}^{n}
\binom nk^2\binom{2k}{k}\binom{2n-2k}{n-k}.
\]
Rogers' Domb generating-function transformation uses the pullback
\[
\phi(x)=\frac{108x^2}{(1-4x)^3}.
\]
At \(x=-1/8\),
\[
\phi(-1/8)=\frac12,
\]
which is exactly the argument of the collapsed \({}_3F_2\) behind \(W_p\).

This motivated the independent diagnostic
\[
\mathcal D_p=
\sum_{n=0}^{p-1}(2n+1)D_n(-8)^{-n}.
\]
For every tested prime \(p\equiv2\pmod3\), \(5\le p\le100\),
\[
\mathcal D_p\equiv-p\pmod{p^3}.
\]
Again, the finite Rogers transformation has boundary terms, so this is not promoted to a proof. It is an independent structural route: Domb/modular pullback rather than the Swisher E.2 finite transformation.

## 10. Deterministic regression

Checker:

`scripts/check_enterprise_brc_half_coupling_inert_minus_second_order_cm_jacobi_lift.py`

Default frozen regression:

- exact Clausen coefficient identity `(C2)`: `n=0..10`, all PASS as rational equalities;
- valuation formula `(V)`: checked for every `0<=n<p` on every prime `5<=p<=1000`;
- broad Sun pattern `W_p == p*(p/3) mod p^3`: `166` primes `<=1000`, failures `0`;
- target classes `p≡17,23 mod24`: `45` primes `<=1000`, failures `0`;
- Swisher bridge `(Bridge-)`: `86` primes `p≡2 mod3`, `p<=1000`, failures `0`;
- Domb diagnostic: `12` primes `p≡2 mod3`, `p<=100`, failures `0`.

The checker prints `proof_status=FINITE_REGRESSION_ONLY` explicitly.

## 11. Dependency map

Frozen predecessor facts used:

- exact `S_p=G_pH_p-T_p`;
- the two-rate expansion identifying `(R0-)` and `(R1-)` with the two base-\(p\) digits of `S_p/p + 1`;
- target prime classes `p≡17,23 mod24`.

New exact facts proved here:

- symmetrization `(S1)`;
- triangular identity `(S2)`;
- finite Clausen coefficient collapse `(C2)`;
- exact one-variable identity `(FC)`;
- valuation formula `(V)` and mod-\(p^3\) endpoint `(T)`;
- equivalence `(EQ)`.

Imported theorem used only for the successor bridge:

- Swisher 2015, `(Sw)`.

Imported conjecture identified, not granted:

- Z.-W. Sun, Conjecture A14(ii), `(Sun-A14)` / `(Sun-W)`.

## Final boundary

Closed:

- the six-variable second-order residue is collapsed to one scalar Ramanujan-type supercongruence;
- `(R0-) + (R1-)` are exactly equivalent to `(W-)`;
- the high tail of `W_p` is killed modulo \(p^3\) at the same endpoint as Swisher's theorem;
- the task is identified exactly with the inert-minus subfamily of Sun A14(ii);
- a single finite transformation bridge `(Bridge-)` to Swisher is isolated;
- a second, Domb/modular, route is isolated;
- a route-specific no-go forbids silently truncating the analytic transformation.

Not closed:

- an all-prime proof of `(W-)` / Sun A14(ii) on \(p\equiv17,23\pmod{24}\);
- equivalently, an all-prime proof of the finite bridge `(Bridge-)`;
- therefore `(R0-) + (R1-)` are not claimed proved.

`HARD_TARGET = NOT_ACHIEVED_AT_FULL_PROOF_STRENGTH`.  
`HARD_TARGET_DISPOSITION = ACHIEVED_AT_STRICT_EXACT_REDUCTION_STRENGTH`.  
`SMALLEST_EXACT_REMAINING_IDENTITY = FINITE_CLAUSEN_TO_SWISHER_BRIDGE_(Bridge-)`.  
`CLASSICAL_IDENTIFICATION = ZW_SUN_A14(ii)_a=1`.  
`FOUNDATION_MUTATION = NONE`.  
`WORKING_TRUTH = NOT_GRANTED`.  
`NOVELTY_OR_PRIORITY_CLAIM = NONE`.

Recommended Driver action: accept the exact collapse and publish, if continuation remains high value, **one** narrow successor for a terminating cubic/WZ/creative-microscoping proof of `(Bridge-)`; do not reopen the proved mod-\(p\) CM cancellation, do not treat Sun A14(ii) as proved without a verified source, and do not substitute a larger prime scan for proof.
