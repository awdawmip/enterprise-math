# R766 — Unbounded theta reserve theorem by exact path-profile reduction

2026-11-24. AUTHOR_PROOF_WITH_EXHAUSTIVE_FINITE_CERTIFICATE / EXACT_JS_CHECKED / NOT_REVIEWED.
Independent portable continuation of R765 at b9a7b587c57fd0f8c7825929e38913377610ad00:research_notes/portable_direct/R765_MIN_PLUS_FORBIDDEN_FAMILY_OPTIMIZER.md, blob 71625d7d2dbce94626d8253cb668e9b495401162. Preserve its frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389. P000 V5, joint-relation and weighted BRC substrate blobs re-read by their exact prior SHA (dc84bdae6595b5e237a2ad50d8b21916adb2e447, 3923890d77a02d84b772f789e6912dd14f220d14, f375a059fa4af8c6eefaddb4d4a8689a0c063674); membership of those blobs at the frozen pin inherits the predecessor record, not independently reverified this turn. Historical generated foundation package previously unavailable, no repin. ACTIVE worldview and current portable/continuation contracts read. Activity RA-708BCC309CE076D8BB599B91 identifies the continuing author EM-DIRECT-82A007. Current owner inventory request r3-20261124-1520-r766-owner-read-v1 observed RUNNING; no new shared task, no protected control write or execution authorization asserted.

## Theorem

For every finite theta graph (three internally vertex-disjoint paths between two endpoints), with any number of subdivisions and arbitrary nonnegative prefix inventories p, in the R765 Boolean local even-triple quotient observer, zero terminal has minimum reserve cost over all terminals. Write B=sum min(p_i,2). Then B-2 <= k_p(0) <= B and k_p(0)<=k_p(w) for every terminal lift w. This is an unbounded-size theorem with a finite exhaustive certificate, not just a check of theta graphs up to a fixed number of vertices. Saving 2 is attained, for example by p=2 at the two endpoints and at least one internal vertex on each of the three paths (the local rank-one blocks then permit two saved events). More generally the profile calculation gives the exact optimum for a specific inventory. The statement concerns universal-prefix Boolean compensation only, not signed amplitudes, ordered provenance, positive branch mass, or native three-axis slice/common-depth reconstruction.

## Exact reduction

K=F2^2 has four candidate lifts. The two endpoints have identity local projection up to basis changes. On each of three paths the internal vertices have the same rank-one functional f, one of the three nonzero linear functionals on K. Choose local basis so the image of f is {0,1}. S0={0}, S1={1,2,3}, S2={0,1,2,3}. Clip p and t at two as in R765. For a fixed suffix and local prefix x the forbidden mask is {z in K:x+w_i+z_i not in S(t_i)}. Local families combine by independent unions; a full K union is precisely a failing prefix. Empty masks can be omitted when a larger mask is present; families with a full mask are unsafe.

On one path let a,b,c denote numbers of p_i=0,1,2 respectively. Subtract the baseline a*0+b+2c from its cost. For any feasible group of suffix choices, its combined forbidden family can, without increasing cost, be reduced to one of four types: N (no forbidden point), H0 (requires f(z)=0), H1 (requires f(z)=1), A (adversarial choice of either half). For zero terminal the exact minimum incremental costs are:
N=2a+b; H0=0 if a+b>0 else infinity; H1=a+b if a>0 else infinity; A=2a+b-1 if c>0 else infinity.
For minimum over *all* terminals, the corresponding four costs are
N=a+b; H0=H1=0 if a+b>0 else infinity; A=a+b-1 if c>0 else infinity.
The free-terminal table describes a dominating set of achievable options, sufficient for optimizing with arbitrary other coordinates.

Proof: at rank one, t=0 is feasible only for p=0 and w in image; it imposes one deterministic half. At t=1, p=0 imposes one half if w in image, none otherwise. For p=1 it imposes one deterministic half if w in image (the unique nonzero image element among prefix choices after the shift), and allows both adversarial halves otherwise; t=0 is impossible. For p=2, t=1 always allows both adversarial halves; t=0 is impossible. t=2 is neutral. At w=0, p=0,t=0 and p=1,t=1 both require f=0; p=0,t=1 requires f=1. Combining opposite deterministic halves is unsafe. Combining an adversarial half with any deterministic half, or two independent adversarial halves, is unsafe because a prefix can cover K. Repeated identical deterministic halves are idempotent. Thus the zero table follows by paying the minimum costs to keep a half or remove all half restrictions; an adversarial option requires exactly one p=2 reduction and all other vertices neutral. In the free case a p=1 adversarial option is dominated by choosing w in image at the same cost with a deterministic half (every allowed exterior is still feasible); p=0 can be neutral at cost 1 instead of 2. Deterministic orientations can be chosen independently and made consistent. The free table is achieved by actual choices of local lifts w; all such choices specify an actual quotient terminal. No independence of the *physical* graph's shared ports is assumed beyond its already defined quotient observer. This proof is about preservation of this cost observer.

## Finite complete comparison

