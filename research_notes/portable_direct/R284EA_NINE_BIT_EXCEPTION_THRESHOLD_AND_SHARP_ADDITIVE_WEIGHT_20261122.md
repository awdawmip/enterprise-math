# R284EA — Sharp nine-bit threshold for the frozen Port quotient exception

Date: 2026-11-22 (Asia/Shanghai)  
Status: `AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED`  
Frozen scientific input: `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py` (blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`); ordered 65,536-codeword SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`. Parent theorem: R284DZ, preserving its seven-bit core quotient and scope.

## Theorem 1 — No-determinant correction predicate

Write the original twelve lower variables as `(u1,a,x,y,u2,w,b,z,u3,g,h,r)∈{1,2}^12`, and four upper mask bits `B0,B1,B2,B3∈{0,1}`. In the sole exceptional six-bit core class `u1=a=x=u2=w=b=2`, set

`(Y,Z,U,G,H,R)=(y-1,z-1,u3-1,g-1,h-1,r-1)`.

Define the **nine-bit score**

```text
S = 13Y + 6Z + 28U + 25G + 11H + 12R + 26B0 + 17B1 + 6B2.
```

For every one of the 1,024 original states in this core class,

```text
1[T < 2879·P] = 1[S >= 77],     P = 17,179,869,143.
```

Here `T` is the frozen unreduced integer determinant, not a floating-point approximation. The fourth upper bit `B3` does not occur. The nine-bit Boolean cube has precisely **223** true inputs, repeated for the two `B3` values, giving the previously certified **446** exceptional states.

Combined with R284DZ, all 65,536 frozen states now have

```text
u=(6-a)(13-b)-xw
p1=(13-b)u1+xu2;    p2=(6-a)u2+wu1
Qcore=floor((13788u-4799p1-4854p2+14)/128)
Q = Qcore - 1[(u1,a,x,u2,w,b)=(2,2,2,2,2,2) and S>=77]
z = T - Q·P
```

The **quotient correction** is determined by nine source bits, with no use of `T` in its decision. `T` remains an input to the final residue calculation, and the original farthest-arc observation remains a separate stage.

### Exact finite proof

The companion checker enumerates all 512 nine-bit assignments and compares `S>=77` with the pinned determinant condition `T<2879P`; it repeats the classification with `B3=1`. It observes

```text
max score among false cases = 76
min score among true cases  = 77
maximum (T-2879P) among true cases  = -27,577
minimum (T-2879P) among false cases = +41,823
```

Thus there are no equality/rounding ambiguities at either boundary. The checker separately enumerates all 65,536 original states, checks the reconstructed quotient against `T//P`, the reconstructed remainder against `T%P`, and verifies the original frozen ordered-codeword digest. These integer assertions provide finite exhaustive proof for the exact frozen domain.

## Theorem 2 — The total integer weight 144 is optimal

Consider **all** classifiers on precisely the nine Boolean coordinates above with an integer additive score `Σ c_j b_j`, arbitrary integer coefficients `c_j`, and an integer threshold `θ`, with true cases scoring at least `θ` and false cases at most `θ-1`. Then

```text
Σ_j c_j >= 144.
```

Consequently, the explicit nonnegative coefficients in Theorem 1, summing to `144`, minimize the total integer coefficient weight in this specified circuit language (even allowing signed candidate coefficients).

An **exact ten-witness certificate** proves the lower bound. Bit order throughout this table is `Y Z U G H R B0 B1 B2`.

| True witness bits | Multiplicity α | False witness bits | Multiplicity β |
|---|---:|---|---:|
| 001000111 | 25 | 001100011 | 36 |
| 010111011 | 23 | 001111000 | 41 |
| 011101001 | 45 | 011100010 | 11 |
| 101110000 | 51 | 011110001 | 6 |
| | | 110100101 | 24 |
| | | 111011001 | 26 |

All four left witnesses have score **77** and determinant `T<2879P`; all six right witnesses have score **76** and determinant `T>=2879P`. Their multiplicities sum to 144 on each side. Direct nine-coordinate integer summation gives

```text
Σ_true α·b − Σ_false β·b = (1,1,1,1,1,1,1,1,1).
```

For any correct integer additive threshold classifier, multiply each true witness inequality by α and each false witness inequality by β. Subtract the latter from the former. The thresholds cancel and the unit margin yields `Σ c_j >=144`. The explicit weight vector meets this bound.

The score formula also makes the correction monotone in each of its nine input bits. Exhaustive pairwise flips show that **every** bit is essential: the numbers of opposite-label edges per coordinate `(Y,Z,U,G,H,R,B0,B1,B2)` are respectively `(45,21,111,95,41,43,103,61,21)`. This is an exact Boolean support statement, not a statement about native X6 coordinates.

## Reproduction, scope, and next work

Run `python R284EA_nine_bit_exception_threshold_checker.py` next to the previously published R284DX module. Its JSON certificate records all witness constraints, integer thresholds, bit influences, 512-bit-cube and 65,536-state coverage, and frozen-codeword digest. Integer arithmetic is exact; this is an author-proved, computationally certified frozen auxiliary Port result, currently **NOT_REVIEWED**. No formal Task/CLAIM or Activity association is inferred from source publication.

Next test whether the new nine-bit predicate and R284DZ's seven-bit quotient stage provide a measurable **end-to-end** improvement after accounting for determinant generation, integer bit lengths, R284DS arc-envelope preprocessing, observation and output recovery. A different nonlinear circuit language or signed representation may have different optimality parameters.
