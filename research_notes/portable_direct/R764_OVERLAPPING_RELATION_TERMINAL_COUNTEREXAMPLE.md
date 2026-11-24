# R764 — Overlapping relations defeat zero-terminal optimality

2026-11-24. AUTHOR_ANALYTIC_COUNTEREXAMPLE / EXACT_JS_CHECKED / NOT_REVIEWED.
Predecessor R763: f6bb9778425aa33b50c00088bd79405586b82021:research_notes/portable_direct/R763_SINGLE_RELATION_EXACT_RESERVE.md (blob 3b039ddd26bf5f862b5a5ec1175319c7c2cc0d3c). Independent portable continuation of its explicitly open dimension-two kernel question. Frozen P000 and joint relation at a72226e2430ffa4786321ac86e7f0c599d5f0389 retained; read actual P000, joint companion and weighted substrate at that ref. The newer foundation package and heartbeat/residual companion paths were absent at this historical ref; no repinning. ACTIVE worldview and current research/portable protocols read. Own original registration recovery confirms no run, execution_authorized=false. No shared task adopted.

## Counterexample and sharp costs

Use R763's unsigned finite Boolean observer. Let H_i=F_2^2, i=0,1,2,3, write elements 0,1,2,3 in binary, and set S(0)={0}, S(1)={1,2,3}, S(2)=H_i. Define the two-dimensional relation kernel K={(a,u,u,u): u=a+2b, a,b in F_2}, inside the direct sum. Let A be the quotient by K. Every H_i injects: each nonzero relation has at least three nonzero coordinates. Define P(p)=A(product S(p_i)) and k_p(v)=min sum(t_i) subject to v+P(p) subset P(t). Stocks clip at two as in R763. Take p=(0,1,2,2), w=(2,0,0,0), v=A(w). Then
k_p(0)=5, k_p(v)=4.
Thus zero terminal is NOT always optimal even for two overlapping relations; cube-specific zero optimality and R763's one-relation/disjoint-support theorem are unaffected.

Proof of the upper bounds: p itself covers zero at cost 5. For v choose t=(1,1,1,1). For any prefix x, the four candidate lifts of A(x)+v are x+w+(a,u,u,u). At coordinate 0, 2+a is never zero; at each of the three remaining coordinates a singleton suffix excludes at most one u. Hence at most three of the four u are excluded, so at least one works. This gives cost 4.

Lower bound for zero: suppose sum t<=4. If t_0=0 or 1, coordinate 0 restricts u to {0,2} or {1,3}, respectively. Every other coordinate has prefix size at least three, so no t_j=0 can work with only two possible lifts. There must therefore be at least two singleton suffixes among coordinates 1,2,3. If both have doubled prefix, independently choose their prefix entries to exclude the two distinct available u. If one is coordinate 1, its nonzero-prefix set can exclude the nonzero member of the available pair, and the other (doubled-prefix) coordinate excludes the remaining member. Either gives a prefix with no feasible lift. If t_0=2, the remaining budget <=2 forces a zero suffix at some j>=1. Fix an admissible x_j; that zero suffix uniquely determines u=x_j. All other prefix coordinates now vary independently, so each of the other two suffixes must have cost at least its prefix cost by cardinality. Their total is at least 3, contradicting the remaining budget. Thus k_p(0)>=5.

Lower bound for v: coordinate 0 needs t_0>=1 since 2+a never vanishes. If total cost<=3, the other three coordinates have budget<=2, forcing some zero suffix. Its prefix entry uniquely determines u, and the other two coordinates again require total cost>=3. Contradiction. Hence k_p(v)=4.

The mechanism is a previously unseen rank-one local relation image: the translated empty prefix coordinate sits outside that image and can use one event without forbidding any of the four lifts. At zero the same coordinate either restricts the lifts to two or costs two events. The three overlapping rank-two coordinates exploit all four lifts jointly. This is a terminal-dependent interaction, not an additive saving from independent cycles.

## Exact finite observer decision by forbidden masks

For arbitrary finite kernel K, prefix p, suffix t and terminal lift w, define F_i(x_i)={z in K: x_i+w_i+z_i not in S(t_i)}. Starting Q_0={empty set}, iterate Q_{i+1}={U union F_i(x): U in Q_i, x in S(p_i)}. Containment holds exactly when K is absent from Q_n. Indeed the union records precisely the lifts rejected by one full prefix tuple, and independent local choices realize every union. Inclusion-maximal masks suffice, since union is monotone and any full-mask completion of a smaller mask also completes a larger mask. In dimension two there are just 16 possible masks on four lifts; checking a fixed p,t,w requires O(16*4*n) constant-width mask unions once the local projections are supplied. This is a decision rule, not a claim that searching optimal t is linear. For general dimension r there are at most 2^(2^r) masks. It preserves the declared terminal compensation predicate, not counts, order, signs, common depth or arbitrary future BRC observations.

## Exact verification executed JavaScript

