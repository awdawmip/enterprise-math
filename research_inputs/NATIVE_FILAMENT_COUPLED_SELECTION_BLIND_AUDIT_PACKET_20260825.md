# Native filament coupled-selection theorem package — blind audit packet

Status: `BLIND_STATEMENT_PACKET / NO_SOURCE_PROOFS`

Date: `2026-08-25`

Audit target: independently prove, narrow, or refute the statements below without reading the source generalization branch or its proof/checker files.

The packet intentionally includes theorem statements and definitions only.

## 0. Allowed starting data

### 0.1 Abstract cyclic shell allocator

For an integer sector count `s>=1`, shell `r>=1` has `s` cyclic blocks, each with side positions `t=0,...,r-1`.

The shell base and label are

`B_r^(s)=1+s*r*(r-1)/2`,

`N_s(r,t,sigma)=B_r^(s)+sigma*r+t`.

Only the specialization `s=3` is claimed to match the current Enterprise tri-sector allocation. Other `s` are abstract combinatorial controls.

### 0.2 Odd-curvature family

For positive odd `B`, define

`eps(r)=r mod2` in `{0,1}`,

`F_B(H,r)=H+(B*r^2+eps(r))/2`.

For a window starting at shell R, write

`chi=(-1)^R`.

### 0.3 Prime-channel transparency

For a prime q, call `H mod q` **transparent** if

`q does not divide F_B(H,r)`

for every integer shell r.

Let `tau_B(q)` be the number of transparent classes.

A prime q is a **universal breaker** if `tau_B(q)=0`.

---

# A. Sector/curvature provenance

## A1. Odd-sector central-filament identity

For odd `s`, let

`sigma_*=(s-1)/2`,

`t=h+ceil(r/2)`.

Claim:

`N_s(r,t,sigma_*)=h+1+(s*r^2+eps(r))/2`.

Therefore the odd-curvature coefficient in this abstract central filament is exactly

`B=s`.

## A2. Even-sector central-seam obstruction

For even `s`, take the two central blocks

`sigma_L=s/2-1`, `sigma_R=s/2`,

at equal distance h from their common seam:

`t_L=r-1-h`, `t_R=h`.

Claim:

`L=s*r^2/2-h`,

`R=s*r^2/2+1+h`,

so

`R-L=2h+1`.

Hence no reflected central-seam pair with both values greater than2 can consist of two primes.

---

# B. Odd-curvature value dynamics

## B1. Window formula

Let

`c=F_B(H,R)` and `chi=(-1)^R`.

Claim for all integers j:

`F_B(H,R+j)`

`=c+B*R*j+(B*j^2+chi*eps(j))/2`.

## B2. Curvature / recurrence

Claim:

`V_j-2V_(j+1)+V_(j+2)=B-chi*(-1)^j`.

Thus local curvature alternates `B-1,B+1`.

Claim also:

`V_(j+4)-2V_(j+3)+2V_(j+1)-V_j=0`.

---

# C. Finite quotient code

For `k>=3`, let `C_(k,B)(M)` be the set of length-k residue words modulo M arising from all integer `(H,R)`.

## C1. Effective period

Let

`L_(B,M)=lcm(2,M/gcd(B,M))`.

Claim that the word depends on R exactly through its class modulo `L_(B,M)` once the intercept is included.

## C2. Exact cardinality

Claim:

`|C_(k,B)(2)|=2`,

and for every `M>2`,

`|C_(k,B)(M)|=M*L_(B,M)`.

The count is independent of k once `k>=3`.

## C3. Fixed-chirality good-prime sheet

If q is prime, `q>max(2,k-1)` and `q` does not divide B, claim that after subtracting

`eta_j=(B*j^2+chi*eps(j))/2`,

the fixed-chirality packets are exactly

`(a+b*j)_(j=0,...,k-1)`.

Thus they form an affine translate of `[k,2,k-1]` Reed--Solomon / MDS.

The RS/MDS classification itself is classical; audit only the exact reduction from the integer family.

---

# D. Dual-parabola arrangement

Assume q odd and q does not divide B.

Define

`Q_e(x)=x^2/(2B)-e/2`, `e=0,1`.

## D1. Tangent representation

Claim that the zero line for index j,

`y=-j*x-(B*j^2+chi*eps(j))/2`,

is the tangent to the corresponding shifted parabola at `x_0=-B*j`.

## D2. Mixed-parity concurrence

Let u,v have common parity e and w opposite parity.

Claim that the three sampled tangent lines are concurrent modulo `q^a` iff

`q^a | B*(w-u)*(w-v)+chi*(1-2e)`.

Three same-parity tangents are concurrent modulo `q^a` iff `q^a|B`, in the distinct-slope range.

## D3. Two-chirality discriminant

For a finite length-k window define

`A_T=(w-u)*(w-v)`

for each mixed-parity triple T and

`mathfrak D_(k,B)=B * product_T (B^2*A_T^2-1)`.

Claim for prime `q>k-1`:

q changes the intersection type for at least one chirality iff

`q | mathfrak D_(k,B)`.

Claim the exact p-adic persistence depth for a fixed chirality equals the maximum q-adic valuation among the corresponding explicit obstruction integers.

---

# E. Transparency / breaker classification

## E1. Exact local factors

Claim:

### q=2

`tau_B(2)=1` iff `B=3 mod4`; otherwise0.

### q=3

`tau_B(3)=1` iff `3|B`; otherwise0.

