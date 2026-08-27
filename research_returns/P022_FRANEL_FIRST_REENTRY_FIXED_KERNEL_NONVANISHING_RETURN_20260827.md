# P022 Franel First-Reentry Fixed-Kernel Nonvanishing Return — 2026-08-27

Task: `RS-P022-FRANEL-FIRST-REENTRY-KERNEL-NONVANISHING`  
Publication: `TP2-18D80E295208AC91EB70`  
Researcher: `EM-P022KERN-4E4834`  
Claim: `chatgpt-p022kern-20260827-2141-4e4834`

## Verdict

`PASS / RETURN-CRITERION MET VIA EXACT REDUCTION TO A NAMED HAHN DIAGONAL INVARIANT`

This execution does **not** prove all-parameter nonvanishing of the P022 first-reentry kernel and does not produce an admissible zero. Instead it reaches the taskbook's explicit exact-reduction stopping condition: the residual fixed rational `3F2` is exactly one diagonal value of the classical Hahn polynomial family, hence is governed by a canonical second-order discrete Hahn operator. The remaining P022 gate is a single arithmetic nonvanishing statement for that named diagonal family.

No Working Truth, Foundation mutation, or canonical theorem promotion is claimed. Driver review is required.

## 1. Reparameterization of the live P022 boundary

Put

\[
n=3m,\qquad p=6n-1=18m-1.
\]

The admissible P022 constellation is

\[
p,\quad 4n-1,\quad 4n+1\quad\text{prime},\qquad 3\mid n.
\]

The accepted parent return leaves

\[
R_m(p)=\sum_{j=0}^{n}
\frac{(-1/6)_j^3}{(1/2)_j(-1/2)_j\,j!}
\pmod p.
\]

Since `6n = 1 (mod p)`, in `F_p` one has

\[
-\frac16\equiv-n,\qquad
\frac12\equiv 1-3n,\qquad
-\frac12\equiv-3n.
\]

Every denominator factor remains a p-unit on `0 <= j <= n`, so termwise substitution is legal. Therefore

\[
\boxed{
R_m(p)\equiv
{}_3F_2\!\left[
\begin{matrix}-n,-n,-n\\1-3n,-3n\end{matrix};1
\right]
\pmod p.
}
\]

## 2. Exact Hahn identification

Use the standard Hahn normalization

\[
Q_k(x;\alpha,\beta,N)
={}_3F_2\!\left[
\begin{matrix}
-k,\ k+\alpha+\beta+1,\ -x\\
\alpha+1,\ -N
\end{matrix};1
\right].
\]

This is the classical definition recorded in NIST DLMF §18.20.5.

Choose

\[
k=n,\qquad x=n,\qquad
\alpha=-3n,\qquad \beta=n-1,\qquad N=3n.
\]

Then

\[
k+\alpha+\beta+1=-n,
\]

so all three upper parameters equal `-n`, while the lower parameters are `1-3n` and `-3n`. Define the exact rational invariant

\[
\boxed{
\mathcal H_n:=Q_n(n;-3n,n-1,3n).
}
\]

Hence, identically over the rationals,

\[
\boxed{
\mathcal H_n=
{}_3F_2\!\left[
\begin{matrix}-n,-n,-n\\1-3n,-3n\end{matrix};1
\right],
}
\]

and on the P022 prime boundary,

\[
\boxed{R_m(p)\equiv\mathcal H_n\pmod p.}
\]

This is not a numerical pattern or an identification from finite data; it is direct parameter equality in the Hahn definition.

## 3. Denominator-free combinatorial form

For `0 <= j <= n`, converting the terminating Pochhammer factors gives

\[
\frac{(-n)_j^3}{(1-3n)_j(-3n)_j\,j!}
=
(-1)^j
\frac{\binom nj^3}
{\binom{3n-1}{j}\binom{3n}{j}}.
\]

Therefore

\[
\boxed{
\mathcal H_n=
\sum_{j=0}^{n}
(-1)^j
\frac{\binom nj^3}
{\binom{3n-1}{j}\binom{3n}{j}}.
}
\]

For `p=6n-1`, the two binomial denominators are p-units, so this also gives a direct finite-field evaluation surface.

## 4. Exact reconnection to the Franel obstruction

The parent result proves

\[
2^{-2n}F_{2n}\equiv
{}_3F_2\!\left[
\begin{matrix}-n,2n,2n+1\\1,1\end{matrix};1
\right]
\pmod p.
\]

The finite reversal identity for a terminating `3F2(-n,a,b;1,1;1)` is exact. With `a=2n`, `b=2n+1`, it gives

\[
{}_3F_2\!\left[
\begin{matrix}-n,2n,2n+1\\1,1\end{matrix};1
\right]
=
(-1)^n\frac{(2n)_n(2n+1)_n}{(n!)^2}\,\mathcal H_n.
\]

Consequently

\[
\boxed{
F_{2n}\equiv
2^{2n}(-1)^n
\frac{(2n)_n(2n+1)_n}{(n!)^2}\,\mathcal H_n
\pmod p.
}
\]

All factors in the displayed prefactor lie strictly below `p=6n-1`, so the prefactor is a p-unit. Thus

