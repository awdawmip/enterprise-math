# R556｜固定 k=15 的 signed BRC 符号自然密度各半与有限零项

Date: 2026-11-05; status: AUTHOR-SIDE EXACT COMPUTER-ASSISTED PROOF / UNREVIEWED.
Scientific input: frozen R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`; prior verified source: R555 `174ccd2f7da6f22eef16deab81b8ab3d69101e9d`. This is an auxiliary scalar Toeplitz–Hessenberg determinant result, not native X6 dynamics.

## 精确定义与命题

固定 k=15，r=2k+1=31；C_j=binom(2j,j)/(j+1)，令
`H_k(t)=binom(r+t,2t) [x^r](1-x)(1+x)^(2t)(1+x²)^(r-t)`
for 2<=t<=r and H=0 otherwise. Define
`D_0(k)=1; D_m(k)=det(H_k(3+i-j))_(0<=i,j<m)`.
Claim:
`lim_(N->infinity) #{0<=m<N:D_m(15)>0}/N = lim_(N->infinity) #{0<=m<N:D_m(15)<0}/N=1/2`,
and `#{m>=0:D_m(15)=0}<infinity`.

## H-kernel and recurrence

An exact binomial evaluation gives
`H_k(t)=binom(r+t,2t) sum_(0<=q<=min(floor((t-1)/2),k)) binom(t-1,2q) 4^q C_(k-q)`.
In particular C_15=9694845 and `H_15(2)/C_15=40920`. Let
`p_t=H_15(t)/C_15, a_j=(-1)^(j-1) p_(j+2)/p_2` for 1<=j<=29,
`s_m=D_m(15)/(C_15 p_2)^m`. Toeplitz–Hessenberg expansion yields
`sum_(m>=0) s_m z^m=1/(1-sum_(j=1)^29 a_j z^j)`.
Consequently `Q(y)=y^29-sum_(j=1)^29 a_j y^(29-j)` controls the sequence. Original H was checked against its independent raw coefficient convolution for all t=2,...,31 (30 identities).

## Exact dominant-root isolation

`R556_VERIFY.py` contains 29 *fixed rational complex centers* at decimal fractions and exact radius 1/10000; numerical root-finding is not used by its certificates. For each center c, expand `Q(c+w)=sum_(j=0)^29 b_j w^j`, then certify the strict rational inequality
`max(|Re b_1|,|Im b_1|) eps > |Re b_0|+|Im b_0|+sum_(j>=2) (|Re b_j|+|Im b_j|) eps^j`, `eps=1/10000`.
This implies Rouché's theorem on each disk, since |b1|>=max components and |bj|<=sum components. Exact arithmetic also checks 406 distinct disk pairs do not intersect. Therefore Q has 29 simple roots, exactly one per disk. The unique maximal-modulus roots are the conjugate non-real pair satisfying `|lambda|>21`, all other 27 roots satisfy `|lambda_j|<8`. The principal angle lies in `pi/4<|arg lambda|<pi/3`. Largest observed exact RHS/LHS ratio is approximately 0.005038156694671 (display approximation only; every underlying comparison is rational).

## Complete cyclotomic exclusion

Over F_65537, all denominators of Q are invertible. Define `E(u)=Res_y(Q(y),u^29 Q(y/u))` and `R(u)=E(u)/(u-1)^29`. Since deg(E)<=841, evaluations at u=0,...,841 uniquely determine E; exact consecutive Newton interpolation yields deg(E)=841 and `deg(R)=812`, with `R(1)!=0` mod 65537. An independent SymPy finite-field resultant at u=842 and 846 agrees with the interpolated polynomial; evaluations, interpolation, and division are exact. The reproducible R coefficient checksum is SHA256
`704303ec06de0fd5ab4c78be0d3f235be0aaaaa7a6a07939ebcf427dc57ddeb3`
for comma-joined little-endian decimal residues.

If two distinct complex Q-roots have ratio a root of unity of exact order q, then `Phi_q | R` over Q; necessarily `phi(q)<=812`. The elementary inequality `phi(q)>=sqrt(q/2)` gives complete finite range `2<=q<=1,318,688`. Exact integer totient sieve gives 1574 candidates, with largest q=3570. The published checker computes `gcd(R mod 65537, Phi_q mod 65537)=1` for each; certified partitions `[0,800),[800,1250),[1250,1574)` cover all candidates, each with the same R SHA256. Since E/R are defined over the localization where 65537 is invertible and deg R survives reduction, a rational cyclotomic factor would necessarily survive reduction. All 1574 candidates are excluded. Thus no ratio of distinct roots is a root of unity, in particular lambda/conjugate(lambda) is not one.

## Asymptotic deduction and zero set

Because the characteristic roots are simple, the generating function has a partial-fraction expansion, with nonzero residues at every simple pole:
`s_m=A lambda^m+conj(A) conj(lambda)^m+O(8^m)=2|A||lambda|^m cos(m theta+arg A)+O(8^m)`, where `|lambda|>21`.
As lambda/conjugate(lambda) is not a root of unity, `theta/(2pi)` is irrational. Weyl equidistribution gives the strict-positive and strict-negative indices natural densities 1/2. The exponentially smaller remainder affects only an asymptotically negligible set of phases close to cos=0.
The recurrence has algebraic coefficients and no quotient of distinct characteristic roots is a root of unity. Skolem–Mahler–Lech then implies that its zero indices form a finite set (nondegenerate recurrence). Scaling by strictly positive `(C_15 p_2)^m` preserves all signs and zeros.

## Evidence and status

`R556_VERIFY.py`: exact H identity for 30 t values, 29 disks, 406 disjoint pairs, dominant >21 / others <8; exact normalized sequence for m=0,...,1024: 514 positive, 511 negative, 0 zero, 306 adjacent sign changes.
`R556_MODULAR.py`: degree-841 E, degree-812 R; verified checksum and 1574/1574 cyclotomic exclusions in three chunks; all checks use exact rational / finite-field semantics. The implementations are adapted from source-pinned R555 certificate code, with an optimized JIT finite-field gcd equivalent to ordinary Euclidean division.
`R556_EVIDENCE.txt` stores actual local execution outcomes. Mathematical status: author-side exact proof / independent Driver verification pending; formal CLAIM, Result and review are separate native-authority events.

Next: establish a uniform dominant-root and non-cyclotomic criterion for all k>=5, or isolate k=16. Alternative previously preserved: s=3,m=63 classification under frozen scope.
