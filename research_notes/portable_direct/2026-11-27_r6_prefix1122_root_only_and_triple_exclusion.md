# PREFIX-1122 — targeted root-only refinement, complete old window closure, and renewed sharp triple exclusion

2026-11-27. Directed continuation of PREFIX-1121; author proof and exact rational auxiliary computation, NOT_REVIEWED. Researcher EM-DIRECT-780BBE, TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. Original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED read back. Current owner read r6-20261127-0850-leased-read SUCCEEDED/error=null, as_of 2026-11-27T00:51:36.225490Z, Source 9b379b336f3e3c0eb6c16fc20446110995618aee, LEASED tasks empty, next_cursor null. No new CLAIM or shared task state change.

## Scope and sources

Parent: 27d503ba8c0dff33ff4f97e2975985130428b684:research_notes/portable_direct/2026-11-27_r6_prefix1121_signed_curvature_sharp_box.md. Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d, joint observer and Heartbeat X6/time companions, ACTIVE worldview, current research continuation and portable research rules read. Global entries verified at 05f11a2ce69d466ed3bcdc818993eabcb8b2c36e. Preserve signed carrier, native X6/time, signed reversal -5 with phase cover 5q, chart O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives and inherited carrier identities. All integer calculations below are auxiliary observations, not native coordinate reinterpretations. No new physical propagation or CT enumeration. Inherit PREFIX-1107 explicit endpoint error E=400000 and sign/monotonicity correspondence. Original 8400/8800 anchor command exits remain unconfirmed; independent review pending.

Frozen exact box input: 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json, blob e03d50ec3c79588577e8aaef7e194adf7562f2c8, SHA256 367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9. R,C,T denote rho,c,d intervals on grid G=10^85. The earlier 122 candidates and full window end come from PREFIX-1117 exact archive; PREFIX-1116 supplies the lossless convergent lattice sweep. PREFIX-1121 supplies the sharp curvature and signed integer-coordinate enumeration.

## 1. Targeted root-only information upgrade

Instead of re-evaluating all high-order density jets, use the inherited signed six-component density representation F(t)=sum_i a_i P_i(t) and the verified anchor dual for the single point observation. Reuse the root-only interval Newton law: for x in the current root interval I, a root t* in I, point enclosure V containing F(x), and a whole-I derivative enclosure D avoiding zero, t* belongs to I intersect (x-V/D), by the mean value theorem. Pay the anchor dual, point rounding and rigorous polynomial tail separately. Transform the resulting t enclosure by b=t^2/36, rho=1/b-1. Preserve C,T unchanged. This is the same auxiliary signed BRC carrier, not a replacement classical propagation.

Actual execution: replay_8000.py unchanged (SHA256 ef7609277d1cbaa80b99689a1965a1d80ecd33da5ff6bbec1d929f2ba4510cfb); N=260, exact recurrence and 6x6 anchor inversion, anchors [8000,8400,8800,9200]. Use the original jet_result.json signed F' enclosure on the inherited domain and 10^140 outward interval grid. Start from the frozen 8800 rho box; truncate the original root_8800.py immediately after intersecting rho with its parent enclosure. Save root, Newton records and anchor metadata at grid 10^85. root_9200_only.py SHA256 8d5625d10651f7d7b99bde29d4e16f074e5bc0e60b7e166dabfc27c8005c337f. Actual command exited normally (0). This resolves the new run's exit evidence, not the historical process exits.

Raw exact output (actual local bytes match remote Git blob):
7c0ecbd38264af8fbee8a352f0b4fa47f62ffc21:research_notes/portable_direct/2026-11-27_r6_prefix1122_root_9200_only.json
blob 00d5be71320bf11115cefb6d75494597d6600f8c
SHA256 b17b098179d915eabbdefc8f6050a8d401e06731a59e7f130350ce6aaab1948f.

New R endpoints (divide by G):
214400367204046439832747905320189591538351105920951930768238591471337001196383230812538
214400367204046439832747905320189591538351105920951930768238591471337001196383230825066
Width of outward certificate = 12528/G = 1.2528e-81. Improvement over frozen 8800 grid width: 762.3987068965517. The internal pre-output-grid width is about 1.2526703527919083e-81. C,T retain their exact prior endpoints. Only a single parameter was refined; no higher density jets were recomputed. Though the earlier worst-case sufficient width reduction 24209 was larger, the actual new center falls into a gap between all 122 disjoint thresholds.

## 2. Full old window closure and new endpoint range

For each old candidate (m,j), form exact lo=R_l*m+C_l+T_l/m-E/m^2, hi=R_u*m+C_u+T_u/m+E/m^2. If lo>j, inherited sign D_m(j)<0; if hi<j, D_m(j)>0. Every one of the 122 old candidates resolves, 62 negative and 60 positive; minimum strict sign margin 1.4916636872650388e-41. Independently rerun the complete convergent lattice sweep of 107 dyadic windows [10^8,M), M=16225927682921336339157801028812800000000. Exact stats: 279 lines, 1573 function evaluations, 0 candidates, maximum 6 lines/window. The full boundary interval width is <1 throughout the scanned range (uniform elementary bound from the coefficient widths and E).

Extend two further windows, 6 lines and 34 evaluations; counts [0,3]. The remaining exact pairs:
(35763703231524369452081938126483743402578,766775110541536709959744552935192176324271)
(52801950178082977264042087882625644459467,1132075750727075563192724031034655296703948)
(63011518788808872386648010758405784326423,1350969276640529380986425315094746462478865).
The full screened range ends at 64903710731685345356631204115251200000000 exclusive. Under the inherited sign correspondence, every integer m from 10^8 through the first new candidate exclusive satisfies K_last(m)=floor((r*m+s+v/m)/G), with r,s,v the following grid midpoint integers:
r=214400367204046439832747905320189591538351105920951930768238591471337001196383230818802
s=991410104376806546245006442360370506919542722555360711737697284896269484488367585280480
v=96908626596415488199625924806903600960651737707918479478269855625061455284990566973195
The same formula is certified for the rest of the screened range except the three candidates. The verifier checked midpoint predictions on all 122 resolved positions.

