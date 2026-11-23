# PREFIX-1042 — Second-moment Bernstein positivity cones at reduced explicit orders

Date: 2026-11-24 (Asia/Shanghai).
Parent: PREFIX-1041.
Classification: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_IMPLICATION_CHECKED / NOT_INDEPENDENTLY_REVIEWED.
Scope: auxiliary six-phase scalar signed-density theorem; no new typed BRC evolution, classical reference experiment, or native residual attribution.

## Frozen scientific scope and provenance

P000 V5 remains frozen at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Preserve native X6 six axes, Cell–terminal-port–grade joint observer, sign, branch identity, multiplicity, provenance, and the Stage46 candidate W=J12-6I12, incoming -e1, blocked bidirectional Link {0,e1}, one negative outgoing step. The scalar reduction has not been proved observer-faithful for native BRC. Mark NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION.

The conditional inputs used here are:
- PREFIX-1033, source commit fec5c00006e3693121ee18f6d0be661506e06410: g continuous, exact Beta representation of normalized Hausdorff differences.
- PREFIX-1037, source commit 928461a6f8c675b9a7bd38586cf47db9d25835e9: g(4)>6371/60 and g(16)>919/90, within the original scalar integral assumptions.
- PREFIX-1040, source commit 58e35fe4a131729405107d736198cf555d53cc8a: local bounds |g(y)-g(4)|<104400 sqrt(|y-4|) and |g(y)-g(16)|<291700 sqrt(|y-16|), respectively for |y-c|<=1/10000.
- PREFIX-1041, source commit 7bcaa3dc08c01119b661f0f9ecc31ca7fa7ba806: global |g(y)|<=611856 and the original two explicit cones. The present argument preserves exactly the original cone widths.

## Theorem: same-width cones at 93.312-fold smaller order thresholds

For integers m,k>=0, put N=m+k, n=N+1, j=m+1 and s=j/n, and adopt the frozen normalization

\[
 D_{m,k}=\frac{(N+1)\binom{N}{m}}{36^{N+1}} E_{m,k}
       =\mathbb E[g(36T)],\quad T\sim\mathrm{Beta}(j,n-j+1).
\]

Under the inherited four scalar results above:

(A) If n>=500000000000000 and |s-1/9|<=1/72000000, then
\[
\boxed{D_{m,k}>\frac{49}{12}>4,\quad E_{m,k}>0.}
\]

(B) If n>=500000000000000000000 and |s-4/9|<=1/72000000000, then
\[
\boxed{D_{m,k}>\frac{10}{9}>1,\quad E_{m,k}>0.}
\]

Both cones include integer pairs for every n above the corresponding threshold. They use exactly the same positive ratio widths as PREFIX-1041, but the sufficient n thresholds are smaller by the exact factor 11664/125 = 93.312.

## Proof

Let c be 4 or 16, a be 1/2000000 or 1/2000000000 respectively, epsilon=1/10000, and U=611856. The cone hypothesis is precisely |36s-c|<=a.

1. The Beta mean is mu=j/(n+1); its variance is j(n-j+1)/((n+1)^2(n+2))<=1/(4(n+2)). Since |mu-s|<=1/n,
\[
\mathbb E[(36T-c)^2]
=1296\operatorname{Var}(T)+(36\mu-c)^2
\le \frac{324}{n}+\left(a+\frac{36}{n}\right)^2=:Q_c(n).
\]
By Jensen (or Lyapunov's moment inequality),
\[
\mathbb E\sqrt{|36T-c|}\le Q_c(n)^{1/4}.
\]

2. Define A={|36T-c|<=epsilon} and p=Pr(A^c). In both cones a<=epsilon/2. Thus A^c implies |T-s|>epsilon/72. The exact Beta order-statistic/binomial-tail identity and Hoeffding inequality give
\[
 p\le2\exp\left(-\frac{n\epsilon^2}{2592}\right).
\]
For n>=500000000000000, n epsilon^2/2592>30; using e>2 gives p<2^-29. Consequently
\[
 2Up<\frac{611856}{2^{28}}<\frac1{10}.
\]

3. The inherited local modulus on A gives g(36T)>g(c)-L_c sqrt(|36T-c|), while on A^c the global bound gives g(36T)>=-U. Because g(c)<=U,
\[
 D_{m,k}\ge g(c)-L_c\mathbb E\sqrt{|36T-c|}-2Up
 >g(c)-L_c Q_c(n)^{1/4}-\frac1{10}.
\]
This truncates the local estimate rather than applying a local Holder condition outside its domain.

4. Q_c(n) is decreasing for positive n. At the two minimum orders, direct integer/Fraction cross-multiplication verifies the exact strict rational inequalities
\[
 104400^4 Q_4(5\cdot10^{14})<102^4,\qquad
 291700^4 Q_{16}(5\cdot10^{20})<9^4.
\]
Hence D_{m,k}>6371/60-102-1/10=49/12 in (A) and
D_{m,k}>919/90-9-1/10=10/9 in (B).
The normalizing factor between D and E is positive.

5. For each n the integer j nearest to nc/36 satisfies |s-c/36|<=1/(2n), which lies within the declared cone for all stated n. These j are strictly between 1 and n. Thus each cone is nonempty at every eligible integer order.

The PREFIX-1041 sufficient order was n_old=9(72/delta)^2 with delta=10^-6 or 10^-9; its ratio half-width delta/72 is unchanged. Exact division by the new threshold gives n_old/n_new=11664/125 in both cases. QED, conditional on the inherited scalar inputs.

## Validation and scientific interpretation

Companion file PREFIX1042_R6_BETA_SECOND_MOMENT_EXACT_CHECK.py verifies the two strict fourth-power comparisons, the two positive margins, the order-to-tail inequalities, identical cone widths and the exact threshold ratio using Python integer/Fraction arithmetic. No Bessel function, pi, external trajectory, or classical physical comparison is evaluated. The new contribution is a Beta second-moment improvement over PREFIX-1041's global worst-case tail strategy: it draws value from already certified critical-point height rather than treating all mass outside an extremely narrow certified band as entirely adversarial.

The statement remains a conditional auxiliary scalar theorem and NOT_REVIEWED. It does not certify g(y)>=0 on [0,36], a native X6 observable mapping, an original BRC propagation, or the mother question B_fix,odd(32) in {19,20}. Earlier authorship remains historical provenance and this file does not claim a formal Task CLAIM, PROGRESS, Result, Review, or a newly authenticated logical-session identity.

## Useful continuation

Use the already established scalar Picard–Fuchs relation to seek larger certified intervals away from 4 and 16, or a rigorous negative witness. An independent reviewer should test the inherited critical-point certificates and the scalar observer map before native attribution. The present moment argument also admits optimization of the center bands and cutoff epsilon while retaining exact rational checks.
