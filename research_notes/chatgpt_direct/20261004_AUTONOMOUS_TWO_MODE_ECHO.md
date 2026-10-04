# Autonomous two-mode Euler echo and exact observation laws

Status: PROVISIONAL MODEL PROOFS AND FINITE CHECKS / NOT FORMALLY ADMITTED.
Date: 2026-10-04. Same-conversation continuation, not independent replication.
Global read snapshot: bf5530f00314518ccfd77a6853042fc1383dd56a.
Mathematical Source snapshot: dfb768b45753e43847cc06199173b9ad3b00e22e.
Registration request: private control Issue 2726, session-20261004-euler-autonomous-09; last observed QUEUED. No prior closed session or CLAIM is borrowed. No formal Task-ID, Result, review or native execution authority is asserted.

## Scope and source

This is a new autonomous-periodic model, not a republication of the previously blocked incidence note or its verification attachment. The earlier blocked files remain pending.

Use the existing first-level incidence ports q_n, n in Z/12, with even ports Cell and odd ports gate. The existing euler_rotation_refinement.py provides successor and phase_kind, blob 55e12f7ffb68a5b241f5d6323f5fde118de2716a. Ports are NOT X6 spatial coordinates. The positive CWM core is src/enterprise_math/brc_weighted.py, blob 3f205696709e847909958a153f8fe10d3f6b70f0; its unchanged bodies are actually executed through the already preserved labelled BRC adapter. Serial composition multiplies count/total/dominant; alternatives use (+,+,max). Positive weights, root/path identity and audit history remain separate from signed algebraic observations. No numerical pi, trigonometry or ordinary reference propagator is executed.

The earlier local evidence archive was read and SHA256-verified as e0472600d1edc71471f457bc48557ecb8e5019b025687e4fa3c799a7d0d5d88a. Its unchanged executable dependencies were reused locally, not republished. Reuse: REUSE_EXECUTED for the CWM/incidence interfaces; EXTEND_EXISTING_TOOL for one binary mode and its observer, not a new accepted BRC family. P000, separate time, native six-space and three-dimensional slice typing are unchanged.

## 1. Halting and cycling are different future contracts

The old countdown rule holds (n,0) and maps (n,r) to (n+1,r-1) for positive r. It is not injective: (4,0) and (3,1) both map to (4,0). Its 36-state minimum for exact future position traces with eventual stopping is not refuted here.

For a finite invertible time-independent dynamics, every orbit is periodic. If a fixed observable vanishes for all sufficiently late times, it vanishes on the entire orbit: add a sufficiently large multiple of the orbit period to each earlier index. Thus a nonzero earlier observable cannot become permanently zero under those assumptions. This is not a demand that native physics be reversible; irreversible dynamics, an infinite state space or changing observations are outside this statement.

We change the requested model behavior to periodic realization of the same selected half-turn at six-step observations, WITHOUT requiring a permanent stop at step six.

## 2. A local autonomous reversible realization

Add an internal mode b in {0,1}, not a spatial dimension, and define

F(n,b)=(n+b mod12,b).

Every update holds or uses one existing incidence edge. The same rule is repeated; b is not reloaded from the current port. The inverse is F^(-1)(n,b)=(n-b,b). On the full 24-state carrier, F commutes with every common position rotation R_r(n,b)=(n+r,b).

Declare the initial selected set A={4,5,10,11} and preparation i(n)=(n,1_A(n)). The initial position/mode correlation is extra model data; its physical origin and cost are not proved.

Let V(n)=n+6 mod12 for n in A and V(n)=n otherwise. Since A is closed under addition by six,

F^6 i(n)=i(V(n)), and F^12 i(n)=i(n).

The moving paths CONTINUE after six steps. This is not the old halting task. The period concerns port/mode, not the external operation index, physical time or full audit histories.

Exactly 20 dynamic states are reachable from all twelve prepared seeds:

R={(n,1):n in Z/12} union {(n,0):n not in A}.

They form one twelve-cycle and eight fixed states. All are future-distinguishable under exact port observation: distinct ports differ now, and different modes at the same port differ after one update. Therefore 20 is the minimal deterministic predictive quotient for THIS dynamics and observer, not a minimum over all implementations of the old task. A 20-bin CWM summary propagates exactly under F, retaining the actual existing serial/recoalescence laws. Source/history-sensitive controls require additional distinctions; fixed bin count is not fixed bit cost.

## 3. The induced Euler readout

Use the already specified primitive phase alpha with alpha^4-alpha^2+1=0, alpha^12=1 and alpha^6=-1. For a positive labelled population define

A0=sum_(mode=0) w_p alpha^(n_p),
B0=sum_(mode=1) w_p alpha^(n_p).

Then actual BRC path transport and alternative addition give

Z_t=A0+alpha^t B0.

Each idle port remains fixed, while each moving port receives exactly t successor operations, proving the identity for every nonnegative integer t. In the external complex readout the twelve values lie on a circle centered at A0 with radius |B0|. This is readout geometry, not a native plane. A zero can be one point on a nontrivial orbit rather than an absent state.

The observable functions g0(n,b)=(1-b)alpha^n and g1(n,b)=b alpha^n satisfy g0 composed with F=g0 and g1 composed with F=alpha*g1. This is a finite application of the established observable-evolution viewpoint, not a new general spectral theorem.

