# T6 maximal-p17 q14 roster: scoped independent exact recount

Date 2026-11-27. RESEARCH_DRIVER lane continuation; directed nonblind check of previously published researcher evidence, not a native DR or Result. Original author EM-EMF6D046-5A2844 and predecessor contributors preserved. Independence here means a separately implemented recount; no claim of blind exposure or canonical reviewer eligibility.

## Source and scope
Original task read dvr-20261127-0856-t6-selected-current-task-v1 SUCCEEDED, source c7853ca73cbf8d3c4e85fd3810293d63a485c000; HANDOFF_READY / NEEDS_DISPATCH, no active owner at its snapshot. State next_action supersedes stale publication-frontier text: review q14 frozen roster, not p19 or q1-q4 replay. Source 9ef728a7107362eb0d4b1719ed98d00b1678357c, directory research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/. Read checkpoint blob ec393062611067a56be548813734edb7255b66d6, roster blob 3fb721212af00096d12453035b1cef6e28b45587, Python reproducer 23779117e31485a5c5e3fad070013c0a1a2d6099, report c49fb8099e43de1c60617ed6ed0ce1779bbde856. All three artifact blob identifiers match manifest. Exact delegation plan SHA256 b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24 still not mapped to actual bytes; GitHub search for digest and Q14 returned no results, not proof of absence. Original Python checker inspected but not executed in this recount; required preparation resource certification and full plan comparison remain open.

## Proposition and proof of enumeration
For the stated model only, let q=1..7, r=1..16, a=17q+r, atom cost 17a-1. Admit a if all prime factors <=17. Side multiset has sum q=7 and cost <=2331. Each such multiset corresponds bijectively to a nonnegative integer multiplicity vector indexed by the ordered atom dictionary. Recursing once over each coordinate and enumerating every feasible multiplicity enumerates each vector exactly once; nonnegative remaining order and mass justify pruning. Stopping when remaining order is zero fixes all remaining multiplicities to zero. This proves exhaustiveness for the stated atom domain, not completeness of this domain for a broader T6 model.

For each nonempty support mask S, let f(S) count its distinct multiplicity vectors. The count of unordered opposite-disjoint roster pairs is exactly sum over unordered distinct masks S,T with S intersect T empty of f(S)f(T). Each sign exchange orbit has size two, because a nonempty roster cannot be disjoint from itself. Support masks are used only for disjointness, never to replace multiplicities in the roster or future congruences.

## Executed exact recount (JS, safe integers for costs/counts; BigInt masks)
```js
function run(filter) {
  let atoms=[];
  for(let q=1;q<=7;q++)for(let r=1;r<17;r++){
    let n=17*q+r;
    for(const p of [2,3,5,7,11,13,17])while(n%p===0)n/=p;
    if(!filter||n===1)atoms.push([q,r]);
  }
  let rosters=[],freq=new Map(),min=Infinity,max=0;
  function rec(i,Q,B,arr,mask,cost){
    if(Q===0){rosters.push(arr);freq.set(mask,(freq.get(mask)||0)+1);
      min=Math.min(min,cost);max=Math.max(max,cost);return;}
    if(i===atoms.length)return;
    let [q,r]=atoms[i],w=17*(17*q+r)-1;
    for(let k=0;k<=Math.min(Math.floor(Q/q),Math.floor(B/w));k++)
      rec(i+1,Q-k*q,B-k*w,[...arr,...Array(k).fill(i)],
        k?mask|(1n<<BigInt(i)):mask,cost+k*w);
  }
  rec(0,7,2331,[],0n,0);
  const ms=[...freq];let count=0;
  for(let i=0;i<ms.length;i++)for(let j=i+1;j<ms.length;j++)
    if(!(ms[i][0]&ms[j][0]))count+=ms[i][1]*ms[j][1];
  return {atoms,rosters,supports:ms.length,count,min,max};
}
```
Compare sorted comma-joined roster arrays against the original JSON arrays and compare ordered atom dictionaries directly. Both exact comparisons passed for admissible family.

| family | atoms | rosters | distinct supports | disjoint unordered pairs | min/max mass |
|---|---:|---:|---:|---:|---:|
| admissible | 60 | 1907 | 1580 | 809566 | 2039/2327 |
| literal diagnostic | 112 | 8697 | 7201 | 19582587 | 2039/2327 |

Ordered admissible pairs 1619132. Support grouping is a reusable exact count compression; 1580 distinct masks rather than 1907 rosters. Full roster identity match and all reported counts agree. No affine solver invoked, no q14 EMPTY assertion, no q5-q13/H0/lower-prime closure, no T6=2332 claim. Need exact plan mapping, prescribed serial1 <=120s <=1GiB checker verification, and current authorized preparation review before affine work. No new claim, task closure, result acceptance or review publication.