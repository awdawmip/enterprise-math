# R5 — Primitive-19 residue is nonzero for every positive failure threshold

**Date:** 2026-11-22 (Asia/Shanghai). **Status:** AUTHOR_EXACT_DERIVATION / INTEGER_CERTIFICATE_CHECKED / NOT_REVIEWED.  
**Independent scalar cost observer, frozen R5 input.** This is a statement about the existing 101-price cost model, not a transfer to the X6 native dynamics or a modification of P000.

## Theorem

With prices `p=214,...,314`, five genuine failure events
`S0={214,215,216,217,218}`,
`S1={214,216,217,218,219,220,221}`,
`S2={215,216,217,218,219,220,221}`,
`S3={223,...,290}`,
`S4={296,...,312}`, and `E_i: sum_{p in S_i} a_p<m`,
let `R_m(q)` be the integer-polynomial numerator of the union-of-events counting series over `D(q)=prod_{p=214}^{314}(1-q^p)`.

**For every integer `m>=1` and every primitive nineteenth root of unity `zeta`, `R_m(zeta)!=0`. Hence**
```text
for every integer m>=1:
    19 divides M_m(O_m(N^3)).
```
Here `M_m` is the least coefficient period of a quasipolynomial approximation with fixed-m remainder `O_m(N^3)`. The five phases `m mod 19 = 0,15,16,17,18` left open by the preceding 14-phase theorem are now included.

The proof is an exact *infinite-m* generating-function reduction plus 38 finite nonvanishing certificates. It does not replace intersections by a union-cardinality cap.

## 1. The genuine intersection generating function

At `q=zeta`, masks containing event E3 or E4 vanish in the numerator because their factors contain respectively `1-q^228` and `1-q^304`. Only the seven masks of {0,1,2} survive.

Work in `K=Q(zeta)`. Define `a=zeta^214=zeta^5`, `b=zeta^215=zeta^6`, `u_i=zeta^(216+i)` for i=0,1,2, and `c_j=zeta^(219+j)` for j=0,1,2. Put
```text
U(t) = product_{i=0}^2 (1-u_i*t)^(-1)
J(t) = product_{j=0}^2 (1-c_j*t)^(-1)
U_B  = product_i (1-u_i)
J_B  = product_j (1-c_j)
B0   = U_B*(1-a)*(1-b)
B1   = U_B*(1-a)*J_B
B2   = U_B*(1-b)*J_B
B_*  = B0*J_B
```
In the three-event model the independent multiplicities are x for price214, y for price215, u for the total multiplicity among216..218 and j for the total among219..221. The **three distinct loads** are `L0=x+y+u`, `L1=x+j+u`, `L2=y+j+u`.

For any nonempty event mask I, the coefficient identity
`sum_{m>=1} 1[m>max_{i in I} L_i] t^(m-1)=t^(max_{i in I} L_i)/(1-t)`
keeps every load separately. Set
```text
V0(t)  = 1/((1-a*t)*(1-b*t))
V1(t)  = J(t)/(1-a*t)
V2(t)  = J(t)/(1-b*t)
W(s;t) = sum_{y,j>=0} s^y*h_j(c0,c1,c2)*t^max(y,j)
X(a,b;t) = sum_{x,y>=0} a^x*b^y*t^max(x,y)
V01(t) = W(b;t)/(1-a*t)
V02(t) = W(a;t)/(1-b*t)
V12(t) = J(t)*X(a,b;t)
V012(t) = sum_{x,y,j>=0} a^x*b^y*h_j(c0,c1,c2)
          *t^(x+y+j-min(x,y,j))
```
where `h_j` is the complete homogeneous polynomial in the three c-weights. The threshold-generating function is EXACTLY
```text
G(t) = sum_{m>=1} R_m(zeta)*t^(m-1)
     = U(t)/(1-t) * [
         B0*V0 + B1*V1 + B2*V2
         - B_* * (V01+V02+V12-V012)
       ].
```
This formula is independent of the numerical certificate.

## 2. Pole bound and all-threshold recurrence

The distinct `c_j` permit the exact partial fraction representation
`h_j(c0,c1,c2)=sum_c C_c*c^j`, with
`C_c=product_{c'!=c}(1-c'/c)^(-1)` in K.

