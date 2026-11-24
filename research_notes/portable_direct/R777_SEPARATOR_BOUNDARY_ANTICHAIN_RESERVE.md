# R777 — Exact cut-boundary residual antichains for robust reserve

2026-11-25. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R776 at a34f4e975e82572a8d0a529f2b069edcfc477469:research_notes/portable_direct/R776_JOINT_LIFT_ANTICHAIN_RESERVE.md. Frozen scientific input a72226e2430ffa4786321ac86e7f0c599d5f0389 retained: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint-relation contract blob 3923890d77a02d84b772f789e6912dd14f220d14 read at that pin. Frozen Heartbeat companion lookup returned 404; this is only the R774–R776 Boolean auxiliary observer, not native signed BRC or a native slice model. Current ACTIVE worldview, continuation/portable and applicable account research rules consulted. Own session recovery r3-20261125-0220-own-metadata-v1 confirmed original registration, no runs and execution_authorized=false; inventory r3-20261125-0220-owner-read-v1 initially QUEUED. No shared task claim, Result, or mathematical acceptance.

## 1. Problem and theorem

G finite loop-free subcubic multigraph, with private ports completing each vertex to three. V_v is even binary triples, V=product V_v, K=cycle space represented by equal edge bits at both ends and zero private bits. S(0)={0}, S(1)=V_v minus {0}, S(2)=V_v. A reserve vector t is feasible iff for every x in product S(p_v) there exists z in K with x_v+w_v+z_v in S(t_v) at every v. Minimize sum alpha_v t_v (nonnegative exact prices). Retain the fixed-reserve forall-prefix exists-lift quantifiers of R776.

Given any rooted binary decomposition of the vertex set into disjoint child sets (single vertices at leaves), let cut(X) be edges with one end in X. Edge IDs, including parallel edges, are distinguished. For every region X define B_X as binary assignments to cut(X) with even parity on the boundary of every connected component of G[X]. Components with no cut edges impose no restriction. If b_X=|cut(X)| and h_X is the number of components touching the cut, then |B_X|=2^(b_X-h_X). Necessity follows by summing local even parity over each component. Sufficiency follows by pairing the endpoints of the active boundary half-edges within that component and xoring any connecting paths, with repeated endpoints allowed. This constructs internal even lifts. At empty cut there is one assignment, the empty bit string.

For a fixed partial reserve t_X and actual prefix x_X define L_X(x_X,t_X) subset B_X: the assignments extendible to internal edge bits satisfying the local even condition and x_v+w_v+z_v in S(t_v) for all v in X. Private z ports are zero. Define A_X(t_X)=Min_{inclusion}{L_X(x_X,t_X): x_X in product S(p_v)}. Families are nonempty, and the family {empty set} is impossible. The representation retains all boundary assignment labels and is an exact observer for any future disjoint exterior, any prefix therein, and any fixed reserve therein. It intentionally does not encode multiplicities, signed amplitudes, paths, time order, source identities or common depth; retain original graph/local inputs and traceback for other observers.

## 2. Separator composition and proof

For children X,Y with X disjoint Y, cut(X) intersect cut(Y) consists exactly of the crossing edges I between the children. Parent boundary is their symmetric difference. For sets a subset B_X and b subset B_Y define J(a,b) as all parent assignments obtained by choosing one member of each with matching bits on I and restricting their union to the parent cut. This is a relational join followed by projection; each internal edge is eliminated only after its two endpoint bits agree.

For any fixed actual prefix and reserve the exact equality L_(X union Y)=J(L_X,L_Y) holds: restricting a parent witness gives both child witnesses; conversely witnesses agreeing on I combine to a parent witness since there are no further cross-child constraints. J is monotone separately under set inclusion, so Min{J(a,b):a in F,b in H} = Min{J(a,b):a in Min(F),b in Min(H)} for any nonempty finite families. Indeed every original element contains a minimal element, and every retained pair is itself an original pair. Prefixes range independently over X and Y, so all pair combinations occur. Thus

    A_(X union Y)=Min{J(a,b):a in A_X,b in A_Y}.

Empty set is absorbing; an impossible child prefix cannot be repaired by exterior bits. At the root the unique boundary assignment is the empty bit string, so feasibility iff the family is the singleton family containing the singleton set of that assignment. The universal quantifier over prefix combinations was preserved before existential projection; taking a union across prefixes would be incorrect.

