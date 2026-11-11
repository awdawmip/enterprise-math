# PREFIX-712-R6 — Sparse dyadic refinement of exact Gamma-clock exclusion certificates

Date: 2026-11-12 (Asia/Shanghai).
Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d (immutable scientific input).
Parent: PREFIX-675, frozen two-stream auxiliary BRC observer global optimization.
Direct predecessor: PREFIX-711, with PREFIX-710 corrected Gamma-completion-clock kernel.
Evidence: AUTHOR_RECOMPUTED / EXACT_INTEGER_GAMMA_KERNEL / UNREVIEWED / NOT_ADMITTED.
This two-coordinate statistical observer is an external auxiliary representation, not a native X6 three-dimensional slice.

## Theorem 712.1 — q>=2

Let N_p be the pinned 189-row stopping count, let the completed independent clocks satisfy T_p | N_p=k ~ Gamma(k,1), and let Y(p,z)=max(T_p,T_z). For x=(p,z) in D=[0,1/2]^2 define mu(x)=E[Y(x)], W(x)=Var(Y(x)), and V_q(x)=q²W(x)-q mu(x). Fix the exact competitor e=(0,3/20).

Partition D into G×G ordered closed cells, G=192, and retain all 28,724 coarse cells already certified by PREFIX-711 for every real q>=2. Split each of the 8,140 *ordered* uncertified coarse cells into four congruent cells. For each new cell [a,h], let U=E[Y(h)²]-mu(a)² and L(t)=W(e)-U-t(mu(e)-mu(a)). Accept that new cell precisely when both strict rational inequalities L(0)>0 and L(1/2)>0 hold. No other cell is accepted.

**Exact exhaustive result:** among the 32,560 refined ordered subcells from previously uncertified coarse cells, 22,272 pass both strict comparisons. Together with 4×28,724 inherited coarse certified subcells, precisely

    4×28724+22272 = 137168

out of 4×192² = 147456 disjoint fine cells are covered. Hence the union of these certified cells has exact relative area

    137168/147456 = 8573/9216 = 93.0230034722...%

of D, and absolute area 8573/36864. For every x in this union and every real q>=2, V_q(e)>V_q(x).

## Theorem 712.2 — 12<=q<=24

Starting from the 28,871 PREFIX-711 coarse cells certified for 12<=q<=24, subdivide only the remaining 7,993 ordered coarse cells. Accept fine cells when both L(1/24)>0 and L(1/12)>0.

The exact checker accepts 21,914 of 31,972 previously uncertified fine subcells. Therefore the covered fine-cell count is

    4×28871+21914 = 137398,

with relative area

    137398/147456 = 68699/73728 = 93.1789822049...%

and absolute area 68699/294912. The associated V_q comparison is strict for every real q in [12,24].

The q>=2 certified union is included in the [12,24] union, as verified cellwise by the analytic endpoint inclusion; the two accepted counts differ by 230 fine cells.

## Proof of the continuous-domain inference

The earlier certified survivor-tail order makes the one-clock completion-time survival, the mean mu(x), and the nonnegative raw second moment E[Y(x)²] coordinatewise nondecreasing. Thus in every rectangular cell [a,h],

    mu(x)>=mu(a)>=0,    E[Y(x)²]<=E[Y(h)²].

Consequently W(x)<=E[Y(h)²]-mu(a)²=U. For t=1/q>=0,

    [W(e)-t mu(e)]-[W(x)-t mu(x)]
        >= W(e)-U-t[mu(e)-mu(a)] = L(t).

As L is affine in t, the two strict endpoint tests on either closed t interval imply positivity at every intermediate real t. Multiplication by q²>0 proves both theorems. An inherited coarse cell retains its earlier continuous inequality on every subset; the finer partition need not recompute its proof.

Disjoint area counting uses cell interiors, so shared boundaries have zero area. The strict inequalities hold on the whole of each accepted closed cell. The mixed adaptive partition is an exact finite covering certificate, not a sampling estimate.

## Exact finite verifier and regression

The attached Python file reconstructs all 189 stopping-count rows under the frozen width predicate using integer arithmetic and checks 9,529 nonzero count cells. It evaluates the correct independent Gamma maximum kernel:

    c_nm = binom(n+m,n) / 2^(n+m+1),
    mu(p,z)=sum_n s_n(p)+sum_m s_m(z)-sum_n,m c_nm s_n(p)s_m(z),
    E[Y²](p,z)=2sum_n(n+1)s_n(p)+2sum_m(m+1)s_m(z)
                  -sum_n,m (n+m+1)c_nm s_n(p)s_m(z).

All grid vertices share the common exact denominator R=[(768^188)^2]×2^377; strict comparisons reduce to integer cross-products. Gamma(max) is not replaced by a maximum of stopping counts.

The checker first reproduces PREFIX-710 (26,445), PREFIX-711 all-q (28,724), and PREFIX-711 q12..24 (28,871) at G=192. It then tests only uncertified coarse cells' four children. Its local execution returned ALL_CHECKS_PASS PREFIX712-R6. The last result file contains exact counts and fractions. No independent mathematical review or remote CI execution was performed.

## Research value and next unit

The q>=2 admissible search region now occupies at most 10,288/147,456 = 6.9769965278...% of D; for 12<=q<=24 it occupies at most 10,058/147,456 = 6.8210177951...%. These are *remaining uncertified regions*, not established optimizer-containing locations.

Next select the 10,288 / 10,058 fine cells still uncertified, refine their exact Gamma moments or apply local derivative/Bernstein bounds. Compare the surviving cells with exact interior stationary points and boundary candidates for the parent global optimizer problem. Reuse the previous source pins; do not repeat certified coarse/fine cells.
