# X6 heartbeat walking: speed, phase resonance and temporal BRC correlation

Researcher-ID: `EM-DIRECT-AD0416`
Research-Activity-ID: `RA-37C0A30C7B1F5A338F03D186`
Progress-Event-ID: `brc-x6-velocity-resonance-20260919-AD0416`
Session: `chat-local-reciprocal-ceec8bd1559acdf8c10ebc9b` (continuing local key, not a platform ID).
Status: `RESEARCH_DERIVATION / EXECUTED_EXACT_CENSUS / NOT_FOUNDATION`.
User: “继续深入研究 看看按怎样的速度在里面走 能走出怎样规律”.
Read pins: GLOBAL_KNOWLEDGE `fdf599460770ec6cf9b7de0442001387f9ce42ab`; EM `738f75d51cd9bffc56a834d45866c00bd154b6fc`.
Prior heartbeat source: `research_notes/brc_x6_heartbeat_20260919_AD0416/verify_heartbeat.py` and its note at `bb3c1c0a541eea1111ed325eee643783d2b6e77c`.
No formal Task-ID/CLAIM, independent review, Foundation change, physical clock calibration, production Nollm mutation or semantic benchmark.

## 1. Question, controls and source audit

The selected question is motion in the previously constructed six-axis scale heartbeat, not replacement of its geometry. Specify motion before attaching the word speed: the number of active-chart unit steps per tick, their fine-native step cost, direction protocol, timing phase, and whether the field breathes or expands indefinitely are distinct inputs. The objects are raw relative Z^6 displacements around a chosen chart anchor, not final Cell addresses or three classical axes counted twice.

Use A_b(z)=(b*z6,z1,z2,z3,z4,z5); A_b^6=bI. The existing exact analysis/synthesis helper retains all division residues. It is executed unchanged, together with existing brc_transport, brc_histogram and predictive_quotient. Coverage conclusion: T0/T5/T6 composition/domain specialization, not a new top-level family. A deterministic cadence is the C=1 BRC case; probabilistic branching is introduced only in the separately declared two ensemble experiments.

Control populations use the same starting point and direction schedule, with no pulse, a lossless pulse without walking, or pulse plus walking. Fine-native movement cost is reported separately from chart steps. We include equal-cost opposite-drift examples and equal-cost closed-versus-drifting schedules; the half-speed phase comparison alone is NOT equal fine cost. No semantic efficacy inference follows from a trajectory shape.

Bottom data: the new module, exact test program, exhaustive finite parameter census, outputs and input seed are available. Four complete reused files are Git-blob checked. The accompanying prime-valuation dependency is the already labeled minimal excerpt, not execution of the whole holonomy module. Full project suite/independent mathematical review/Lean were not run. Previous heartbeat tests are consumed, not rebranded as new work.

## 2. A fixed, reversible breathing experiment

For phase phi=0,...,11 let j(phi)=min(phi,12-phi). At that phase analyze x to j coarse beats, retaining the chronological residues; move by s(phi)*n*e1 in the active chart; synthesize using the same residues. Choose the diagnostic direction protocol
s(phi)=+1 for phi<6; s(phi)=-1 for phi>=6.

Because synthesis is affine in the coarse coordinate, the fine displacement is exactly

x_(t+1)=x_t+n_t*g_phi,
g_phi=s(phi)*A_b^j(phi)*e1.

At b=2 the ordered stencil is
(e1,e2,e3,e4,e5,e6,-2e1,-e6,-e5,-e4,-e3,-e2).

All entries are integral, signed-axis moves. The -2e1 entry costs two fine primitive steps, not one free physical jump. The sum of the stencil is -(b-1)e1. Performing no walking is identity for all phases; chart changes alone are not motion. The signed direction reversal is an imposed test policy, not spontaneous orientation selection. Other direction policies have different stencils and drift.

## 3. Rational speed is an exact carry machine

Let nu=p/q in lowest terms, p>=0, q>=1, and initial clock carry rho in {0,...,q-1}. Define

n_t=floor(((t+1)p+rho)/q)-floor((tp+rho)/q).

No fractional Cell step occurs. The online equivalent is
n_t,new_rho=divmod(rho_t+p,q).

