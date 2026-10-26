'use strict';
function ec44_verify(){
  const wP=[3,1],wQ=[1,3],acts=[];
  for(let p=0;p<=4;p++)for(let q=0;q<=4-p;q++)acts.push({P:p,Q:q,C:4-p-q});
  const eq=(x,y)=>x.length===y.length&&x.every((v,i)=>v===y[i]);
  function direct(first,k){
    let eP=0,eQ=0,tP=64,tQ=64;
    for(let i=0;i<2;i++){
      const a=first[i];
      eP+=wP[i]*(4*a.Q+a.C*k);
      eQ+=wQ[i]*(4*a.P+a.C*(4-k));
      tP+=4*wP[i]*a.C;
      tQ+=4*wQ[i]*a.C;
    }
    return [eP,eQ,tP,tQ];
  }
  function sourceFlow(first,k){
    const z=first.map(a=>({r0:16,root:{P:4*a.P,Q:4*a.Q,C:4*a.C},r1:4*a.C,child:{P:a.C*(4-k),Q:a.C*k,C:0}}));
    for(let i=0;i<2;i++){
      const u=z[i];
      if(u.root.P+u.root.Q+u.root.C!==u.r0||u.child.P+u.child.Q+u.child.C!==u.r1||u.r1!==u.root.C)throw Error("flow conservation");
    }
    for(const a of ["P","Q","C"])if(z[0].child[a]*z[1].r1!==z[1].child[a]*z[0].r1)throw Error("rank-one");
    let eP=0,eQ=0,tP=0,tQ=0;
    for(let i=0;i<2;i++){
      eP+=wP[i]*(z[i].root.Q+z[i].child.Q);
      eQ+=wQ[i]*(z[i].root.P+z[i].child.P);
      const depth=z[i].root.P+z[i].root.Q+2*(z[i].child.P+z[i].child.Q);
      tP+=wP[i]*depth;tQ+=wQ[i]*depth;
    }
    return [eP,eQ,tP,tQ];
  }
  const cmp=(a,b)=>a.n*b.d-b.n*a.d;
  function derived(v){
    const ca=(3*(v[2]-64)-(v[3]-64))/32;
    const cb=(3*(v[3]-64)-(v[2]-64))/32;
    const ua=(3*v[0]-64+v[1])/8;
    const ub=(3*(64-v[1])-v[0])/8;
    return [ca,cb,ua,ub];
  }
  function member(v){
    const [ca,cb,ua,ub]=derived(v);
    if(![ca,cb,ua,ub].every(Number.isInteger))throw Error("unexpected finite-grid rational denominator");
    if(ca<0||ca>4||cb<0||cb>4)return false;
    let lo={n:0,d:1},hi={n:1,d:1};
    for(const [c,u] of [[ca,ua],[cb,ub]]){
      if(c===0){if(u<0||u>16)return false;continue}
      const low={n:u-16+4*c,d:4*c},up={n:u,d:4*c};
      if(cmp(low,lo)>0)lo=low;
      if(cmp(up,hi)<0)hi=up;
    }
    return cmp(lo,hi)<=0;
  }
  let count=0;
  for(const a of acts)for(const b of acts)for(let k=0;k<=4;k++){
    const first=[a,b],v=direct(first,k);
    if(!eq(v,sourceFlow(first,k)))throw Error("path/flow mismatch");
    if(!member(v))throw Error("membership rejected valid point");
    count++;
  }
  let pure=0,maxL=-1,maxPlans=[];
  for(const a of ["P","Q","C"])for(const b of ["P","Q","C"])for(const t of ["P","Q"]){
    const pick=x=>({P:x==="P"?4:0,Q:x==="Q"?4:0,C:x==="C"?4:0});
    const v=direct([pick(a),pick(b)],t==="Q"?4:0),L=v.reduce((s,x)=>s+x,0);
    if(L>maxL){maxL=L;maxPlans=[a+","+b+";x="+t]}else if(L===maxL)maxPlans.push(a+","+b+";x="+t);
    pure++;
  }
  if(count!==1125||pure!==18||maxL!==320)throw Error("coverage / support");
  const A=direct([{P:0,Q:0,C:4},{P:4,Q:0,C:0}],4);
  const B=direct([{P:0,Q:4,C:0},{P:0,Q:0,C:4}],0);
  const mid=A.map((v,i)=>(v+B[i])/2),bit=[48,48,128,128];
  if(!eq(A,[48,48,112,80])||!eq(B,[48,48,80,112])||!eq(mid,[48,48,96,96]))throw Error("witness");
  if(!eq(derived(mid),[2,2,16,0])||member(mid)||member(bit))throw Error("witness feasibility");
  if(bit.reduce((a,b)=>a+b,0)!==352)throw Error("public strict support");
  const wrong={ra:8,rb:8,dQa:8,dQb:0};
  if(wrong.dQa*wrong.rb===wrong.dQb*wrong.ra)throw Error("false rank-one witness");
  return {
    schema:"EM_R4_EC44_SOURCE_RANK_ONE_CHECK_V1",status:"PASS",
    arithmetic:"exact integers, each four-observer coordinate scaled by 64",
    grid:{root_action_simplexes_per_root:acts.length,terminal_Q_values:5,randomized_policies_checked:count,source_path_flow_equalities_checked:count,rank_one_checks_at_terminal:3*count,membership_checks:count},
    deterministic:{pure_current_symbol_policies:pure,max_L:"5",maximizers:maxPlans},
    nonconvex:{A_over_64:A,B_over_64:B,midpoint_over_64:mid,derived_midpoint_ca_cb_out_of_4_and_ua_ub_out_of_16:derived(mid),midpoint_memoryless_feasible:false},
    memory_gap:{one_bit_memory_over_64:bit,one_bit_L:"11/2",public_hull_max_L:"5",exact_gap:"1/2"},
    deliberately_bad_flow_rank_one_rejected:true,
    research_scope:"finite auxiliary positive-rational two-hypothesis labelled-source stop/decision trees",
    unperformed:["native_X6_heartbeat_update","full_native_activity_guard","independent_driver_review","formal_theorem_admission"]
  };
}
if (typeof module !== 'undefined' && require.main === module) process.stdout.write(JSON.stringify(ec44_verify(),null,2)+'\n');
if (typeof module !== 'undefined') module.exports={ec44_verify};