For a single geometric weight c, exact summation gives:
```text
sum_{y,j>=0} b^y*c^j*t^max(y,j)
 = (1-b*c*t^2)/[(1-b*t)(1-c*t)(1-b*c*t)].

X(a,b;t) =
 (1-a*b*t^2)/[(1-a*t)(1-b*t)(1-a*b*t)].

sum_{x,y,j>=0} a^x*b^y*c^j
       *t^(x+y+j-min(x,y,j))
 = (1-a*b*c*t^3)/
   [(1-a*t)(1-b*t)(1-c*t)(1-a*b*c*t^2)].
```
The last identity follows by factoring the common minimum `k=min(x,y,j)`, then removing the all-positive remainder.

All linear poles of G(t) occur at nineteenth roots with residues among
`{0,5,6,7,8,9,10,11,12,15,16,17,18}`, and the quadratic factors are
`1-zeta^e*t^2` for `e in {2,3,4}`. Every root therefore has order dividing 38. Checking each individual summand gives pole multiplicity at most two: the common U(t) roots 7,8,9 are disjoint from the remaining factors, and the only repeated linear/quadratic poles arise at the indicated coincident residues (notably c=ab=zeta^11). A sum cannot have a pole order greater than its summands.

Each summand is a strictly proper rational function of t (at infinity, `G(t)=O(t^-6)`). Therefore
```text
G(t) = P(t)/(1-t^38)^2,       degree(P) <= 75.
R_(m+76)(zeta) - 2 R_(m+38)(zeta) + R_m(zeta) = 0
for every integer m >= 1.
```
The degree bound follows from properness; this is a rigorous unbounded-threshold recurrence, not a fitted pattern.

Consequently, for `1<=r<=38` and every `k>=0`,
```text
R_(r+38*k)(zeta) =
 R_r(zeta) + k*(R_(r+38)(zeta)-R_r(zeta)).
```

## 3. Exact 38-phase nonvanishing certificate

Represent each `R_m(zeta)` by its 18 coefficients in the integer basis `1,zeta,...,zeta^17` of `Z[zeta]`. The accompanying integer-only verifier computes the first **76** vectors using the genuine joint-load maximum, and checks the historical immutable 1..19 regression vector where applicable.

For **r=1,...,33**, `R_r` and `R_(r+38)` are linearly independent over Q: the certificate contains a NONZERO 2x2 minor in their coordinate vectors for every such r. Thus their affine combination cannot vanish for any real k.

For **r=34,...,38**, the full 18-coordinate vectors obey `R_(r+38)=2*R_r`, with `R_r!=0` in each case. Thus `R_(r+38*k)=(k+1)R_r!=0` for all k>=0.

These 38 cases exhaust the positive thresholds. Since `Phi_19` is the irreducible minimal polynomial of every primitive nineteenth root, nonzero basis vectors imply nonzero evaluation at every such root.

Finally `D(q)` has exactly five factors vanishing at zeta, namely p=228,247,266,285,304. The nonzero numerator supplies an exact fifth-order pole, hence a degree-four primitive-19 character in the coefficient quasipolynomial. Fourier uniqueness forces 19 to divide every coefficient period at error `O_m(N^3)`. QED.

## Validation, model scope and next problem

`VERIFY_ALLM.py` is dependency-free, integer-only arithmetic in `Z[z]/(z^19-1)`, reduced to `Z[z]/Phi_19`. The result artifact `CERTIFICATE.json` contains the 38 nonvanishing witnesses and bounded verifier outputs. A second program `VERIFY_DIRECT.py` enumerates literal seven-mask constraints for independent small-m crosschecking, and tests the 38-step second-difference recurrence beyond its finite basis. The checker recomputes all thresholds m=1..19; exact full-vector regression is asserted for m=1,2, and the prior two-coordinate certificate is asserted for m=15,...,19. The separate literal-load checker independently verifies m=1,2,3,13,19,20,21, with an additional 44 recurrence checks.

This certifies the primitive-19 necessary factor in the frozen R5 scalar model, without a new formal Result or independent mathematical review. Combining it with earlier author-derived full-threshold necessary factors 11,13,16,17 yields the **conditional, cross-result** universal factor `16*17*11*13*19=739024` at error `O_m(N^3)`. The other four derivations retain their own review states.

Next: check the remaining candidate root orders (in particular the factors 3,5,7 and the primitive-24 cancellation) under **genuine intersections**, to determine the all-threshold exact minimum rather than only necessary factors.

**Pinned scientific provenance:** prior 19-phase proof `b6bf656360b90a800043ea2f00cbd706db571386`; genuine-intersection correction `75d986aa23b68a7ecf9b29dc1006f0e322b35a15`; historical m=1 exact-period case `ba976ca1d5ea32392e409b5dec08c1607140a610`. P000 and ACTIVE worldview are unchanged. No BRC/X6 numerical claim is made by this scalar observer.
