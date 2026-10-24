# N14 auxiliary iid stage87 exact continuation — candidate only

**Mother question:** horizon 14, ordered outcomes 0/1/2, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Minimize max(E_P T,E_Q T) with both errors <=alpha, permitting full ordered-history randomized stopping tests.

**Verified author-level predecessor:** stage86 proof, scripts and certificate in this directory. Exact endpoint alpha86=5172378783158315543/14900301753911083008, V86=24313786683642713729/1862537719238885376, balancing s86=9865487497784809/13926400000000000. Fix A86=(12,3,0) to immediate P, B=(12,0,1) remains a randomized balance state; retain earlier frozen actions.

**New candidate, not proved:** K87=26244/13 at A87=(13,7,3), continue versus immediate P. First compute all 680 exact Bellman gaps at that dual parameter and identify possible additional ties. Then enumerate true ordered first-hit prefixes and their *P and Q probability masses* separately from word counts; enumerate suffix decisions, examine overlap with B and other randomized cones, solve errors and time, and either prove an all-real optimal interval with sharp endpoint or give the exact obstruction. Record provenance, program/source identity and any native-transfer limitations.

**Authority:** stage86 is author-side auxiliary finite-model work only. Native session_start was denied by static read-only authorization and task inventory hit CONTROL_QUOTA; no live Owner, CLAIM, native Result, or independent Driver review has been certified. Publication of this successor question grants none.
