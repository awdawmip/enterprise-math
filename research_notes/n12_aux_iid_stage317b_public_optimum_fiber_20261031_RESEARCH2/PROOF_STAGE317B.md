# Stage317-B — exact public-optimum fiber and unique source-tagged Pareto endpoint

Status: **PORTABLE_AUTHOR_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED**. This is a theorem within the explicit finite positive-rational BRC auxiliary model, using an earlier proved algebraic minimization; no native CLAIM, independent Driver admission or P000/X6 transfer is asserted.

Frozen reads (2026-10-31): GLOBAL_KNOWLEDGE_V1 main@192cdd698ae11e544173ee52965831be163c1cb8; enterprise-math main@12ed14a642cf4fba3120eb76758f7f456f828937; P000 V4 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE worldview blob 99238c3466eb0805748bae01fd1a20868a5a351e. Immutable mathematical premises: Stage307-B.2 proof at 128d2ce6aeb0299cdf842d0ad65082a64ba9d475, Stage315-B proof at 388bd4f074dfba8a6e8ff9b9d242819822e85bee, Stage316-B proof at ae57c9c8159db7694546e9a35969888ac604715e, all in Draft PR #1736. Stage307's global certificate is reused, not re-executed or re-claimed as a new proof.

## Model, observers and question

S is a fair binary source; conditionally on S=s, J correctly copies S with probability 7/8, W correctly copies S with probability 3/4, and Y~Bern(p_s) with p_0=1/4, p_1=3/4, independently. Private history h=(J,W,Y) has joint (S=0,S=1) masses (a_h,b_h)/256 in h=000,...,111 order:

(63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63).

The compressed representation chooses eight locked real Bernoulli rates t_h in [0,1] across three future F visits. The alternate operation H produces an independent fair bit. Public observer sees G=(W,Y) and the future transcript; tagged observer sees (S,J,G) and the transcript. Their worst-case TV errors over all public-history-adaptive H/F strategies are P_3(t),T_3(t). As previously proved, the all-F three-bit trace attains both maxima, because other adaptive transcripts are common Markov postprocessings of presampled F/H randomness.

Let F_3(z)=min{T_3(t): P_3(t)<=z} whenever this constraint is feasible. Stage316 reduced its optimal calculations to two complemented outer blocks. The present question is the exact lower public-budget endpoint z=P_min, including *all* eight-rate public minimizers and the corresponding tagged-risk minimizer. This endpoint classification and tagged value were not supplied by Stage307's two-rate minimizer theorem or Stage316's block formula.

## Theorem — four public minimizers, one tagged optimum at the public floor

Define B_k(t)=t^k(1-t)^(3-k), with word multiplicities (1,3,3,1). The Stage307 two-rate conditional residual is

d(x,y)=1/2 sum_{k=0}^3 binom(3,k)| (4/5)B_k(x)+(1/5)B_k(y)-(9/10)B_k(p0)-(1/10)B_k(p1)|.

Let a_* be the unique root in (7689/10000,769/1000) of

(41/16-4a^2)^3-(61/32-4a^3)^2=0,

and set x_*=1-a_*, y_*=1-sqrt(41/16-4a_*^2). Stage307-B.2 **proved**, by a local uniqueness argument and an exhaustive rational-rectangle certificate on [0,1]^2, that (x_*,y_*) is the unique global minimizer of d over both real parameters. Its two-rate sign pattern is r0=r1=0,r2>0,r3<0.

**(I) Full eight-rate public floor.** For every t in [0,1]^8,

P_3(t) >= P_min = 9/256-(4*x_*^3+y_*^3)/8 = 0.00755826723771693829...

Equality holds for **exactly four** full eight-rate vectors: their outer rates obey

t000=x_*, t100=y_*, t011=1-y_*, t111=1-x_*,

and each central pair independently obeys

(t001,t101) in {(p0,p1),(p1,p0)},
(t010,t110) in {(p0,p1),(p1,p0)}.

**(II) Sharp tagged Pareto endpoint.** Among these four public minimizers the **unique** minimum tagged risk is achieved by choosing both central pairs in MAP order (p0,p1). Write A(z)=1-3z^2+2z^3. Then

F_3(P_min) = 33/1024 + [63(1-x_*)^3+A(x_*)-2A(y_*)-1295/64]/128

= 0.09813463505252243496...

Swapping *either complete central pair* away from MAP preserves P_min and adds **exactly 99/1024** to tagged TV; swapping both adds 198/1024. No budget below P_min is feasible. The endpoint result determines the sharp endpoint of the *full* Pareto frontier; it does not determine F_3(z) for P_min<z<11/256.

### Proof of (I), with complete minimizer classification

The public observation partitions into four disjoint G values. At G=00, the two private rates t000,t100 have conditional mixing weights (4/5,1/5) and the true source rates have weights (9/10,1/10). Their contribution is exactly (5/16)d(t000,t100). At G=11, bit complementation yields exactly (5/16)d(1-t111,1-t011). The remaining G=01,10 contributions are separately nonnegative. Thus for *any* eight-rate vector,

P_3(t) >= (5/16)[d(t000,t100)+d(1-t111,1-t011)] >= (5/8)d(x_*,y_*)=P_min.