\[
\boxed{
p\mid F_{2n}
\iff
\mathcal H_n\equiv0\pmod p.
}
\]

For `n=3m`, this is exactly the original P022 first-reentry visibility obstruction `p | F_(6m)`.

## 5. The residual now has a canonical rank-two discrete operator

Hahn polynomials satisfy the standard second-order difference equation (NIST DLMF §18.22). In the present specialization,

\[
A(x)=(x-3n+1)(x-3n),\qquad
C(x)=x(x-4n),
\]

and `Q(x)=Q_n(x;-3n,n-1,3n)` obeys

\[
A(x)Q(x+1)-[A(x)+C(x)]Q(x)+C(x)Q(x-1)+n^2Q(x)=0.
\]

At the required diagonal point `x=n`, this becomes the exact local relation

\[
\boxed{
2(2n-1)Q(n+1)+2Q(n)-3nQ(n-1)=0.
}
\]

Thus the remaining cancellation is no longer an unnamed truncated hypergeometric sum: it is a single diagonal readout of a standard rank-two discrete Hahn system.

## 6. Why standard Hahn orthogonality does not already close the task

The usual real positive-weight Hahn zero/interlacing theory is stated under standard admissible parameter regimes. Here

\[
\alpha=-3n=-N,\qquad \beta=n-1,
\]

which lies on/outside the usual positive-orthogonality range. Therefore ordinary positivity, real-zero location, and interlacing cannot simply be invoked to conclude `Q_n(n) != 0 (mod p)`.

The audited standard Hahn references supply the named polynomial, Rodrigues structure, and second-order operator, but do not by themselves supply the required arithmetic nonvanishing theorem at this singular moving-parameter diagonal.

Accordingly the exact unresolved residue is now

\[
\boxed{
Q_n(n;-3n,n-1,3n)\not\equiv0\pmod{6n-1}
}
\]

for

\[
3\mid n,\qquad 6n-1,\ 4n-1,\ 4n+1\text{ prime}.
\]

That is the strictly smaller named invariant required by the taskbook's exact-reduction return clause.

## 7. Exact regression and falsification evidence

The frozen checker independently evaluates the Hahn form, the original fixed rational kernel, and the Franel recurrence modulo every prime boundary `p=6n-1<50000`.

It verifies:

- exact rational Hahn/binomial identity for `1 <= n <= 12` as a deterministic symbolic regression;
- `Hahn diagonal == fixed rational kernel (mod p)` on every scanned prime boundary;
- `F_(2n) == unit * Hahn diagonal (mod p)` on every scanned prime boundary;
- total prime boundaries `p=6n-1<50000`: **2575**;
- residue counts modulo 18: `5 -> 866`, `11 -> 854`, `17 -> 855`;
- zeros in the unrestricted `p=6n-1` scan: exactly `(n,p)=(1,5)` and `(25,149)`;
- admissible P022 twin-boundary candidates with `3|n` and `4n±1` prime: **90**;
- admissible Hahn zeros among those 90: **0**.

The `p=149,n=25` zero is the parent control counterexample `149 | F_50`, now recovered exactly as a Hahn-diagonal zero. It lies outside the P022 admissible `3|n` sector.

These finite results are **regression/falsification only**. They are not an all-parameter proof.

Frozen artifacts:

- `scripts/check_p022_franel_first_reentry_fixed_kernel_nonvanishing.py`;
- `research_artifacts/P022_FRANEL_FIRST_REENTRY_FIXED_KERNEL_NONVANISHING/regression_p_lt_50000.json`;
- this return.

## 8. P022 consequence and next research unit

The q=3r-1 boundary is **not** declared closed. The contribution of this execution is the exact equivalence

\[
\boxed{
q\mid F_{6m}
\iff
Q_{3m}(3m;-9m,3m-1,9m)\equiv0\pmod q,
\qquad q=18m-1.
}
\]

The highest-value successor, if Driver accepts this exact reduction, is no longer a larger finite census. It is one of:

1. prove the specialized moving-parameter Hahn diagonal cannot vanish in the `n=0 (mod 3)` twin-prime sector;
2. obtain a finite-field/Jacobi-sum or Cartier realization of this Hahn diagonal and prove its Frobenius readout nonzero;
3. produce an admissible Hahn-diagonal zero and classify its arithmetic mechanism.

A successor should treat the second-order Hahn operator and the exact Franel-unit bridge as the starting surface.

## 9. Provenance and prior-art boundary

Consumed project input: accepted parent P022 arithmetic-core exact reduction `RR-8323CFDCB99F7832F51F`.

Classical external structures used only for identification/operator semantics: NIST DLMF §§18.19, 18.20, 18.22 (Hahn polynomials, orthogonality regime, and difference equation). No novelty claim is made for Hahn theory.

Parallel-source disclosure: after the registered CLAIM, Draft PR #741 was inspected. It contains an independent nonterminal P022 double-horizon / conductor-18 three-section route. That branch was **not** used to derive the Hahn identification or the Franel-to-Hahn unit equivalence here, and it likewise does not claim all-m nonvanishing.

No all-parameter Hahn nonvanishing theorem is claimed in this return.