## 3. Exact weighted optimization and complexity

For every leaf compute its at most three local reserve families and keep the cheapest reserve for each distinct feasible family. At each parent merge all pairs of child families by the formula above, dropping impossible ones, and keep the minimum sum of child costs for each equal family. By induction every partial reserve is covered, and equality of families is sufficient for all exterior joins, so the cheaper representative dominates. Recover a minimum root reserve by backtracking chosen child states; for any actual prefix, compute actual L bottom-up (without universal-family minimization) and choose matching boundary assignments top-down to recover a compensating lift. Hence the algorithm is exact.

Let W=max_X(b_X-h_X), Q=2^W, D=M(Q)-2, where M is the Dedekind number including the empty family and {empty}. Each node has at most D feasible nonempty antichains. The number of pairs per merge is <=D^2, with each family size <= binom(Q,floor(Q/2)). At most Q^2 assignment pairs per join; comparisons of labeled boundary bit vectors and antichain subset checks cost a function of the raw cut width and Q. Boundary labels can be mapped to local indices in polynomial preprocessing; a straightforward implementation on supplied decomposition takes O(n*(1+b_max)^O(1)*f(W)) exact price operations with f determined by these bounds. A supplied bounded-cut-width decomposition gives linear in n arithmetic operations with a width-dependent constant, regardless of total cycle rank. Explicit decomposition construction/optimization is separate; this is not a general polynomial-in-width claim. Retaining all tables/backpointers uses O(n D) state records plus state representations. For streaming prefix decompositions, two layers suffice for costs, with separate traceback if desired. No measured runtime speed claim. The experiment uses raw cut labels (including parity-infeasible labels in bit positions but never in actual sets).

For the L-column 2-by-L ladder graph, take order top,bottom in each column; all nonempty prefix induced subgraphs are connected, max prefix cut is at most 3; leaves have degree <=3. Thus W<=2, at most four legal boundary assignments, at most M(4)-2=166 feasible antichains at every node of this decomposition, whereas r=L-1 and the R776 global lift universe has 2^(L-1) states. This is an unbounded-rank family with constant boundary-state bound. It is a bound, not a claim all 166 occur.

## 4. Explicit failure of union-only compression

Two vertices joined by two parallel edges, private third port at each. Let w=0, p=(2,0), and on the first vertex t=1. The legal boundary assignments are 00 and 11 (denote 0 and 1). Prefix 0 forces boundary 1, prefix equal to the nonzero cycle projection forces 0, and the other two prefixes allow both. The minimum family is {{0},{1}}, whose union is {0,1}. With t=2 instead the family is {{0,1}}, same union. Exterior vertex t=0,p=0 forces boundary 0. The first reserve fails on the zero prefix; the second succeeds for every prefix. Therefore recording just the union loses exactly the quantifier-relevant joint residual. The example uses an actual graphic Port kernel.

## 5. Exact tests

The JS code below independently enumerates full edge-cycle lifts, quotient representatives and all reserve coverage sets on small graphs. The separator solver does not use the cycle lifts. For n<=4 all prefix inventories and quotient targets were compared for unit prices and the mixed nonnegative prices alpha_i=i mod 4; n=6 uses 128 deterministic sampled prefix-target pairs per price vector (not exhaustive). All arithmetic in coverage masks is BigInt, small indices use exact integers. Larger ladder tests check the R770 saturation value with unit prices and compare forward versus reverse ordering for 16 deterministic sampled weighted instances per length; the order comparisons are consistency checks, not independent direct enumeration. All assertions passed.

