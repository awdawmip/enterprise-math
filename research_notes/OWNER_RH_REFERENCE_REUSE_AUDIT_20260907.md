# Independent audit of N8 prime+Cauchy reference reuse

Status: **PASS_WITH_EXPLICIT_PARAMETER_GATES / BOUNDED_REUSE_AUDIT**.
Date: 2026-09-07. Role: `ANCHOR_EXPOSED` internal owner helper; not an official
review, registered Researcher-ID, new tool family, or RH proof.

**Conclusion.** The existing archimedean, prime, and pole routines can supply
the declared cutoff-free N8 reference consumer, with the parameter and
enclosure conditions below. The Cauchy Laplace factor -1/2 and uniform
10240/C_cut^3 tail bound are correct. Reuse must preserve the old/shell
permutation, signed entry errors, and the exact cross-term exclusions.
The old eta=1 positivity certificate is not a certificate for this reference.

This audit read only the current intake, the old script, and the following
two directly related mathematical notes. It did not run the old certificate,
read other RH routes, build a new producer, or edit a frozen file.

| Read-only source | SHA256 |
|---|---|
| `OWNER_RH_FINITE_CERTIFICATE_INTAKE_20260907.md` | `0bde55d47149d04a9c34d049bc9e9473604d16ac554d1f47e6ef2b467dc42b66` |
| `scripts/rh_log3_n8_arb_certificate.py` | `4e337855d8605125ded80c029022fdc950d1b92cf78ce772480a7b99b9dad49b` |
| `RH_LOG3_N8_ARB_POSITIVITY_CERTIFICATE_20260906.md` | `0ab4b8cf31fcf0574848681a93aaff6b33e4d09e657de439db7e953ead260356` |
| `RH_LOG2_LOG3_N8_THRESHOLD_INERTIA_DIAGNOSTIC_20260906.md` | `68f9cac3329ceb74a30017c7275d7c8c169418e25a6e6093911043ef497f6d3b` |

## 1. Fixed carrier and the target being assembled

The source basis is exactly four disjoint-interior intervals, in order
`S-, O-, O+, S+`, with eight Dirichlet sine modes per interval. Its real
orthonormality is an exact mathematical premise, not a floating observation.
Each basis function is zero outside its own interval and has normalization
sqrt(2/ell). Reuse here freezes these intervals, modes, and normalization.

The old/shell partition and full permutation, in zero-based source indices,
are

```text
old O = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
shell S = [0,1,2,3,4,5,6,7,24,25,26,27,28,29,30,31]
permutation = O followed by S
```

This is a permutation of all 32 indices; it does not merge parity, inversion,
or support-branch identities. Let
`M=M_arch+M_prime+M_pole`. The diagonal blocks are the complete restrictions
`A=M[O,O]` and `D=M[S,S]`, including every within-block cross-branch entry.
In particular, pole and regular-arch terms remain inside both A and D.

The complete cross decomposes as

`M[O,S] = B_prime + C + (B_arch-C) + B_pole`.

The reference keeps `B_ref=B_prime+C` and deletes the **entire** regular
archimedean cross `B_arch-C` and the **entire** two-channel pole cross.
It is not merely deleting a high-degree regular Taylor remainder. C acts
on all four old/shell branch pairs, including separated nonadjacent pairs,
not just the two touching boundaries. Substituting the complete M[O,S]
would construct a different matrix.

At eta=9/10, the final matrix is
`[[81 A/100, B_ref],[B_ref^T,D]]`. Only A receives eta squared; the cross
does not receive an additional eta factor. The old diagnostic's candidate
negative count eight is a target to check, not an admissible assumption.

The finite prime dictionary `{2:2,3:3,4:2,5:5,7:7,8:2,9:3}` correctly
encodes Lambda(q)=log(p), with coefficient -log(p)/sqrt(q) multiplying
the sum of the forward overlap and its transpose. Support tests use exact
multiplicative Fraction endpoints. At q=9 only extreme endpoint contact
is possible and the overlap is zero. The pole routine retains
`l_+l_-^T+l_-l_+^T`, as required, rather than a rank-one replacement.

