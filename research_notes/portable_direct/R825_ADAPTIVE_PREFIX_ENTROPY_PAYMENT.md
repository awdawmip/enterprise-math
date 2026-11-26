# R825 — Adaptive prefix entropy payment for heterogeneous Port residuals

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_PREFIX_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH, existing own session metadata recovered by r3-20261127-r825-own-read (no run, execution_authorized=false), EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91. Running inventory original request r3-20261127-r825-running-read pending during derivation; no claim/owner changes. Frozen science input a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read directly. Current global entries verified at main@0d87428739dab1d15178fd3cd76223ac5aafeb9c, ACTIVE worldview read. Current portable, method, BRC-only and residual policies read. Sources: R824 at 959953e7df4c8240f3e6f471245bf5913ce838d6:research_notes/portable_direct/R824_EDGE_COVER_MOMENT_DOMINATION_AND_LEAF_FREE_FPTAS.md; R822 at b94082079b66ce4832bc43007a1c20565a34607f:research_notes/portable_direct/R822_DIRECT_PORT_HYPEREDGE_ENTROPY_PAYMENT.md; R820 at d84938639538e5d9db1a0c3aec0846a3c3c24b9d:research_notes/portable_direct/R820_STEINER_OVERLAP_HOST_SUPPORT_FPTAS.md. Reuse their scoped R812/R813 exact independent group representation and pinned observer hypotheses. This is auxiliary nonnegative fixed-charge combinatorial theory, not a native Heartbeat computation or native residual attribution. Retain signed BRC, complete road matrices, branch source, time order and common depth.

## 1. Adaptive prefix entropy theorem

In R824 write Z=Z_base P(1), P(t)=E prod_f(1-delta_f t^c_f I_f) for independent groups B, labeled hyperedges F_f of s_f distinct groups, exact nonnegative joint moments m(A) bounded by prod_{f in A} lambda_f. Let a_f=2^s_f delta_f lambda_f. Remove a_f=0 only for this observer (delta=0 or I_f=0 almost surely); preserve original state. Assume polynomial-time, polynomial-bit joint pinned group oracles and explicit incidence. For each f choose a nonnegative integer L_f so every group satisfies the Kraft inequality
  sum_{f incident B} 2^(-L_f) <= 1.
Assign c_f=s_f+L_f. If additionally
  beta_B=sum_{f incident B} a_f 2^L_f <=1/8,
then a deterministic FPTAS exists for this fixed-charge partition, without a bound on group degree or hyperedge arity.

Proof: Kraft inequality permits a deterministic canonical binary prefix code on each group's incident labels, all using the prescribed lengths L_f. A sole label may have length zero. Encode each connected labeled support by the R822 FIFO queue: at a processed group, for each newly discovered selected label in fixed order emit 1 then its local prefix codeword, mark the label and add all unseen incident groups to queue in fixed order; then emit 0. If root is given, every label is emitted once. Prefix decoding is unique (including empty code for a singleton because 1 was consumed). The queue processes at most 1+sum_f(s_f-1) groups. Total bits <=1+sum_f(s_f+L_f)=1+c(C). Enumerate all roots and binary words of length <=k+1, decode and reject malformed/repeated labels, check cost and deduplicate. There are g 2^{O(k)} words. For enormous supplied lengths one need only consider factors with c_f<=k; canonical codes can be represented as a trie or constructed with lengths capped by polynomial input size when the witness is constructed below. In particular the theorem assumes polynomial-bit constructible codes (the rational witness below provides this), or restrict to eligible factors and construct a fresh valid code for their unchanged lengths. Either way each retained length <=k, avoiding huge materialization. The full generating polynomial still retains all factors.

With q_f=2^{c_f}delta_f lambda_f=a_f 2^{L_f}, R824/R820's polymer proof applies unchanged: |w(C)|<=prod_f(delta_f lambda_f R^{c_f}) by the joint moment envelope; prod_{h adjacent f}(1-q_h)^2 >= (7/8)^{2s_f} >=(7/8)^{2c_f}. Since 3/2<49/32, at R=3/2 its deletion-ratio hypothesis holds. Hence log P analytic on the disk, |log P|<=g/7, and E_k <=(2g/7)(2/3)^k. Exact formal logarithmic coefficients are obtained by R822's subset Mobius differences on connected supports with c(C)<=k. Exact joint moments, not lambda_f products, are used in every coefficient. Local pinning, rational bit complexity and final certified scalar exponential follow R822 section 4 (auxiliary algorithm, not executed native arithmetic). Choose k=O(log((g+1)/epsilon)); complexity g 2^{O(k)} poly(N,k), hence FPTAS. Zero baseline mass is handled as exact zero.

## 2. Square-root load and near-tight continuous budget