```json
{
  "rows": [
    {
      "name": "theta",
      "n": 2,
      "rank": 2,
      "maxcut": 3,
      "checks": 72,
      "peak": 3
    },
    {
      "name": "triangle",
      "n": 3,
      "rank": 1,
      "maxcut": 2,
      "checks": 1728,
      "peak": 4
    },
    {
      "name": "K4",
      "n": 4,
      "rank": 3,
      "maxcut": 4,
      "checks": 5184,
      "peak": 15
    },
    {
      "name": "ladder2",
      "n": 4,
      "rank": 1,
      "maxcut": 2,
      "checks": 20736,
      "peak": 4
    },
    {
      "name": "ladder3",
      "n": 6,
      "rank": 2,
      "maxcut": 3,
      "checks": 256,
      "peak": 9
    },
    {
      "name": "prism",
      "n": 6,
      "rank": 4,
      "maxcut": 4,
      "checks": 256,
      "peak": 36
    },
    {
      "name": "K33",
      "n": 6,
      "rank": 4,
      "maxcut": 9,
      "checks": 256,
      "peak": 58
    }
  ],
  "long": [
    {
      "L": 8,
      "n": 16,
      "rank": 7,
      "maxcut": 3,
      "sat": 25,
      "orderComparisons": 16,
      "peak": 9
    },
    {
      "L": 16,
      "n": 32,
      "rank": 15,
      "maxcut": 3,
      "sat": 49,
      "orderComparisons": 16,
      "peak": 9
    },
    {
      "L": 32,
      "n": 64,
      "rank": 31,
      "maxcut": 3,
      "sat": 97,
      "orderComparisons": 16,
      "peak": 9
    },
    {
      "L": 64,
      "n": 128,
      "rank": 63,
      "maxcut": 3,
      "sat": 193,
      "orderComparisons": 16,
      "peak": 9
    }
  ],
  "total": 28488
}
```

