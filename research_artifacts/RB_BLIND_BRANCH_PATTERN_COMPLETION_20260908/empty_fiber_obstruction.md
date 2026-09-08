# Blind obstruction to a geometrically square empty fiber

Status: exact partial theorem for the remaining 4+2 branch pattern. It excludes its geometrically trivial empty-fiber square classes, not the entire pattern. The 2+2+2 pattern is untouched. No map, period normalization, final raw freeze or unblinding is asserted.

Researcher: EM-HODGEH0O-82EF42, under the unchanged canonical RB task, TP2, ER and winning claim. Inputs are only the two task-whitelisted mathematical sources at `c73816d3552b4247861e12e476101e94a4a2ce5a` and our own blind checkpoints. The corrected square-class/RR checkpoint was reported by the owner as published at `2a2b39cc41b96c827df83cbe42f6c1882da05894`. Its corrected checker and certificate are pinned by the accompanying checker. The previously rejected RR sign draft is not used.

## 1. Statement and exact scope

Let C: t^2=R^3-3R, with the same origin O, six branch points B=T union {P,-P}, source cover w^2=(R+2)t, and fixed nonzero k from the task. Let X have degree six on C and satisfy the target-cover and differential equations with the task's local ramification conditions. Suppose its branch assignment is 4+2+0+0. Use an actual target V4 transformation to put an empty special fiber at infinity. If e is its other, finite empty special value, then

**The geometric square class of X-e is nontrivial.**

Here geometric means over an algebraic closure. Consequently no extension of the coefficient field and no constant-square-class adjustment can rescue a geometrically trivial case. This theorem does not claim descent or exclude any nontrivial unramified class.

For the corrected normalized certificate, the base representative of the finite empty fiber is 1. The theorem therefore removes precisely the four compatible twist triples with T_e=O from each of the 45 fixed-parameter assignments. It removes 180 of 720 components, leaving 540 for 4+2 and all 1440 for 2+2+2. These counts describe parameter components, not maps, solved systems or probabilities.

## 2. A degree-three function and its mandatory branch triple

Suppose for contradiction that X-e is geometrically square. Absorb a nonzero constant symbolically and write X=e+g^2. Then g is a rational function of degree three on C. No root is numerically evaluated in this argument.

Let a be the special value containing four branch points. It is distinct from e and from infinity. Over the algebraic closure, X=a corresponds to two distinct nonzero values of g. Each of these two g fibers has degree three. At every one of the four source branch points the multiplicity of X-a, hence of the corresponding g-value fiber, is one. At all other points of these fibers the multiplicity is even, by the prescribed source-cover square class; since the g fiber has total degree three, that multiplicity can only be two.

Each fiber thus contains an odd number, either one or three, of the four distinct branch points. The split is necessarily 3+1. In particular a complete g fiber is a divisor [U]+[V]+[W] of three distinct points in B, each simple.

Let D_g be the degree-three pole divisor of g. On the elliptic curve, its class is therefore

D_g ~ [U]+[V]+[W] ~ 2[O]+[S], where S=U+V+W.

This step supplies a finite restriction on the pole class. It is not an arbitrary choice of pole normalization.

## 3. The ten possible pole classes

There are twenty triples of six distinct branch points. Their group sums lie in exactly

C[2] union {P+T,-P+T: T is a nonzero two-torsion point}.

This is a ten-point set. Three points of C[2] sum to the remaining two-torsion point; one two-torsion point together with P and -P sums to that two-torsion point; two distinct two-torsion points sum to a nonzero T. Distinctness of the six translates follows because P is not two-torsion and 2P is not two-torsion, as proved in the first blind assignment checkpoint. The finite integer certificate enumerates every triple and its sum, without evaluating an elliptic addition formula numerically.

Put s=sqrt(3) as a formal algebraic generator and L=Q(s). Every finite horizontal coordinate u=x(S) of these ten points belongs to L. For the two-torsion points the coordinates are 0,s,-s. For the translates, the usual chord law, with P=(-2,i sqrt(2)), gives

x(P+T0)=x(-P+T0)=3/2,

x(P+Tplus)=x(-P+Tplus)=7s-12,

x(P+Tminus)=x(-P+Tminus)=-7s-12.

These are unevaluated paper identities. Equivalently, for r in {0,s,-s}, the translation formula obeys

(x(P+T_r)-r)*(-2-r)=3r^2-3.

For r=0 one may clear the denominator as 2x=3. For r=+/-s, use (2+s)(2-s)=1 to obtain the displayed polynomial expressions. Negating a point preserves x.

The permitted constant is k^2=12sqrt(2)-10sqrt(3), which is not in L. Indeed sqrt(2) is not in Q(sqrt(3)): writing sqrt(2)=a+b sqrt(3) with rational a,b and squaring forces ab=0; the two possibilities would make either 2 or 2/3 a rational square, contradicted by the parity of the prime exponents. Thus the nonzero sqrt(2) coefficient in k^2 cannot disappear. This is a characteristic-zero algebraic-field statement, not a computed real approximation.

Two useful consequences hold for every finite candidate S=(u,v):