The cumulative number of chart steps through T is floor((Tp+rho)/q), with error less than one relative to T*p/q. For 0<p<q, this is a wait/move cadence; p>q permits multiple steps per tick. This clock carry is distinct from each point's spatial division residue.

The control pair (heartbeat phase, clock carry) has exact period
L=lcm(12,q).
For one control cycle define
Delta=sum_(t=0)^(L-1) n_t*g_(t mod12).
Then for all t>=0,
x_(t+L)=x_t+Delta.

Proof: both the stencil and cadence repeat at L, so each translated interval has the same increment. Delta=0 gives a periodic full trajectory; Delta!=0 gives a periodically repeated shape translated each supercycle. A fixed cadence in this affine-translation model cannot become chaotic merely by running longer.

### Phase resonance theorem

Let d=gcd(12,q). Define
H_r=sum_(0<=i<q, i=r mod d) n_i, r=0,...,d-1.
Then phase phi receives exactly H_(phi mod d) chart steps in L ticks, and
Delta=sum_(phi=0)^11 H_(phi mod d)*g_phi.

Proof: phi+12k mod q, k=0,...,q/d-1, visits each residue congruent to phi mod d exactly once. Thus only d cadence classes can bias the twelve heartbeat phases. In particular, if gcd(q,12)=1 then H_0=p and
Delta=-(b-1)p e1,
Delta/L=-(b-1)*(p/q)*e1/12,
independently of rho. This is exact arithmetic phase sampling; it does NOT prove a stable synchronization interval or Arnold tongue under perturbation.

### Executed b=2 examples

|rate|rho|ticks L|Delta|chart steps|fine cost|
|---|---:|---:|---|---:|---:|
|1|0|12|(-1,0,0,0,0,0)|12|13|
|1/2|0|12|(0,0,0,0,0,0)|6|6|
|1/2|1|12|(-1,0,0,0,0,0)|6|7|
|1/3|0|12|(0,-1,1,0,-1,1)|4|4|
|1/3|1|12|(0,1,-1,0,1,-1)|4|4|
|1/5|any|60|(-1,0,0,0,0,0)|12|13|
|1/7|any|84|(-1,0,0,0,0,0)|12|13|
|2/3|0|12|(0,0,0,0,0,0)|8|8|

At half rate, rho=0 selects odd phases; its moves are e2,e4,e6,-e6,-e4,-e2 and it closes. Rho=1 selects even phases and drifts -e1. This comparison has fine costs6 and7, respectively. With no scale pulse, both half-rate phases close under the same sign reversal.

At rate1/3, rho0 and rho1 have the same number of ticks, steps and fine cost but opposite drift. Also the schedules of six active phases {1,3,5,7,9,11} and {1,2,3,7,8,9} both cost6 fine steps and have average rate1/2; the first closes, the second drifts (0,1,1,0,-1,-1). Average speed and work alone do not determine the route.

## 4. A second arithmetic lock: spatial precision residues

For the fixed fine translation x->x+v, observed modulo M, the exact period is
T=M/gcd(M,v1,...,v6).
This is the additive order of v in (Z/MZ)^6: M must divide T*v_i for every i. Equivalently combine the individual M/gcd(M,v_i) by lcm. This does not imply visiting all M^6 points.

At precision M=16, walking along one axis at speeds1,2,4 gives residue periods16,8,4. The faster walkers skip more fine residue classes. A repeat of the residue is NOT a return of the unbounded physical coordinate.

For the breathing trajectory, observed modulo M AND retaining both clocks, the exact first return is
P=L*M/gcd(M,Delta1,...,Delta6).
Any full-state return must first return the two clocks, hence occur at a multiple of L; thereafter the condition is the additive order of Delta. At most L*M full states are visited in this model, not generally all points of the six-dimensional torus.

Executed T6 example: the half-rate closed orbit has12 raw phase states but4 currently distinct positions. Original predictive_quotient gives classes (4,10,12,12,12,12,12) for horizons0..6. Other tested drifting/mod3 examples also require their complete temporal orbit after a bounded horizon. This is not a claim that every application must retain the entire cycle: a coarser observer can admit more compression, and a shared external clock may supply phase without duplicating it on each atom.

