# CBRC F7 r474 — exact constrained gauge space and the off-axis positivity obstruction

Date: 2026-11-22 (Asia/Taipei).
Research: original RESEARCH_DRIVER logical lane `EM-DVR-DEBB5E`. Original F7 Task, frozen Result and scientist `EM-CBRCF7-83A1D4` retain their actual authorship, Source and admission status. This is a new algebraic structural result about the same exact F7 shear operator, not an independent review or a native admitted Result.

## Frozen operator and exact scope

For every real-valued `q: Z² -> R` put `k=a-2b-c+2d` and
```
D_q(a,b,c,d) = q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).
```
Use the already proved r473 exact kernel identity
```
D_g == 0  <=>  g(x,y) = A(x-y)+B(x-2y)
```
for arbitrary `A,B:Z->R`, with uniqueness up to a constant. No symmetry or sign bound was imposed on that kernel in r473.

Call a gauge `g` *linearly F7-compatible* if it obeys the homogeneous requirements corresponding to the original F7 scalar conditions:
```
g(-x,y)=g(x,y) for every x,y in Z,
g(x,0)=0 for every x in Z,
g(2,1)=g(-1,-1)=0.
```
These are the original first-coordinate evenness, prescribed axis/origin values, and two fixed marks *for differences of admissible functions*. The nonhomogeneous off-axis inequality `q(x,y)>=1/2` for `y!=0` remains separate. No claim is made that an arbitrary compatible gauge preserves this inequality for a given q.

Define the exact mod-three sign function `s:Z->{-1,0,1}` by
```
s(n)=0 if n=0 (mod 3), +1 if n=1 (mod 3), -1 if n=2 (mod 3).
```

## Theorem — exactly two dimensions survive the linear F7 constraints

Every linearly F7-compatible global zero-defect gauge is uniquely of the form
```
g_{c,b}(x,y) = A_{c,b}(x-y)-A_{c,b}(x-2y),   c,b in R,
A_{c,b}(n)  = c*n + b*(-1)^n + (2*b-c)*s(n).
```
Thus the intersection of the infinite-dimensional shear kernel with the original F7 *homogeneous linear* constraints is precisely a **two-dimensional real vector space**, with explicit basis `g_{1,0}` and `g_{0,1}`.

Moreover, if such a gauge is nonnegative at **every off-axis lattice point**, then it is identically zero:
```
D_g=0, homogeneous F7 scalar constraints, g(x,y)>=0 for all y!=0
       =>  g=0.
```
In particular, no nonzero fixed additive global gauge preserves the entire original F7 admissible class: the admissible baseline `q_base(0,0)=0`, `q_base(x,0)=1` for `x!=0`, and `q_base(x,y)=1/2` for `y!=0` is mapped outside the class by any nonzero compatible gauge.

## Proof — completeness, not just construction

**1. Axis reduction.** By the r473 kernel theorem, `g(x,y)=A(x-y)+B(x-2y)`. The zero-axis condition `g(x,0)=0` for every integer x forces `B(n)=-A(n)`. Hence
```
g(x,y)=A(x-y)-A(x-2y).
```
Every pair `(m,n)=(x-y,x-2y)` is attained by a unique `(x,y)=(2m-n,m-n)`; therefore the only invisible variation of A is an additive constant.

**2. Restriction from evenness at y=1 and y=2.** Let `d(t)=A(t)-A(t-1)`. At `y=1`, evenness gives
```
d(t)=d(-t-2)    for every t in Z.                       (1)
```
At `y=2`, and using (1) on the reflected side, it gives
```
d(t)+d(t-1)=d(t+2)+d(t+3)                               (2)
```
for all integers t. With the invertible shift `Sd(t)=d(t+1)`, the shift of (2) becomes
```
(S^4+S^3-S-1)d=(S+1)(S^3-1)d=0.
```
As `(S^6-1)=(S^3-1)(S+1)(S²-S+1)`, this implies `d(t+6)=d(t)`.