Define W_B=sum_{f incident B} sqrt(a_f), W_f=max_{B incident f} W_B. For any feasible lengths, Cauchy-Schwarz gives
  W_B^2 <= (sum 2^-L_f)(sum a_f 2^L_f) <= beta_B.
Thus W_B<=1/sqrt(8) is NECESSARY for this certificate, not for approximation itself. Conversely take L_f=ceil(log2(W_f/sqrt(a_f))) (nonnegative). Then 2^-L_f <=sqrt(a_f)/W_f, and 2^L_f <2 W_f/sqrt(a_f) unless equality is exact, where the same weak bound applies. Therefore Kraft holds, and
  beta_B <=2 sum_{f incident B} W_f sqrt(a_f).
In particular max_B W_B<=1/4 suffices. This is within factor sqrt(2) of the universal necessary threshold in the square-root-load norm. For one group, continuous real lengths attain beta_B=W_B^2 (use 2^-L_f=sqrt(a_f)/W_B), before integer rounding. This does not claim global optimality across overlapping groups.

Exact rational implementable variant: choose positive rational t_f, let U_B=sum t_f, U_f=max U_B over incident groups, and take the least nonnegative L_f with 2^L_f t_f>=U_f. Then Kraft holds and beta_B <=2 sum_{f incident B} a_f U_f/t_f. All comparisons, doubling and the final exact beta check use rationals of polynomial bit size. E.g. t_f chosen as a dyadic upper approximation of sqrt(a_f) within a fixed relative factor by integer comparisons. Alternatively when a rational M>=max W_B is certified, select the least L_f>=0 with 2^(2L_f) a_f>=M^2, yielding beta_B<=2 M W_B. A rational upper certificate for W_B can be obtained by interval bounds, without evaluating irrational code lengths. No log/sqrt numerical approximation is needed for a supplied valid M.

## 3. Explicit leaf-free, degree-four separating family with mixed strong and weak interfaces

Use R824's retained ladders, g=b+1 odd >=5, b even, one nonretained connector for each pair of ladders, using each ladder vertex once. One distinguished corner per ladder connects to its cyclic successor, and no connector joins two distinguished corners. Thus each connector touches at most one distinguished corner; original degrees are 3 or 4, no leaves or subdivisions, treewidth unbounded (K_g minor). Each local ladder has width two. On the two retained edges at the distinguished corner take S=(1,1,1,1), so theta=1/2. On every other retained ladder edge take diagonal S00=1,S11=b^8, offdiagonals zero; theta=1/b^4 is valid by R824. Every nondistinguished vertex has at least one such edge (simple ladder min degree 2 and at most one edge to distinguished vertex). On each connector take diagonal S00=S11=1 and envelope theta=1. All admissible eta and feasible charges remain permitted. Since s_f=2, d_f>=3, a_f<=1/128 at distinguished corner (p_ladder<=1/4), and a_f<=1/(32 b^4) elsewhere. Select L_f=1 at distinguished corners, and L_f=ceil(log2(2b)) otherwise. Ladder Kraft <=1/2+(b-1)/(2b)<1; connector Kraft <=1/2+1/(2b)<1. At a ladder,
 beta_B<=1/64+(b-1)/(8b^3)<1/8.
At a connector with one distinguished endpoint, beta_B<=1/64+1/(8b^3); with none, beta_B<=1/(4b^3). Both pass for b>=4.

For the saturated residual example delta_f=2^(-2d_f-1), R824's uniform index cost for the distinguished corner is 2+ceil(log2 b). For ANY admissible R824 envelope on the two uniform retained edges, theta>=1/2 at the distinguished corner; the diagonal connector also forces theta>=1/2. Thus lambda_f>=1/8 and a_f>=1/256 (d=3). The old uniform beta_B >=b/256>1/8 for b>32, even with optimized asymmetric road envelopes. The new certificate passes with no structural change. This compares sufficient certificates, not computational hardness. This is an admissible auxiliary rational-weight family; native road-generator realization remains open.

## 4. Parity support pruning before code allocation

For R824 local charge t_B, if a shared vertex v has odd charge at that block, every feasible parity support F contains at least one incident retained edge; such an edge forces both ports to be 1. Hence z_Bv=0 surely, and every factor containing it has I_f=0 surely. More generally the event all selected interfaces A are empty requires a parity support contained in J with all edges incident to A removed. For an undirected retained graph the necessary and sufficient parity-support feasibility criterion is that every component of that reduced graph has even total charge: necessity by summing mod 2, sufficiency by solving on a spanning forest. With S_e(11)>0 this is a certificate of impossibility whenever the criterion fails; it need not certify positive emptiness when other weights are zero. It gives a polynomial-time exact zero-moment screen on queried subsets, independent of the envelope. Singletons with impossible emptiness can be removed from the code alphabet before assigning lengths, while full charge and road provenance remain. For feasible subsets the old edge-cover envelope still applies. This is not a uniform product improvement for arbitrary parity charges.

