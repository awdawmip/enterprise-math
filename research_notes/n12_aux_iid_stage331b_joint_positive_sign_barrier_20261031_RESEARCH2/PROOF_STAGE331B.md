# Stage331-B — Joint-positive Bernoulli residual exclusion and exact six-chamber census

Date: 2026-10-31. Status: PORTABLE_AUTHOR_PROOF / EXACT_INTEGER_INTERVAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Verified sources and scope

GLOBAL_KNOWLEDGE_V1 frozen for this research run: main@1116bb082f6753de1b4f83b8284168c421622035; Enterprise Math canonical main@de8cc395170abe428e02abdcf8ee27a2aa4a09b2. Loaded current 00_BOOTSTRAP, OPERATING_MANUAL, project route, P000, ACTIVE worldview and portable research protocol. P000 startup projection matched original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Scientific predecessor: Stage330-B immutable commit f7143ddfe77676fceea52da64b9864cc9eb5b0aa. This is the inherited *auxiliary* Bernoulli BRC observer, not the native P000 X6 dynamics, third slice coordinate, triadic closure, time or final lossless Cell-address theorem.

For k=0,1,2,3, define B_k(z)=z^k(1-z)^(3-k), m=(61,21,9,9), w=(1,3,3,1), r_k(x,y)=(4B_k(x)+B_k(y))/5-m_k/160, and b(x,y)=(5/32) sum w_k |r_k(x,y)| for x,y in [0,1]. The binomial multiplicities are retained. Exact normalization yields r0+3r1+3r2+r3=0.

## Theorem A — full real square, not a grid experiment

For EVERY real x,y in [0,1]:
  
  r1(x,y)>=0 AND r3(x,y)>=0  IMPLIES  b(x,y)>1831/200000=0.009155.

This includes both sign-zero boundaries. It does not rely on Stage307 or the inherited cusp budget.

Proof. Set D=2^22, D3=D^3, Q_k(n)=27 n^k (D-n)^(3-k). For every closed dyadic interval [a,b]/D the extrema of Q0 and Q3 are the endpoints. For Q1,Q2 the minimum is attained at an endpoint; the maximum also considers 4 D3 when the interval contains D/3 or 2D/3 respectively. These are the only critical maxima, since B1 and B2 attain 4/27 at z=1/3 and z=2/3. For a closed rectangle [a,b]/D x [c,d]/D obtain the exact integer univariate bounds Xlo_k,Xhi_k,Ylo_k,Yhi_k. Define integer L_k=32(4Xlo_k+Ylo_k)-27m_k D3 and U_k=32(4Xhi_k+Yhi_k)-27m_k D3. For all real points of that rectangle, L_k/(160*27D3)<=r_k<=U_k/(160*27D3). Define d_k=L_k if L_k>0, -U_k if U_k<0, and 0 otherwise. Then b>=A/(1024*27D3) where A=sum w_k d_k, all integers.

The complete recursive covering verifier accepts a rectangle when one of three strictly certified cases holds: U_1<0 (r1<0), U_3<0 (r3<0), or 200000 A>1831*1024*27D3 (b>1831/200000). Otherwise it splits at an exact dyadic midpoint: x when x width>1 and (y width=1 or 4*x width>=y width), else y. This produces 97 closed rectangles with disjoint interiors: 43 certified r1<0, 31 certified r3<0, 23 certified b>1831/200000, maximum depth 41. The verifier independently reclassifies EVERY leaf, checks positive extents, bounds, and exact total area sum D^2=17,592,186,044,416. Recursive bisection and exhaustive child traversal prove that union is all [0,1]^2; shared boundary overlap is harmless. At a point with r1>=0 and r3>=0 only the third case is possible. All arithmetic and inequalities are exact unbounded integers, so this proves the statement on every real point, not merely at a finite grid. The full manifest is reproducible with the executable; local expanded certificate manifest SHA256=8e9d078696618d28e12934c4eb2921d86870a934aa548c0ae1ca2084587f74ac, and independent compact verifier manifest SHA256=fa446d39556388456d655c9ff6ef5f798fd49c76e70afe1098e23ea285a280ae. They serialize distinct label strings, but certify the same deterministic rectangles.

## Theorem B — six sharp strict sign chambers through the inherited cusp (conditional)

Stage330-B proved b<=61/10000 implies r2>0 over the full real square. Since 61/10000<1831/200000, Theorem A eliminates the two strict triples (r0,r1,r3)=(-,+,+) and (+,+,+) from that low-budget region. The remaining six triples ALL occur at an individual additional budget smaller than the inherited epsilon_dagger, as the following rational witnesses show:

| sign r0,r1,r3 | x | y | exact b |
| --- | --- | --- | --- |
| --- | 23/100 | 3/5 | 38523/8000000 |
| --+ | 23/100 | 31/50 | 5563/1000000 |
| -+- | 47/200 | 53/100 | 921/160000 |
| +-- | 9/40 | 3/5 | 63/12800 |
| +-+ | 9/40 | 5/8 | 5337/1024000 |
| ++- | 23/100 | 13/25 | 45987/8000000 |

At every point, exact Fraction evaluation checks the stated three strict signs, r2>0, and r0+3r1+3r2+r3=0. The checker also verifies b(x,y)-23860079/6400000000 < 2181407226/10^12. Stage330's inherited global minimum lower bound beta*>23860079/6400000000 and Stage329's inherited cusp bound epsilon_dagger>2181407226/10^12 imply b(x,y)-beta*<epsilon_dagger. Therefore each sign triple occurs at some feasible two-source cusp budget when paired with a global minimizer. This conditional statement makes NO claim that these six patterns are simultaneously optimal or that all zero-boundary strata / sixteen tagged comparisons have been classified.

## Proposition C — nearly sharp global budget separation

At x=248529/1000000 and y=603541/1000000, exact fractions give
r1=334726228977/5000000000000000000>0;
r3=122816228977/5000000000000000000>0;
b=146485940681228977/16000000000000000000 < 9155372/1000000000.
Compactness and Theorem A give the exact strict bracket

  1831/200000 < min{b(x,y): x,y in [0,1], r1>=0, r3>=0}
              < 9155372/1000000000.

Hence the joint-positive chamber exists globally but is separated by a proven public-cost barrier from the small-budget search. The bound is not claimed to equal the exact constrained minimum.

## Execution, dependency and next problem

Expanded local stdlib Fraction/integer verifier and separately executed compact independent stdlib verifier each ran twice with byte-identical respective stdout. Compact executable SHA256=59fa067fa44c60cebe284488387e9dec2351438a39c118045081e4d9415ab02e, compact executed stdout SHA256=94b0854f21b4ff65cfa6110f27371a83505fa74b00c77a19f2b331d21e064a2b. Terminal line STAGE331B_GLOBAL_JOINT_SIGN_EXCLUSION_AND_SIX_CHAMBERS_EXACT_PASS. The expanded local source/log are also retained separately and do not have the same bytes as the compact remotely published verifier.

Theorem A and Proposition C are standalone exact results within the auxiliary model; the cusp-shell interpretation in B depends explicitly on inherited Stage307/329/330 author claims, not on independent acceptance. Owner enumeration encountered CONTROL_QUOTA and no native execution authority was established. This is portable author evidence, NOT a formal CLAIM, Source Result, Driver review or Foundation promotion.

Stage332-B must classify the sixteen source-tagged Bernoulli comparisons and zero-boundary strata within these six retained public chambers for 1/5000<E<=epsilon_dagger, then construct an exact off-branch KKT/interval exclusion or an earlier strict rational competitor. The full global eight-parameter Pareto switching point remains open.
