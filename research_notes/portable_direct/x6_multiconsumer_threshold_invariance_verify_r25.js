"use strict";
// R25: exact signed-Port future language of a one-resource two-consumer
// controller; all movements and guards are declared conditional.
// Run: node x6_multiconsumer_threshold_invariance_verify_r25.js
function runR25(){
 const binom=(n,k)=>{let x=1;for(let j=1;j<=k;j++)x=x*(n-j+1)/j;return Math.round(x)};
 const popcount=x=>{let n=0;while(x){n+=x&1;x>>>=1}return n};
 const cases=[],failures=[];let memoStates=0,roots=0;
 for(let m=1;m<=3;m++)for(let q1=1;q1<=2;q1++)
 for(let q2=q1;q2<=3;q2++)for(let u=1;u<=2;u++){
  const qMax=q2,h=2*q1+1,hLong=Math.max(h,2*q2+5);
  const memo=new Map(),intern=new Map([["",0]]);let sid=1;
  function sig(theta,phase,issued,r,done,depth){
   if(depth===0)return 0;
   const key=[theta,phase.join(""),issued.join(""),r,done,depth].join("/");
   if(memo.has(key))return memo.get(key);
   const edges=[];
   for(let i=0;i<m;i++){
    const ps=phase.slice(),cs=issued.slice();let rr=r,symbol;
    if(ps[i]===0){ps[i]=1;symbol="B"+i+"+";}
    else{
      ps[i]=0;symbol="B"+i+"-";
      if(cs[i]<u){cs[i]++;if(theta&(1<<i))rr=Math.min(qMax,r+1)}
    }
    edges.push([symbol,sig(theta,ps,cs,rr,done,depth-1)]);
   }
   for(let j=0;j<2;j++){
    const need=j===0?q1:q2;
    if(!(done&(1<<j))&&r>=need)
      edges.push(["A"+j+"+",sig(theta,phase,issued,r-need,done|(1<<j),depth-1)]);
   }
   edges.sort((a,b)=>a[0].localeCompare(b[0]));
   const word=edges.map(e=>e[0]+"="+e[1]).join("|");
   if(!intern.has(word))intern.set(word,sid++);
   const result=intern.get(word);memo.set(key,result);return result;
  }
  const zero=Array(m).fill(0),short=[],at=[],late=[];
  for(let theta=0;theta<(1<<m);theta++){
    short.push(sig(theta,zero,zero,0,0,h-1));
    at.push(sig(theta,zero,zero,0,0,h));
    late.push(sig(theta,zero,zero,0,0,hLong));
  }
  const t=Math.ceil(q1/u);
  let expected=1;for(let j=t;j<=m;j++)expected+=binom(m,j);
  const toGroups=(arr)=>{
   const x=new Map();for(let j=0;j<arr.length;j++){
     const z=arr[j];if(!x.has(z))x.set(z,[]);x.get(z).push(j)
   }return [...x.values()].map(z=>z.join(",")).sort().join(";");
  };
  const expectedGroups=[Array.from({length:1<<m},(_,j)=>j).filter(j=>popcount(j)<t)];
  for(let j=0;j<(1<<m);j++)if(popcount(j)>=t)expectedGroups.push([j]);
  const ref=expectedGroups.filter(z=>z.length).map(z=>z.join(",")).sort().join(";");
  const passed=new Set(short).size===1 && new Set(at).size===expected &&
      toGroups(at)===ref && toGroups(late)===ref;
  if(!passed)failures.push({m,q1,q2,u,short:new Set(short).size,
                            at:new Set(at).size,late:new Set(late).size,expected});
  cases.push({m,q1,q2,u,first_horizon:h,long_horizon:hLong,
              expected_classes:expected,least_bits:Math.ceil(Math.log2(expected)),
              states_checked:memo.size,pass:passed});
  roots+=(1<<m);memoStates+=memo.size;
 }
 return {schema:"X6_R25_MULTI_CONSUMER_THRESHOLD_INVARIANCE_V1",
   checked_parameter_sets:cases.length,root_assignments:roots,
   memoized_labelled_horizon_states:memoStates,all_pass:failures.length===0,
   failures,cases,
   scope:"m=1..3, q_min=1..2, q_max=q_min..3, source grant cap u=1..2; exact signed-Port words and all source assignments"};
}
if(typeof require!=="undefined" && require.main===module){
 const x=runR25();console.log(JSON.stringify(x,null,2));if(!x.all_pass)process.exitCode=1;
}