## 5. Exact auxiliary verification

Executed deterministic JS below. On four labeled hypergraph shapes and 8 weight patterns each, construct rational witness t_f and canonical codes, check Kraft, exact local load with a_f=t_f^2/(16M^2), and exhaustively check every connected support encode/decode and length bound. Additional exact integer checks of mixed-family Kraft and a conservative load inequality for even b=4..2048. Results: {"instances":32,"kraft":200,"loads":200,"connected":33536,"roundTrips":33536,"family":1023}. All executed assertions passed. The family check uses the inequality 2 b^4+4(b-1)P<=16 b^4 with P=2^ceil(log2(2b)), a conservative sufficient bound for the ladder beta above. No native BRC operation, no physical comparison and no production FPTAS timing. General result rests on the analytic proof and previously stated exact-oracle hypotheses.

```javascript
function verify(){
const shapes=[[[0,1],[1,2],[2,0]],[[0,1],[0,1],[0,2,3],[1,3],[2,3]],Array.from({length:12},(_,i)=>[0,i+1]),[[0,1,2],[0,2,3],[0,3,4],[1,4],[2,4],[1,2,3,4]]];
let counts={instances:0,kraft:0,loads:0,connected:0,roundTrips:0,family:0};
for(const F of shapes)for(let trial=0;trial<8;trial++){
 const n=1+Math.max(...F.flat()),m=F.length,adj=Array.from({length:n},()=>[]);F.forEach((s,i)=>s.forEach(v=>adj[v].push(i)));
 const t=F.map((_,i)=>BigInt(1+((i*17+trial*13)%31)**2)),W=adj.map(A=>A.reduce((z,i)=>z+t[i],0n)),M=W.reduce((a,b)=>a>b?a:b,0n);
 const ell=F.map((s,i)=>{let L=0;const v=s.reduce((a,j)=>a>W[j]?a:W[j],0n);while((t[i]<<BigInt(L))<v)L++;return L});
 const codes=adj.map(A=>{let next=0n,old=0,dict={};for(const i of [...A].sort((a,b)=>ell[a]-ell[b]||a-b)){let L=ell[i];next<<=BigInt(L-old);if(next>=1n<<BigInt(L))throw Error("Kraft");dict[i]=L?next.toString(2).padStart(L,"0"):"";next++;old=L}return dict});
 for(let v=0;v<n;v++){const L=Math.max(0,...adj[v].map(i=>ell[i]));if(adj[v].reduce((z,i)=>z+(1n<<BigInt(L-ell[i])),0n)>1n<<BigInt(L))throw Error("kraft");counts.kraft++;
 // a_i=t_i^2/(16 M^2); q_i=a_i 2^ell_i
 if(adj[v].reduce((z,i)=>z+(t[i]**2n<<BigInt(ell[i])),0n)>2n*M*M)throw Error("load");counts.loads++}
 for(let mask=1;mask<2**m;mask++){const chosen=F.map((_,i)=>i).filter(i=>mask&(1<<i)),root=F[chosen[0]][0];let q=[root],vs=new Set(q),fs=new Set(),bits="";
 for(let j=0;j<q.length;j++){let v=q[j];for(const i of adj[v])if(mask&(1<<i)&&!fs.has(i)){fs.add(i);bits+="1"+codes[v][i];for(const u of F[i])if(!vs.has(u)){vs.add(u);q.push(u)}}bits+="0"}
 if(fs.size!==chosen.length)continue;counts.connected++;
 if(bits.length>1+chosen.reduce((z,i)=>z+F[i].length+ell[i],0))throw Error("length");
 q=[root];vs=new Set(q);fs=new Set();let p=0;for(let j=0;j<q.length;j++){let v=q[j];while(bits[p++]==="1"){const i=adj[v].find(i=>bits.startsWith(codes[v][i],p));if(i===undefined||fs.has(i))throw Error("decode");p+=ell[i];fs.add(i);for(const u of F[i])if(!vs.has(u)){vs.add(u);q.push(u)}}}
 if(p!==bits.length||fs.size!==chosen.length||chosen.some(i=>!fs.has(i)))throw Error("roundtrip");counts.roundTrips++;
 }counts.instances++;
}
for(let b=4n;b<=2048n;b+=2n){let P=1n;while(P<2n*b)P*=2n;if(b-1n>P/2n)throw Error("family Kraft");if(2n*b**4n+4n*(b-1n)*P>16n*b**4n)throw Error("family load");counts.family++}
return counts;
}
console.log(verify());
```

Next: optimize overlapping-group Kraft/weighted load jointly with asymmetric edge-cover envelopes; investigate whether parity cut screens can be upgraded to quantitative joint moment domination for weakly biased roads. General Port FPTAS and native realization remain open.
