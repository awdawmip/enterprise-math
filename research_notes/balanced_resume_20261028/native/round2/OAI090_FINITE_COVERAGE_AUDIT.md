# OAI7-090: finite certificate coverage and premise audit

Researcher: `EM-NATIVE-A8C19E`; activity: `RA-BALANCE-NATIVE-20261028-A8C19E`.
Date: 2026-10-28. Status: bounded source audit; formal task remains unmodified.

## Result and evidence boundary

The fixed checker implements all five families of finite inequalities in
`lem:finite-certificate`, with the matrix and polynomial correspondence given
below. Static parsing identifies 11 assertion sites, 30 `lt` call sites, 4
`near` call sites, and 6 square-root call sites. These are syntactic counts,
not observed invocation counts. The 659 Bernstein row minima are the structural
count `27*21 + 4*23` from the loops and paper, not a new execution trace.

The audit independently rederives several premises that are not established
merely by passing numerical assertions: all square-root domains, positivity of
the four Fourier-wave decay rates, the continuous-frequency jet-envelope
monotonicity, parameter-polytope membership and its row-minimum formula. No
finite-code/paper mismatch was found in this bounded correspondence check.
These are checks of existing source mathematics, not newly discovered theorems.
The infinite correction, all-radius signs, and universal energy result have
not received a complete independent proof review here.

There is a process exception. The original checker was run before obtaining
the formal task's claim/runtime binding. Its unchanged receipt records exit
0 and empty stdout/stderr; it is **UNBOUND_EXECUTION_EVIDENCE**. A direct RA
registration does not authorize an existing formal task's core run. The
separate `NO_RETROACTIVE_AUTHORIZATION.json` records the exception, immediate
disclosure, and stop on repeat/instrumented runs. No canonical RR, task
completion, formal acceptance, or retrospective authorization is asserted.
All work after that stop is static reading, parsing and mathematical analysis.

## Frozen inputs and task overlap

