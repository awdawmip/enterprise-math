# Intrinsic HBW doubling is etale; the squared defect is normal to the conic

Status: PURE_SYMBOLIC_GEOMETRIC_RESULT / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

The residual cocycle correctly gives ambient Jacobians 2v^2 and 2w^2. This note separates that ambient degeneracy from the intrinsic orbit geometry. It supplies a coordinate-free interpretation of the two native bit maps and a precise connection to the torus square-character tool.

## 1. Domain and the split geometric chart

Work over a commutative base ring R in which 2 and Delta=k^2-4 are units, with k fixed during the dynamics. In particular R may be Z/NZ for odd N with the admitted discriminant. The conic is

    C: F(v,w)=v^2-k*v*w+w^2+Delta=0.

It is smooth. The simultaneous vanishing of F_v=2v-kw and F_w=2w-kv would force v=w=0, since their coefficient matrix has unit determinant -Delta. That would contradict F=0 and unit Delta. This argument holds after every residue-field specialization and gives the relative Jacobian criterion.

Adjoin a root lambda of X^2-kX+1 through the finite faithfully etale quadratic algebra. It is a unit, its other root is lambda^-1, and lambda-lambda^-1 is a unit because its square is Delta. Over that algebra set

    v=z+z^-1,
    w=lambda*z+lambda^-1*z^-1.

Conversely,

    z=(w-lambda^-1*v)/(lambda-lambda^-1),
    z^-1=(lambda*v-w)/(lambda-lambda^-1).

The product of these two proposed inverse coordinates is

    [k*v*w-v^2-w^2]/Delta=1

on C. They therefore give an actual isomorphism between C and the multiplicative group after the splitting extension. Descent exchanges lambda with lambda^-1 and z with z^-1; the original conic is the corresponding norm-one torus, with identity (2,k).

This is a proof chart. The native program does not receive or compute lambda, a modular square root of Delta, or local prime factors. Its actual state remains the ordered pair (v,w).

## 2. The two bit maps have the same intrinsic covering degree

The already implemented polynomial updates are

    D0(v,w)=(v^2-2, v*w-k),
    D1(v,w)=(v*w-k, w^2-2).

Substitution in the geometric chart gives exactly

    D0: z -> z^2,
    D1: z -> lambda*z^2.

The first is doubling in the torus, and the second is doubling followed by translation by the fixed base element lambda. Both descriptions descend to R. Since 2 is a unit, z -> z^2 on the multiplicative group is finite etale of degree two; translation is an isomorphism. These properties descend through the faithfully etale splitting algebra. Thus both native bit maps restricted to C are finite etale covers of degree two everywhere.

There is no intrinsic ramification at v=0 or w=0. Over a finite local field, a target can have zero or two rational predecessors despite the geometric cover always having degree two. Distinguishing rational lifting from geometric degree is precisely where a square character can be useful. No inverse square-root computation or free branch selector is supplied by the geometric degree statement.

## 3. Tangential evolution and normal defect are different objects

The ambient polynomial identities, valid even off C, are

    F(D0(v,w))=v^2*F(v,w),
    F(D1(v,w))=w^2*F(v,w).

The ambient determinants are 2v^2 and 2w^2. They can vanish even while the restricted map on C is etale, because the two-dimensional ambient map also moves the normal direction. Modulo the square of the ideal (F), the pullback on the conormal line is multiplication by v^2 or w^2. A zero or nonunit multiplier can erase normal-defect information; it is not a vanishing tangent derivative of the torus motion.

The intrinsic invariant differential makes the distinction explicit. On the open patches where its denominators are units, put

    omega=dv/(2w-kv)=-dw/(2v-kw).

The equality follows from dF=0, with k fixed. Smoothness makes these expressions glue to a regular nowhere-zero differential. In the split chart,

    omega=[1/(lambda-lambda^-1)]*dz/z.

Consequently both D0 and D1 pull omega back to 2*omega. There is no factor v or w in the intrinsic multiplier. Translation by lambda is constant over the base and does not change dz/z.

For example, on C at v=0 one has w^2=-Delta, so w is a unit. Although the first row of the ambient D0 derivative vanishes, its second row is (w,0), which acts nontrivially on the one-dimensional tangent. The cover remains unramified there. The symmetric w=0 situation for D1 has the same interpretation.

## 4. Research meaning and limits

The two-carry residue chart now has three distinct interfaces: the reversible one-step torus translation, the intrinsic degree-two bit cover, and the ambient defect transport. Their different properties must not be mixed. The earlier residual cocycle remains correct and its warning about failed backward membership inference remains necessary. A terminal zero defect still cannot certify an off-conic input history when a normal multiplier was nonunit.

For parameter/order research, the useful next question is whether rational lifting through the degree-two cover can be characterized and used without factoring. The separate torus square-character note answers one level using k+2 for the base element. A character can label a local lifting obstruction, but it does not construct a root or reveal the unknown odd part of an order. Repeated exponentiation, local-order inference and any selector integration retain separate proof and cost obligations.

No new runtime register, defect observer, square root, character evaluation or scientific fixture was added to the frozen adjacent-trace run. This result is a symbolic geometric clarification available to any authorized continuation. It is not a physical zero-energy argument, a new general factoring algorithm, or Shor closure.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1.
