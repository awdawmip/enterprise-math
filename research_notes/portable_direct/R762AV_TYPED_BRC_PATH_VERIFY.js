'use strict';
// Deterministic standard-library-free exact integer verifier. Run: node R762AV_TYPED_BRC_PATH_VERIFY.js
const compute=function compute(){
  const ck=(v,m)=>{if(!v)throw Error(m)};
  const match=[[[0,1],[2,3],[4,5]],[[0,2],[1,4],[3,5]],[[0,3],[1,5],[2,4]],[[0,4],[1,3],[2,5]]];
  const events=[[0,1],[1,2],[2,0]];
  const triads=[];
  for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)triads.push([i,j,k]);
  const key=s=>s.join('');
  const from=s=>[...s].map(Number);
  const c=Object.fromEntries(triads.map(s=>[key(s),match.map(p=>
    p.every(([a,b])=>s.includes(a)!==s.includes(b))?
    p.reduce((v,[a,b])=>v*(s.includes(b)?-1:1),1):0)]));
  const neighbors=s=>triads.filter(t=>s.filter(x=>t.includes(x)).length===2);
  function score(s,t,n,m){
    const M=Array.from({length:4},()=>Array(4).fill(0));
    events.forEach(([a,b],i)=>{M[a][b]=n+((m>>i)&1)});
    const u=[-2,-4,-3,10].map((v,i)=>v+M[i].reduce((a,b)=>a+b,0)-M.reduce((a,r)=>a+r[i],0));
    const a=c[key(s)],b=c[key(t)];
    let z=0;
    for(let i=0;i<4;i++){z+=u[i]*b[i];for(let j=0;j<4;j++)z+=a[i]*(M[i][j]-M[j][i])*b[j]}
    return z;
  }
  const winners=(s,n,m)=>{
    const opts=neighbors(s), val=Math.max(...opts.map(t=>score(s,t,n,m)));
    return opts.filter(t=>score(s,t,n,m)===val).map(key).sort();
  };
  ck(triads.length===20,'states');
  const U={},W={};
  for(const s of triads){
    const label=key(s), ed={};
    for(let m=0;m<8;m++)for(const t of winners(s,16,m))ed[t]=(ed[t]||0)+1;
    U[label]=Object.keys(ed).sort(); W[label]=ed;
    for(let m=0;m<8;m++)ck(JSON.stringify(winners(s,16,m))===JSON.stringify(winners(s,17,m)),'stationarity check');
  }
  const cycle=['012','123','234','034','035','025'];
  const cyclic=new Set(cycle);
  const successor=Object.fromEntries(cycle.map((s,i)=>[s,cycle[(i+1)%6]]));
  for(const s of cycle){ck(JSON.stringify(U[s])===JSON.stringify([successor[s]]),'cycle edge');ck(W[s][successor[s]]===8,'cycle multiplicity')}
  ck(Object.values(U).reduce((a,v)=>a+v.length,0)===27,'27 edges');
  ck(Object.values(W).reduce((a,v)=>a+Object.values(v).reduce((x,y)=>x+y,0),0)===172,'172 branch edges');
  const depths={},stack=new Set();
  function depth(s){
    if(cyclic.has(s))return 0;
    if(depths[s]!==undefined)return depths[s];
    ck(!stack.has(s),'exterior cycle');stack.add(s);
    depths[s]=1+Math.max(...U[s].map(depth));stack.delete(s);
    return depths[s];
  }
  for(const s of Object.keys(U))depth(s);
  ck(Math.max(...Object.values(depths))===3,'height3');
  const countDepth=Object.fromEntries([1,2,3].map(h=>[h,Object.values(depths).filter(d=>d===h).length]));
  ck(JSON.stringify(countDepth)===JSON.stringify({'1':10,'2':3,'3':1}),'depth census');
  function paths(start,n,weighted){
    let dist={[start]:1};
    for(let k=0;k<n;k++){
      const next={};
      for(const [s,v] of Object.entries(dist)){
        if(weighted){for(const [t,w] of Object.entries(W[s]))next[t]=(next[t]||0)+v*w}
        else {for(const t of U[s])next[t]=(next[t]||0)+v}
      }
      dist=next;
    }
    return dist;
  }
  const sum=d=>Object.values(d).reduce((a,b)=>a+b,0);
  const counts=[];
  for(const s of Object.keys(U).sort()){
    const A=paths(s,3,false),B=paths(s,9,false),M=paths(s,3,true),M4=paths(s,4,true);
    ck(JSON.stringify(cycle.map(x=>A[x]||0))===JSON.stringify(cycle.map(x=>B[x]||0)),'period6');
    ck(sum(M4)===8*sum(M),'multiplicity8');
    ck(Object.keys(A).every(x=>cyclic.has(x)),'all paths enter');
    counts.push({state:s,unlabeled_paths_at_3:sum(A),mask_tagged_paths_at_3:sum(M)});
  }
  ck(Math.max(...counts.map(x=>x.unlabeled_paths_at_3))===6,'max support paths');
  ck(Math.max(...counts.map(x=>x.mask_tagged_paths_at_3))===880,'max BRC paths');
  const root='145',unl=paths(root,3,false),lab=paths(root,3,true);
  ck(JSON.stringify(cycle.map(x=>unl[x]||0))===JSON.stringify([1,1,1,1,1,1]),'six one each');
  ck(JSON.stringify(cycle.map(x=>lab[x]||0))===JSON.stringify([192,16,448,48,64,112]),'weighted cycle vector');
  ck(sum(lab)===880,'880');
  const directions=[];for(let a=0;a<6;a++)for(const sign of [-1,1])directions.push([a,sign]);
  let tripleZero=0;for(const [i,x] of directions.entries())for(const y of directions)for(const z of directions){
    const vec=Array(6).fill(0);for(const [a,sgn] of [x,y,z])vec[a]+=sgn;
    if(vec.every(q=>q===0))tripleZero++;
  }
  ck(tripleZero===0 && directions.length===12,'signed X6 odd-step obstruction');
  const cert={
    schema:'R762AV_TYPED_BRC_PATH_MULTIPLICITY_CERT_V1',status:'PASS',
    model:'V23 four matching code + V29 cumulative 3-PASS mask + V25 exponent maximum; n>=16 stabilized relation',
    declared_input:'20 three-axis sets, four matchings, 8 masks, 9 Johnson neighbors per source, n=16; AU affine proof supplies unbounded n>=16',
    source_comparison:'R762AU PR2451/f42064096ba3014a63a8d75bbe9f4b7dcdaff447',
    states:20,masks:8,mask_erased_union_edges:27,mask_tagged_edges_counting_ties:172,
    cycle,cycle_mask_multiplicity:8, exterior_height_census:countDepth,
    distinct_unlabeled_path_max_after_3:6,distinct_mask_tagged_path_max_after_3:880,
    root145:{support_path_counts_length3:cycle.map(x=>unl[x]||0),labeled_path_counts_length3:cycle.map(x=>lab[x]||0),labeled_total_length3:sum(lab),support_total_length3:sum(unl),labeled_growth_formula:'880 * 8^(k-3), k>=3',unlabeled_growth_formula:'6, k>=3'},
    count_by_initial_state:counts,
    union_adjacency:U, mask_multiplicity:W,
    x6_signed_spatial_steps:{signed_primitive_directions:12,checked_three_step_paths:1728,zero_spatial_returns:tripleZero,reason:'parity of coordinate sum is odd after 3 signed unit steps'},
    validation:'Exact integers only; branch-word semiring coefficients; all 20x8 winner sets at n=16; n=17 sanity check; universal n>=16 uses the source AU affine dominance proof; not a native force model nor independent review'
  };
  return cert;
};
console.log(JSON.stringify(compute(),null,2));
