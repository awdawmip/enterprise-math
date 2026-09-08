# Remaining nontrivial empty fibers: the exact critical numerator

Status: necessary differential constraints only. No additional component is excluded. The current exact residual is 540 components in 4+2 and 1440 in 2+2+2.

This is the next bounded unit of the same authorized blind RB task and claim, by EM-HODGEH0O-82EF42. The permitted source set is unchanged. Inputs are the corrected RR certificate (`d861e5b4d9d5b562c7e2a972c56b30144f2cd41275963f80a3aa80c5f1d3a289`) and the preceding empty-fiber obstruction certificate (`1757b252b5926bcda198e4a652259e8d46da4cd3a32464ae66c09f3d403eafb9`). No originating map, field-of-definition answer, coefficients, basepoint, period, replay or external research was read.

## 1. The three remaining twists and their actual degrees

Normalize the two empty fibers of a 4+2 assignment as before. Its finite empty fiber now has one of the three nontrivial unramified geometric classes

gamma_T=R-r_T, with r_T=0,s,-s and s^2=3.

Work geometrically over an algebraic closure for this necessary-condition argument; a constant square factor may be absorbed symbolically. Put zeta^2=gamma_T and X=e+g^2, where

g=zeta*u.

The curve C_T here means the normalization of this algebraic extension of C, not an evaluated square root at any native coordinate. Since div(gamma_T)=2[T]-2[O] and the square class is nontrivial, C_T -> C is a connected unramified double cover, including at O and T after normalization. It has genus one. Pulling the degree-six X back to C_T gives degree twelve, so **g has degree six**, not degree three. The earlier degree-three obstruction must not be copied to this case.

Write the degree-three half-pole divisor on C as D_infinity ~ 2[O]+[S]. The corrected RR construction supplies

d in L(2[O]+[S]), n in L(3[O]+[S]-[T]), and u=n/d.

Each space has degree and dimension three on the genus-one curve. This uses the same class parameter S, without setting S=O. The two section spaces differ by the nontrivial two-torsion line bundle. Exact degree, nonzero and cancellation conditions still apply. These are geometric RR spaces, not evaluated bases or arithmetic descent data.

## 2. Differentiation without discarding the connection term

Let D=2delta. On C it is the integer derivation

D(R)=2t, D(t)=3R^2-3, D(s)=0.

Differentiating zeta^2=gamma_T gives zeta*D(zeta)=t, because D(gamma_T)=2t. Multiplying by zeta gives gamma_T*D(zeta)=t*zeta. No square root or quotient is numerically evaluated.

For g=zeta*n/d define

W_T=t*n*d+gamma_T*((D n)*d-n*(D d)).

The exact cleared identity is

gamma_T*[(D(zeta*n))*d-zeta*n*(D d)]=zeta*W_T.

Thus the term t*n*d is compulsory. The accompanying checker verifies this as an integer polynomial ideal-membership identity. With formal zeta and Dzeta, the difference of its two sides is

n*d*[zeta*(zeta*Dzeta-t)-Dzeta*(zeta^2-gamma_T)],

an explicit combination of the differentiated-cover and cover relations. This does not add an unproved differential axiom.

## 3. Correct local interpretation at all six lifts of Q

At each of the three prescribed Q on C, t=-k!=0 and gamma_T is a unit: if R=r_T then t=0, contradicting k!=0. The normalized double cover is unramified there and zeta is a unit. The base derivation D is nonvanishing there as well.

The fixed pullback differential requires local degree two for X at an ordinary value and four at a special value, exactly as in the earlier proof. If g is zero or has a pole, the squaring map doubles its local degree, so g must have local degree two. If g is finite and nonzero, an ordinary X value gives local degree two for g; another special value gives local degree four. The latter is now possible because deg(g)=6. In every case, g must be critical at each lift of each Q. The sign of zeta does not change this necessary condition.

Use regular local numerator and denominator sections N,D0 with no common zero. Gamma and zeta are units at Q. For a finite g value with D0(Q)!=0, vanishing of the corresponding W_T is the usual derivative criterion. If N(Q)=0, the criterion becomes the vanishing of its first derivative, detecting zero order at least two. If D0(Q)=0 and N(Q)!=0, the criterion becomes the vanishing of the first derivative of D0, detecting pole order at least two. These statements use the nonvanishing local derivation; they do not compare values of a displayed rational derivative at a pole.

For a common frame factor rho, direct differentiation gives

W_T(rho*n,rho*d)=rho^2*W_T(n,d).

Consequently a common factor that vanishes at Q must be removed in the local section frame before testing criticality. A nonunit factor cannot be left in place and then counted as a critical zero. The checker verifies the scaling identity without assuming rho is a unit, and the paper uses the regular frame to make the evaluation meaningful.

After such local normalization, the three necessary conditions are

W_T(Q_i)=0, for i=1,2,3.

On an actual regular RR basis chart these are three bilinear scalar equations in the three numerator and three denominator coefficients. Exceptional basis charts require the same exact local-frame treatment; none is silently removed or accepted.

## 4. Two decisive guard examples

Set n=d=1. Then the true numerator is W_T=t, so its value at Q is -k!=0. Omitting the connection term would instead produce zero and falsely report criticality. This is a counterexample to the incorrect differential predicate, not a new degree-six task map: g=zeta in this example has lower degree.

Next multiply both sections by rho=t+k. The unnormalized numerator is (t+k)^2*t and vanishes at every Q. The regular-frame numerator remains t and is nonzero there. Thus counting zeros before cancelling a common local frame would also give a false criticality assertion. Again this is a formula guard example, not an admissible reconstruction.

Both examples are checked for all three nontrivial gamma choices by integer polynomial identities. No point coordinates or roots are evaluated.

## 5. What was actually checked and what remains

The first actual run of `check_twisted_critical_numerator.py` produced certificate SHA256 `a36593100cdc3a67465c45b1569222349575cda61660576595e4541df5056ef8`. It verified six derivative/frame identities and six missing-term/nonunit-frame counterexamples across the three twists. The selected static V2 gate passed for the one new script. There were zero evaluated divisions, roots, rational-function values or BRC calls.

No new component has been ruled out or solved. The three bilinear conditions are only necessary: the finite branch-fiber equations at the fixed target lambda, exact degree and local valuations, full cover and ODE identities, nonzero scale, field descent, basepoint and absolute period remain separate gates. This construction is for the 4+2 empty-fiber situation and is not asserted as a reduction of 2+2+2. The preceding 180-component exclusion and 1980-component residual remain unchanged. No final raw freeze or unblinding has occurred.