## 2. Archimedean prefix and tail: actual conditions

The source constructs
`M_arch=h0 I+sum_(n>=0) J_(2n+1/2)` with
`J_c=2I/c-L_c-L_c^T`. The one-sided matrix entry is

`L_ij(c)=integral_(x<y) phi_i(x)phi_j(y) exp(-c(y-x)) dxdy`.

For same-interval entries, integrating the second sine explicitly gives
the source numerator
`c I_ss + beta I_sc - beta (-1)^l alpha (exp(-c ell)-(-1)^k)/(c^2+alpha^2)`
over `c^2+beta^2`, multiplied by the two normalizations. The source I_sc
formula is the elementary sine-cosine integral, including its exact k=l
zero case. For ordered distinct intervals, the integral factors and expands
into the four endpoint exponentials in `ordered_distinct_laplace`. Their
gaps are nonnegative for these ordered disjoint supports.

The leading c^(-1) coefficient of L_c is exactly I by orthonormality.
It cancels the 2I/c term after adding the transpose. The source therefore
correctly omits that coefficient before calling Hurwitz zeta. This omission
would be invalid for an arbitrary newly substituted nonorthonormal basis.
No divergent zeta(1) coefficient should be numerically approximated instead.

The algebraic tail expands the denominator terms with q equal to 1, 2, or 4.
For the single inverse term, its first omitted index is
`r=floor((P-q)/2)+1`, its power is `p=q+2r`, and the bound uses

`rho_single=(abs(alpha)_upper/c_K)^2`, where `c_K=2K+1/2`.

It requires rho_single<1. For a product of two inverses, the source actually
uses `M=abs(alpha)_upper+abs(beta)_upper`, not max(alpha,beta). With
`T=floor((P-q)/2)+1`, its convolution remainder is bounded using

`rho_product=(M/c_K)^2 < 1`

and

`rho_product^T [(T+1)/(1-rho_product)+rho_product/(1-rho_product)^2]`.

This follows by summing `sum_(t>=T)(t+1)rho^t`; the coefficient of total
denominator degree t has at most t+1 terms. It is a valid conservative
bound only under the geometric convergence condition. Merely proving the
single-frequency condition is insufficient for the code's product bound.

Every retained or remainder power passed to
`2^(-p)zeta(p,K+1/4)` must have p>1 and K+1/4>0. Keeping the shipped
contract P>=6 guarantees the needed omitted powers for q=1,2,4. Any integer
P>=6, even or odd, is mathematically allowed with the corresponding first
omitted power. This audit does not propose reducing P below that API contract.

For every exponential remainder, its gap d must be strictly positive.
Touching gaps are recognized by an exact Fraction ratio equal to one and
retained in the algebraic part; they must not enter a bound divided by
`1-exp(-2d)`. The fixed four-interval geometry gives positive d for every
remaining term. The bound then follows from
`sum_(n>=K) e^(-c_n d)/c_n^4 <= c_K^(-4)e^(-c_K d)/(1-e^(-2d))`.

The new consumer must check K is a positive integer, P is an integer at
least six, all these denominators have strictly positive certified lower
bounds, and all returned entry/error balls are finite. The old command-line
entry checks only P>=6. For example, K=1 is not justified by that check:
even the first shell frequency exceeds 6, while c_K=5/2, so its geometric
ratio already exceeds one. An unsupported K is an invalid invocation of
this proof, not a negative-inertia result.

## 3. A rigorously admissible smaller prefix: K=256, P=10

No small-K suggestion here rests solely on a program assertion. The basic
constant bounds are

`pi<4`, `log2>2/3`, `log(3/2)>2/5`.

