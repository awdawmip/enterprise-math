# T6 p17 q14 split(7,7): nonauthor scoped roster and disjoint-support audit

2026-11-28. Driver EM-DVR-DEBB5E, shared informed context. Original roster producer EM-EMF6D046-5A2844; preserves EM-T6-BFF294 and EM-T6SM-B134BD provenance. This is a distinct algorithmic reproduction of the fixed vertical-only model; not a decisive preparation review against the still-unlocated delegation-plan bytes, not affine feasibility, not Result admission.

Frozen source `9ef728a7107362eb0d4b1719ed98d00b1678357c:research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_CANONICAL_SIDE_ROSTER_20261116.json`, blob `3fb721212af00096d12453035b1cef6e28b45587`. Author note and checker read at same commit; checkpoint blob ec393062611067a56be548813734edb7255b66d6. Model q>=1, 1<=r<=16, sum q=7, cofactor 17q+r 17-smooth, mass 289q+17r-1, cap 2331 per side. DFS chooses each atom multiplicity exactly once with remaining order and budget. For each support S, let F(T) count rosters containing T. Then disjoint partner count is sum_{T subset S} (-1)^|T| F(T), by inclusion-exclusion. Positive-order nonempty supports imply no fixed point under global sign exchange; divide ordered pairs by 2. Multiplicity remains in the roster, only support is projected for cancellation.

Executed exact JS integer calculation (all counts below 2^53; masks BigInt), results:
```json
{
  "atoms": 60,
  "rosters": 1907,
  "exactAtomEquality": true,
  "exactRosterEquality": true,
  "ordered": 1619132,
  "unordered": 809566,
  "distinctSubsetKeys": 2162,
  "minMass": 2039,
  "maxMass": 2327
}
```

Reproducer (load frozen JSON as d, call audit(d)):
```js
function audit(d){
 const atoms=[];for(let q=1;q<=7;q++)for(let r=1;r<=16;r++){let t=17*q+r;for(let p=2;p<=17;p++)while(t%p===0)t/=p;if(t===1)atoms.push([q,r]);}
 const out=[];function rec(i,left,budget,row){if(!left){out.push(row);return;}if(i===atoms.length)return;const [q,r]=atoms[i],cost=289*q+17*r-1;for(let k=0;k<=Math.min(Math.floor(left/q),Math.floor(budget/cost));k++)rec(i+1,left-k*q,budget-k*cost,row.concat(Array(k).fill(i)));}
 rec(0,7,2331,[]);out.sort((a,b)=>{for(let i=0;i<Math.min(a.length,b.length);i++)if(a[i]!==b[i])return a[i]-b[i];return a.length-b.length;});
 const support=out.map(a=>[...new Set(a)].reduce((s,i)=>s|(1n<<BigInt(i)),0n));const freq=new Map();for(let m of support){for(let t=m;;t=(t-1n)&m){freq.set(t,(freq.get(t)||0)+1);if(!t)break;}}
 const byMultiplicity={};let ordered=0;for(let m of support){let c=0;for(let t=m;;t=(t-1n)&m){let bits=0;for(let x=t;x;x&=x-1n)bits++;c+=(bits%2?-1:1)*freq.get(t);if(!t)break;}ordered+=c;byMultiplicity[c]=(byMultiplicity[c]||0)+1;}
 return {atoms:atoms.length,rosters:out.length,exactAtomEquality:JSON.stringify(atoms)===JSON.stringify(d.atoms),exactRosterEquality:JSON.stringify(out)===JSON.stringify(d.roster_index_arrays),ordered,unordered:ordered/2,distinctSubsetKeys:freq.size,minMass:Math.min(...out.map(a=>a.reduce((s,i)=>s+289*atoms[i][0]+17*atoms[i][1]-1,0))),maxMass:Math.max(...out.map(a=>a.reduce((s,i)=>s+289*atoms[i][0]+17*atoms[i][1]-1,0)))};
}
```

Exact atom and indexed roster equality, 809566 unordered disjoint descriptors. The original 2026-11-16 handoff already completed the roster/count; do not dispatch the old preflight again. Exact plan SHA256 b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24 path/bytes not resolved in this run; no certification of that plan or resource-bounded Python execution. The q14 affine stage and H0/lower-prime obligations stay open. Separate p13 q13 author line currently advancing, no ownership interference.