### odd q>=5, q|B

`tau_B(q)=q-2`.

### odd q>=5, q does not divide B

`tau_B(q)=[q-3 + Legendre(B/q)+Legendre(-B/q)]/4`.

## E2. Complete universal-breaker set

Claim no prime `q>=7` is a universal breaker.

Claim:

`Break(B)`

`= ({2} if B=1 mod4 else empty)`

`union ({3} if 3 does not divide B else empty)`

`union ({5} if Legendre(B/5)=-1 else empty)`.

## E3. First-breaker classes mod60

Among odd B mod60, claim:

- first breaker2:
  `{1,5,9,13,17,21,25,29,33,37,41,45,49,53,57}`;
- first breaker3:
  `{7,11,19,23,31,35,43,47,55,59}`;
- first breaker5:
  `{3,27}`;
- no universal breaker:
  `{15,39,51}`.

## E4. Sharp nonzero-run capacities

Claim that the first-breaker phases have sharp maximum consecutive breaker-coprime run lengths:

- q=2 ->1;
- q=3 ->5;
- q=5 ->9.

For q=5 in the breaker phase, the two normalized extremal/tangency transverse classes are `H=0` and `H=2 mod5`.

---

# F. Legendre-dual value-set interpretation

For q odd and q not dividing B, define

`I_e=-Q_e^*(F_q)`.

## F1. Hit sets

Claim:

- I_0 is exactly the set of H classes hit by some even shell;
- I_1 is exactly the set of H classes hit by some odd shell.

## F2. Intersection formula

Claim:

`|I_0|=|I_1|=(q+1)/2`,

and

`|I_0 intersect I_1|`

`=[q+1+Legendre(B/q)+Legendre(-B/q)]/4`

`=tau_B(q)+1`.

Hence q is a universal breaker iff the two hit images have minimal possible overlap1.

Cyclotomic-number / quadratic-residue intersection formulas are classical; audit the exact identification with this filament only.

---

# G. Finite-wheel / high-dimensional basin

For squarefree

`M=product_(q in S) q`,

let `Theta_B(M)` be the number of H mod M transparent to every q|M for the entire filament.

## G1. Exact CRT product

Claim:

`Theta_B(M)=product_(q|M) tau_B(q)`.

Thus a finite wheel kills every filament iff it contains at least one universal breaker.

## G2. Primorial extinction dimensions

For `P_d=product_(i<=d) p_i`, claim:

- first breaker2 -> extinction at d=1;
- first breaker3 -> d=2;
- first breaker5 -> d=3;
- no-break B -> `Theta_B(P_d)>0` for every finite d.

## G3. No-break asymptotic

For no-break B (`15,39,51 mod60`), claim there is `C_B>0` such that

`Theta_B(P_d)/P_d ~ C_B * 4^(-d)/(log p_d)^3`.

Equivalently

`Theta_B(P_d) ~ C_B * P_d/[4^d (log p_d)^3]`.

This uses classical Mertens/Dirichlet/PNT inputs; audit the local-factor-to-asymptotic derivation.

## G4. Squarefree profinite phase

Let

`S_sq=product_p F_p`

with primorial ultrametric and

`Tcal_B=product_p T_B(p)`.

For no-break B claim:

- Tcal_B is nonempty, compact, perfect, uncountable;
- Haar measure0;
- Hausdorff dimension1, equal to ambient dimension.

Also claim:

`Tcal_B intersect Z = empty`

under the diagonal embedding of ordinary integers, even though every finite subsystem has an integer solution.

General profinite/Cantor tools are classical; audit the application and metric normalization.

---

# H. Native tri-sector selection corollary

Use only the already-frozen native facts:

- actual sector count is3;
- native seven-Cell star satisfies
  `sum six neighbors -6*center =18`;
- central-filament local second differences are `{2,4}`.

Claim the same scalar is recovered three ways:

`sector count =3`,

`mean filament curvature=(2+4)/2=3`,

`normalized local Poisson source=18/6=3`.

Combining with E gives:

`local prime-free scalar3 -> channels2,3 nonbreaking -> channel5 first breaker -> sharp filament capacity9`.

Claim among positive odd abstract sector counts with a finite universal breaker, `s=3` is the smallest sector count attaining the latest possible first breaker (5).

---

# I. Finite prime control witness

Comparator family `B=15`.

Claim the following twelve consecutive values at `R=610`, `H=977767522784021` are all prime:

`977767525574771`,
`977767525583929`,
`977767525593101`,
`977767525602289`,
`977767525611491`,
`977767525620709`,
`977767525629941`,
`977767525639189`,
`977767525648451`,
`977767525657729`,
`977767525667021`,
`977767525676329`.

Audit primality independently and verify they are consecutive values of F_15.

This witness is used only to refute the hypothesis that 9 is a universal cap of the generic quadratic/parity family.

---

# J. Audit boundary

Do NOT treat the following classical ingredients as candidate novelty:

- characteristic quasi-polynomials / finite-field method for arrangements;
- arithmetic/G-Tutte theory;
- Reed--Solomon/MDS;
- CRT;
- order-2 cyclotomic numbers;
- Legendre transform / conic duality;
- standard quadratic character sums;
- Mertens/Dirichlet/PNT Euler-product asymptotics;
- generic profinite compactness and Hausdorff-dimension methods.

The audit target is correctness and statement-strength of the *coupled selection family*, not novelty of these tools.