## 4. Exact echo, with preparation explicitly accounted for

Take three paths at ports 0,4,8 with positive weight 1/3 each, then prepare their modes as 0,1,0. Put omega=alpha^4. The mode observers are A0=-omega/3 and B0=omega/3, so

Z_t=(omega/3)(alpha^t-1).

Thus Z_0=0, Z_6=-2omega/3, Z_12=0. At t=6 the four coefficient output is (2/3,0,-2/3,0). No external switch is applied at step six. CWM remains exactly (3,1,1/3); no branch proliferation, positive mass cancellation or energy interpretation is used.

The order of preparation matters. Let E be the existing equal alternative program I,S^4,S^8, preserving each existing mode. The identity 1+omega+omega^2=0 kills BOTH A0 and B0 separately under E. This typed E commutes with F as an endpoint/mode distribution update, so F cannot generate an echo from its output. The example prepares modes AFTER the positional three-route split, rather than filtering AFTER preparation. These operations have the same current total phase but different joint mode/position information. The initial correlation is not free or automatically native.

## 5. Exact invisibility criterion and two-sample reconstruction

For differences between two populations, current invisibility means Delta A+Delta B=0. Invisibility under every future F iterate means exactly Delta A=Delta B=0. Proof: the equalities at times zero and one yield (alpha-1)Delta B=0; alpha differs from 1 in a field. The converse follows from the transport identity. These differences are signed observations, not negative positive-weight populations.

Given adjacent exact algebraic outputs Z0,Z1,

B0=(Z1-Z0)/(alpha-1), A0=Z0-B0.

In fact alpha-1 is a unit in the integer phase ring:

(alpha-1)(-alpha^2-alpha^3)=1,

because alpha^4-alpha^2=-1. Decoding therefore uses the existing alpha coefficient recurrence and addition/subtraction, not a divided Cell or a floating-point phase division.

All future phase observations satisfy

Z_(t+2)=(1+alpha)Z_(t+1)-alpha Z_t.

Two adjacent zero samples imply permanent zero for this phase under this two-mode model. One zero does not. Sampling only at 0,12,24,... sees perpetual zero in the echo example and misses the nonzero intermediate values. This is a precise sampling alias, not absorption.

These two phase observations do not reconstruct the entire positive population. Equal positive opposite-port pairs inside the same mode have zero phase forever and remain distinguishable by local port observations. The allowed observer/action scope cannot be silently enlarged.

For four-coefficient input errors bounded by epsilon in each of the two samples, the inverse has B error at most 8epsilon and A error at most 9epsilon. Each of the twelve alpha multiplication matrices has row absolute sum at most two, hence every future predicted coefficient error is at most 25epsilon. These are symbolic coefficient-interface bounds, not a precision guarantee for an unspecified physical sensor.

## 6. Actual finite validation and source boundary

The new local suite passed 26,645 assertions. It covers all 4096 binary initial position populations; all 20 reachable atomic states with inverse/period and 24-step traces; all 190 reachable-state pairs; all 288 full-carrier rotation covariance cases; mode-preserving filtering; the echo through 36 steps; permanent within-mode zero; 256 coefficient-error vertex pairs over twelve phases; and 20-bin CWM quotient comparisons.

Actual CWM calls: cwm_edge=102491, cwm_propagate=77186, cwm_recoalesce=173974. Source incidence calls: successor=18459, phase_kind=40, reflection=0. These are call/assertion counts, not independent experiments or full package tests.

An initial checker evaluated the recurrence at t=1 using the duplicated initial sample. Restricting that check to t>=2 fixed the harness. The model and dependencies did not change; the failed checker is preserved locally. This is an indexing error, not physical residual.

Local reproducible package: euler_autonomous_echo, run python check_autonomous.py with Python3.10+.
New module brc_autonomous.py SHA256 d8268e8723cd314ad28df1af51d0014ff48db7329035f4632b8867f8da421224.
New checker check_autonomous.py SHA256 e6989803026bded58da29bbf097ec20caad73a037414764e405b9a1f32f9d235.
Detailed local NOTE.md SHA256 30a2b0adc807be820133aa8c1898b86c661ddfd65d5960660578206f9db73a7d.
The executed code, complete logs and dependency bytes remain in the conversation artifact; this Source note is a proof/validation-frontier record, not a claim that those entire bytes were newly published here. Prior check suites were consumed rather than rerun as new results.

Background attribution: Kamb et al., Time-Delay Observables for Koopman, arXiv:1810.01479v2; Das and Giannakis, Koopman spectra in reproducing kernel Hilbert spaces, arXiv:1801.07799v8. Abstracts were checked for attribution only, not for a native-physics bridge or numerical fallback.

Still open: derive the mode and preparation from a specified native local field/triadic transition rule; prove the full-X6 bridge, occupancy and interaction constraints; establish physical clock, distance, energy and sensor laws. No quantum entanglement, native-force generation, independent review or algorithmic speedup is asserted. Next scientific unit: a specified local mode-changing interaction with an exact joint BRC transfer and analysis of the resulting permanent-invisibility subspace. Do not rederive this autonomous echo or its two-sample recurrence as new progress.