The log bounds follow from the positive expansion
`log((1+u)/(1-u))=2(u+u^3/3+...)`, with u=1/3 and u=1/5.
Thus every old frequency is below 48, every shell frequency below 80, and
every product M is below 160. Consequently **K>=80 is a simple sufficient
N8 convergence range**, since c_K>=160.5. Adequate precision must still
certify these same inequalities for the upper endpoints used by the code.
This convergence condition alone does not promise a small error radius.

For a useful bounded example set K=256, P=10, and c=c_K=1025/2. Define the
exact rational upper bound

`S_p = c^(-p)+c^(1-p)/(2(p-1))`.

Monotonicity of (2t+1/2)^(-p) shows
`sum_(n>=K)c_n^(-p)<=S_p`. The following bounds cover every exact coefficient:

- The q=1 single-inverse coefficient is at most one: it is exactly one on
  the diagonal and zero otherwise.
- The q=2 single-inverse coefficient has absolute value at most 160, since
  `norm_i norm_j |I_sc|<=2` on one interval and beta<80.
- Product and endpoint coefficients are below 32000, since both frequencies
  are below 80 and the normalization product is below five.
- Every nonzero endpoint gap exceeds 2/5. Also
  `1-exp(-2d)>1/2`, because `exp(4/5)>1+4/5+(4/5)^2/2>2`.

Put `r1=(80/c)^2`, `rp=(160/c)^2`, `u=2c/5`. Per one-sided L entry, the
three uniform algebraic bounds and one endpoint bound are

```text
e1 = 80^10 S_11/(1-r1)
e2 = 160*80^10 S_12/(1-r1)
e4 = 32000*160^8*[5/(1-rp)+rp/(1-rp)^2]*S_12
ee = 64000*c^(-4)/(1+u+u^2/2)
```

Here `exp(-u)<=1/(1+u+u^2/2)`. There are at most four exponential terms
per directed entry, and a J entry subtracts two directed entries. Therefore

`r_entry = 2(e1+e2+e4+4ee)`

is a conservative uniform analytic truncation-radius bound. This deliberately
overcounts terms that cannot occur together and does not rely on cancelling
signed remainder terms.

An independent Fraction calculation, without importing or executing the
old script, gave the following display values and exact rational checks:

```text
rho_single  = 0.0243664485425342058
rho_product = 0.0974657941701368233
e1 = 4.57372651322879111e-10
e2 = 1.30296190262249138e-10
e4 = 5.75565700655558394e-9
ee = 4.37209727490137825e-11
r_entry = 1.30364194782735346e-8
32*r_entry = 4.17165423304753108e-7
exact assertion r_entry < 1/50000000: PASS
exact assertion 32*r_entry < 1/1000000: PASS
```

Thus K=256, P=10 is a mathematically supported smaller-prefix option.
These bounds concern the analytic truncation only; coefficient evaluation,
Hurwitz-zeta evaluation, finite-prefix rounding, and final interval export
must still be enclosed by the actual ball calculation. Neither this bound
nor the old floating spectral gap guarantees a successful inertia witness.
K=10000, P=10 remains within the same conditions. K is a series prefix,
not a frequency cutoff or a Cauchy integration endpoint.

## 4. Cauchy normalization, ordering, and uniform tail

The original diagnostic explicitly defines the principal cross kernel as
`K_C(s)=-1/(2s)`. For a left interval i and a right interval j, the identity
`1/(y-x)=integral_0^infinity exp(-c(y-x))dc` therefore gives

`C_ij=-(1/2)integral_0^infinity L_ij(c)dc`.

The factor is -1/2, not -1. Appending the transpose cross block in the full
real matrix already supplies the other ordered quadratic-form term; it does
not justify multiplying each cross entry by another two.

The absolute exchange is justified for these disjoint-interior supports.
At a touching corner set y-x=u+v with u,v>=0. Bounded sine functions reduce
the local majorant to 1/(u+v), whose double integral over a bounded corner
is finite. Away from touching corners the kernel is bounded. No positivity
of the signed sine product is assumed.

