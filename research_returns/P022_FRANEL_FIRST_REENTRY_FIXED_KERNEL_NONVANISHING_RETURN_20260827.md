# P022 Franel First-Reentry Fixed-Kernel Nonvanishing Return — 2026-08-27

Task: `RS-P022-FRANEL-FIRST-REENTRY-KERNEL-NONVANISHING`
Publication: `TP2-18D80E295208AC91EB70`
Researcher: `EM-P022KERN-4E4834`
Claim: `chatgpt-p022kern-20260827-2141-4e4834`

## Verdict

`PASS / EXACT_REDUCTION_TERMINAL_ALLOWED_BY_TASKBOOK`

This execution does not prove all-parameter nonvanishing and does not produce an admissible zero. It reaches the taskbook's explicit stopping condition by reducing the residual fixed rational hypergeometric cancellation to one named classical Hahn-polynomial diagonal value with a canonical second-order discrete operator.

No Working Truth or canonical promotion is claimed. Driver review is required.

## 1. Exact Hahn reduction

Put
\[
n=3m,\qquad p=6n-1=18m-1.
\]
The admissible P022 constellation is
\[
3\mid n,\qquad p,\ 4n-1,\ 4n+1\ \text{prime}.
\]

The accepted parent return leaves
\[
R_m(p)=\sum_{j=0}^{n}
\frac{(-1/6)_j^3}{(1/2)_j(-1/2)_j\,j!}\pmod p.
\]

Since \(6n\equiv1\pmod p\),
\[
-\frac16\equiv-n,\qquad
\frac12\equiv1-3n,\qquad
-\frac12\equiv-3n.
\]
All denominator factors are \(p\)-units for \(0\le j\le n\). Hence
\[
R_m(p)\equiv
{}_3F_2\!\left[
\begin{matrix}-n,-n,-n\\1-3n,-3n\end{matrix};1
\right]\pmod p.
\]

In the standard Hahn normalization
\[
Q_k(x;\alpha,\beta,N)
={}_3F_2\!\left[
\begin{matrix}-k,k+\alpha+\beta+1,-x\\
\alpha+1,-N
\end{matrix};1
\right],
\]
take
\[
k=x=n,\qquad \alpha=-3n,\qquad \beta=n-1,\qquad N=3n.
\]
Then \(k+\alpha+\beta+1=-n\), so the exact rational invariant
\[
\boxed{\mathcal H_n:=Q_n(n;-3n,n-1,3n)}
\]
satisfies
\[
\boxed{R_m(p)\equiv\mathcal H_n\pmod p.}
\]

Equivalently,
\[
\boxed{
\mathcal H_n=
\sum_{j=0}^{n}
(-1)^j
\frac{\binom nj^3}
{\binom{3n-1}{j}\binom{3n}{j}}
}.
\]

This is direct parameter equality, not an inference from finite data.

## 2. Exact Franel reconnection

The parent result gives
\[
2^{-2n}F_{2n}\equiv
{}_3F_2\!\left[
\begin{matrix}-n,2n,2n+1\\1,1\end{matrix};1
\right]\pmod p.
\]

Exact reversal of the terminating series yields
\[
{}_3F_2\!\left[
\begin{matrix}-n,2n,2n+1\\1,1\end{matrix};1
\right]
=
(-1)^n\frac{(2n)_n(2n+1)_n}{(n!)^2}\,\mathcal H_n.
\]
The prefactor is a \(p\)-unit because all of its factorial/Pochhammer factors lie below \(p=6n-1\). Therefore
\[
\boxed{
p\mid F_{2n}
\iff
\mathcal H_n\equiv0\pmod p
}.
\]

For \(n=3m\), this is precisely the P022 first-reentry obstruction
\[
\boxed{
q\mid F_{6m}
\iff
Q_{3m}(3m;-9m,3m-1,9m)\equiv0\pmod q,\qquad q=18m-1.
}
\]

## 3. Canonical second-order Hahn operator

Classical Hahn polynomials satisfy a second-order difference equation. In this specialization,
\[
A(x)=(x-3n+1)(x-3n),\qquad C(x)=x(x-4n),
\]
and \(Q(x)=Q_n(x;-3n,n-1,3n)\) obeys
\[
A(x)Q(x+1)-[A(x)+C(x)]Q(x)+C(x)Q(x-1)+n^2Q(x)=0.
\]
At the target diagonal point \(x=n\),
\[
\boxed{
2(2n-1)Q(n+1)+2Q(n)-3nQ(n-1)=0.
}
\]

Thus the residual is no longer an unnamed truncated \( {}_3F_2 \): it is one diagonal readout of a standard rank-two discrete Hahn system.

The usual positive-weight Hahn orthogonality/zero-interlacing theorems do not directly close this case because
\[
\alpha=-3n=-N,\qquad \beta=n-1
\]
lies on/outside their standard positive-orthogonality parameter range. The audited Hahn references therefore identify the family and operator but do not supply the required arithmetic nonvanishing theorem.

The exact remaining residue is
\[
\boxed{
Q_n(n;-3n,n-1,3n)\not\equiv0\pmod{6n-1}
}
\]
under
\[
3\mid n,\qquad 6n-1,\ 4n-1,\ 4n+1\ \text{prime}.
\]

## 4. Regression / falsification evidence only

The frozen checker evaluates the original fixed rational kernel, the Hahn diagonal, and the Franel recurrence modulo every prime boundary \(p=6n-1<50000\).

Results:

- prime boundaries scanned: **2575**;
- exact zeros in the unrestricted scan: \((n,p)=(1,5)\) and \((25,149)\);
- the \(p=149,n=25\) zero recovers the parent control counterexample \(149\mid F_{50}\);
- admissible P022 candidates with \(3\mid n\) and \(4n\pm1\) prime: **90**;
- admissible Hahn zeros: **0**;
- all scanned points satisfy `Hahn == original R_m (mod p)` and `Franel == p-unit * Hahn (mod p)`.

These computations are regression/falsification only and are not an all-parameter proof.

Artifacts:
- `scripts/check_p022_franel_first_reentry_fixed_kernel_nonvanishing.py`
- `research_artifacts/P022_FRANEL_FIRST_REENTRY_FIXED_KERNEL_NONVANISHING/regression_p_lt_50000.json`

## 5. Exact next unit

The q=3r-1 P022 boundary is not declared closed. If Driver accepts this reduction, the next task should attack the specialized moving-parameter Hahn diagonal itself, preferably by finite-field/Jacobi-sum, Cartier/Frobenius, or discrete-operator methods; enlarging the finite cutoff is explicitly not a substitute.

Consumed project input: accepted parent result `RR-8323CFDCB99F7832F51F`.

Classical identification/operator references: NIST DLMF §§18.19, 18.20, 18.22. No novelty claim is made for Hahn theory.

Parallel-source disclosure: Draft PR #741 was inspected after the registered CLAIM. Its independent double-horizon/conductor-18 route was not used to derive the Hahn identity or the Franel-to-Hahn unit equivalence here.

No all-parameter nonvanishing theorem is claimed.
