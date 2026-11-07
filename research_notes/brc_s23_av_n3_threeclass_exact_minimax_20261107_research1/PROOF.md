# S23 AV n=3: exact minimax for a three-class output observer

Date: 2026-11-07. Status: author-side exact proof, independently reviewable, not formally accepted.
Frozen scientific input: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Previous frontier: Draft PR #1777@5cfad8fd3e02ee67cc4cfb952f2f1c84d2ae0281. Its certified FULL 4x10 error interval is [5211/21952, 5211/21952 + 49/100000000000].

## Theorem (three-class observer exact minimax)
Let a,c range independently over all real numbers in [1/2,7/8], z=(1-a)c. The same unknown pair (a,c) governs three independent ternary outputs with probabilities (a,z,1-a-z). Three compressed observations are independent Bernoulli(z), with "distinguished" symbol of probability z.

Consider the three-class observer on the complete three-output sequence:
A = at least one symbol 2;
B = no symbol 2, but at least one symbol 0;
C = all three symbols 1.
The target probabilities are
A: f(a,z)=1-(a+z)^3;
B: (a+z)^3-z^3;
C: z^3.

The minimax total-variation reconstruction loss, over all parameter-independent row-stochastic maps from eight ordered binary input words to these three classes, is exactly

    epsilon_ABC = 5211/21952.

A constructive optimal decoder depends only on k, the number of input symbols of probability 1-z, and outputs A with probabilities

    t_A=(0,0,1381/1764,919/37044),

C with probabilities

    t_C=(1,0,0,0),

and B with probabilities 1-t_A-t_C. All entries are nonnegative and all rows sum to one, so this defines a legitimate 4x3 stochastic matrix and an 8x3 lift (one row per ordered input).

Its A probability is

    q(z)=sum_{k=0}^3 binom(3,k) z^(3-k)(1-z)^k*t_A[k]
        =(1-z)^2*(86084*z+919)/37044.

Its C probability is exactly z^3 (only input k=0 can output C). Thus the true minus reconstructed three-class residual vector is (r,-r,0), r=f(a,z)-q(z), and its total variation is |r|.

## Lower bound
Two lawful parameter pairs, (a,c)=(1/2,1/2) and (5/7,7/8), both yield z=1/4, hence identical distributions on all three compressed observations. Their probabilities of A are 37/64 and 2269/21952 respectively. Their B probabilities differ by the opposite amount, while C=z^3 is identical. The output-TV distance is 5211/10976. Every reconstruction from their common compressed law must have worst-case TV at least half the distance: 5211/21952.

## All-real upper bound: four exact polynomial sign certificates
The exact range of z is [1/16,7/16]. For fixed z, a_min=max(1/2,1-2z), a_max=min(7/8,1-8z/7).
Since f(a,z)=1-(a+z)^3 decreases with a, define H(z)=f(a_min,z), L(z)=f(a_max,z). Then

    H(z)=1-(1-z)^3                  for z<=1/4;
    H(z)=1-(1/2+z)^3                for z>=1/4;
    L(z)=1-(7/8+z)^3                for z<=7/64;
    L(z)=1-(1-z/7)^3                for z>=7/64.

For d=5211/21952, the four required slacks have EXACT identities:
1. z in [1/16,1/4]:
   d-H(z)+q(z) = (4z-1)*(196160z^2-191428z-155401)/592704 >=0.
   The two factors are <=0; for the quadratic use 196160z^2<=12260<155401 and -191428z<0.

2. z in [1/4,7/16]:
   d-H(z)+q(z) = (4z-1)*(492512z^2-339604z+363215)/592704 >=0.
   Here 4z-1>=0 and the quadratic >=363215-339604*(7/16)>0.

3. z in [1/16,7/64]:
   d-q(z)+L(z) = (-15760384z^3+9473088z^2-21674424z+2573053)/4741632 >=0.
   The numerator is >= 2573053-21674424*(7/64)-15760384*(7/64)^3 = 46538583/256 >0.

4. z in [7/64,7/16]:
   d-q(z)+L(z) = (4z-1)^2*(125993-85976z)/592704 >=0.
   The second factor >=125993-85976*(7/16)>0.

The four intervals cover all real feasible parameters. They prove H-q<=d and q-L<=d, and therefore |f(a,z)-q(z)|<=d. At z=1/4, q=935/2744, H=37/64 and L=2269/21952, with equality in BOTH error bounds. Therefore epsilon_ABC=d. The binary observer "any output label 2" is an exact-optimal coarsening as a corollary.

## Evidence and status
The companion VERIFY.py is a runnable exact Fraction checker. Each of four cubic identities is certified by evaluation at four distinct rational nodes on its branch, plus analytic sign inequalities, not by sampling as a substitute for an all-real proof. Executed locally with standard-library Python; see RUN_EVIDENCE.txt for full stdout and verifier source for all actual assertions.

This is a NEW RESULT about an explicitly lossy THREE-CLASS observer and the original 3-observation compressed Bernoulli law. It sharpens understanding of the fiber lower bound: the existing 5211/21952 bound is exact even with A/B/C separated. Any strict additional lower bound on the 10-hist/27-ordered FULL observer must exploit finer distinctions discarded here or extra restrictions on the declared observation. No unchanged native X6 joint relation/ordered path is presumed recoverable from this quotient. The original 10-label S23 mother-model bridge is separate. Neither P000 nor the frozen scientific pin is modified. Researcher/Owner/CLAIM are not created by the author-side GitHub proof. Independent mathematical review remains pending.

Next: split A into exactly one label 2 versus >=2 label 2, solve the refined 4-class minimax via exact rational primal/dual verification. See NEXT_TASK.md.
