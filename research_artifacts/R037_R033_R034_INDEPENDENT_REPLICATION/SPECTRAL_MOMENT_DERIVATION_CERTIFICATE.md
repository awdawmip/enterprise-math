# R037 spectral / moment independent derivation certificate

Researcher-ID: `EM-R037-204389`

## Scope and provenance

This certificate records the algebra used by the R037 audit.  It does not import the frozen R034 experiment.  A separate provenance caveat applies because an owner-head metadata lookup unexpectedly displayed a partial frozen-script patch before the independent R034 implementation was complete; see the return and R034 atlas.

## Local second and third order

Normalize every NN step to physical length one.  FCC uses the twelve permutations of `(±1,±1,0)/sqrt(2)`.  For HCP use basal basis

`e1=(1,0,0)`, `e2=(1/2,sqrt(3)/2,0)`, layer height `h=sqrt(2/3)`, and offset `delta=(e1+e2)/3`.

Direct exact summation gives zero conditional drift and covariance `I/3` for FCC, HCP-A and HCP-B.  Hence for the walk

`E[X_n X_n^T] = n I/3`,  `E|X_n|^2=n`.

The FCC cubic contraction is zero.  From an A layer the HCP cubic contraction is

`sqrt(3)/72 * y*(3*x^2-y^2)`

and from a B layer it has the opposite sign.  Thus rooted local memory appears already at order three.

## Exact radial fourth and sixth moments

Write `R=|X|^2`, `a=X·V`, with `|V|=1`.  Since `E[a|X]=0` and `E[a^2|X]=R/3`,

`R' = R+1+2a`

implies

`E[(R')^2|X]=R^2+(10/3)R+1`.

Therefore

`E|X_n|^4=(5*n^2-2*n)/3`

for both FCC and HCP.

For sixth order, the conditional recurrence contains `C_state(X)=E[(X·V)^3|state]`.  FCC has `C=0`.  For HCP, `C` is the signed cubic harmonic above.  A direct one-step symbolic expansion using the twelve HCP step vectors gives, for either current layer type,

`E[C_next(X+V) | X,current_state] = -1/432`.

Consequently, for `n>=1`, `E C_state(X_n)=-1/432`, and solving the exact recurrence gives

- FCC: `E|X_n|^6 = n*(35*n^2-42*n+16)/9`;
- HCP: `E|X_n|^6 = (210*n^3-252*n^2+95*n+1)/54`;
- difference: `HCP-FCC = -(n-1)/54`.

Thus scalar radial memory first appears at order six.  Integer path enumeration through `n=12` independently checks all three formulas.

## FCC transition symbol

Direct averaging over the twelve FCC steps gives

`lambda_F(k)=[cos(x/sqrt(2))cos(y/sqrt(2))+cos(x/sqrt(2))cos(z/sqrt(2))+cos(y/sqrt(2))cos(z/sqrt(2))]/3`.

Expanding `log lambda_F` at the origin gives

`log2_F=-(x^2+y^2+z^2)/6`,

`log4_F=-(x^4+x^2*y^2+x^2*z^2+y^4+y^2*z^2+z^4)/144`.

On the unit sphere the quartic term ranges from `-1/144` to `-1/216`, hence under `k=q/sqrt(n)` the angular exponent spread is `q^4/(432*n)+O(n^-2)`.

## HCP principal Bloch band

With basal Fourier variables `(x,y)`, set

`C=cos(x)+2*cos(x/2)*cos(sqrt(3)*y/2)`.

The two-layer Bloch fiber has diagonal `C/6`, and the principal eigenvalue near zero is

`lambda_H=C/6 + cos(sqrt(2/3)*z)*sqrt(3+2*C)/6`.

Its logarithm has

`log2_H=-(x^2+y^2+z^2)/6`,

`log4_H=-(9*x^4+18*x^2*y^2+24*x^2*z^2+9*y^4+24*y^2*z^2+8*z^4)/1728`.

The quartic unit-direction range is `[-1/168,-1/216]`, giving angular exponent spread `q^4/(756*n)+O(n^-2)`.  Therefore the common diffusion tensor does not imply finite-time spherical equality; principal spectral memory begins at order four.

After rotating FCC into stacking coordinates with axes

`(1,-1,0)/sqrt(2)`, `(1,1,-2)/sqrt(6)`, `(1,1,1)/sqrt(3)`,

the quartic difference simplifies exactly to

`log4_FCC-log4_HCP = -sqrt(2)*y*z*(3*x^2-y^2)/432`.

## Barlow layer-gauge theorem

For an arbitrary legal bi-infinite registry sequence, basal Fourier transform turns the NN transition operator into a Jacobi operator on the layer line.  Let the registry turn on an edge be `epsilon_n=±1`.  The two possible interlayer structure factors are conjugates,

`F_+(q)=exp(i q·delta)*(1+exp(-i a)+exp(-i b))`,  `F_-(q)=conj(F_+(q))`,

so every off-diagonal hopping has the same magnitude

`beta(q)=|1+exp(-i a)+exp(-i b)|/12`.

The stacking only chooses edge phases.  Because the layer graph is `Z`, it has no cycle and hence no gauge-invariant flux.  For `beta>0`, fix `u_0=1` and choose `u_{n+1}` recursively so conjugation by `diag(u_n)` makes each hopping equal to positive `beta`; when `beta=0`, the hopping already vanishes.  Every fiber is therefore unitarily equivalent to

`J_q = alpha(q) I + beta(q)(S+S*)`,

with `alpha(q)=[cos(a)+cos(b)+cos(a-b)]/6`.

Because `u_0=1`, the root layer vector is preserved.  Direct integration over basal momentum proves, within the ideal NN bi-infinite Barlow scope, identical return probabilities for every time and identical root local spectral measures.  This is an exact operator proof, not an inference from finite enumeration.  Four unrelated legal stackings were also enumerated independently through `n=12` as a regression check.

The gauge is momentum-dependent and is not a physical-coordinate vertex permutation.  It therefore does **not** remove physical wavevector-labelled angular dispersion or imply a pointwise nonperiodic local CLT / uniform heat-kernel bound.
