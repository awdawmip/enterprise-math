# RSA-270 continuation: exact theta-product form and complete-product Galois-orbit lower bound

Status: `RESEARCH NOTE / EXACT PRODUCT IDENTITY + SCOPED ORBIT LOWER BOUND / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T02:32:00+08:00`  
Parents:
- `research_notes/RSA270_CARTIER_CHARACTER_PRODUCT_BRIDGE_20260908.md`
- `research_notes/RSA270_GALOIS_EQUIVARIANT_STATE_LOWER_BOUND_20260908.md`

No RSA-270 factor is obtained.

## 1. Exact theta quotient for the full BRC product

Start from the exact Ramanujan/Kac-Cheung BRC product

`F(Q,u)=prod_(n>=1) ((1-Q^(2n))^2 (1-u^2 Q^(2n))(1-u^(-2) Q^(2n))) /
                    ((1-u Q^(2n-1))^2(1-u^(-1)Q^(2n-1))^2)`.

Put

`q=Q^2`,

and define the multiplicative theta product

`theta(x;q)=(x;q)_inf (q/x;q)_inf (q;q)_inf`.

Then exactly

**Theorem (theta-product form).**

`F(Q,u)
 = (q;q)_inf^3 * theta(u^2;q)
   / [(1-u^2) theta(uQ;q)^2]`.

### Proof

First,

`theta(u^2;q)
 =(u^2;q)_inf(u^(-2)q;q)_inf(q;q)_inf`

and

`(u^2;q)_inf=(1-u^2)(u^2 q;q)_inf`.

Therefore

`(u^2q;q)_inf(u^(-2)q;q)_inf
 = theta(u^2;q)/[(1-u^2)(q;q)_inf]`.

Second, because `q/(uQ)=u^(-1)Q`,

`theta(uQ;q)
 =(uQ;q)_inf(u^(-1)Q;q)_inf(q;q)_inf`.

Substitution into the original product gives the displayed identity.

A numerical truncated-product regression at `u=zeta_m`, `m in {3,5,9}`, and `Q in {0.03,0.1}` agrees to approximately `1e-15` or better; the theorem itself is the formal Pochhammer algebra above.

## 2. Order-3 specialization is an explicit eta/Pochhammer quotient

Let `omega^3=1`, `omega!=1`. Since

`(1-omega x)(1-omega^2 x)=1+x+x^2=(1-x^3)/(1-x)`,

the product simplifies to

`F(Q,omega)
 = (Q;Q)_inf^2 (Q^6;Q^6)_inf^3 /
   [(Q^2;Q^2)_inf (Q^3;Q^3)_inf^2]`.

Equivalently it is an eta quotient up to the standard leading q-power normalization. This explains why the order-3 BRC torsion channel lies in a very small modular object and, under the public H2 branch, carries no new RSA-270 digit.

The higher `l^e` torsion specializations are generalized theta/Siegel-function type objects rather than evidence for a fixed-level collapse.

## 3. Complete-product Galois orbit

Let

`m=l^e`, `e>=2`,

with l odd prime and `zeta=zeta_m`. Let `h=(l-1)/2` and apply the repeated middle Cartier section from the odd-prime-power atlas:

`C_(l,h)^e F(Q,u)
 = sum_(R>=0) P_(l^e(2R+1))(u) Q^R`.

Define the normalized complete-product specialization

`Z_e(Q;zeta)
 = ((zeta^2-1)/(2zeta)) C_(l,h)^e F(Q,zeta)`.

For every unit `a mod m`, Galois acts by

`sigma_a(zeta)=zeta^a`,

hence

`sigma_a Z_e(Q;zeta)=Z_e(Q;zeta^a)`.

So the full family of torsion product specializations is one Galois orbit.

## 4. Every primitive odd character occurs in the complete-product orbit

For each primitive odd Dirichlet character chi modulo m, the previously proved all-level projector theorem gives

`Pi_chi Z_e(Q;zeta)
 = 2 chi(2)^(-1)
   sum_(R>=0) A_chi(2R+1) Q^R`,

where

`A_chi(n)=sum_(d|n) chi(d)`.

The right-hand series is nonzero because its constant coefficient is

`A_chi(1)=1`.

Therefore the chi-isotypic projection of the **complete product orbit** is nonzero for every primitive odd chi.

Distinct characters give distinct one-dimensional eigenspaces of the abelian Galois group. Consequently:

**Theorem (complete-product orbit lower bound).**

`dim_C span{ Z_e(Q;zeta^a) : a in U_(l^e) }
 >= (1/2) l^(e-2)(l-1)^2`.

The lower bound is exactly the number of primitive odd characters at conductor `l^e`.

This conclusion is basis-independent. It is not caused by choosing a character decomposition; the character decomposition merely diagonalizes a high-dimensional orbit already present in the complete BRC theta product.

## 5. Consequence for a fixed-dimensional theta/modular compression

A proposed representation that simultaneously supports the exact Galois/torsion family inside a d-dimensional linear theta/modular state must have

`d >= (1/2)l^(e-2)(l-1)^2`.

Thus no level-independent or polynomial-in-e full-Galois linear basis change can compress the complete torsion family.

For the pure ternary route this lower bound is

`2*3^(e-2)`;

at the Coppersmith handoff e=141 it is `2*3^139`.

This closes the tempting idea that replacing the coefficient profile by a theta quotient automatically places the higher torsion tower inside one fixed-dimensional modular-form space.

## 6. Weight-one Eisenstein interpretation

For a primitive odd character chi, the nonconstant coefficients

`A_chi(n)=sum_(d|n)chi(d)`

are the standard coefficients of a weight-one Eisenstein series with nebentypus chi. Thus the primitive projections of the theta-product orbit are exactly the twisted weight-one Eisenstein channels already identified arithmetically.

This matches standard modular-form theory: weight-one Eisenstein series attached to primitive odd Dirichlet characters have divisor-sum q-coefficients. The modular-language reformulation is useful for classification, but it does not give an index-fast coefficient algorithm at an RSA-sized composite index.

## 7. Scope boundary

The theorem rules out only a **simultaneous full-Galois linear** fixed-dimensional theta/modular state. It does not rule out a target-N asymmetric nonlinear identity computing one requested local branch without supporting all torsion conjugates.

However, together with:

- the global finite-state no-go;
- the full primitive-odd spectrum of one local trace;
- the Galois translated-query rank theorem;
- the additive operation-safe residue-state no-go;

there is now no surviving evidence that a mere change of representation (profile -> characters -> theta functions -> modular forms) lowers the exact state complexity.

The remaining opening must exploit a **special target-specific nonlinear identity of the complete product**, not a fixed-dimensional linear coordinate transform.
