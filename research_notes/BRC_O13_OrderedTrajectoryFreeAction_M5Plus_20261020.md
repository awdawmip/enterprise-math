# O13 ordered-port trajectory orbits for horizons m >= 5

Date: 2026-10-20 (Asia/Taipei)
Research activity: RA-C136DC4098B78DB73EEACE8D
Researcher identity: EM-DIRECT-C83D21
Scope: finite O13 Boolean-support BRC auxiliary model only; not a native X6 physical theorem.

## Question

Extend the established three- and four-step ordered-port orbit counts to every horizon m >= 5, and state the exact orbit-size distribution by initial support size.

## Frozen model

Let V = F_5^* x F_5, so |V| = 20. Let G consist of the 80 transformations
g_{u,v,t}(a,s) = (u a, v s + t), where u,v are in F_5^* and t is in F_5. G acts on an initial support S subset V and an ordered tuple (p_1,...,p_m) of distinct ports, with S disjoint from the tuple. The trajectory object is (S,p_1,...,p_m), and the group acts diagonally on all labels.

## Theorem: free action from five distinct ordered ports

Every nonidentity g in G fixes at most four ports.

Proof. If g(a,s)=(a,s) and a is nonzero, then ua=a implies u=1. If u != 1, g fixes no ports. For u=1, the second coordinate is the affine map s -> vs+t. Unless (v,t)=(1,0), this map has at most one fixed s in F_5: none if v=1,t!=0, and exactly one if v!=1. Since there are four choices of a, a nonidentity g fixes at most four points. Hence a trajectory containing m>=5 distinct ordered ports has trivial stabilizer under the diagonal action.

## Exact orbit formula

For a fixed initial support size k, the number of labeled trajectory objects is binom(20-m,k) (20)_m, where (20)_m = 20!/(20-m)!. Since the action is free for m>=5, every orbit has size 80. Therefore

N_{m,k} = ((20)_m / 80) binom(20-m,k), for 5 <= m <= 20 and 0 <= k <= 20-m.

Summing over k gives

N_m = ((20)_m / 80) 2^(20-m).

For m=5, (20)_5/80 = 23,256, so

N_{5,k} = 23,256 binom(15,k), k=0,...,15,
N_5 = 23,256 * 2^15 = 762,052,608.

The 16 coefficients are:
23256, 348840, 2441880, 10581480, 31744440, 69837768, 116396280, 149652360, 149652360, 116396280, 69837768, 31744440, 10581480, 2441880, 348840, 23256.

## Extension through m=20

The same proof yields:
m=6: 5,715,394,560
m=7: 40,007,761,920
m=8: 260,050,452,480
m=9: 1,560,302,714,880
m=10: 8,581,664,931,840
m=11: 42,908,324,659,200
m=12: 193,087,460,966,400
m=13: 772,349,843,865,600
m=14: 2,703,224,453,529,600
m=15: 8,109,673,360,588,800
m=16: 20,274,183,401,472,000
m=17: 40,548,366,802,944,000
m=18: 60,822,550,204,416,000
m=19: 60,822,550,204,416,000
m=20: 30,411,275,102,208,000

## What this proves and does not prove

This is an exact orbit count for the specified finite group action and ordered distinct-port trajectory object. It does not assert that the sequence of single-step orbit labels alone determines the full trajectory orbit; the previously exhibited double-coset alignment residual remains necessary. It also does not establish a native X6 physical correspondence or solve the separate amplitude-4 global injectivity question.

## Verification

The group has 80 elements and the port set has 20 elements. Direct enumeration of all 80 permutations gives maximum fixed-point count 20 only for the identity and at most four for every nonidentity element. Exact integer arithmetic verifies (20)_m divisible by 80 for each m=5,...,20 and reproduces the counts above.

## Next question

Construct the stabilizer/double-coset transport law for five-step trajectories, then determine whether the minimal alignment state composes associatively without storing the entire intermediate trajectory.
