# Stage174: open exact primal after Stage173 saturation

Mother problem: external IID N14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Optimize V14(alpha) among all full ordered-history randomized stopping/deciding strategies with eP,eQ<=alpha.

Source: Stage173 author-exact result in this directory, frozen GLOBAL_KNOWLEDGE_V1 main@32303b81b21f488a745aa9af6a05aaef150cf33d, EM main@b03d306acf9763f8db33e09d9fd434f35e4640fd. No native CLAIM/independent admission. P000 unchanged.

Frozen Stage173 endpoint: alpha173=611493515114730101/1752976676930715648; V173=1267557322258081771/109561042308169728. Prior tied R=(10,0,1) is now saturated at stop-Q probability 1; Z=(14,0,0) retains terminal Q probability z*=406062589150005409/409600000000000000.

Along ray dK=dL=-1 from K173=L173=451080/1909, exact first positive gap closure occurs at epsilon=955052028/133666271. Candidate K174=L174=16044588/70019, H174=2630296570966281555483145/15342709242751472369664. At this new dual point, ties are T=(8,2,0) P/continue and Z=(14,0,0) P/Q; R has become uniquely Q. Other 1238 action gaps strictly positive; minimum 39435024594685/1926840855822336. Stage174 is DUAL ONLY.

Next independent unit: compute all four exact deterministic corner observers for stopping P at T versus continuing, and deciding Q at Z versus P, by (i) rational suffix DP and (ii) unmerged integer-numerator ordered DFS. Check disjoint first-hit cones (T has two occurrences of symbol 0; Z has none), derive exact balanced z(t), legal coin range (do not assume [0,1]), Stage173 endpoint match, P-time dominance, common-error monotonicity, dual tightness, and strict right support. If infeasible, produce a rational obstruction rather than claiming a theorem. Preserve separate P/Q masses and full provenance; no native-world transfer without its typed embedding proof.