External repository: `openai/math`, commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`, directory
`preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026`.

| File | Exact Git blob |
|---|---|
| `verification/check_certificate.py` | `23768a5c2d88e100399bb5c4347447e86a7160cb` |
| `verification/README.md` | `e2b9d904c74538450cea628476bcd6c772776c23` |
| `build/main.tex` | `dad316cc2ad861a7482d79b46b6f840ed83d2a5e` |

SHA256, byte lengths and exact-source reconstruction details are in
`ORIGINAL_SOURCE_PINS.json`. Source files used for analysis were byte-checked
against their Git blobs. Reading-cache files under `source/090_*` are not
the byte-exact originals and are not evidence substitutes.

The existing formal task is `RS-OAI7-090-A-20261007-6F2A81`, publication
`TP2-79BD2127769C593E5315`. At EM commit
`66f3b23d112fba1dfb555576a91e2fac20746251`, the publication blob is
`ec10af59db61bc9ec286d064f6c161723aed3bfc` and taskbook blob is
`a5638eb5b100dc86e9fc3aa98cec2cf719870271`. Both explicitly include the
unchanged checker run in the intended task. Neither contains `NO_INVOKE`;
neither establishes a current claim/runtime grant. Definition fields
`ACTIVE`, `claimable: true`, and `taskbook/unassigned` are not a live owner
inventory. Current formal owner is **UNKNOWN**.

The old OAI7 source bundle and monthly catalogue were read first. A bounded
GitHub code search for `oai7` returned no matches despite the known bundle,
so that search is an index false negative. Exact path-scoped commit history
for the old bundle since 2026-10-22 returned no commits. This excludes updates
only under that directory; global novelty since that date is not established.
The present contribution is a supplemental audit of the known 090-A question,
not a new formal task or a new research direction.

The model is external Euclidean two-dimensional space with squared distances,
Gaussian/Fourier analysis and two-body energy. No part supplies a native
plane, native clock, native motion law, or an adapter from the full signed
affine Z6 Cell torsor. Native preservation obligations stay open.

## Matrix and parameter correspondence

In the following table line numbers refer to the pinned checker, while labels
refer to the pinned TeX source. The code's `R` is the residue list; its matrix
`A` inside `approx` is the paper's opposite-side matrix `R`.

| Construction | Code lines | Paper object and dimensions |
|---|---:|---|
| Residues, frequencies, first tail period | 148–155 | 15 residue nodes; `f` has 10 nodes; `L` has 11; `T` is the 15-node period representative `T_0` |
| Laurent coefficients and folded constant | 169–180 | `PJ=P_0,...,P_15`; code `U` is paper `V`, 16 by 1; zero frequency is not doubled |
| Node quantities | 181–189 | `Q_n`, `D_n`, periodic mod 36, appendix formula |
| Finite atomic columns | 191–197 | `M`, 16 by 22, alternating `c_n,d_n` on `L`; `analytic:atomic-c/d` |
| Tail variation columns | 199–203 | `W`, 16 by 2; `analytic:tail-variation` |
| Wave parameters | 205–219 | `rho`, `lambda`, `zeta`, derivative moduli and decay rates; `analytic:fourier-wave` |
| Opposite-side jets | 226–233, 319–321 | `SL`, 20 by 22; `SC`, 20 by 1; `R`, 20 by 20; `R0`, 20 by 3; `eq:finite-jet-map` |
| Fixed and target coefficients | 307–317 | `gamma_i`, 3 by 8; `Y_f`, 20 by 8; first four node targets only |
| Coupled finite solution | 322–330 | two 20 by 20 inverses; `A_i`, 23 by 8, in order `c_0,d_0`, 20 unknowns, `C_i`; `eq:finite-system` |
| Divided Taylor rows | 248–258, 348–354 | 21 by 8 arrays for the degree-20 divided remainder |
| Exceptional rows | 359–375 | substitutions at `z=0,Z`, degree at most 22, padded to 23 by 8 |

Dimension checking is material: `zip` in the small matrix helpers would
silently truncate arbitrary malformed inputs. The audit covers the fixed
shapes above, not a general matrix API. The target columns are `(z,1,zw,w,zu,u,zp,p)`.
The finite polytope instead permits

\[
 e=(z,1,Zw-\Delta,w,a,u,r,p),\quad
 0\le z\le Z,\quad 0\le w\le W_*,\quad 0\le\Delta\le\Delta_*,
 \quad 0\le u\le U_*,\quad0\le a\le Zu,\quad0\le r,p\le P_*.
\]

Constants are `Z=.391`, `W_*=.0061`, `Delta_*=.00018`, `U_*=.00048`,
`P_*=.0000003`, `h=.34`, `H=.54`, `B=4/3`, `b=sqrt(3)/2`.
The fixed coefficients are `(c_0,d_0,C_1)=(.44,0,-.006)` and
`(c_0,d_0,C_2)=(.44,0,.006)`.

## Full finite-inequality correspondence

`lt(a,b)` at line 136 asserts `upper(a)<lower(b)`. Grouped `lt` calls below
account for all 30 syntactic call sites, including the `near` helper.
Machine-readable coverage is in `OAI090_PROOF_COVERAGE.json`.

| Code lines | Exact finite obligation |
|---|---|
| 128–129 | Each diagonal-order pivot of both 20 by 20 systems has absolute value strictly between .12 and 1.74 |
| 146–147 | Machin/alternating-series enclosure lies inside the declared width-1e-50 interval for pi |
| 270–272 | Gaussian `z` upper bound, bounds for exp(-2/Z), exp(-3/Z), exp(-6/Z), and delta's critical value below .00015 |
| 273–274, 282 | .157 < Q_n < 40; abs(D_n) < 2.83; min(Q_16,Q_19,Q_21) > 16 |
| 281 | 15 midpoint lower bounds, in ordered residue gaps, as item 2 of `lem:finite-certificate` |
| 283–284, 286–288 | norm(W)<119 and jet expressions <335, 2.3e-8, 1.27e-7, 7e-15, with the exact `(N,S,k,v)` assignments in lemma item 3 |
| 290, 294 | Repetition expression <2.5e-10; omitted finite target <8.1e-8 and tail target <9.2e-29 |
| 300–302 | Three raw curvature expressions at s=0,1,2,14.5,23 equal the stated table's recipe and are bounded by its entries |
| 305 | Taylor envelope <.00161 for m=1, <.0000075 for the other six nodes, for both signed displacements |
| 328 | Norms of `(I-R)^-1` and `(I+R)^-1` below 16.16 and 3.89 respectively |
| 357, 381 | Side-two on all 14 signed half-cells and side-one on 13: 27 degree-20 Bernstein tests |
| 375 | Four exceptional polynomials at m=y=1, degree at most 22, lower bounds .046,.056,.024,.027 |
| 385 | Supremum coefficient norms over the entire parameter polytope below 2.58 and 2.80 |
| 138, 377, 386, 388 | `near` comparisons: endpoint row, Q_1/D_1, and selected matrix entries; these are auxiliary diagnostics |

The side-one corrections are exactly `Q_1/(2Z)-T_1` at `(m,y)=(1,-1)`
and `.8 Q_1 w-T_1` at `m=3`. Elsewhere the ordinary polynomial is `-T_1`.
The exceptional branch omits the right half-cell's ordinary side-one test and
uses the paper's four combinations of `A=-T_1|z=0`, `D=-T_1|z=Z`,
`B_0=v^2`, `B_1=v^2+2Zv`, `B_2=v^2+4Zv+6Z^2`.
This explains the 27 ordinary tests; it is not 28 plus four extras.

## Static mathematical premises checked independently

### 1. Arithmetic contracts and square-root domains

The fixed-grid operations enclose exact sums/products by integer endpoint
rounding. Reciprocal endpoints reverse on either component of the nonzero
real line; the sign test at line 30 is sufficient. Complex multiplication
is rectangular interval arithmetic. Repeated occurrences may widen intervals
but do not invalidate enclosure. `imin` and `imax` take the corresponding
minimum/maximum of lower and upper endpoints, enclosing the exact extremum.

Assertions are at lines 8,30,41,45,55,61,99,118,136,161,242. Line 41 only
checks a nonnegative upper endpoint. The exact argument of a clipped square
root must also be known nonnegative. All six source call families satisfy this:

* line 85: the exact argument is a sum of two squares (complex modulus);
* line 148: the exact argument is 3;
* line 216: `t^2+(k-h)^2` is a sum of squares;
* line 217: `X=B/(k^2+t^2)>0`, since B>0 and k is h or H;
* line 218: `v^2+(B-2kv)X>0`, since
  `B-2kv >= 4/3-2(27/50)^2 = 2813/3750 > 0`;
* line 269: `1+2Z>0`.

These are proofs about the fixed callers; they do not turn clipped `sqrt`
into a valid function on arbitrary intervals with negative exact inputs.

For `expo`, the line-99 test enforces reduced modulus at most one. The omitted
Taylor tail after degree 60 is at most
`(1/61!)/(1-1/62)<2/61!<10^-60`; adding that radius to each used real
component then squaring ten times encloses the original exponential. The
scale `1024=2^10` is exact. The phase reduction modulo 36 is justified by
the exact exponent `i*pi*j/18`; the pi enclosure and periodicity are separate
ingredients. The Machin identity and alternating-series tail bound are
mathematical premises of the pi test, not conclusions of the assertion alone.

For elimination, an induction tracks the exact augmented matrix. After each
pivot, the exact previous pivot columns are unit columns. Thus leaving those
columns untouched while setting the new pivot to one and its other column
entries to zero is legitimate; the remaining interval row operations retain
inclusion. Nonzero pivot intervals yield existence of the inverse.

### 2. Actual Gaussian data lie in the tested polytope

For alpha>=1, `z=1/(pi*(alpha/b-h))` is positive and decreases in alpha.
The scalar check at line 270 therefore controls its full range. For j>0,
`exp(-j/z)` increases on z>0, so the three endpoint checks at line 271
control w,u,p. To bound `Delta=(Z-z)exp(-2/z)`, differentiate:

\[
 \frac{d}{dz}\bigl((Z-z)e^{-2/z}\bigr)
 =e^{-2/z}\frac{2Z-2z-z^2}{z^2}.
\]

The numerator decreases strictly from 2Z to a negative value on [0,Z].
Its sole positive root is `z_*=sqrt(1+2Z)-1`, which lies in (0,Z).
Both endpoint values are zero (using the right limit at zero), so the
line-272 evaluation bounds the global maximum. Finally `zu<=Zu` and
`zp<=p` since 0<z<=Z<1. Thus all original Gaussian vectors are included;
the larger polytope deliberately contains non-Gaussian vectors as well.

For the coefficient-norm bound, the first two columns form `a*z+b`.
Its l1 norm is convex, hence at most its endpoint maximum on [0,Z].
The remaining coordinates have absolute bounds
`(.0024,W_*,ZU_*,U_*,P_*,P_*)`, since
`max(Z W_*,Delta_*)=.0023851<.0024`. This proves the bound recipe in
`approxnorm`; it is not a vertex search over only the physical curve.

### 3. Decay and continuous-frequency jet envelopes

This is a local proof audit of the existing analytic bridge in
`analytic:fourier-wave` and `analytic:jet-envelope`, not a new theorem.
Let `t in [0,5/6]`, `k,v in {17/50,27/50}` and
`X=(4/3)/(k^2+t^2)`. Then `kX-v` is minimized at t=5/6. For
`(k,v)=(h,h),(h,H),(H,h),(H,H)`, its endpoint values are exactly

\[
 \frac{100079}{455650},\quad \frac{8949}{455650},\quad
 \frac{216419}{554650},\quad \frac{105489}{554650}.
\]

All are positive, so the geometric tail denominator `1-exp(-36E_b)` is
positive for `E_b=pi*(kX-v)`. For fixed residue node n>=1 and Q_n>0, define

\[
 \psi(X)=\frac{(1+|D_n|+\pi\sqrt{v^2+C X})\sqrt X}{Q_n}
             e^{-\pi(kX-v)n},\qquad C=4/3-2kv>0.
\]

Writing `a=1+|D_n|>0` gives

\[
 \frac{d}{dX}\log\bigl((a+\pi\sqrt{v^2+CX})\sqrt X\bigr)
 =\frac1{2X}+\frac{\pi C}
 {2\sqrt{v^2+CX}(a+\pi\sqrt{v^2+CX})}
 \le\frac1{2X}+\frac{C}{2(v^2+CX)}\le\frac1X.
\]

For k=h and H respectively,

\[
 \frac1X\le\frac{k^2+25/36}{4/3}
 =\frac{9113}{15000},\ \frac{11093}{15000};\qquad
 3k-\frac{k^2+25/36}{4/3}
 =\frac{6187}{15000},\ \frac{13207}{15000}>0.
\]

Since pi>3 and n>=1, `d(log psi)/dX < 0`. As X decreases with t,
psi increases with t. Therefore each right endpoint t_j dominates the
whole interval [t_(j-1),t_j], and multiplying by the interval variation
bound W_j is valid. Together with the *assumed exact spectral variation
identity* for W, this supplies the continuous-frequency interpretation of
the finite envelope sum. The checker itself evaluates endpoints and does
not carry this derivative proof.

This proves one required analytic bridge. It does not prove all spectral
identities, Schwartz convergence, the infinite Schur system or global signs.

### 4. Exact row minimum and uniform Bernstein bounds

For an exact scalar row `(b,c,l,d,k,j,n,r)`, substitute the polytope
coordinates to obtain

\[
 c+bz+(d+Zl)w-l\Delta+ka+ju+nr_0+rp.
\]

The box coordinates minimize independently. The `(a,u)` factor is a triangle
with vertices `(0,0),(0,U_*),(ZU_*,U_*)`, so its minimum is
`U_* min(0,j,j+Zk)`. Consequently the complete exact minimum is

\[
 c+Z\min(b,0)+W_*\min(d+Zl,0)+\Delta_*\min(-l,0)
 +U_*\min(0,j,j+Zk)+P_*[\min(n,0)+\min(r,0)].
\]

This is precisely code `vmin`, after renaming row variables. The box
variable `r_0` in the derivation is the seventh data coordinate; row
coefficient `r` is distinct. Applying interval arithmetic to this formula
encloses the minimum even when coefficients are interval-enclosed and
dependent; the lower bound remains conservative.

For degree N, `bern` uses
`b_i=sum_{r<=i} binom(i,r)/binom(N,r) t_r`. The extra r>i terms in its
rectangular formula are zero. The Bernstein basis functions are nonnegative
and sum to one on [0,1], so a common lower bound for every row acting on
every e in the polytope bounds the full polynomial for every `(tau,e)`.
The result is uniform, not a mesh test. Degree padding to N=22 in the
exceptional branch is correct, including its first polynomial of smaller
actual degree.

## Obligations not discharged by the checker or this bounded audit

| Interface | Further mathematical obligation |
|---|---|
| Folded atoms and W to actual functions | Spectral identities, removable values, total-variation estimates and Fourier normalization, including `analytic:atomic-c/d`, `analytic:tail-c/d` and Schwartz convergence |
| Finite envelopes to full operator | All l1 column bounds and repeated-pole signs, assembly of `analytic:block-bounds`, convergence and inverse of `analytic:schur-tail` |
| Finite interpolant to exact one | Exact interpolation equations, omitted target restoration, rational error bounds and half-sum transfer to individual sides |
| Raw curvature table to uniform control | Frequency-extremum proof in `lem:curvature-envelopes`; the five listed raw evaluations alone do not prove interval-wide maxima |
| Taylor polynomials to signs | Deleted-jet comparison, exceptional Gaussian divided difference, sine-product barriers and all remaining radial ranges in `prop:global-signs` |
| Sharp Gaussian functions to energy | Poisson/linear-programming comparison, limit passages and completely monotone potential transfer in `energy:section` |
| External theorem to native research | A separately defined, preservation-checked native carrier/observable bridge; none is supplied here |

Some of these proofs are present in the source paper. Their presence is not
being reported as a discovered defect or as absence of a proof. They are
outside the support of a finite run and outside this bounded independent
review. The present local rederivation closes only the explicitly stated
premises in the previous section.

## Reuse, frontier and execution gate

Reusable artifact: a pinned code/paper coverage map and a read-only AST
inventory tool. New theorem count: **0**. New mathematical tool-family count:
**0**. Original task acceptance: **UNKNOWN / not requested here**.

A minimal follow-up independent proof obligation is the continuous curvature
extremum in `lem:curvature-envelopes`: prove that its selected frequencies
bound each relevant whole frequency interval and carry the raw numerical
table to the stated radial ranges. It must preserve both damping choices
and the distinction between finite atoms and continuous tail densities.
This follow-up should be assigned through the parent controller; it is not
silently claimed here. Any additional original-task core checker run must
first pass actual current claim/runtime gates. Quota exhaustion is not a
substitute authorization. The current round stops after this bounded audit
and independent review, preserving fair rotation to the other research lines.
