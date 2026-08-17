# R059D Stage AG — N-Resolver Algebraic Beatty Proof and Sturmian Jump Law

Researcher-ID: `EM-R059D-AG-8C2E47`  
Task-ID: `RS-R059D-STAGE-AG-N-BEATTY-PROOF-STURMIAN-JUMP-LAW`  
Taskbook source: `f1dcbd5d26b79be6dc8b2f495c81266a1c41ce9f`  
Frozen source main: `fb5b7880e469c8e16769cf55601da15bb5f96b4f`  
Accepted AF owner head: `9e863cfc89cab71118959deb38187a21fe1e96e1`

## Primary disposition

`N_BEATTY_STURMIAN_JUMP_LAW_PROVED`

Stage AG proves the AF N-side candidate for every integer radius:

`J_N(r)=floor(alpha*r+1/3)`

where `alpha` is the unique positive root of

`3alpha^2+6alpha-1=0`.

The proof is native to the frozen N-resolver bridge semantics. It starts from exact centroid occupancy and edge-supported dual incidence; no classical circumference, pi, Euclidean curvature, equal-distance definition, or runtime square root is used.

## Exact geometric reduction

For first-sector dual vertex `(a,b)` the six incident-edge support costs reduce to

`G(a,b)=9(a^2+ab+b^2)-9 max(a,b)+3`.

Thus selection is exactly

`3(a^2+ab+b^2)-3 max(a,b)+1<=3r^2`.

AF's Motzkin height is exactly `h=a+b-r`. Column monotonicity and the diagonal inequality

`Phi(a-1,b+1)-Phi(a,b)=2-(a-b)`

show that all up events occur before all down events. Hence the maximum selected shell is

`M_r=r+J_N(r)`.

Minimizing the support cost at fixed shell `m=a+b` yields the uniform integer criterion

`(3m-1)^2<=12r^2`.

If `beta=1+alpha`, then `3beta^2-4=0`, so

`M_r=floor(beta*r+1/3)`,

and therefore

`J_N(r)=floor(alpha*r+1/3)`.

## Exact event recurrence

Given `j=J_N(r-1)`, the new pair appears iff

`(3j+2)^2+6r(3j+2)-3r^2<=0`.

This is equivalent to the AF integer recurrence and is proved equivalent to the floor theorem for all radii.

The runtime generator is fully integer-only and forward autonomous.

## Jump law

For the first radius with `J_N=m`:

`r_m=ceil((m-1/3)/alpha)`.

With `lambda=1/alpha`, `lambda` is the positive root of

`lambda^2-6lambda-3=0`.

Since `6<lambda<7`:

`r_(m+1)-r_m in {6,7}`

for every `m`, and both gaps occur infinitely often.

## Sturmian theorem

The binary jump word is

`s_r=floor(alpha*r+1/3)-floor(alpha*(r-1)+1/3)`.

With index `n=r-1`, this is the lower mechanical word of slope `alpha`, intercept `1/3`.

It is balanced because any length-L block contains either `floor(Lalpha)` or `ceil(Lalpha)` ones. It is aperiodic because its one-density is the irrational number `alpha`. Hence it is Sturmian.

## Continued fraction

The same quadratic equation gives

`alpha=[0; overline{6,2}]`.

Convergents begin

`1/6, 2/13, 13/84, 28/181, 181/1170, 390/2521, ...`.

This periodic continued fraction is derived after the N quadratic threshold; it is not an imported sequence fit.

No intercept-specific single fixed substitution is promoted. The exact lower-mechanical generator and the integer recurrence are sufficient forward generators for J.

## Motzkin count consequences

Exactly:

`#1=#3=floor(alpha*r+1/3)`,

`#2=r-floor(alpha*r+1/3)`,

`|W_r|=r+floor(alpha*r+1/3)`.

Asymptotically the word-symbol densities are

`d1=d3=alpha/(1+alpha)`,
`d2=(1-alpha)/(1+alpha)`.

AF's negative theorem remains immutable: J alone does not determine B or the internal Motzkin arrangement.

## Validation

The symbolic theorem is implementation-validated through `r=16384` using three exact integer views:

1. the N source shell-support criterion `(3m-1)^2<=12r^2`;
2. the integer recurrence;
3. direct floor-interval certificates using the polynomial `x^2+6rx-3r^2`.

All agree.

Finite validation through 16384 gives only jump gaps `6` and `7`. The first 512 theorem values also reproduce the AF accepted N candidate, whose frozen discovery and untouched holdout both had zero mismatches.

## C status

After proving N, the AF observation that all N/C J disagreements through 512 are one-radius delays is retained as `FINITE_CENSUS_ONLY`. No C phase theorem is claimed.

## Next hard problem

AG does not solve `W_r -> W_(r+1)`. The control plane may now freeze the proved N Sturmian jump skeleton as input to the full Motzkin-word growth problem.

`STOP_FOR_DRIVER_REVIEW`
