# PREFIX-1123 — exact pair-gap profile, sharp independent-box witnesses, and close-pair lacunarity

2026-11-27. Author analytic proof and exact rational auxiliary computation; NOT_REVIEWED. Own Researcher EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322; original registration r6-20261123-2358-session-start-own-v1 read back SUCCEEDED. Current LEASED read r6-20261127-0950-leased-read SUCCEEDED/error=null, as_of 2026-11-27T01:51:06.003618+00:00, Source de172667470a089fed901dd752f14fa8e1258435, tasks=[], next_cursor=null. Independent directed continuation; no new CLAIM or shared Task state change.

## Inputs and scope

Parent f693b04242fc5b68c77a8bb7bc67c0f226617014:research_notes/portable_direct/2026-11-27_r6_prefix1122_root_only_and_triple_exclusion.md. Preserve frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d, joint relation observer, Heartbeat native X6/time, residual-fidelity companion, signed BRC carrier, signed reversal -5 with phase cover 5q, chart O incoming -e1, next incoming -d, both orientations of Link{O,e1} blocked without renormalization, exactly two negatives and inherited carrier identities. Current global entries main@7b7d94b79d64fbe5cb5615053c42a478cb21783e, current portable and continuation protocols read. The integer coordinate below is an auxiliary observation preserving the line relation, not a new native spatial object, dynamics or CT calculation. No new anchor evaluation.

Frozen exact box inputs (grid 10^85):
- 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json, SHA256 367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9, supplies C,T.
- 7c0ecbd38264af8fbee8a352f0b4fa47f62ffc21:research_notes/portable_direct/2026-11-27_r6_prefix1122_root_9200_only.json, SHA256 b17b098179d915eabbdefc8f6050a8d401e06731a59e7f130350ce6aaab1948f, supplies R.
Both local archive inputs exactly match the frozen hashes; 8400/8800 anchor exit evidence remains unconfirmed. Inherit PREFIX-1107 endpoint sign correspondence and E=400000, PREFIX-1118 collinearity, PREFIX-1120 small-q exclusion and unimodular V, PREFIX-1122 finite sweep. Stage46 applications are conditional on inherited certificates. The generic proofs apply to their declared arithmetic hypotheses.

## 1. Signed pair strip, including a positive lower payment

Write f(m)=rho*m+c+d/m, d>0, e_m=f(m)-j_m. A near hit is an integer pair with m>0 and |e_m|<=E/m^2. For two different m, a<b in [L,2L), let their primitive line be q*j-p*m=h, gcd(p,q)=1, q>0. Then b-a is a positive multiple of q. Let delta=rho-p/q, gamma=c-h/q. Exact elimination gives
delta=d/(ab)+(e_b-e_a)/(b-a),
gamma=-d*(1/a+1/b)+(b*e_a-a*e_b)/(b-a).

Use R=[rho_l,rho_u], C=[c_l,c_u], T=[d_l,d_u]. The original PREFIX-1120 small-q certificate applies to L>=M=16225927682921336339157801028812800000000. It was independently verified with the smaller R here: let P=72486411641368782354423090020719211170157, Qw=3380890274893182433251695995418378677023, Q0=544447235321021556325566186117974922692. For eta=max_{r in R}|r-P/Qw|, the exact inequality 1/Qw-Q0*eta-(d_u*Q0+2E)/M^2>0 holds (display 2.5982453965748043e-40). Rational separation and q*|delta|<=(d_u*q+2E)/L^2 exclude all q<=Q0. Thus q>=q0=Q0+1. Also q0>16E/d_l.

Set k=d_l/4-2E/q0>0, K=d_u+2E/q0, g=d_l-4E/q0>0, H=2d_u+4E/q0. Since L<=a<b<2L and b-a>=q, the slope error magnitude is at most 2E/(q L^2), and the intercept error magnitude at most E*(a+b)/(L^2*(b-a))<4E/(q L). The exact signed identities imply
k/L^2 <= delta <= K/L^2,
g/L <= -gamma <= H/L.
In particular every pair in this fixed window satisfies the joint strip
(rho_l-K/L^2)q <= p <= (rho_u-k/L^2)q,
(c_l+g/L)q <= h <= (c_u+H/L)q.
For all future L>=L0 one can use the larger monotone tail strip with p/q in [rho_l-K/L0^2,rho_u], h/q in [c_l,c_u+H/L0]. This is an enclosing strip, not a claim that all its lattice vectors give near hits. It retains the common denominator, intercept, and the directed signs of both residuals.

