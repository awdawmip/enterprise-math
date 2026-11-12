# X6 serial signed-word observations: exact gap graph and sharp two-stage injectivity

Date: 2026-11-12 (Asia/Shanghai)  
Status: DRIVER_AUTHORED_EXACT_AUXILIARY_THEOREM / CANDIDATE_OBSERVER_MODEL / NOT_NATIVE_RESULT  
Line: X6 native signed Cell directions, time-ordered phase readouts, BRC path provenance.  
Contributing role: existing RESEARCH_DRIVER scientific author (not an independent review of its own earlier notes).

## 1. Exact scope and upstream distinction

This note combines the signed **single-probe** difference lemma from
`research_notes/driver/2026-11-12_x6_signed_word_alias_threshold_and_common_increment_phase_recovery.md`
(source blob `2de1866d846ee13b801339293b9bac8c99dbdbcf`)
with the **serial coherent-state** setup in
`research_notes/driver/2026-11-12_x6_coherent_serial_phase_depth_alias_sharp_observation_box.md`
(source blob `3f7825a4e6e78b19c9b7a4cbfb3c3c552922c8f4`).
The former allowed independent registered probes or a specified shared increment; the latter made successive rotations act on the actual preceding state but permitted only positive-axis words. The present question is serial dynamics with unrestricted signed-axis words of fixed known lengths. None of these change the other's assumptions or conclusions.

Let `n>=2`, `D=(1,...,1)`, `q(z)=z-(min_j z_j)D`, and let `r=q(z_0)` be known. The hidden integer depth is `h`, with `z_0=r+hD`. For each registered stage `i=1,...,m`, a known signed permutation `g_i` acts first, then a signed native word of exactly `M_i` steps contributes net displacement `b_i`:
[
z_i=g_i z_{i-1}+b_i,qquad y_i=q(z_i),
qquad b_iin W_{M_i}.
]
Here `W_M` contains **net displacements** of words of exactly `M` symbols from `{+e_j,-e_j}`; the ordered words, BRC branches, multiplicities and any triadic interaction state remain separate carriers. Put `epsilon_i=g_iD`; it has `k_i` negative and `n-k_i` positive signs. We compare complete histories `(h,b_1,...,b_m)`, not ordered words.

## 2. Exact multistage collision theorem (all n)

For two histories with equal readouts at every stage, there are uniquely determined integer raw-depth gaps `d_0,...,d_m` such that `d_0=h-h'` and `z_i-z'_i=d_i D`, and
[
b_i-b'_i=d_iD-d_{i-1}epsilon_i.	ag{1}
]
Conversely, every integer gap chain satisfying the feasibility conditions below can be realized by two histories with equal registered observations, for **every** initial registered relative chart `r`.

Define the exact step cost
[
C_{n,k}(a,b)=(n-k)|b-a|+k|b+a|.
]
The two-word difference lemma for signed unit-step words gives the necessary and sufficient edge condition
[
oxed{C_{n,k_i}(d_{i-1},d_i)le2M_i,qquad
C_{n,k_i}(d_{i-1},d_i)equiv0pmod2.}	ag{2}
]
Proof: equation (1) has `n-k_i` entries `d_i-d_{i-1}` and `k_i` entries `d_i+d_{i-1}`. A vector `v=b-b'` is a difference of two exact-length-`M` signed words iff `||v||_1<=2M` and `||v||_1` is even: concatenate a word for `b` with the reversal/negation of a word for `b'` and split a parity-correct length-`2M` realization in half. This proves both necessity and sufficiency. Inductively applying (1) yields equal min-zero readouts, because each raw-state difference is an integer multiple of `D`.

For even `n`, parity in (2) is automatic. For odd `n`, it is exactly `d_i≡d_{i-1} (mod 2)`, since `C_{n,k}(a,b)≡nb-(n-2k)a (mod 2)`.

**Gap-graph recovery certificate.** Create integer depth-gap vertices at each stage and draw a directed edge `a->b` when (2) holds. The complete-history-to-registered-endpoints map is injective iff the graph has **no** path `(d_0,...,d_m)` with any nonzero gap. A nonzero initial `d_0` is precisely a hidden-depth collision; a chain with `d_0=0` but a later nonzero gap is a fixed-initial-depth displacement alias.

For a stage with `0<k<n`, put `u=min(k,n-k)>0`. The cost obeys
[
C_{n,k}(a,b)/2ge umax(|a|,|b|).
]
Thus any admissible gap endpoints for that stage obey `|a|,|b|<=floor(M/u)`, making the graph finite whenever the relevant gap chain passes a mixed-sign stage. For pure-sign stages `k=0,n`, retain their exact edge equation rather than pretending this bound applies. The graph is a decision procedure for this declared model, not an assumed Heartbeat law.

## 3. Sharp two-stage theorem for every even n

Assume `n` even, `m=2`, and both `k_1,k_2` are mixed-sign (`1<=k_i<=n-1`). Set `u_i=min(k_i,n-k_i)` and `N=n/2`. The complete map
[
(h,b_1,b_2)mapsto(y_1,y_2)
]
is injective for every `r` **if and only if**
[
oxed{M_1<N,quad M_2<N,quad
       (M_1<u_1 	ext{or} M_2<u_2).}	ag{3}
]
Equivalently, a collision exists iff
[
oxed{M_1ge Nquad	ext{or}quad M_2ge N
quad	ext{or}quad(M_1ge u_1 	ext{and} M_2ge u_2).}	ag{4}
]
These thresholds are sharp.