## 5. Irrational cadence: exact aperiodicity, not random coverage

Choose alpha=sqrt(2)-1 and rho=0. Then
n_t=isqrt(2(t+1)^2)-isqrt(2t^2)-1.
This uses integers only because floor(t*alpha)=isqrt(2t^2)-t for nonnegative integer t. The cumulative count N(T)=isqrt(2T^2)-T has asymptotic mean alpha. If the cadence were eventually periodic its mean would be rational, a contradiction. Therefore its complete move/wait trace is not eventually periodic. Individual positions may still be revisited; no everywhere-nonreturn claim is made.

For each fixed heartbeat phase phi, the fractional parts of (12k+phi)*alpha are uniformly distributed. One elementary route is the geometric-sum estimate for every nonzero integer Fourier mode, followed by approximation of the interval [1-alpha,1). Hence the phase-conditioned mean move count is alpha and
lim x_T/T=-(b-1)*alpha*e1/12.
This is phase equidistribution, not spatial ergodicity of the whole six-axis field. Nonperiodicity is not chaos or automatic semantic exploration.

Exact 120000-tick run:49705 moves, endpoint(-4114,2,10,-4,7,-4), phase counts [4154,4134,4152,4138,4140,4150,4134,4154,4133,4142,4142,4132]. The finite run checks the integer implementation, not the infinite theorem. Finite rational approximations eventually repeat, and deciding an arbitrary future tick needs unbounded integer precision in t; no finite autonomous clock can generate a truly aperiodic deterministic sequence forever.

## 6. BRC: same one-tick speed distribution, different long-time transport

Compare two declared positive branch ensembles at average rate1/2 and b=2.

Persistent ensemble: choose initial cadence rho=0 or1 with probability1/2 ONCE; preserve it. After K cycles the endpoints are 0 and -K e1. Thus
E[X_K]=-(K/2)e1,
Cov(X_K)=(K^2/4)e1 e1^T.

Fresh ensemble: at EACH tick independently choose stay or move with probability1/2. Each move is the same g_phi used above. Then
E[X_K]=-(K/2)e1,
Cov(X_K)=(K/4)*diag(5,2,2,2,2,2).
More generally with per-tick independent probability nu,
E[X_K]=-K*nu*(b-1)e1,
Cov(X_K)=K*nu*(1-nu)*diag(1+b^2,2,2,2,2,2).

Proof: the Bernoulli innovations are independent, so their centered cross covariances vanish; sum the outer products of the stencil vectors. In the persistent ensemble the initial phase is a shared latent variable across all ticks, so those cross-time correlations do not vanish.

Both ensembles have the SAME move probability1/2 at every tick, the SAME expected6 chart steps and13/2 fine steps per cycle, and the SAME endpoint mean. Nevertheless one has two persistent branches with spread proportional to K; the other's centered spread is proportional to sqrt(K). At K=20, their covariance diagonals are (100,0,0,0,0,0) versus(25,10,10,10,10,10).

This is the useful BRC extension: retain the temporal/control port. A transition has
(phi,rho,x) -> (phi+1 mod12, (rho+p) mod q, x+floor((rho+p)/q)*g_phi).
Serial composition must match the output clock carry to the next input carry. Replacing a once-selected path by independent per-tick alternatives changes the branch measure; it is not safe recoalescence. Existing BRC affine packets handle each fixed phase/fiber exactly. Scalar speed histograms or endpoint-only moments cannot reconstruct erased temporal dependence.

Executed original MomentState for240 ticks, representing2^240 positive paths in the fresh ensemble, gives mass1, mean(-10,0,...), covariance above. Only4096 choices for a single cycle were literally enumerated, with972 distinct endpoints, and checked against both endpoint aggregation and exact moments. No huge path enumeration or constant-bit storage is claimed.

## 7. When the field grows indefinitely: a separate speed threshold

Closed breathing has no net scale multiplication per cycle. Do not apply an exponential-expansion threshold to it.