Independent quotient bitsets and direct suffix search verified all prefix/terminal combinations for the counterexample type: {"checks":5184,"bad":128,"example":{"p":[0,1,2,2],"b":2,"k0":5,"k":4,"t":[1,1,1,1]},"profile":{"4":32,"5":32},"K":[0,85,168,253]}. Forbidden-mask recurrence compared against direct quotient containment for 419904 triples (p,t,b), with no mismatch. The smaller dimension-two cases were normalized by independent local changes of basis: a local map has rank 0, rank 1 with one of the three possible kernels, or rank 2 equivalent to identity. Coordinate permutations permit nondecreasing type lists; injectivity and no single-coordinate nonzero kernel vectors impose the exact admissibility filters. All admissible types with n=2,3 were checked: [{"n":2,"cases":1,"checks":36},{"n":3,"cases":9,"checks":3888}]. There is no smaller number of supports for this counterexample within the dimension-two binary rank-two local model (n=1 is impossible by injectivity). This finite minimality concerns support count only.

Reproduction (Node/JS, exact BigInt bitsets):
```javascript
const maps=[[0,0,0,0],[0,1,0,1],[0,0,1,1],[0,1,1,0],[0,1,2,3]],S=[[0],[1,2,3],[0,1,2,3]];
function stocks(n){return n?stocks(n-1).flatMap(x=>[0,1,2].map(t=>[...x,t])):[[]]}
function data(types){let n=types.length,D=4**n,K=maps[0].map((_,u)=>types.reduce((s,t,i)=>s+(maps[t][u]<<(2*i)),0));if(new Set(K).size!==4||K.slice(1).some(k=>types.filter((_,i)=>((k>>(2*i))&3)!==0).length<2))return null;let canon=x=>Math.min(...K.map(k=>x^k)),B=Array.from({length:D},(_,x)=>x).filter(x=>canon(x)===x),ss=stocks(n).sort((a,b)=>a.reduce((s,v)=>s+v,0)-b.reduce((s,v)=>s+v,0)),R=ss.map(t=>{let a=[0];for(let i=0;i<n;i++)a=a.flatMap(x=>S[t[i]].map(y=>x^(y<<(2*i))));return a.reduce((m,x)=>m|(1n<<BigInt(canon(x))),0n)});return {K,B,ss,R,canon}}
const cost=t=>t.reduce((s,v)=>s+v,0);
function scan(types,all=false){let d=data(types);if(!d)return null;let {K,B,ss,R,canon}=d,checks=0,bad=0,example=null,profile={};for(let i=0;i<ss.length;i++){let p=ss[i],xs=B.filter(x=>(R[i]>>BigInt(x))&1n),k0=null;for(let b of B){let target=xs.reduce((m,x)=>m|(1n<<BigInt(canon(x^b))),0n),j=R.findIndex(a=>(a&target)===target),k=cost(ss[j]);if(b===0)k0=k;if(k<k0){bad++;example??={p,b,k0,k,t:ss[j]}}checks++;if(all&&p.join()==="0,1,2,2")profile[k]=(profile[k]??0)+1;}}return {checks,bad,example,profile,K}}
function cover(types,p,t,w){let reachable=new Set([0]);for(let i=0;i<types.length;i++){let v=(w>>(2*i))&3,fs=S[p[i]].map(x=>maps[types[i]].reduce((m,a,u)=>m|(!S[t[i]].includes(x^v^a)?1<<u:0),0));reachable=new Set([...reachable].flatMap(a=>fs.map(b=>a|b)));}return !reachable.has(15)}
function* types(n,lo=0){if(!n){yield [];return}for(let t=lo;t<5;t++)for(let a of types(n-1,t))yield [t,...a]}
let d=data([1,4,4,4]), dp=0;
for(let i=0;i<d.ss.length;i++){let xs=d.B.filter(x=>(d.R[i]>>BigInt(x))&1n);for(let b of d.B){let a=xs.reduce((m,x)=>m|(1n<<BigInt(d.canon(x^b))),0n);for(let j=0;j<d.ss.length;j++){if(cover([1,4,4,4],d.ss[i],d.ss[j],b)!==((a&d.R[j])===a))throw Error("DP mismatch");dp++}}}
let small=[];for(let n=2;n<=3;n++){let cases=0,checks=0;for(let ts of types(n)){let q=scan(ts);if(q){if(q.bad)throw Error("small counter");cases++;checks+=q.checks}}small.push({n,cases,checks})}
console.log(JSON.stringify({small,ex:scan([1,4,4,4],true),dp}));
```

## Next

Identify structural hypotheses restoring zero optimality, particularly incidence graphs whose degree-three local maps come from actual cycle spaces. The counterexample has three rank-two projections, one rank-one projection, and is an abstract quotient; whether an incidence graph realizes the same effect is open here. Test a theta graph and compare independent cycles against overlapping cycles using the mask recurrence. Preserve the source model's signed, ordered and slice-depth distinctions; no native BRC execution or general native compression claim. No formal task result/review.
