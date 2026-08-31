# R025 Law Matrix

Researcher-ID: `EM-R025-1B6E63`  
Status: `NOT_CANONICAL`  
Evidence vocabulary: `EXACT_PROVED_OR_DERIVED`, `EXHAUSTIVE_FINITE_CONFIRMED`, `STATISTICALLY_SUPPORTED`, `CONJECTURAL`, `KILLED_WITH_COUNTEREXAMPLE`.

| ID | Frozen candidate / new law | Status | Result / weakest current assumptions | Attack / witness |
|---|---|---|---|---|
| H1 | Extremal envelope | `EXACT_PROVED_OR_DERIVED` | Identity or common monotone operation layer; positive integer lifts; arbitrary exponent word. DOWN/UP are pointwise extrema of every endpoint-selector path and ALL_ENDPOINTS support. | 240,480 reference checks, 0 violations; operation probes preserve H1 |
| H2 | Physical monotonicity | `EXACT_PROVED_OR_DERIVED` | Identity pure tower: DOWN normalized nonincrease, UP nondecrease. Not operation-free. | 0 reference violations; `+1` and `×2` operations give immediate counterexamples to raw monotonicity |
| H3 | Near/far complement | `EXACT_PROVED_OR_DERIVED` | Same nonexact integer basin. Opposite endpoints; error magnitudes sum to G; outputs sum L+U. | Algebraic derivation; no midpoint ties |
| H4 | p-power covariance | `KILLED_WITH_COUNTEREXAMPLE` | False for DOWN/UP/NEAREST/FARTHEST. | DOWN: p=2,a=2,n=3 gives 9 vs 4; others at p=2,a=2,n=2 |
| H5 | Aligned precision freeze | `EXACT_PROVED_OR_DERIVED` | Constant p, every `r_t=a_t^p`, identity between lifts/collapses. | Direct perfect-power algebra; 240,480 reference checks, 0 violations |
| H6 | p-power-free kernel reduction | `KILLED_WITH_COUNTEREXAMPLE` | False: p-power factor changes root microphase. | p=2,r=8=2^2*2; policy-specific witnesses frozen |
| H7 | Precision scaling | `EXACT_PROVED_OR_DERIVED` | Fixed exact physical x. Finite law is 1/M inside root plateau; envelope asymptotic M^-1/p with exact binomial bounds. | 60 cross-precision p/x families through p=32 |
| H8 | Exponent sparsification / phase | `EXACT_PROVED_OR_DERIVED` | `k_p` nonincreasing; k=1 iff n<2^p. Other error/variance metrics nonmonotone due phase/exact hits. | 310,031 root checks; minimal up/down metric witnesses |
| H9 | 50/50 not locally unbiased | `EXACT_PROVED_OR_DERIVED` | Every nonexact natural state. Drift = G/2-d; G odd, so drift never zero. | 150,015 one-step exact checks |
| H10 | Distance-weighted martingale | `EXACT_PROVED_OR_DERIVED` | Identity precision tower, deterministic/predictable exponent/refinement schedule. | Exact conditional expectation proof; 18,180 multilayer cases |
| H11 | Stochastic variance law | `EXACT_PROVED_OR_DERIVED` | Same as H10. One-step Var=d*u; terminal variance = expected sum d_t*u_t/M_t^2. | Exact algebra + 18,180 distribution cases |
| H12 | Order defect phase | `EXHAUSTIVE_FINITE_CONFIRMED` | Correct axes: policy algebra × refinement × divisibility. DOWN/UP comparable commute at r=1; NEAR/FAR may not; refinement may break closure/interior commutation. | 756 pair-regime rows; 85,017 UP comparable checks; minimal witnesses |
| H13 | Recoalescence funnel | `EXACT_PROVED_OR_DERIVED` | Constant p,r, identity, positive post-collapse support. Strong exact trichotomy by r vs 2^p and pth-power alignment. | 431,361 funnel interval cases + 179,140 binary checks, 0 violations |
| LAW-014 | No integer midpoint | `EXACT_PROVED_OR_DERIVED` | p>=1,k>=0. Consecutive p-power gap is odd. | Parity proof; 31,031 checks through p=32,k=1000 |
| LAW-015 | NEAREST = threshold(1/2) | `EXACT_PROVED_OR_DERIVED` | Natural integer state model. | LAW-014 + 310,031 pointwise checks |
| LAW-016 | Scale microphase subdivision | `EXACT_PROVED_OR_DERIVED` | p>=1,a>=1,n>=0. `root_p(a^p n)=a root_p(n)+j`, 0<=j<a. | Basin scaling proof; 98,049 checks |
| LAW-017 | Threshold antitonicity | `EXACT_PROVED_OR_DERIVED` | alpha<=beta; common monotone inter-layer dynamics. | 240,480 layer cases, 0 violations |
| LAW-018 | UP divisibility commutation | `EXACT_PROVED_OR_DERIVED` | r=1, p|q. Upper p-power closures onto nested anchor sets. | Closure-operator proof; 85,017 checks |
| LAW-019 | BRC precision-exponent trichotomy | `EXACT_PROVED_OR_DERIVED` | Constant p,r, identity. Aligned pth-power r freezes; unaligned r<2^p funnels; unaligned r>2^p doubles collision-free. | Exact floor-spacing proof + attacks above |
| LAW-020 | Plateau-then-jump precision law | `EXACT_PROVED_OR_DERIVED` | Fixed exact physical x; integral Mx. | Root basin inequality + cross-precision table |
| LAW-021 | Stochastic observability barrier | `EXACT_PROVED_OR_DERIVED` | In k=1 sparse phase, unbiased one-step sample mean needs N >= Var/(eps^2 n^2)=Theta(2^p) for relative RMS eps at fixed n; multilayer variance may be much larger. | Exact formula + fixed n0=1000,r=3,depth16 p-sweep |

## Minimal counterexample set

### H4

- DOWN: `(p,a,n)=(2,2,3)`: `S(12)=9 != 4*S(3)=4`.
- UP: `(2,2,2)`: `S(8)=9 != 4*S(2)=16`.
- NEAREST: `(2,2,2)`: `9 != 4`.
- FARTHEST: `(2,2,2)`: `4 != 16`.

### H6

With `p=2,r=8=2^2*2`:

- DOWN, k=2: `25/8 != 2`;
- UP, k=1: `9/8 != 2`;
- NEAREST, k=1: `9/8 != 1/2`;
- FARTHEST, k=1: `1/2 != 2`.

### Order defects

- DOWN comparable + lift: `n=1,r=4,(p,q)=(2,4)`: `1/4 != 1`.
- UP comparable + lift: `n=1,r=2,(2,4)`: `8 != 2`.
- NEAREST comparable with no lift: `n=7,r=1,(2,4)`: `16 != 1`.
- FARTHEST comparable with no lift: `n=3,r=1,(2,4)`: `1 != 16`.

### Exponent metric monotonicity killed

- gap increases at `n=2`, p 2→3: 3→7;
- gap decreases at `n=8`, p 2→3: 5→0;
- nearest error increases at `n=3`, p 2→3: 1→2;
- nearest error decreases at `n=7`, p 2→3: 2→1.