## 2. Exact enumeration and minimum gap

Reuse V (rows given in the verified script), det V=1, W=V^{-1} integral. For q0<=q<=Q, n=V(q,p,h). The component extrema of each n_i are attained at corners of the q, p/q, h/q product intervals (the map is multilinear). Take integer ceil/floor bounds. Enumerate the two shortest component ranges; solve the remaining coordinate range by intersecting all six linear inequalities after substitution (q,p,h)=W*n, using exact rational ceil/floor. Retain gcd(p,q)=1. This exhausts the relaxed strip with no enumeration over individual q or m. A q>Q cannot improve a verified minimum q<=Q.

For L0=43135914667441023671467224139231409077819431076064915969765776398745600000000 (about 4.3135914667441024e76), with Q=q1 below, the monotone tail strip has n1 in [-9,-1], n2 in [-10,49], n3 in [-60,2]. Only 540 coordinate pairs need inspection. Exactly one primitive integer vector survives:
q1=25525828069781181809194072375836326527854111431881463
p1=547274691134844133100660660565507569107331663159748751
h1=2530656387096617982971408986731143970024460336871611503.
Hence for EVERY integer L>=L0 and any two actual near hits a,b in [L,2L), b-a>=q>=q1. This is a tail interval-information bound, approximately 2.552582806978118e52, over fourteen times the previous 1.8e51 exclusion threshold, beginning below the old 1e80 tail threshold.

Fixed-window signed strips (cap Q=10^53) sharpen the result in the five successive fixed doubling windows. Values below are exact q minima of the relaxed strips; each is attained by an exact pair witness inside the independent parameter box, so also the true minimum possible pair gap over that box for the indicated window.

| L (display) | Primitive vectors in strip | Min q (exact) | Coordinate pairs |
|---|---:|---|---:|
| 4.3135914667441024e76 | 90 | 35251909703052195906876986765398933871019858693974178 | 6755 |
| 8.627182933488205e76 | 56 | 29416260723089587448267238131661369465120410336718549 | 2156 |
| 1.725436586697641e77 | 41 | 27471044396435384628730655253748847996487260884300006 | 1020 |
| 3.450873173395282e77 | 36 | 27471044396435384628730655253748847996487260884300006 | 672 |
| 6.901746346790564e77 | 32 | q1 | 500 |