1. S is neither Q nor -Q for any of the three prescribed critical points. Otherwise u^3-3u=k^2 would put k^2 in L.
2. Both v-k and 18u+k^2 are nonzero. The former, if zero, again gives v^2=k^2=u^3-3u in L; the latter directly puts k^2 in L.

These facts will justify every denominator clearing at the critical points. They avoid treating a spurious zero caused by a singular basis formula as a geometric solution.

## 4. Criticality includes ordinary values, special values and poles

The whitelisted reduction proves that the three points Q with t=-k are distinct, have finite distinct R coordinates, avoid the source branch divisor, and lift to the six simple zeros of the prescribed differential on D. A valid pullback map has ramification index two at each lift. Therefore the local degree of X at Q is two at an ordinary target value and four at a special target value.

If g(Q)=0, then X=e and the local degree of X is twice the local degree of g, giving degree two for g. If g has a pole at Q, the same statement applies at infinity. If g is finite and nonzero, the squaring-and-translation map is unramified there: an ordinary X value gives local degree two for g; a remaining special X value would give local degree four for g, already impossible because deg(g)=3.

Thus in every noncontradictory case all three Q are critical points of g. This is a local-degree argument. It does not infer criticality from a rational derivative before checking zero or pole cancellations.

If S=O, the preceding corrected RR paper already excludes this situation by the independent L(3O)=<1,R,t> argument, including the pole case. It suffices below to consider finite S in the ten-point set.

## 5. General finite pole class and an exact determinant

For S=(u,v) finite, with v^2=u^3-3u, a basis of L(2[O]+[S]) is

1, R, h=(t+v)/(R-u).

For v!=0, h has a simple pole at S and at O; the apparent pole at -S is removable. For v=0, R-u has order two and t order one at S, again giving a simple pole. These three sections are independent and the positive-degree genus-one RR theorem gives dimension three. Since the actual pole divisor of g is linearly equivalent to 2[O]+[S], we may write

g=(a*h+b*R+c)/(d*h+e1*R+f)

with independent, basepoint-free numerator and denominator sections. Write their minors

A=a*e1-b*d, B1=a*f-c*d, C1=b*f-c*e1.

The checker labels these three minors A,B,C. If all three vanish, g is constant, a contradiction.

For compactness put

U=(R-u)^2*(2delta h)=R^3-3uR^2+3R+3u-2vt.

The cleared derivative numerator for g is

W=A*[R*U-2t*(t+v)*(R-u)]+B1*U+2C1*t*(R-u)^2.

At each Q all factors R-u are nonzero by section 3. For finite g values the usual derivative criterion applies. At a pole, use the numerator and denominator as local sections: they do not vanish together and a pole of local degree at least two again forces the section Wronskian to vanish. Multiplication by (R-u)^2 has not created or removed this condition. Consequently W vanishes at all three Q.

Restrict to t=-k and use their cubic R^3-3R-k^2=0. The remainder is a quadratic in R whose three coefficients are the following matrix times (A,B1,C1):

M =

| | A | B1 | C1 |
| --- | --- | --- | --- |
| R^2 | 6 | -3u | -2k |
| R | -k^2-6u+4vk | 6 | 4ku |
| 1 | -uk^2-2uvk | k^2+3u+2vk | -2ku^2 |

Since the three R values are distinct, M*(A,B1,C1)^T=0. Integer polynomial expansion, using only v^2=u^3-3u, yields

det(M)=2k*(v-k)^2*(18u+k^2).

Section 3 shows all three factors are nonzero for the ten possible pole classes, and k!=0 is already a permitted premise. Hence the minors all vanish. The supposed degree-three function is constant, contradicting its degree.

This proves the theorem. In particular it extends the earlier pole-class-3O exclusion to every possible pole class for this geometrically trivial empty fiber. It does not claim that the determinant describes all degree-three maps at the excluded basis-degenerate values S=+/-Q; those values were ruled out first by the exact branch-triple field constraint.

## 6. Actual execution and remaining task

The accompanying task-local checker independently differentiates the displayed h numerator and denominator with the integer derivation 2delta. It verifies the matrix after the critical-divisor substitution, its determinant factorization, and rejection of a one-coefficient matrix alteration. All operations are integer polynomial additions and multiplications with formal curve-relation rewrites. It then enumerates all twenty triples and identifies the four excluded compatible twists at each of the 45 already-frozen assignments. It reads the corrected prior certificates; it does not rerun the original assignment search or historical checker.

The actual first certificate has SHA256 `1757b252b5926bcda198e4a652259e8d46da4cd3a32464ae66c09f3d403eafb9`. It records three checked integer identities and the exact component counts 180 excluded, 540 remaining in 4+2, and 1440 untouched in 2+2+2. The selected static V2 gate passed for the new checker. No numerical division, remainder, root, rational-function evaluation or BRC call occurred. The field, divisor and local-degree implications above are paper arguments, not claims of an independent generator replication.

The remaining 1980 components still require actual RR/ODE solutions or obstructions. In 4+2 the finite empty fiber now has one of the three nontrivial unramified geometric classes; the 2+2+2 components keep all sixteen compatible twists per assignment. No original-field descent, explicit X/Y, basepoint, absolute period or task terminal result has been obtained. The source remains blind and this checkpoint is not an unblinding authorization.