For a different declared model x_(t+1)=A_b*x_t+u_t, six-step unrolling gives
X_(k+1)=b*X_k+W_k,
W_k=sum_(i=0)^5 A_b^(5-i)*u_(6k+i).
With comoving readout Y_k=X_k/b^k,
Y_K=X_0+sum_(k=0)^(K-1) W_k/b^(k+1).

A transparent coherent example applies s_k=a^k fine steps along e1 only on the sixth tick of each block, so W_k=a^k e1. For nonnegative coherent input:
- a<b: Y_K converges; constant speed has finite comoving reach, not a physical stop.
- a=b: Y_K=X_0+(K/b)e1.
- a>b: comoving displacement grows geometrically.

At b=2,K=16,a=1,2,4, the extra comoving displacements are65535/65536,8,65535/2. Speeds and work grow explicitly; no cost-free transport is inferred.

The boundary is not just an exponential label. For s_k=floor(b^k/(k+1)^gamma),
Y_K-X_0=(1/b)*sum_(k=0)^(K-1)1/(k+1)^gamma - E_K,
0<=E_K<1/(b-1).
Thus gamma=1 still gives logarithmic comoving escape despite s_k/b^k tending to zero; gamma>1 gives bounded reach. Merely saying 'slower than expansion' is insufficient without a summability condition.

For N_k INDEPENDENT centered unit steps injected at each block end, Cov(W_k)=N_k*Sigma, and
Cov(Y_K)=sum N_k*Sigma/b^(2k+2).
If N_k=a^k, the variance threshold is a=b^2, not b. If one coherent randomly signed burst of length s_k is used instead, its variance is s_k^2*Sigma; that is a different correlation model. Speed in steps and root-mean-square displacement must not be conflated. This statement concerns exact moments only, not hitting probabilities or semantic retrieval.

## 8. Verification inventory and prior-art boundaries

12 groups PASS:
-4 complete pinned source identities;
-1440 signed lossless chart-interaction checks;
-9519 reduced rate/initial-carry cases through q=36, plus23 faster-than-one cases;
-3898728 explicit tick updates for the main census;
-84 exact first-return torus checks;
-4 original T6 predictive profiles;
-500 additive spatial-residue checks;
-120000 exact irrational ticks;
-4096 literal BRC path choices plus independent aggregation/moment comparison;
-200 general six-step expansion unrollings, speed/variance regimes and8 borderline checks;
-8 invalid-input rejections. Compilation passed.

163 of the9519 parameter/phase cases close in the selected census. This is not an unbiased probability over speeds, not a statistical estimate, and not a universal resonance density. Formulae are proved within the declared model; finite enumeration is a reproducibility check.

External primary comparison pages inspected on2026-09-19 (abstract/metadata only, not a full PDF/raw-data audit):
- Rahav, Horowitz, Jarzynski, *Directed flow in non-adiabatic stochastic pumps*, arXiv:0808.0015v2 / PRL101(2008): periodic driving has nontrivial pumping/no-pumping conditions. Their thermally activated stochastic hypotheses are NOT our deterministic stencil theorem.
- Le Vot, Abad, Yuste, *Continuous-time random-walk model for anomalous diffusion in expanding media*, arXiv:1706.06793v2 / PRE96(2017): expanding-medium and comoving transport are established subjects. Our integer six-step recurrence is proved directly, not imported from a fractional PDE.
- Glodkowski, Miekisz, *Fast ergodicity of rotations on the circle...*, arXiv:2401.15736v1(2024): irrational rotations/Sturmian coding provide context. Their ground-state stability result is not a claim about our memory field.

No novelty priority is claimed for cadence words, periodic affine transport, additive orders, or phase lifting. The project contribution is their exactly costed X6/BRC composition, equal-budget witnesses and the explicit persistent-versus-resampled temporal branch comparison.

## 9. Next actual unresolved unit

Introduce one fixed geometry-derived, state-dependent interaction at equal fine-step and clock budgets, retaining the exact baseline. The present g_phi does not depend on occupancy or the previous path. Such coupling can invalidate the simple translated-cycle law; its first failure should yield a concrete repair variable or a stability bound. Compare useful overlap/coverage and resource cost, not just visually attractive or fast trajectories. Do not change production Nollm or promote these candidates without its normal tests and mathematical admission.