Write `d_i=d(i)`, subscripts modulo 6. Equation (1) forces `d_0=d_4` and `d_1=d_3`. Equation (2) then forces `d_5=d_1+d_2-d_0`, and its remaining translates add no further conditions. Therefore the possible derivatives constitute a real vector space of dimension at most three, parametrized by `(d_0,d_1,d_2)`.

The three sequences
```
d^{lin}(n) = 1,
d^{par}(n) = 2*(-1)^n,
d^{mod3}(n)=s(n)-s(n-1), with mod-3 pattern [1,1,-2]
```
obey (1)–(2) and are independent: their columns on indices `n=0,1,2` form the matrix
```
[ 1   2   1 ]
[ 1  -2   1 ]
[ 1   2  -2 ]
```
whose determinant is 12. Thus every possible derivative is exactly a unique combination `c*d^{lin}+b*d^{par}+e*d^{mod3}`. Integrating the derivative over Z gives
```
A(n)=c*n+b*(-1)^n+e*s(n)+constant.
```
The constant cancels in g.

**3. Sufficiency for all y, not just y=1,2.** The linear term gives `g(x,y)=c*y), independent of x. For the parity term,
```
(-1)^(x-y)-(-1)^(x-2y) = (-1)^x*((-1)^y-1),
```
also even in x. For the mod-three term, `s(-n)=-s(n)` and `2y ≡ -y (mod 3)`; hence
```
s(-x-y)-s(-x-2y) = -s(x+y)+s(x+2y)
                 = -s(x-2y)+s(x-y),
```
which proves evenness for every x,y. All three terms give zero on y=0.

**4. The original two marks are one independent equation.** Here
```
g(2,1)=A(1)-A(0)=c-2b+e,
g(-1,-1)=A(0)-A(1)=-(c-2b+e).
```
Both marks vanish exactly when `e=2b-c`. The resulting `g_{c,b}` are unique because g determines A up to a constant and the three derivative sequences are independent. Thus the dimension is exactly two.

**5. No everywhere-nonnegative nonzero gauge.** In `g_{c,b}`, the parity and mod-three contributions are bounded periodic functions of x and y, while the linear contribution is `c*y`. Fix x=0 and send y through integers of a fixed residue class modulo 6 to `+infinity` and `-infinity`. Unless `c=0`, `g(0,y)` is negative in one direction. With `c=0`, the formula gives exactly
```
g_{0,b}(0,1)=-6b,     g_{0,b}(0,-1)=2b.
```
Both can be nonnegative only when `b=0`. Thus g=0.

## Scoped exact verification and research significance

An independent integer-only check evaluated the three coefficient pairs `(c,b)=(1,0),(0,1),(2,3)`, verified all evenness/axis/mark equalities on `[-9,9]^2`, and found exact `D_g=0` on every one of the `7^4=2401` original input quadruples in `[-3,3]^4`. These finite tests corroborate the algebraic argument; the complete proof is the shift-recurrence and explicit basis proof above.

**Consequence for global F7 optimization.** The unrestricted r473 approximation `dist∞(q,ker D)≤E∞(q)/2` does not by itself produce an F7-admissible approximation. Even after enforcing all homogeneous linear F7 restrictions, there remain two gauge directions; neither is a universally safe positivity-preserving adjustment. A genuine global minimax reduction must carry the off-axis inequality and the two-dimensional residual gauge parameters together, not quotient out the entire kernel.

This is a proved structural subunit about `D_q` and the linear F7 constraints; it does not resolve `E_{15}^*=1/2` or improve the full-lattice bracket `1/2≤E_∞^*≤4/7`. No Lean claim, custom axiom, Native Review, Result acceptance, Task completion, parent closure, or fresh CLAIM is asserted.

Dependencies with immutable evidence:
- r473 exact unrestricted gauge kernel and stability: `enterprise-math@fbb6b8bec82c41a3708d4373ea075314fb05b2ed:research_notes/driver/2026-11-22_f7_r473_exact_gauge_kernel_and_sharp_global_stability.md`.
- r471 exact fiber-swap formula: `enterprise-math@013c38ab95d45a1c5fc6f3e583d6e62e688395f7:research_notes/driver/2026-11-22_f7_r471_exact_fiber_swap_global_quarter_audit.md`.
