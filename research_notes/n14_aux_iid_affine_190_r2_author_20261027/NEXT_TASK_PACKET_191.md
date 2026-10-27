# Stage191 — portable next research unit (DUAL ONLY)

Mother problem: external IID three symbols, horizon N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Minimize max(E_PT,E_QT) under eP,eQ<=alpha and arbitrary ordered-history randomized stopping.

Stage190 author-verified full real segment endpoint:
alpha190=28137949158459611576537/80134219991312171532288,
V190=3422790017676192400495567/320536879965248686129152,
X=(8,0,1) Q/C decision coin x=21216994209825749/44937930240000000, and Y=(4,2,0) P/C coin y=1 (forced P at boundary).

Exact Stage191 dual scan ONLY:
K191=610519409541/3646579780,
L191=30208318184/182328989,
H191=531209309176160736181221937/4161698766215586030551040.
Ties exactly X=(8,0,1): Q/C, Z=(10,5,2): P/C. There are 680 states and 1238 strict positive gaps, min=8957179515094375931/451573216820267581440. First gap closure parameter is 129843274250808073495776/78610651785691125766097 under dK=-1080671/869760, dL=-1, first new tie Z. No Stage191 primal has been established.

Next independent unit: evaluate four X/Z deterministic strategies by rational suffix DP and a separately unmerged ordered-history positive P/Q integer mass DFS. The cones should be disjoint: from X to Z the first symbol count must increase 0 to 5 in just two draws; reverse depth is impossible. Verify mixed term equals zero, derive eP=eQ balancing x(z), test x(0) equals Stage190 endpoint, legal real range, tP>=tQ, support equality, and strict right sharpness. Return full theorem or exact obstruction; then scan Stage192 dual-only. Keep proofs, executable code, stdout, rational certificate and unresolved questions. This is an external auxiliary model, not native P000 X6.