There are exactly three path groups. Each can save at most one relative to its baseline, while each endpoint can save at most two. Hence total negative contributions are at most seven, and an option costing more than +7 can never improve or attain the baseline total, which is feasible at zero. Replace costs above 7 by infinity. Each of a,b may now be capped at 8: any changed value in the displayed positive cost expressions is >=8 (including the -1 term only when actual a+b>=9; at the cap 8, the actual value may be 7 when count=8, so care is needed). To handle that boundary correctly, when a or b is at least 8, distinguish 8 from >=9 if necessary. However the potentially affected value 7 is for A, and using A entails a saving of 1 already counted in that group. Other two groups and endpoints can save at most 6, so A at +7 cannot attain the baseline; it can be discarded. The code conservatively retains capped A at +7, which cannot change either minimum. All other expressions at the cap are above 7 or unchanged. The number c matters only through c>0. Consequently every unbounded path profile is equivalent for purposes of the optimum to one of the 9*9*2 capped profiles, with the +7 adversarial boundary harmless. Deduplicating identical two cost tables gives 54 profiles. This is a finite, fully justified reduction of arbitrary path lengths.

For each pair of endpoint stocks in {0,1,2}^2 and each triple of the four group-family choices, enumerate endpoint stocks t=0,1,2 and lifts w=0 (zero mode) or w=0,1,2,3 (free mode) independently. Use exact four-bit forbidden-union safety to obtain minimum endpoint incremental cost, or infinity. Add each triple of path costs and minimize. Exact check of 9*54^3=1,417,176 profile combinations yields equality of zero and free optima everywhere (free <= zero by inclusion; no strict free improvement). Zero savings distribution across these deduplicated profiles: 0:1,416,528; 1:640; 2:8. These are profile counts, not frequencies of graphs or physical states. All comparisons are integer arithmetic. Infinity sentinel 99 cannot enter a minimum <=0, since other contributions are bounded below by -7. Baseline zero is always feasible via t=p at zero. This proves the theorem including the sharp uniform saving bound. Attainment can also be exhibited without reading the distribution: with both endpoints and one internal vertex on each path p=2, choose t=1 at the two endpoints and t=2 internally. Each endpoint can exclude only one of four candidates; their union excludes at most two. Cost B-2.

For loop-free maximum-degree-three incidence graphs of total cycle rank at most two, remove bridges. Rank-zero projections are independent coordinates, costing at least p_i for any terminal (local attainable sets have strictly increasing sizes), attained at zero. If the two cycles have disjoint support, apply R763 on the independent blocks; if a nontrivial bridgeless component has rank two, R765's degree count gives two degree-three vertices and the component is a theta (suppress degree-two vertices; any pair of disjoint loops joined by an edge would create a bridge). Thus zero optimality extends to this graph class. This is a scoped structural contrast to R764, which has three rank-two local projections at relation rank two and is not a graph incidence kernel of this class.

## Executed finite certificate

The following exact JS was executed with result {"profiles":54,"checks":1417176,"better":0,"distribution":{"0":1416528,"-1":640,"-2":8}}. The earlier execution printed first failures if present; none occurred. The code below differs only in omission of that diagnostic print and has the same arithmetic. Run with Node or another conforming JS runtime. No numerical rounding is used.

```javascript
function verify(){
 const S=[[0],[1,2,3],[0,1,2,3]], fns=[[0,1,0,1],[0,0,1,1],[0,1,1,0]];
 const masks=(p,w,t)=>S[p].map(x=>[0,1,2,3].reduce((m,z)=>m|(!S[t].includes(x^w^z)?1<<z:0),0));
 const group=fns.map(f=>{let a=f.reduce((m,x,z)=>m|(x?1<<z:0),0);return [[0],[a],[15^a],[a,15^a]]});
 const safe=fs=>{let q=[0];for(let f of fs){q=[...new Set(q.flatMap(a=>f.map(b=>a|b)))];if(q.includes(15))return false}return true};
 const P=new Map();for(let a=0;a<=8;a++)for(let b=0;b<=8;b++)for(let c=0;c<=1;c++){let z=[2*a+b,a+b?0:99,a?a+b:99,c?2*a+b-1:99],f=[a+b,a+b?0:99,a+b?0:99,c?a+b-1:99];z=z.map(x=>x>7?99:x);f=f.map(x=>x>7?99:x);P.set(JSON.stringify([z,f]),[a,b,c,z,f])}
 let checks=0,better=0,distribution={};const ps=[...P.values()];
 for(let p=0;p<3;p++)for(let q=0;q<3;q++){
 let T=[[],[]];for(let i=0;i<4;i++)for(let j=0;j<4;j++)for(let k=0;k<4;k++){
 for(let mode=0;mode<2;mode++){let best=99;for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let w=0;w<(mode?4:1);w++)for(let v=0;v<(mode?4:1);v++)if(a+b-p-q<best&&safe([group[0][i],group[1][j],group[2][k],masks(p,w,a),masks(q,v,b)]))best=a+b-p-q;T[mode].push(best)}
 }
 for(let A of ps)for(let B of ps)for(let C of ps){let z=99,f=99;for(let i=0;i<4;i++)for(let j=0;j<4;j++)for(let k=0;k<4;k++){let idx=16*i+4*j+k;z=Math.min(z,T[0][idx]+A[3][i]+B[3][j]+C[3][k]);f=Math.min(f,T[1][idx]+A[4][i]+B[4][j]+C[4][k])}if(f<z)better++;checks++;distribution[z]=(distribution[z]??0)+1}
 }
 return {profiles:ps.length,checks,better,distribution}
}
console.log(JSON.stringify(verify()));
```

## Next

Investigate cycle-rank-three bridgeless subcubic cores (four rank-two vertices); first identify whether an actual incidence graph can realize strict nonzero-terminal advantage. Generalize the local-family aggregation with eight candidate lifts, keeping the Boolean compensation observer separate from native signed BRC, event order and slice depth. Do not repeat the theta finite profile comparison.