Reproduce in Node.js (no dependencies):
```javascript
function verify(){
 const S=[[0],[1,2,3],[0,1,2,3]], even=[0,3,5,6], bit=i=>1n<<BigInt(i);
 const minfam=xs=>{const a=[...new Set(xs)];return a.includes(0n)?[0n]:a.filter(x=>!a.some(y=>x!==y&&(x&y)===y)).sort((x,y)=>x<y?-1:x>y?1:0)};
 const tuples=(n,b)=>Array.from({length:b**n},(_,x)=>Array.from({length:n},()=>{let y=x%b;x=Math.floor(x/b);return y}));
 function graph(n,E){return {n,E,inc:Array.from({length:n},(_,v)=>E.flatMap((e,j)=>e.includes(v)?[j]:[]))}}
 function prep(G,order){
  const {inc}=G;let cut=[],maxcut=0;const steps=[];
  for(const v of order){
   const I=inc[v],union=[...new Set([...cut,...I])],next=union.filter(e=>!(cut.includes(e)&&I.includes(e)));
   const pick=(x,A)=>A.reduce((s,e,j)=>s|(((x>>union.indexOf(e))&1)<<j),0);
   const triples=Array.from({length:2**union.length},(_,x)=>[bit(pick(x,cut)),bit(pick(x,I)),bit(pick(x,next))]);
   const local=Array.from({length:3},(_,p)=>Array.from({length:4},(_,w)=>Array.from({length:3},(_,t)=>minfam(S[p].map(x=>{
    let mask=0n;for(let b=0;b<2**I.length;b++){let j=even.indexOf(b);if(j>=0&&S[t].includes(x^w^j))mask|=bit(b)}return mask;
   })))));
   steps.push({v,triples,local});cut=next;maxcut=Math.max(maxcut,cut.length,I.length);
  }return {steps,maxcut};
 }
 function solve(P,p,w,alpha){
  let dp=new Map([["1",{a:[1n],c:0}]]),peak=1;
  for(const {v,triples,local} of P.steps){
   const next=new Map(),cache=new Map();
   function join(a,b){const key=a+","+b;if(cache.has(key))return cache.get(key);let m=0n;for(const [x,y,z] of triples)if((a&x)&&(b&y))m|=z;cache.set(key,m);return m}
   for(const {a,c} of dp.values())for(let t=0;t<3;t++){
    const f=local[p[v]][w[v]][t];if(f[0]===0n)continue;
    const h=minfam(a.flatMap(x=>f.map(y=>join(x,y))));if(h[0]===0n)continue;
    const k=h.join(","),nc=c+alpha[v]*t;if(!next.has(k)||next.get(k).c>nc)next.set(k,{a:h,c:nc});
   }
   dp=next;peak=Math.max(peak,dp.size);
  }
  return [dp.get("1").c,peak];
 }
 function direct(G){
  const {n,E,inc}=G,N=4**n,lifts=[];
  for(let z=0;z<2**E.length;z++){let a=0;for(let v=0;v<n;v++){let b=inc[v].reduce((s,e,i)=>s|(((z>>e)&1)<<i),0);let j=even.indexOf(b);if(j<0){a=-1;break}a|=j<<(2*v)}if(a>=0)lifts.push(a)}
  const q=Array.from({length:N},(_,x)=>Math.min(...lifts.map(z=>x^z)));
  const reps=[...new Set(q)],ps=tuples(n,3),xs=ps.map(p=>p.reduce((a,t,i)=>a.flatMap(x=>S[t].map(y=>x|(y<<(2*i)))),[0]));
  const cov=xs.map(a=>a.reduce((m,x)=>m|bit(q[x]),0n));
  function costs(alpha){return ps.map((p,i)=>[p.reduce((s,t,j)=>s+t*alpha[j],0),cov[i]]).sort((a,b)=>a[0]-b[0])}
  return {reps,ps,rank:Math.log2(lifts.length),costs,opt:(i,w,c)=>{const need=xs[i].reduce((m,x)=>m|bit(q[x^w]),0n);return c.find(([_,mask])=>(need&mask)===need)[0]}};
 }
 const ladder=L=>graph(2*L,[...Array.from({length:L},(_,i)=>[2*i,2*i+1]),...Array.from({length:L-1},(_,i)=>[2*i,2*i+2]),...Array.from({length:L-1},(_,i)=>[2*i+1,2*i+3])]);
 const cases=[["theta",graph(2,[[0,1],[0,1],[0,1]])],["triangle",graph(3,[[0,1],[1,2],[2,0]])],["K4",graph(4,[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]])],["ladder2",ladder(2)],["ladder3",ladder(3)],["prism",graph(6,[[0,1],[1,2],[2,0],[3,4],[4,5],[5,3],[0,3],[1,4],[2,5]])],["K33",graph(6,[0,1,2].flatMap(i=>[3,4,5].map(j=>[i,j])))]];
 let seed=777;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n};
 const rows=[];
 for(const [name,G] of cases){const n=G.n,P=prep(G,Array.from({length:n},(_,i)=>i)),D=direct(G);let checks=0,peak=0;
  for(const alpha of [Array(n).fill(1),Array.from({length:n},(_,i)=>i%4)]){
   const C=D.costs(alpha),samples=n<=4?D.ps.flatMap((p,i)=>D.reps.map(w=>[i,w])):Array.from({length:128},()=>[rnd(D.ps.length),D.reps[rnd(D.reps.length)]]);
   for(const [i,w] of samples){const [a,b]=solve(P,D.ps[i],Array.from({length:n},(_,j)=>(w>>(2*j))&3),alpha),v=D.opt(i,w,C);if(a!==v)throw Error(JSON.stringify({name,i,w,a,v}));checks++;peak=Math.max(peak,b)}
  }rows.push({name,n,rank:D.rank,maxcut:P.maxcut,checks,peak});
 }
 const long=[];
 for(const L of [8,16,32,64]){const G=ladder(L),n=G.n,order=Array.from({length:n},(_,i)=>i),P=prep(G,order),Q=prep(G,[...order].reverse());let peak=0;
  const [sat,b]=solve(P,Array(n).fill(2),Array(n).fill(0),Array(n).fill(1));if(sat!==2*n-(L-1))throw Error("saturation");
  for(let i=0;i<16;i++){let p=Array.from({length:n},()=>rnd(3)),w=Array.from({length:n},()=>rnd(4)),alpha=Array.from({length:n},(_,j)=>j%4);const [a,b]=solve(P,p,w,alpha),[c,d]=solve(Q,p,w,alpha);if(a!==c)throw Error("order");peak=Math.max(peak,b,d)}
  long.push({L,n,rank:L-1,maxcut:P.maxcut,sat,orderComparisons:16,peak:Math.max(peak,b)});
 }
 return {rows,long,total:rows.reduce((s,r)=>s+r.checks,0)};
}
console.log(JSON.stringify(verify(),null,2));
```

## 6. Next

Derive tighter boundary antichain bounds for small cuts and test dominance between distinct families (not merely equality); study how to choose inexpensive decompositions on highly coupled subcubic graphs. Keep original signed BRC, provenance, order and common depth separate. No mathematical admission or formal task closure claimed.
