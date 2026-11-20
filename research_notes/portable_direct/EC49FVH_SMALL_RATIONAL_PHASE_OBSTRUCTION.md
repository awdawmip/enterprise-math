# EC49FVH — no small rational threshold phase at any rational width

Date: 2026-11-21, Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_INTEGER_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.

## Scope and frozen parent

Continues EC49FVG, Draft PR #2880 at immutable scientific commit 08d05adcc95b1d2fc141e519f56c06f7a050f9ec, within the unchanged derived Bernoulli hit-observer scientific pin BRC16943@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. The theorem is algebraic and concerns the exact derived rational model. It does not re-pin P000, claim native X6 physics, or independently verify the upstream FUQ/FUR reduction for composite minimax risk.

For real 0<x<1 put

\[
 u=\frac{4822040484}{8132285009},\qquad
 \gamma=\frac{141024}{1653649},\qquad
 a(x)=\frac{x(640-3x)}{637},\qquad
 b(x)=1-u(1-x)(1+\gamma x).
\]

In the frozen model, \(0<a<b<1\). The strict separation can be checked directly:

\[
 b(x)-a(x)=
 \frac{115(1-x)(18335876195-2489980929x)}{5180265550733}>0.
\]

Set

\[
 R(x)=\frac{1-a(x)}{1-b(x)},\quad
 S(x)=\frac{b(x)(1-a(x))}{a(x)(1-b(x))},\quad
 t(x)=\frac{\log R(x)}{\log S(x)}\in(0,1).
\]

## Theorem — all reduced rational phases of denominator at most 25 excluded

For every \(x\in\mathbb Q\cap(0,1)\) and every coprime \(h,k\) with \(1\le h<k\le25\),

\[
 \boxed{t(x)\ne h/k.}
\]

There are exactly \(\sum_{k=2}^{25}\varphi(k)=199\) reduced fractions in this domain. The theorem quantifies over *all* rational widths, with no width-height bound.

### Algebraic reduction

If \(t=h/k\), then \(R^k=S^h\). Rearrangement gives

\[
 a^h(1-a)^{k-h}=b^h(1-b)^{k-h}.
\]

Write \(f(z)=z^h(1-z)^{k-h}\). Because \(a\ne b\), equality requires the zero of the rational-coefficient polynomial

\[
 Q_{h,k}(x)=\frac{f(a(x))-f(b(x))}{a(x)-b(x)}
 =\sum_{i=h}^{k}(-1)^{i-h}\binom{k-h}{i-h}
   \sum_{j=0}^{i-1}a(x)^{i-1-j}b(x)^j.
\]

This formula is polynomial, not an expression with a variable denominator. Since \(1-a\) and \(1-b\) each have a factor \(1-x\), while \(a-b\) has exactly one, \(Q_{h,k}(x)\) has the removable boundary factor \((x-1)^{k-h-1}\). Remove that factor and clear rational denominators, then divide the integer coefficient content. This yields a primitive integer polynomial \(H_{h,k}(x)\), of degree \(k+h-1\), whose vanishing is necessary for the proposed rational phase at an interior width.

### Modular projective obstruction

Let \(H(X)=c_DX^D+\cdots+c_0\in\mathbb Z[X]\). If a prime \(p\) satisfies \(c_D\not\equiv0\pmod p\) and \(H(r)\not\equiv0\pmod p\) for every \(r\in\mathbb F_p\), then \(H\) has no rational root. Indeed, a reduced rational root \(m/d\) would make

\[
 H^*(m,d)=\sum_{j=0}^D c_jm^jd^{D-j}=0.
\]

If \(p\nmid d\), reduction gives a forbidden finite root. If \(p\mid d\), coprimality gives \(p\nmid m\) and \(H^*(m,d)\equiv c_Dm^D\ne0\pmod p\). This argument covers the point at infinity and all denominator-divisible rational widths.

The attached exact standard-library Python verifier constructs each \(H_{h,k}\) from the displayed identity, synthetically divides the specified boundary factor (checking remainder zero at every division), makes its coefficients primitive integers, and exhaustively checks every point of \(\mathbf P^1(\mathbb F_p)\). It finds an obstruction prime \(p\le53\) for **every one of the 199 coprime pairs**. Local execution returned ALL PASS and emitted a 199-row machine-readable certificate table.

| Certifying prime p | 5 | 11 | 17 | 19 | 31 | 37 | 41 | 43 | 47 | 53 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Number of certified fractions | 1 | 109 | 41 | 12 | 21 | 3 | 3 | 1 | 5 | 3 |

The counts sum to 199. These finite-field checks are complete finite calculations for the exact 199 phase conditions. Since none of the resulting polynomials has a rational root, the theorem follows.

### Independent hand proof for t=1/2

The half-phase has a simpler closed form. \(R^2=S\) is equivalent to \(a(1-a)=b(1-b)\), hence

\[
 (a-b)(1-a-b)=0.
\]

Since \(a\ne b\), the necessary and sufficient condition is \(a+b=1\), which becomes

\[
 237554096781x^2+8014351242260x-3071639788308=0.
\]

At a reduced rational width \(x=m/d\) this homogenizes to an integer quadratic which modulo 5 is

\[
 m^2+2d^2=0\pmod5.
\]

No nonzero projective pair solves it: \(-2\equiv3\pmod5\) is a quadratic nonresidue. Thus no rational width has phase \(1/2\). There is one irrational *real* crossing in the interval, approximately \(x=0.379009538134533\).

The seven-prime coordinate witnesses of EC49FVF/FVG remain valid as observations about lossy valuation projections: even when those coordinates admit the candidate 1/2, the original exact functions have this global extra obstruction.

## Reproduction and evidence limits

Run Python 3 on EC49FVH_SMALL_DENOMINATOR_PHASE_VERIFY.py from any writable directory; it uses only fractions.Fraction and Python integer arithmetic. The script prints all k/h/p/degree certificates and emits EC49FVH_PHASE_CERTIFICATES.csv beside itself. Its full 199-case run completed with CERTIFIED: 199/199 and ALL PASS. The mathematical argument is algebra plus an explicit finite projective check; no numerical approximation enters the obstruction. The single displayed approximate real crossing is illustrative only.

No conclusion is yet established for rational phases of reduced denominator \(k\ge26\). An all-denominator irrationality theorem for every rational width (or an exact rational-phase counterexample) remains open. Independent review, formal result admission and composite-model transfer are separate pending obligations.

## Next discriminating scientific unit

Determine whether the current projective-obstruction mechanism extends uniformly over unbounded k, or construct a rational phase from an exact rational width. A successful uniform argument would eliminate the present finite-denominator cutoff; any failure should retain exact polynomial and prime-local evidence.