# Stage106 — Exact minimax affine interval and sharp support endpoint (external iid N=14)

**Status:** AUTHOR exact-rational, computation-assisted proof, verified with separately implemented bottom-up and literal ordered-history DFS algorithms. **Not** independent Research Driver admission, native Task CLAIM/Result, or P000/X6 theorem. Pinned inputs: GLOBAL_KNOWLEDGE_V1 main@04aa116d3c89bc5fee453d6467cd87eed27221fe and Enterprise Math author frontier main@7166bbdfc462e38336b46d55485f8e2cdf2f0b96, including `research_notes/n14_aux_iid_affine_105_20261025/PROOF_STAGE105.md`. The global P000 startup projection matched its immutable canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.

## Theorem

Under three-symbol iid P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), allow all **complete ordered-history** randomized decision/stopping rules with tau<=14. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau, V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ). From the Stage105 author endpoint

```text
alpha105 = 38038153259411651/109561042308169728
V105     = 353483207227801957/27390260577042432
```

the following identity holds for **every real** delta in the specified interval:

```text
V14(alpha105+delta) = V105 - (211068/101)*delta
0 <= delta <= eta106 = 2850725/51737158867746816
alpha106 = 646648605512624167/1862537719238885376
V106     = 6009214469256084569/465634429809721344
```

This support line is strictly unattainable beyond alpha106. This does not determine the subsequent optimal segment.

## Proof 1: universal Bellman dual

At count prefix z=(n,a,b), likelihood ratio Q/P=2^(a+b)/3^a. Set K=lambdaQ=107892/101, L=lambdaP=72+(8/9)K=103176/101 and Gamma=K+L=211068/101. At n<=14 compute exact rational backward recursion

```text
D(z)=min( K*2^(a+b)/3^a [decide P],
          L                 [decide Q],
          1+P0 D(n+1,a+1,b)+P1 D(n+1,a,b+1)+P2 D(n+1,a,b) [continue] )
```

(continue omitted at n=14). Backward induction at every ordered prefix, without a count-policy assumption, gives D(root)<=tP+L*eP+K*eQ<=max(tP,tQ)+Gamma*alpha for all policies respecting both error caps. The exact enumeration has **680** count states, **1240** nonselected-action comparisons, **1238** strictly positive, zero negative, and exactly **two ties**:

```text
A=(11,5,4): decide Q vs continue
B=(12,0,1): decide Q vs continue
minimum positive gap = 7273/130896
D(root)=1021430518484691292987/1383208159140642816
```

**Important correction of an easy-to-make assumption:** the new tie at A is Q/C, **not P/C**. The preceding Stage105 handoff identified the competing action C, but that alone does not fix the old action. The policy choosing Q at A and B (and the unique action elsewhere) has nonnegative pinned action gaps at both K106=107892/101 and K105=2212824096/1992661; every pinned-policy gap is affine along L=72+8K/9, so there is no intervening dual crossing. Exact equality D(root)=V105+Gamma*alpha105 holds.

## Proof 2: actual ordered first-hit carrier and disjointness

Following the unique strict action until either tie, retain each *ordered* prefix and its positive P/Q mass. Exhaustive exact totals:

| First hit | Ordered prefixes | P probability | Q probability |
| --- | ---: | --- | --- |
| A=(11,5,4) | 2258 | 28225/195689447424 | 28225/92876046336 |
| B=(12,0,1) | 12 | 48828125/725594112 | 48828125/362797056 |

Forced continuation at each tie then strict optimal successors produces tuple (conditional P-error, conditional Q-error, additional P-time, additional Q-time, ordered terminal suffix count):

```text
RA=(1493/1536, 7/576, 239/192, 167/144, 9)
RB=(63/64, 1/144, 9/8, 13/12, 5)
```

The two cones are **causally disjoint**: A already contains 5 occurrences of symbol 0, so cannot lead to B with zero occurrences; B has depth 12 and cannot lead backward to depth-11 A. Consequently mixing effects contain no u*s term. Aggregation occurs only after preserving history multiplicity and P/Q probability; this positive-rational branch carrier is applicable BRC-style information preservation, not a native X6 theorem.

## Proof 3: exact primal family on the full real interval

At alpha105 choose Q at A and Q at B with probability

```text
s0=241563037007287/307200000000000
```

(otherwise continue at B). Let u in [0,1] be the probability to **continue instead of Q** at A; let s be the probability to decide Q at B. Using the real first-hit and forced suffix data, the errors are exactly

```text
eP=alpha105 + x*u + e*(s-s0),   x=-1213675/300578991243264, e=48828125/46438023168
eQ=alpha105 + y*u + f*(s-s0),   y= 197575/53496602689536, f=-48828125/52242776064
```

The unique equality eP=eQ forces

```text
s(u)=s0 + (67761451/17408000000000)*u
s(1)=4106591957559179/5222400000000000
eP(u)=eQ(u)=alpha105 + eta106*u
eta106=2850725/51737158867746816>0
```

Both s endpoints lie strictly within (0,1), so every real u defines an admissible randomized test. Exact ordered-root endpoint tuples (eP,eQ,tP,tQ) are

```text
u=0: (alpha105,alpha105,353483207227801957/27390260577042432,111940980237083111/9130086859014144)
u=1: (alpha106,alpha106,6009214469256084569/465634429809721344,5708989891929406961/465634429809721344)
```

tP>tQ at both endpoints and therefore throughout, by disjoint-cone affinity. All used actions minimize Bellman at K106. Thus tP+L*eP+K*eQ=D(root) and max(tP,tQ)=tP=D(root)-Gamma*alpha everywhere on the full real interval, attaining the universal lower bound.

## Proof 4: strict sharpness

Suppose a rule attained the same support line at a larger cap. Equality in all dual/error/worst-time slack forces eP=eQ=alpha, tP>=tQ and only Bellman-minimizing actions on reached prefixes. The exhaustive table has ties only A,B. Even an order-dependent mixing rule is equivalent in global moments to its P-first-hit weighted average at each tie: prefixes sharing the count state share the same Q/P ratio and conditional strict suffixes. Their two cones are disjoint. Thus some u,s in [0,1] must satisfy the exact displayed balance equations, which force alpha=alpha105+eta106*u<=alpha106, contradiction. Minima exist by compactness of the finite randomized-policy space. So the same support line cannot extend rightward.

## Exact checks and limits

Two separately written author programs were executed with Python `fractions.Fraction`. The primary bottom-up checker verifies all 680 states and 1240 comparisons, pinned dual-gap interpolation, real ordered first-hit sums, continuation suffixes, full root moments, endpoints and midpoint. The independent top-down Bellman + literal ordered-word DFS visits 995800 nodes at u=0, 1022896 at u=1 and 1022896 at u=1/2; all four rational moments match. Both are **author-side checks**, not independent mathematical review. The full local reproduction packet includes proof, two executables, certificate, run logs and SHA manifest. The next **dual-only candidate** is K107=778896/767, state (10,3,0), competing P action. Its primal interval is unproved.

Native `em_control_tasks` returned `CONTROL_QUOTA`; `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` and `operation_sent=false`. Hence current native owner/session/CLAIM/Result and Driver admission remain unverified. This ordinary author note is not a native research writer result and no denied access was bypassed through Google Drive.