**Proof.** Write the gap chain as `a=d_0,b=d_1,c=d_2`. The convex absolute-value cost obeys `min_x C_{n,k}(a,x)/2=u|a|` and, symmetrically, `min_x C_{n,k}(x,b)/2=u|b|`; both minima are achieved at an integer `x=+a` or `x=-a` (according to the minority-sign side).

If `b≠0`, the two edge costs are at least `u_1|b|` and `u_2|b|`; a collision requires both `M_i>=u_i`. Conversely, `b=1`, with the corresponding integer minimizers `a,c=±1`, realizes it at the exact corner `(u_1,u_2)`.

If `b=0`, a nonzero gap chain must have `a≠0` or `c≠0`. The edge costs reduce exactly to `N|a|` and `N|c|`. Thus the respective thresholds are `M_1>=N` or `M_2>=N`, and the witnesses `(a,b,c)=(1,0,0)` or `(0,0,1)` realize them. For even `n` all such edge differences have even L1 norm; by the exact two-word lemma every threshold witness is realizable by signed native words of the prescribed exact lengths (with any surplus distributed by common padding). These cases exhaust all nonzero chains. QED.

The statement is about net displacements. Two different ordered words can give the same `b_i` even when (3) holds.

**Hidden depth versus full history.** The criterion for unique **initial depth alone**, still for all unrestricted depths and every `r`, is
[
oxed{M_1<Nquad	ext{and}quad(M_1<u_1 	ext{or} M_2<u_2).}	ag{5}
]
Indeed a collision with `d_0≠0` either merges immediately (`d_1=0`, needing `M_1>=N`) or passes a nonzero intermediate gap (needing both minority thresholds). `M_2>=N` by itself can alias `b_2` at fixed initial depth, without making the hidden initial depth ambiguous. This separates two information-recovery claims that should not be conflated.

## 4. Concrete X6 signed triad-rotation example

Use the previously registered candidate `R(z_1,z_2,z_3,z_4,z_5,z_6)=(-z_3,z_1,z_2,z_4,z_5,z_6)`, with two successive serial stages `g_1=g_2=R`. Each stage has `k=1`, hence `u_1=u_2=1`, `N=3`. Full histories are uniquely reconstructible from both relative readouts precisely for integer length pairs
[
(M_1,M_2)in{(0,0),(0,1),(0,2),(1,0),(2,0)}.
]
All remaining nonnegative pairs allow a collision. A two-step signed history can therefore lose initial-depth identifiability already at `(M_1,M_2)=(1,1)`, in contrast with the positive-only serial model's exact first collision at `(15,10)`; the path alphabets are different.

For an explicit length-(1,1) witness take `r=0`, initial `h=1` and per-stage word `+e_1,+e_1` in history A; take `h'=0` and `-e_1,-e_1` in history B. After the first stage, raw states are respectively
[
(0,1,1,1,1,1),quad(-1,0,0,0,0,0),
]
both with `y_1=(0,1,1,1,1,1)`. After the second stage the raw states are
[
(0,0,1,1,1,1),quad(-1,-1,0,0,0,0),
]
both with `y_2=(0,0,1,1,1,1)`. Both ordered words contain no immediate reversal.

At `(3,0)`, the gap chain `(1,0,0)` gives **actual raw-state synchronization** after stage 1, so no later observation can undo that particular collision when both subsequent paths coincide. At `(0,3)`, the chain `(0,0,1)` instead makes the final signed net displacement nonidentifiable even with known initial depth. These are distinct mechanisms.

## 5. Exact finite validation and next Source-typed test

Independent exhaustive construction of reachable displacement sets `W_M` in four signed dimensions and actual two-stage signed sign-flip state transitions compared both readouts for all `(M_1,M_2)` in `{0,1,2,3}^2` and initial depths `{-2,-1,0,1,2}`. Every cell agreed with (3)-(4): the 5 allowed pairs were injective, the other 11 had an explicit colliding input. A separate integer gap-edge enumeration for the six-axis `k_1=k_2=1` case over `0<=M_i<=4` agreed with all 25 threshold decisions. The universal proof is (1)-(4), not finite testing. The concrete `R,R` witness above was separately computed coordinatewise with exact integers.

P000 V5 supplies six signed primitive Cell directions and triadic-force closure; `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` explicitly does not install a fixed heartbeat program. Neither this note nor the positive-only theorem supplies an actual `model_law_id`, admissible global-state transition, triadic coupling or phase/path-correlation rule. A future registered Heartbeat update candidate must first type its admissible words and information retained at each observation, then restrict the exact graph (2) to coherent state histories before a physical-dynamics claim or Native Result acceptance. Ordered BRC branch identity and joint relation preservation remain required wherever future operations use them.

Administrative status: authored auxiliary mathematical theorem saved for X6 time/rotation task intake; no Claim, independently reviewed DR, Source-native Result, terminal Task verdict, mother-objective completion or Foundation/P000 promotion follows from its publication.