The integration routine must first put intervals in physical left/right
order. Old-to-S- entries require `ordered_distinct_laplace(S-,old,c)`;
old-to-S+ entries require `ordered_distinct_laplace(old,S+,c)`. Calling
the old `laplace_overlap(old,S-,c)` directly would return zero and silently
delete an entire group of nonzero reference entries. This adapter hazard
was sent to the producer before completion of this note.

For c>0 all four exponential endpoint factors in the closed expression
have absolute value at most one, and both denominators are at least c^2.
Writing `b=norm_i norm_j alpha_i alpha_j`, this gives `|L_ij(c)|<=4b/c^4`.
For a Cauchy cutoff C_cut>0,

`|(1/2)integral_(C_cut)^infinity L_ij(c)dc| <= 2b/(3 C_cut^3)`.

For old/shell pairs, the sharper normalization product is below
sqrt(3*5)<4. Combining alpha_old<48 and alpha_shell<80 gives
`b<15360`, hence exactly the advertised uniform bound

`epsilon_C < 10240/C_cut^3`.

At C_cut=20000, the exact bound is `1/781250000 = 1.28e-9` per entry.
The 16-by-16 cross error has row and column sums at most 16 epsilon_C,
so its operator norm is at most `1/48828125 = 2.048e-8`. The symmetric
32-by-32 off-diagonal error has the same operator norm, not twice that
amount. The analytic tail is added as a **two-sided** entry radius: the
sine product changes sign and the discarded cross matrix is not a PSD
remainder. The finite c-interval still requires its own rigorous enclosure.

The source rational-exponential formula is nonsingular on the positive real
c axis, but its complex continuation has denominator poles at the imaginary
frequencies. Any analytic quadrature adapter must honor its actual callback
contract and handle integration-domain balls containing such poles. This
audit has not read or certified an uncompleted adapter implementation.

## 5. Symmetric enclosures and inertia authority

All target entries are real and the target matrix is exactly symmetric.
The old arch formula explicitly combines L_ij and L_ji; prime and pole
formulas likewise have symmetric real targets. If independently computed
ball entries differ slightly, export one valid enclosing triangle and
mirror it, or another justified common enclosure. Do not silently discard
radii while symmetrizing midpoints. Exact rational endpoints must enclose
the original balls; display-decimal strings are not automatically endpoints.

The accelerated arch tail already adds `arb(0,err)` after retaining the
algebraic terms. That err bounds both signs of the omitted algebraic and
exponential contributions. Although the full J series is PSD term by term,
the error relative to a retained asymptotic approximation is not thereby
a PSD error. The new A and D must include the complete prefix, accelerated
tail, and all ball radii. No additional old frequency-tail budget is added
to this cutoff-free construction, and no analytic radius is silently removed.

Scale the old block's intervals, including radii, by 81/100. Add Cauchy
finite-integration and tail errors before exporting B_ref. For a symmetric
center M and symmetric entry-radius matrix R, an exact bound
`delta>=max_i sum_j R_ij` controls the operator error in both directions.
The full row-sum bound includes diagonal-block and cross-block errors
together; the separate uniform examples above are not replacements for
the exported radius matrix.

The old no-pivot interval LDL routine accepts only strictly positive pivots.
It is unsuitable as a negative-inertia counter. A failed positive pivot,
a ball containing zero, integration-budget exhaustion, or an overly broad
tail radius does not prove a negative count or a mathematical failure.
The separately assigned exact rational inertia verifier must check its
actual two-sided matrix bounds and congruence witnesses, without taking
q=8 from the diagnostic as input truth. A post hoc rational check only
certifies inertia for matrices inside the claimed enclosure; the producer's
entry construction must also be valid.

The reuse is therefore accepted with explicit gates. The old eta=1 result
and unexamined source-code execution are not being replayed or silently
promoted. The output to be certified remains one declared eta=9/10,
32-dimensional prime+Cauchy reference matrix, not the full Weil cross,
the infinite operator, a Galerkin complement, or RH.

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
