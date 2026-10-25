// R4-EC29 independently executable exact BigInt source-labelled BRC certificate.
// Run: node EC29_verify.js
const verifyEC29 = function verifyEC29(){
  const MAX=25, BRUTE=8;
  const fail=(cond,msg)=>{if(!cond)throw Error(msg)};
  const fact=[1n];for(let k=1;k<=MAX;k++)fact.push(fact[k-1]*BigInt(k));
  const opts=(q)=>q===1?[["A","A0",1],["B","B0",0],["C","C0",0],["C","C1",0]]:[["A","A0",1],["B","B0",0],["C","C0",0]];
  const inc=(p,l)=> l==="A"?[p[0]+1,p[1],p[2]]:l==="B"?[p[0],p[1]+1,p[2]]:[p[0],p[1],p[2]+1];
  const sum=(map,key,v)=>map.set(key,(map.get(key)||0n)+v);
  const closed=(a,b,c)=>{let z=0n, n=a+b+c;for(let r=0;r<=Math.min(a,c);r++)z+=fact[n-r]/(fact[r]*fact[a-r]*fact[b]*fact[c-r]);return z};
  const polystep=(p1,p2)=>{const o=Array.from({length:p1.length+1},()=>0n);for(let j=0;j<p1.length;j++){o[j]+=2n*p1[j];o[j+1]+=p1[j]}for(let j=0;j<p2.length;j++)o[j]+=p2[j];return o};
  let dp=new Map([["0,0,0,0",1n]]), history=[{coords:[0,0,0],q:0,trace:""}];
  let pPrev2=[1n],pPrev1=[2n,1n];
  const checks={dynamic_states:0,endpoint_closed_form:0,grade_recurrence:0,explicit_histogram:0,unique_labelled_paths:0};
  const samples={};
  for(let n=0;n<=MAX;n++){
    const e=new Map(),g=Array.from({length:n+1},()=>0n);
    for(let [key,value] of dp){const [a,b,c,q]=key.split(",").map(Number);fail(a+b+c===n,"typed path length");checks.dynamic_states++;sum(e,`${a},${b},${c}`,value);g[b]+=value}
    for(let [key,value] of e){const [a,b,c]=key.split(",").map(Number);fail(value===closed(a,b,c),`closed form n=${n} endpoint=${key}`);checks.endpoint_closed_form++}
    const pred=n===0?pPrev2:n===1?pPrev1:polystep(pPrev1,pPrev2);
    if(n>=2){pPrev2=pPrev1;pPrev1=pred}
    fail(g.length===pred.length && g.every((x,j)=>x===pred[j]),`grade recurrence n=${n}`);
    checks.grade_recurrence+=n+1;
    if(n<=BRUTE){
      const bh=new Map();
      for(let h of history)sum(bh,h.coords.join(","),1n);
      fail(bh.size===e.size && [...e].every(([k,v])=>bh.get(k)===v),`brute n=${n}`);
      checks.explicit_histogram+=e.size;
      const unq=new Set(history.map(h=>h.trace));
      fail(unq.size===history.length,"source trace identity collision");
      checks.unique_labelled_paths+=history.length;
    }
    if([0,1,2,3,10,25].includes(n))samples[String(n)]={grade:g.map(String),source_total:String(g.reduce((a,b)=>a+b,0n))};
    if(n<MAX){
      const ndp=new Map();
      for(let [key,value] of dp){const [a,b,c,q]=key.split(",").map(Number);for(let [l,label,nq] of opts(q)){let [aa,bb,cc]=inc([a,b,c],l);sum(ndp,`${aa},${bb},${cc},${nq}`,value)}}
      dp=ndp;
    }
    if(n<BRUTE){
      const next=[];
      for(let h of history)for(let [l,label,nq] of opts(h.q))next.push({coords:inc(h.coords,l),q:nq,trace:h.trace+label+"/"});
      history=next;
    }
  }
  const qAB=opts(opts(0).find(x=>x[0]==="A")[2]).find(x=>x[0]==="B")[2];
  const qBA=opts(opts(0).find(x=>x[0]==="B")[2]).find(x=>x[0]==="A")[2];
  const cAB=opts(qAB).filter(x=>x[0]==="C").map(x=>x[1]);
  const cBA=opts(qBA).filter(x=>x[0]==="C").map(x=>x[1]);
  fail(qAB===0 && qBA===1 && cAB.length===1 && cBA.length===2,"witness failed");
  fail(closed(1,1,1)===8n,"endpoint witness");
  return {schema:"EM_R4_EC29_EXACT_BRC_VERIFICATION_V1",status:"PASS",arithmetic:"BigInt integer-only",
    model:"Declared source-labelled native X6 primitive-step restricted test automaton, not native heartbeat dynamics",
    max_dynamic_depth:MAX,max_explicit_source_enumeration_depth:BRUTE,
    checks,samples,
    same_state_witness:{words:["AB","BA"],same_raw_x6_endpoint:[1,1,0,0,0,0],same_step_n:2,same_grade:1,same_current_individual_source_count:1,
     q_after_AB:qAB,q_after_BA:qBA,next_C_branches_from_AB:cAB,next_C_branches_from_BA:cBA,
     next_raw_x6_endpoint:[1,1,1,0,0,0]},
    identity:"1/(1-t*(x+u*y+z)-t*t*x*z)",
    coefficient_formula:"sum_(r=0..min(a,c)) (a+b+c-r)!/(r!(a-r)!b!(c-r)!)",
    scope_exclusions:["No actual native heartbeat update","No formal CLAIM/Result","No independent Driver review","No EC27-to-X6 map"]};
};
console.log(JSON.stringify(verifyEC29(),null,2));
