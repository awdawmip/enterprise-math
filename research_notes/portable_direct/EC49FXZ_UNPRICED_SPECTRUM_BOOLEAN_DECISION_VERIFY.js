'use strict';
// EC49FXZ: no-free-spectrum physical Boolean query tree; frozen BRC16943.
const assert=(p,msg)=>{if(!p)throw Error(msg)};
const mod=(n,m)=>(n%m+m)%m;
const gcd=(a,b)=>b?gcd(b,a%b):a;
const inverse=(a,m)=>{for(let x=1;x<m;x++)if(mod(a*x,m)===1)return x;throw Error('no inverse')};
const slopes={'0,0':[3],'0,1':[0,3,4,5],'1,0':[2,3,4,5],'1,1':[2,3]};
function P(h,n){h=mod(h,10);n=mod(n,10);if(h%5===0&&n%5===0)return false;
  const s=h%5===0?5:mod(n*inverse(h%5,5),5);
  return slopes[`${h%2},${n%2}`].includes(s)}
const reps=new Map();
for(let a=0;a<10;a++)for(let c=0;c<10;c++)if(gcd(gcd(a,c),10)===1){
  let x=-1,y=-1;
  outer:for(let xx=0;xx<10;xx++)for(let yy=0;yy<10;yy++)if(mod(c*xx-a*yy+1,10)===0){x=xx;y=yy;break outer}
  assert(x>=0,'missing primitive representative');
  let u=0;for(let t=0;t<10;t++)if(P(x+a*t,y+c*t))u|=1<<t;
  reps.set(`${a},${c}`,{x,y,u});
}
assert(reps.size===72,'primitive direction census');
const U=[...new Set([...reps.values()].map(q=>q.u))].sort((a,b)=>a-b);
assert(U.length===50&&U.every(u=>u>0),'50 nonempty masks');
function normalize(a,c){
  const b=a+c,e=inverse(a,b),h0=(a*e-1)/b,n0=e-h0, rep=reps.get(`${a%10},${c%10}`);
  assert(rep!==undefined,'primitive residue missing');
  let t0=-1;for(let t=0;t<10;t++)if(mod(h0+a*t-rep.x,10)===0&&mod(n0+c*t-rep.y,10)===0){t0=t;break}
  assert(t0>=0,'shift missing');
  const L0=9*(h0+a*t0)+10*(n0+c*t0),L1=9*a+10*c;
  const z=mod(L1,11)===0?-1:mod(-L0*inverse(mod(L1,11),11),11);
  assert(z!==-1||mod(L0,11)!==0,'forbidden zero factor');
  return {a,b,c,t0,h0,n0,u:rep.u,z};
}
const witnessed=new Map();
for(let a=1;a<=79;a++)for(let c=1;c<=79;c++)if(gcd(a,c)===1){
  const s=normalize(a,c),key=`${s.u}/${s.z}`;
  if(!witnessed.has(key))witnessed.set(key,s);
}
assert(witnessed.size===600,'600 full genuine anchor image');
const states=[];
for(const u of U)for(let z=-1;z<=10;z++){
  const key=`${u}/${z}`;
  assert(witnessed.has(key),'missing genuine witness '+key);
  states.push({u,z,w:witnessed.get(key)});
}
const query=(s,t,j)=>Number((s.u>>t&1)===1&&s.z!==j);
let rawChecks=0;
for(const s of states){
  const w=s.w;
  for(let k=0;k<110;k++){
    const h=w.h0+w.a*(w.t0+k),n=w.n0+w.c*(w.t0+k);
    const original=Number(P(h,n)&&mod(9*h+10*n,11)!==0);
    assert(original===query(s,k%10,k%11),'original C11 mismatch '+s.u+'/'+s.z+':'+k);
    rawChecks++;
  }
}
// Fixed deterministic min-max split. Ties: smaller CRT row t, then smaller column j.
let internal=0,leafCount=0;const hist={};let deepest=null;
function build(ids,depth,path){
  if(ids.length===1){
    leafCount++;hist[depth]=(hist[depth]||0)+1;
    if(!deepest||depth>deepest.depth)deepest={u:states[ids[0]].u,z:states[ids[0]].z,depth,path};
    return {leaf:ids[0]};
  }
  let best=null;
  for(let t=0;t<10;t++)for(let j=0;j<11;j++){
    let n1=0;
    for(const id of ids)n1+=query(states[id],t,j);
    if(n1===0||n1===ids.length)continue;
    const worst=Math.max(n1,ids.length-n1);
    if(best===null||worst<best.worst)best={t,j,worst,n1};
  }
  assert(best!==null,'cannot separate candidate states');internal++;
  const no=[],yes=[];
  for(const id of ids)(query(states[id],best.t,best.j)?yes:no).push(id);
  return {t:best.t,j:best.j,n:ids.length,n0:no.length,n1:yes.length,
    no:build(no,depth+1,[...path,[best.t,best.j,0]]),
    yes:build(yes,depth+1,[...path,[best.t,best.j,1]])};
}
const tree=build(states.map((_,i)=>i),0,[]);
assert(internal===599&&leafCount===600&&tree.t===8&&tree.j===0&&tree.n0===303&&tree.n1===297,'tree census/root');
let maxDepth=0,totalDepth=0;
for(let k=0;k<states.length;k++){
  let node=tree,steps=0;
  while(node.leaf===undefined){
    node=query(states[k],node.t,node.j)?node.yes:node.no;
    steps++;
    assert(steps<=110,'too many probes');
  }
  assert(node.leaf===k,'wrong leaf');
  assert(steps<=16,'upper bound failed');
  totalDepth+=steps;maxDepth=Math.max(maxDepth,steps);
}
assert(maxDepth===16,'non-sharp measured depth');
// Lower bound: for each full factor, the eleven one-hole variants have disjoint difference columns.
let lowerBoundVerified=0;
for(const u of U){
  const full=states.find(s=>s.u===u&&s.z===-1);
  for(let j=0;j<11;j++){
    const hole=states.find(s=>s.u===u&&s.z===j);
    const differences=[];
    for(let t=0;t<10;t++)for(let jj=0;jj<11;jj++)
      if(query(full,t,jj)!==query(hole,t,jj))differences.push([t,jj]);
    assert(differences.length>0&&differences.every(q=>q[1]===j),'disjoint-column proof');
    lowerBoundVerified++;
  }
}
const out={schema:'EC49FXZ_BOOLEAN_ONLY_DECISION_BOUNDS_V1',frozen_scientific_pin:'BRC16943',result:'ALL_PASS',
    premise:'original frozen C11 physical Boolean probes; all 600 normalized states possible; no free indexed spectrum',
    exact_domain:{genuine_anchor_square:'1<=a,c<=79; gcd(a,c)=1',masks:50,column_factors:12,states:600,sites:110},
    proven_bounds:{unconditional_adaptive_identification_lower:11,constructive_upper:16},
    lower_reason:'for fixed U and full V, all 11 single-column deletions differ on disjoint columns',
    algorithm:'deterministic recursive minimax cardinality split; ties lexicographic (t,j)',
    decision_tree:{internal_nodes:internal,leaves:leafCount,root:{t:tree.t,j:tree.j,no:tree.n0,yes:tree.n1},max_depth:maxDepth,average_depth:totalDepth/states.length,leaf_depth_histogram:hist},
    exact_checks:{original_C11_integer_equalities:rawChecks,full_vs_hole_disjoint_column_pairs:lowerBoundVerified,complete_tree_paths:states.length},
    deepest_sample:deepest,
    proof_scope:'finite exhaustive constructive upper bound, analytic lower bound; exact optimum within [11,16] is open',
    status:'AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED',
    native_X6_transfer:'NOT_CLAIMED'};
console.log(JSON.stringify(out,null,2));