Equality requires both outer pairs to be their **unique** respective two-rate minimizers, and each of the two central group contributions to vanish. For either central G group, the two private histories have **equal** total masses 24/256 and the true source mixture gives equal probabilities to p0,p1. If the two represented rates are r,s, zero TV of the three-bit laws implies equality of the first and second Bernoulli-rate moments:

r+s=p0+p1=1, r^2+s^2=p0^2+p1^2=5/8.

Consequently rs=3/16, and r,s are the two roots of z^2-z+3/16, namely 1/4 and 3/4. Conversely, either permutation reproduces the entire three-bit mixture exactly by commutativity. The choices in the two disjoint central groups are independent. Hence the four stated vectors are **all** public minimizers. This completes (I).

### Proof of (II), including the exact algebraic value

The tagged TV separates by private source/provenance history. For a history with source masses (a,b)/256, its contribution is [a D_3(p0,t)+b D_3(p1,t)]/256, where D_3 is the TV of three independent Bernoulli observations. Stage315's strict weighted-triangle bound establishes the **unique** tagged minimizer for each central history: MAP, because its source masses are (21,3) or (3,21) and D_3(p0,p1)=11/16. Swapping both rates in one central public group changes its combined source-weight coefficient from 6 to 42, so its tagged risk rises by

(42-6)*D_3(p0,p1)/256=36*(11/16)/256=99/1024.

In MAP order the central groups together contribute K=12*D_3(p0,p1)/256=33/1024. The two outer tagged contributions are equal after bit complement. Stage316 gives one outer contribution as

c_3(x,y)=[63D_3(p0,x)+D_3(p1,x)+9D_3(p0,y)+7D_3(p1,y)]/256.

Stage307 confines (x_*,y_*) to the rational rectangle [23/100,24/100] x [55/100,56/100]. On this **whole** rectangle the exact ordered-word sign comparisons give:

D_3(p0,x)=(1-x)^3-27/64, D_3(p1,x)=A(x)-5/32,

D_3(p0,y)=27/32-A(y), D_3(p1,y)=A(y)-5/32.

Here the four identities follow by comparing each B_k to the fixed B_k(p_s) and summing the positive part with word multiplicities; all needed inequalities hold at rational endpoints with monotonicity of the relevant cubic factors. Substitution yields

c_3(x_*,y_*)=[63(1-x_*)^3+A(x_*)-2A(y_*)-1295/64]/256.

Therefore F_3(P_min)=K+2c_3(x_*,y_*), exactly the displayed algebraic value. The strict central MAP preference proves uniqueness of the tagged optimum among all four public-minimizing vectors; (I) excludes every other full eight-rate vector. QED.

## Independent exact Fraction checks and rigorous numerical brackets

REPRO_STAGE317B.py (standard-library Fraction, no floating assertions) directly checks the Stage307 defining polynomial's signs at a=768916059144478/10^15 and a=768916059144479/10^15, with uniqueness inherited from Stage307's proof. Squared rational inequalities enclose y_* within (555508857277/10^12,555508857278/10^12); the bracket for x_* is obtained by x_*=1-a_*. Using monotonicity of A(x) and A(y) gives exact rational interval enclosures

7558267237/10^12 < P_min < 7558267239/10^12,

98134635052/10^12 < F_3(P_min) < 98134635054/10^12.

The program separately enumerates all **128** (S,h,three-bit word) probability atoms for a rational outer-rate approximation, verifies the P=2b_3 and T=K+2c_3 block formulae, and checks all four central pair swap choices, including the exact 99/1024 increment. Actual output REPRO_STAGE317B_EXECUTED_STDOUT.txt ends STAGE317B_PUBLIC_FLOOR_TAGGED_ENDPOINT_EXACT_PASS. The script's discrete checks and root brackets are **not a replacement** for Stage307's continuum global-minimum certificate; this result inherits and explicitly cites it.

## Scientific synthesis and scope

This closes the sharp **public-minimum endpoint** of the still-open Pareto frontier, including exact full-cube equality cases and the tagged error there. Stage316's bound P_3>5/7168 is mathematically valid but **strictly weaker** than the already proven exact global bound P_3>=P_min from Stage307; it should not be presented as the best currently known global public floor. The newly supplied content is the exhaustive eight-rate equality-fiber classification, the source-tagged endpoint, and the exact per-swap provenance cost.

**BRC reuse (REUSE_APPLIED):** positive rational (S,h) source masses, public versus tagged observers, future-operation postprocessing, exact word-level signed TV residuals, and information-loss preservation. An external finite Bernoulli model has no automatic P000 native meaning. The native-transfer task still requires a declared six-axis X6 path embedding, nontrivial three-dimensional slice/third-coordinate semantics, triadic-force closure, time order and final Cell-address encoding, together with preservation of the stated future observers.

**Next Stage318-B:** determine the exact one-block cost envelope C_3(s) for s>a_3=(5/16)d(x_*,y_*) by resolving the active sign chambers near (x_*,y_*), and then minimize the two-block infimal convolution to identify whether the first transition before the algebraic Stage314 one-fiber cusp is caused by one-block chamber switching or non-symmetric budget allocation. Preserve the floor endpoint and complete equality fibers as boundary conditions, not a task to re-prove.
