# N14 external iid Stage105 portable handoff

**Question:** For \`P=(1/8,1/24,5/6)\`, \`Q=(1/12,1/12,5/6)\`, full ordered-history randomized tests with \`tau<=14\`, extend the exact minimax value \`V14(alpha)\` from the Stage104 right endpoint. This is an external auxiliary model and does not assert a P000/X6 bridge.

**Frozen Stage104 author frontier:** \`PROOF_STAGE104.md\` and \`certificate104.json\`; two author-level exact-rational implementations executed in this research run. Exact proven interval \`V(alpha103+delta)=V103-(9535248/4373)*delta\` for all real \`0<=delta<=48103/275931513961316352\`. Endpoint:
\`\`\`
alpha104=646648471503178867/1862537719238885376
V104=6009287153480025269/465634429809721344
K104=4881384/4373
\`\`\`
At this endpoint choose P at A104=(11,8,3) and choose Q at B=(12,0,1) with probability \`4103853056103079/5222400000000000\`.

**New dual-only candidate:** Decreasing K on \`lambdaP=72+(8/9)K\`, the first additional fixed-policy zero is \`K105=2212824096/1992661\` at \`A105=(8,5,1)\`, new P/continue tie. **No Stage105 primal theorem has been proven.**

**First executable scientific unit:** Compute all exact Bellman action gaps at K105 and across [K105,K104], genuine ordered first-hit prefix masses and continuation suffix tuples for A105 and B. Check whether new A105 cones overlap the post-Stage104 A104/B causal cones (the old A104 is strict P at lower K); preserve any real interaction instead of using an unjustified linear approximation. Solve exact error balance and probability feasibility; establish positive interval, tP>=tQ and right-support sharpness, or give a rigorous obstruction. Independently verify by ordered DFS and store exact rational certificate.

**Evidence and authority:** Keep immutable prior author frontier, P000 locked, full branch provenance and exact rational arithmetic. Require Source readback for any new author note; a GitHub author note does not constitute native CLAIM/Result or independent Driver acceptance.