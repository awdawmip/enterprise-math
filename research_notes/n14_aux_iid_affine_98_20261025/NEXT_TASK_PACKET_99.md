# Stage99 portable continuation — dual candidate, not theorem

**Mother question:** For iid P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) on three symbols and stopping time <=14, determine the minimal maximum expected sampling time among all randomized ordered-history tests with both decision errors bounded by alpha.

**Latest Stage98 author frontier:** At K98=17496/13, Gamma98=33984/13, every real 0<=delta<=eta98=4993625/12934289716936704 has V14(alpha97+delta)=V97-Gamma98*delta, with alpha98=2586269937332842327/7450150876955541504 and V98=757686022002985135/58204303726215168. At the endpoint A98=(13,6,4) always continues, and B=(12,0,1) decides Q with probability s98=12366057190345211/20889600000000000. Author-side proof and executable exact checker: PROOF.en.md and CHECKER.py in the same source directory. Independent Driver review remains pending.

**New dual candidate only:** Affine gap scan of all 680 count states and all action gaps for decreasing K, holding the K98 endpoint policy fixed, identifies the largest lower crossing K99=6696/5 at A99=(11,3,0), between continuing C and deciding P. At K99 the only Bellman ties are A99 and B; this does not prove any positive Stage99 primal interval.

**Next exact work:** Enumerate true ordered first-hit P/Q masses to A99 and continuation suffix error/time, preserving the order and branch identity. Determine whether its cone intersects B; if overlap exists, retain joint visits and conditional interaction instead of an invalid disjoint affine formula. Derive exact error compensation, feasible randomization interval, P/Q expected durations, Bellman support equality, and sharp endpoint or exact obstruction. Calculate the next lower dual crossing only after this proof.

**Source/authority:** External finite iid model, not native P000/BRC/X6. Native owner and CLAIM unverified (tasks CONTROL_QUOTA; session_start STATIC_READONLY_SCOPE_DENIED, operation_sent=false). This packet is author handoff evidence, not formally dispatched Task, reviewed Result or Foundation theorem.