All five witnesses have residuals exactly zero, not only within the E/m^2 band. For any primitive relation (q,p,h), choose a congruent to -h*p^{-1} mod q, b=a+q, and set
d0=(d_l+d_u)/2,
rho'=p/q+d0/(ab),
c'=h/q-d0*(1/a+1/b).
Then f'(a) and f'(b) (here f' denotes the function for the alternative tuple, not a derivative) equal the two integers (p*m+h)/q. On the finite arithmetic progression of allowable a, rho' decreases and c' increases. Binary search for the first a satisfying rho'<=rho_u and c'>=c_l, then check the remaining two box bounds. The exact script verifies both integer observations, all bounds and b-a=q for every witness.

In fact for EVERY integer L>=Ltail=690174634679056378743475586227702545245110897217038655516252422379929600000000 (16*L0), the minimum gap over the independent box is exactly q1. To see this, let a be the greatest integer <=2L-q1-1 in the above congruence class, so 2L-2q1<=a<b<2L. Let A=2*Ltail-2q1>=Ltail. Direct exact verification gives rho_l<p1/q1<rho_u and c_l<h1/q1<c_u, and
p1/q1+d0/A^2<rho_u, h1/q1-2*d0/A>c_l.
The two strict margins are about 4.316823512982178e-82 and 6.429657861598279e-79. These inequalities hold for every later L by monotonicity, hence the construction gives a gap-q1 exact pair for every such L. This is sharp independent-box information, with alternative tuples allowed to vary with L. It does not exhibit actual BRC near hits or establish their presence at every L for one fixed tuple.

## 3. New general close-pair lacunarity theorem

For fixed actual parameters and L>=M, by q>=q0>16E/d, the signed slope identity gives d/(8L^2)<delta<9d/(8L^2). Call a dyadic window close-pair type (A,theta), A>0 and 0<theta<1, if some pair has distance b-a<=A L^theta. Then q<=A L^theta. The actual line is unique when at least two near hits exist because PREFIX-1118 collinearity applies at L>=10^8; for exactly two it is defined by that pair.

For two such windows L<=L' with distinct slopes p/q and p'/q', integer rational separation gives
1/(q*q') <= |p/q-p'/q'| = |delta-delta'| <= (9d_u/8)/L^2.
Since q*q'<=A^2 L^theta L'^theta, this implies
L' >= L^((2-theta)/theta) / ((9d_u/8)*A^2)^(1/theta).
Same slope entails d/(8L^2)<delta<9d/(8L'^2), hence L'<3L. It can occur at most twice on the fixed doubling grid. For K0=9d_u/8, beta=(2-theta)/theta>1 and B=(K0*A^2)^(1/(2(1-theta))), distinct slope starts obey L'/B >= (L/B)^beta. Thus, from any fixed grid start Ls>max(M,B), the number of distinct close-pair slopes through X>=Ls is at most 1+floor(log_beta(log(X/B)/log(Ls/B))); number of close-pair windows is at most twice this. Earlier finite starts add only a constant. This proves O(log log X) for any fixed A,theta, without assuming a finite irrationality exponent. It applies to pairs (not necessarily triples) whose gap satisfies the declared sublinear condition. For arbitrary pairs without the sublinear gap condition this particular conclusion remains unproved.

## 4. Sharp square-root-gap exclusion

For theta=1/2, A=1, all close-pair windows have q<=sqrt(L). No pair before M on the fixed grid by PREFIX-1122 finite sweep. For M<=L<L0, q>=q0 and q0^2>L0, so no sqrt-gap pair. For L>=L0, q>=q1 and hence L>=q1^2 is necessary. Exact q1^2 is
651567898648028893865846754858096566169398738826897543142031121259205420310491598391008605010384083020369.
The first fixed doubling start at or above this is
854394814368364032958008682467820845841081808942661107978816643128887890312256220009184834774630400000000
(about 8.54394814368364e104). It exceeds Ltail; an exact gap-q1 alternative witness is verified there. This is therefore the sharp first possible sqrt-gap window for the independent box, under the inherited prefix and parameter assumptions. If an actual close-pair slope first appears no earlier than this, a SECOND DISTINCT slope must start at >=Lfirst^3/(9d_u/8)^2, approximately 5.24742075910179906e312. General close-pair theorem covers all larger scales, while this finite-parameter exclusion cannot by itself establish eventual absence.

## 5. Evidence and next problem

Exact Python standard-library Fraction computation ran normally, all assertions passed. No new native CT or anchor work. Total inspected coordinate pairs in the tail strip and five local strips: 11643 (540+6755+2156+1020+672+500). No timing speed-up inferred from these counts. Input SHA256s above. Exact code:
d300f30526b4314276ef48e2d1951408087c01a4:research_notes/portable_direct/2026-11-27_r6_prefix1123_pair_gap_verify.py (Git blob e2d40e3916d06b7a775aaaad6134d97fd1f0fbff; local SHA256 f84c728e08e51883061e7086f4e1bb000d41bcd1ab15a7a42fc2250d90aa81ae).
Compact integer witness certificate, retaining exact a,b and q,p,h with exact reconstruction formula (not floating-point parameters):
27b998bc9f492af8a0be4cd0ff85693eddea73c0:research_notes/portable_direct/2026-11-27_r6_prefix1123_pair_gap_certificate.json (Git blob e59b116b12f5a815f41dc236baeb7e78ae69a3e7; SHA256 3ca07744bb9d1b00aa0cc395d00b0d0b292ab72267dfac820f133d03c1c3a4ee). Earlier transcription was replaced after exact blob mismatch; final content is verified byte-identical to the compact local certificate.
Run the verifier beside frozen inputs named root_8800_result.json and root_9200_only.json. Full output pair_result.json SHA256 951e31bd1b32acf3cd24b979e208e5397f1b1ff32be4b2970e20c6787074e857; execution log pair.log SHA256 f4188a98ce37d68d4397bade2ebfeb0dd884304e2e315b0191f9c2d4de49dd23. Raw output and log also retained in execution package.

Next: use directional BRC root/jet correlations or a new low-cost root-only refinement on the three PREFIX-1122 endpoint candidates. The present results strengthen pair geometry and constrain rare close-pair windows; actual isolated hits, pairs with macroscopic gaps, all-scale eventual separation, exact-zero classification and mother B_fix,odd(32) remain open. Existing continuous endpoint upper bound remains 35763703231524369452081938126483743402578 exclusive and triple exclusion first possible dyadic window 6.51851512427e99, both conditional as before. Independent review and Activity observation audit pending.