## 3. Renewed sharp box boundary for triple near hits

For any true triple on a primitive integer relation q*j-p*m=h within a dyadic window [L,2L), PREFIX-1121 gives q^2<4EL/d. Its prior full-box denominator lower bound q>=q0=2655223732550132521125580881859760580045275386620690 remains valid for the smaller box.

Using the exact two-hit signed identities, for q>=q0 the enclosing inequalities are
R_l*q-up <= p <= R_u*q,
C_l*q <= h <= C_u*q+uh,
where J=4E/T_l, K=9T_u/8, H=2T_u+4E/q0, up=K*J^2/q0^3 and uh=H*J/q0. These follow from 0<rho-p/q<=K/L^2, 0<h/q-c<=H/L and L>=q^2/J. The signs are retained. The prior q0 candidate is excluded already by its rho gap: new rho-p*/q* between about 1.397117e-79 and 1.409645e-79, much greater than K*J^2/q0^4. Exact enumeration below covers all q0<=q<=10^53.

Reuse the PREFIX-1120/1121 unimodular V:
(13241695572016246280452795405,-614903515325433031059117378,-586453816401334287434546)
(1182616791650392258028253444,-74796824988556406807726418,4246778208283374384362279)
(-7752265403315380654172299023,382363756442351370763912993,-4494886358260478563501531).
For n=V(q,p,h), compute corner bounds of the signed enclosing polytope: n1 in [-9,-1], n2 in [-41,2], n3 in [-36,10]. Its inverse W is integer (check V*W=Id). For each of 396 n1,n2 pairs, intersect the integer n3 range with all six transformed inequalities by exact rational ceil/floor. Retain gcd(p,q)=1. All 27 surviving primitive vectors are enclosed; their minimum denominator is
q1=25525828069781181809194072375836326527854111431881463
p1=547274691134844133100660660565507569107331663159748751
h1=2530656387096617982971408986731143970024460336871611503.
For q>10^53 the lower bound is trivial; q<q0 was excluded by the parent. Hence q>=q1 and L>q1^2/J >3.9464093870183e99 on the fixed grid, inheriting the initial finite sweep. First possible dyadic start is
L1=6518515124270355476059026202910010115364698859730996002035649437934020159242677459786871603200000000.
This is exactly 128 times the prior box boundary. It is a triple exclusion range, distinct from the endpoint certification range.

## 4. Sharpness of the new independent parameter box

The alternative tuple construction of PREFIX-1121 is executable with (q1,p1,h1) and L1. Let d0=(T_l+T_u)/2, r0=(-h1*inverse(p1 mod q1)) mod q1, U=2L1-2q1-1, a=U-((U-r0) mod q1), b=a+q1, z=a+2q1. Actual a:
13037030248540710952118052405820020230729397719408046899518091904825316237046919237439825989482992305.
Set lambda=d0*q1^2/(2*a*b*z), rho'=p1/q1+d0/(a*z), c'=h1/q1-d0*(1/a+1/z)+lambda. Exact substitution gives e_a=lambda,e_b=-lambda,e_z=lambda, with all three integer observations (p1*m+h1)/q1. The verifier checked L1<=a<b<z<2L1, rho',c' in the strict interiors of the new boxes, and each |e_m|<=E/m^2. Maximum budget usage lambda*z^2/E=0.6054153916625369 (rounded). This proves the first possible fixed-grid triple window is sharp for the NEW independent parameter box, not that this alternative tuple is the true BRC tuple.

## 5. Reproducibility and next action

Reproduction delta: extract PREFIX-1117 execution archive. Run root_9200_only.py (same root_8800.py through the line rho=I(max(rho.a,rl),min(rho.b,ru)), replacing anchor list and parent input, then output root/t/Newton/anchor). With the retained prefix1116_lattice.py, run prefix1122_window.py and prefix1122_triple.py. The latter is the exact PREFIX-1121 verifier with R overridden by new root grid endpoints, qmin=q0, Q=10^53, output filename changed. All runs completed normally. Full local execution package includes scripts, original frozen inputs, logs, exact result JSONs and manifest. No timing advantage claimed merely from operation counts.

Local output hashes:
root_9200_only.py 8d5625d10651f7d7b99bde29d4e16f074e5bc0e60b7e166dabfc27c8005c337f
prefix1122_window.py a8149f9155d467b6e3c9eacc17c9d3336faba2e14ff7090776ebc1b0809eee41
prefix1122_window_result.json 43119d1b0a618d33e5e12187ca7e82630991f75c7459a93a1ca73e35ec2ce1df
prefix1122_triple.py abb30ba0609ce12aee26429e311be9af728950f000c236576a62e5dbcce72c8b
prefix1122_triple_result.json 0342555d89a3d29fdf5cbf2232bd4d3b535ca1202f64a065cb21b4b4a698c19b

Next: use a small targeted root refinement for three new endpoint ambiguities, or compute directional joint root/jet support (rather than axis-aligned c,d marginal widths) against the surviving triple line. Investigate the precision bottleneck of 261-term anchor error versus native moment information, retaining all signed terms. Single/pair exceptional arithmetic, exact zero, actual triple existence, all-scale separation, remaining spectrum and mother B_fix,odd(32) open. Independent review and Activity observation audit pending.
