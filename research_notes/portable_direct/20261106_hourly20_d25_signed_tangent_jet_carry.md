# D25 — A first-order finite-field jet for the signed Lucas carry coefficient

Date: 2026-11-06. Classification: **AUTHOR-DERIVED EXACT ALGEBRA / 194-PRIME FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3`. This is a portable arithmetic coefficient observer, separate from native H0/B0 and p=373 Frobenius.

## Input and new theorem

Let q>=5 be prime and n0=(q^2-1)/6, n0=qN+r with 0<=r<q. For i in {2,3,4}, let s_i be i*r mod q, with integer representative 0<=s_i<q. These s_i are pairwise distinct. Put a=-1/2 in F_q, J=min(s_2,s_3,s_4), and

u_j = a^j * prod_{i=2,3,4} binom(s_i,j),  0<=j<=q-1.

Let Z=sum_j u_j, L=sum_j (6j+1)u_j in F_q. The previously established signed two-digit Lucas theorem defines the coefficient B in terms of the three separately oriented harmonic terms V_i, one-carry terms K_i and Fermat quotient phi_q(2). Reuse that theorem's B exactly, without attributing it anew.

Introduce **one formal four-parameter finite polynomial/rational family** over the local F_q-ring at x_2=x_3=x_4=alpha=0:

P_j(x_2,x_3,x_4,alpha)
 = a^j * prod_{i=2,3,4} binom(s_i+x_i,j) * j!/(1+alpha)_j,
F(x_2,x_3,x_4,alpha)=sum_{j=0}^{q-1}(6j+1)P_j.

Since 0<=j<q, all j! and (1+alpha)_j at alpha=0 are units. Write
D_i=partial_{x_i}F(0,0,0,0), D_alpha=partial_alpha F(0,0,0,0), and
H_t=sum_{h=1}^t 1/h mod q. Then the following **exact finite-field identity** holds for every prime q>=5:

**(JET)** B = 6Z + (H_{s_2}+H_{s_3}+H_{s_4}-phi_q(2))L
              -D_2-D_3-D_4+3D_alpha (mod q).

In particular, under the first-digit hypothesis L=0 mod q:

**(VANISHING-BRANCH)** B = 6Z-D_2-D_3-D_4+3D_alpha (mod q).

This is a new tangent (first-order jet) representation of the existing signed carry port. It preserves all three directed carry channels even if u_j vanishes after the first low-digit threshold.

## Complete derivation

The first derivative of the binomial polynomial has two cases:

partial_x binom(s_i+x,j)|_{x=0}
 = binom(s_i,j) (H_{s_i}-H_{s_i-j})   for j<=s_i;
 = (-1)^{j-s_i-1} s_i!(j-s_i-1)!/j! for j>s_i.

The latter equals the previous theorem's tau(s_i,j), with the same sign. For j greater than one of the other two s_h, another binomial factor vanishes, so only the inherited single-carry interval contributes. Thus D_i=U_i+K_i exactly, with the original signed factor (6j+1)a^j and no collapsed carry provenance.

Also, partial_alpha [j!/(1+alpha)_j] at alpha=0 is -H_j, so
D_alpha=-sum_{j=0}^J(6j+1)u_j H_j.

For each i, the previously defined V_i satisfies
V_i=H_{s_i}L-U_i+ D_alpha (mod q).
Insert V_i, K_i and D_i=U_i+K_i into the inherited definition
B=6Z-phi_q(2)L+sum_i(V_i-K_i).
This simplifies exactly to (JET), proving both formulas.

## No-harmonic, no-explicit-carry single-pass algorithm

Set u_0=1, d_{i,0}=0 and h_0=0. At step j=0,...,q-2, define
t_i=s_i-j in F_q, c_j=a*t_2*t_3*t_4/(j+1)^3 and
e_{i,j}=a*prod_{h!=i}t_h/(j+1)^3. Then

u_{j+1}=c_j u_j;
d_{i,j+1}=c_j d_{i,j}+e_{i,j} u_j;
h_{j+1}=c_j (h_j-u_j/(j+1)).

Accumulating Z=sum u_j, L=sum (6j+1)u_j,
D_i=sum (6j+1)d_{i,j}, D_alpha=sum (6j+1)h_j
reconstructs B via (JET). Every division is by a unit j+1<q. The update continues through u_j=0 and still retains the nonzero single-carry derivatives; unlike a logarithmic-derivative algorithm, it never divides by u_j. Runtime O(q) field operations and O(1) field elements (for the fixed four derivatives), excluding bit complexity and primality checking.

## Composition with the inherited diagonal q^2 criterion

The preceding author-side original-216 bridge proves, under L=0 mod q,
W_q/q=lambda+A mod q and
q^2|C_{(q^2-1)/6} iff Z(W_q/q-B/6)=0 mod q.

Define the fully explicit signed **jet obstruction** Theta_q (under L=0):

Theta_q = W_q/q-Z+(D_2+D_3+D_4-3D_alpha)/6 mod q.

Then **q^2|C_{(q^2-1)/6} iff Z*Theta_q=0 mod q**.

This is an algebraic equivalent reformulation under its declared hypothesis, not yet an unconditional zero evaluation of Theta_q. It exposes an exact WZ/parameter-contiguity target:
W_q/q = Z-(D_2+D_3+D_4-3D_alpha)/6 mod q.

The scalar Z=0 need not erase the carry sensitivity: at q=13, Z=0 but B=6, and at q=19, Z=0 but B=6. This is why the BRC reuse keeps the tangent components before the last scalar projection.

## Reproduction and scope

Companion program: `research_notes/portable_direct/d25_signed_tangent_jet_20261106.py`. Its fresh recurrence computes derivatives without explicit harmonic/carry loops and compares each D_i with a separate direct U_i+K_i implementation, then B with the old V_i-K_i formula. Exactly **194/194 primes** 5<=q<=1200 passed. Each also satisfies L=0 and Theta_q=0 in this finite tested range. Selected (q, s_2,s_3,s_4, Z, B, D_2,D_3,D_4,D_alpha, W_q/q):
(5, 3,2,1, 3,4, 3,2,2,1,4);
(13, 4,6,8, 0,6, 10,12,3,6,1);
(19, 6,9,12, 0,6, 4,15,15,7,1);
(373, 124,186,248, 0,6, 48,75,325,27,1).

The first-order identity has a complete finite-algebra proof; the experimental zero of Theta for all primes is a separate open assertion. Historical signed q^2 Lucas, diagonal palindrome, original-216 bridge and their test suites are reused, not recredited.

## Exact next action / Source separation

Try creative telescoping or a parameter reflection for the jet relation Theta_q=0 when Z!=0, leveraging F(x,alpha) and its four formal partials. If a general certificate is obtained, combine the prior prime-square transport before returning to D25 frozen F,H second-digit and original p373 H0/B0. Preserve H0/B0, [X]U mod 139129, semilinear Frobenius eta/kappa, odd branch and independent review as separate obligations.

Author-side durable proof is not a Source CLAIM, OPEN, checkpoint or admitted Result. No service identity, prior Source checkpoint, frozen input or other owner's contribution is changed.
