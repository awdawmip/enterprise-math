# PREFIX-1133 — Two-moment joint separation of the last two lines

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

Continue PREFIX-1132 at eab9003f04bde31248d82d1a05ea90660d680819:research_notes/portable_direct/2026-11-27_r6_prefix1132_transverse_moment_strips.md, frozen P000 V5 and companion pins f42f2906d77f24085c123f3ccfe9667d41caa96d. Same signed reversal -5, 5q cover, O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. Auxiliary algebraic readouts, no new native spatial axes or native CT execution. Existing carrier correspondence, analytic boundary, root isolation, and unresolved inherited 8400/8800 process exit evidence remain conditions. Current global entries checked at c08e75c9e6571105e25752f3db4f7bd73c1e9385. Existing activity record EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 / TASK_RESEARCH read at main, 75 checkpoints; this run did not establish a new CLAIM or assume that a Sites identity is the old Chat session. Owner read r6-20261127-1947-leased-read SUCCEEDED, as_of 2026-11-27T11:47:35.110532Z, LEASED tasks=[], next_cursor=null, Source 40334090ce5d25e6d7d44aed05e57ce22357f6bd.

## Proof and actual computation

For L>=10^100 retain the full candidate rectangle rho in [p/q,p/q+K/L^2], c in [h/q-H/L,h/q], where K,H,q0,d,E are the fixed PREFIX-1132 constants. The same coefficients a must satisfy F_a(t*)=G_c(a,t*)=0 and the k=10000,10400 moment inequalities |M_k a-y_k|<=eps_k. On the entire necessary rectangle enclose the four observers by the shared anchor outer set m+sum_j[-1,1]C_j+[-e,e]; the moment errors include their permissible target residuals. All entries of the compact certificate are in common grid 10^-125. Necessarily zero belongs to this set. For any integer n, necessity implies |n dot m| <= sum_j |n dot C_j|+sum_i |n_i|e_i. A strictly reversed inequality is a complete certificate of exclusion; no optimizer accuracy assumption is needed. The integer normals are found from the generators of the enclosing zonotope, including the error axes, by exact integer minors. This is the same separation principle as PREFIX-1131 in four observation coordinates.

Executed two_observers.py (PREFIX-1131 tail_observers.py with the two lines from scan_moment.json instead of prefix1128_result.json, and output two_observers.jsonl). Reused inherited exact basis and 9600 compact anchor, product-rule tail payments, outward 10^180 Horner evaluation, and frozen extra_rows.json from the 1131/1132 archives. The point/root and G_c enclosures are uniform on the full candidate rectangle, not just on its center. No new high-order anchor or matrix inverse. For each line, single moment searches at 10000,10400,10800 (105 nonzero normals each) did not separate; the paired 10000+10400 test (525 nonzero normals) strictly separated both. Nonseparation alone is not a feasibility proof for the exact model.

Both share the exact same normal and columns, with different centers. Center/support ratios 34.714347973285086 and 213.51446668020867. Independently ran verify_two.py: exact Fraction rerun of rounded PREFIX-1132 lattice enumeration (18 points, determinant 1, two primitive lines), then integer dot products for both separation witnesses and exact dyadic boundary calculation. All assertions passed. Thus for all L>=10^100 any true pair has q>3*10^61, hence gap>=q>3*10^61. Under inherited sharp curvature q^2<4EL/d for triple anomalies and q<=sqrt(L) for close pairs, first not-excluded fixed dyadic starts (base 10^8) are:
L3=7515336264876266329246337909725878487602184156506623586263331108903068880366747019083836794831259849702191923200000000
L2=985050154909861980306976002503590345126993481761636166698707335106143044287430265285356656372122891020165699757670400000000
These improve the prior starts by factors 8 and 4. Earlier windows retain their inherited coverage. No claim of attainability at these new starts.

## Compact exact witness and reproducibility

Common 12 projected columns for F,G_c, in order:
```python
C=[[3744138645775498910841297928701976010966640315,-87125244309961656188605995439254644350120196792],[-161039656349520894471888359937205864380223,3746573643488776666579887859681069553495355],[2298254077145580893797380295013148626,-53458267472769732129352373972486955517],[-47952155714854405058160188075338,1115182088175091721930947313324566],[970258271083964521363312982548236062773,-72120495286988764488827521413216860724180],[-466583415180187615239670236197498944780635,40347985749191228916185797857499750580988601],[-4422552409729,-14544658619171738],[-30551863247001164,2239318452415096038],[-36535640931316125,2363560184834305474],[814480300480595744,-19198820539636586492],[5395617291183169,-401062895330366980],[-1525853534519761,131948789140695908]]
e=[778398383415451143,7186278565963893173986745928764695745,120600466,120600014]
k10000=[-9439727292964913715644,563814399574156417,-12547204637116,543387970,0,0,66,-14,-1,0,0,0]
k10400=[-33057192159364659829729,1850874067992514339,-36609963069810,1189019200,0,0,64,-13,-1,0,0,0]
U=[v+[k10000[j],k10400[j]] for j,v in enumerate(C)]
n=[47060861440738090360099441454334029238204137499157446227105230927859385761171983877,544210994542182934889244412685928085380302514182243507532777114352251120650624895,-47362095591152182135657220791657063946426266987522833348029762315639085449501669769255701700683054509376963,17420509818126641016416272032863043260523822662802069894011886462697186045424886674351881591688965870543603]
m1=[2214347817314167573882690788350419893081343,-63390526291718076026146704353917690779554866,-5125943210844204295,-17950719237217173155]
m2=[2463087783338763487826660163395794195860131,-81957528329677233510352647727776792498122067,-5125943210844204295,-17950719237217173155]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
B=sum(abs(dot(n,v)) for v in U)+dot(list(map(abs,n)),e)
assert abs(dot(n,m1))>34*B>0
assert abs(dot(n,m2))>213*B>0
```
The preceding code is a compact transcription of the executed certificates, not an independent re-generation of the basis and observer intervals. Full executed local file hashes:
- two_observers.py 6c297fcb132158686fd50d848b9bf5a5170857320a34da043f930fb840b38a3d
- two_observers.jsonl 9ba43ad58213469fbab92f75ad1cf3de0dbc94cf7b8b1aa88c8e5e02d731250e
- two_observers.log 15cd73cff61907c1ce729778dd412f38ebcbdc02cc085ce373d8f923df4226d7
- verify_two.py 3e85d8215afe71c1b199a2d0f0b63d10df4cd5ab7eefb8f822c2e5c22952b5c2
- verify_two.log eb5e01af4897606d29e523cd81dd1fd67785e236a7fe63f46a866d7622f9fff8
- two_summary.json 97a118a3ed392060ac579321375b6f7f622a6917ae00f52ebdc2669c00a06af0

Next: convert the shared four-observer normal to a normalized affine strip using Q=G-sF+w1(M10000 a-y1)+w2(M10400 a-y2), with s=-n0/n1, wi=n(i+1)/n1. Attempt affine_two.py reached basis ready but timed out, no new parameter interval. Avoid uncontrolled denominators; use fixed-grid coefficient intervals and perform point/derivative evaluation in separate checkpoints. Alternatively expand existing integer enumeration beyond 3e61 using the current four-observer separator. Remaining single endpoint m=47247757565973207955345875119021762026915609, true fixed-spectrum unbounded separation and B_fix,odd(32) remain open. Independent review pending.
