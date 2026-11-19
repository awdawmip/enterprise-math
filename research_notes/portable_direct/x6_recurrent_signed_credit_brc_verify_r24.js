"use strict";
/*
 R24 exact source/signed-Port Boolean-BRC trace-language checker.
 Run: node x6_recurrent_signed_credit_brc_verify_r24.js
 Each B_i alternates +E1,-E1. Only completion of a return cycle can
 grant 1 credit if theta_i=1 and fewer than u grants have been issued.
 The single A+ event costs q credits.
*/
function runR24(){
  const checks=[],failures=[];let totalStates=0,totalWitnesses=0,totalRoots=0;
  const popcount=x=>{let k=0;while(x){k+=x&1;x>>>=1}return k};
  const binom=(n,k)=>{let x=1;for(let i=1;i<=k;i++)x=x*(n-i+1)/i;return Math.round(x)};
  for(let m=1;m<=4;m++) for(let q=1;q<=Math.min(m+1,4);q++) for(let u=1;u<=q;u++){
    const H=2*q+1,intern=new Map([["",0]]),memo=new Map();let nextId=1;
    const sig=(mask,phase,counts,credit,done,depth)=>{
      if(depth===0)return 0;
      const stateKey=[mask,phase.join(""),counts.join(""),credit,done?1:0,depth].join("/");
      if(memo.has(stateKey))return memo.get(stateKey);
      const edges=[];
      for(let i=0;i<m;i++){
        const ps=phase.slice(),cs=counts.slice();
        let r=credit,label;
        if(ps[i]===0){ps[i]=1;label="b"+i+"+";}
        else {
          ps[i]=0;label="b"+i+"-";
          if(cs[i]<u){cs[i]++;if(mask&(1<<i))r=Math.min(q,r+1);}
        }
        edges.push([label,sig(mask,ps,cs,r,done,depth-1)]);
      }
      if(!done && credit>=q)
        edges.push(["a+",sig(mask,phase,counts,credit-q,true,depth-1)]);
      edges.sort((a,b)=>a[0].localeCompare(b[0]));
      const word=edges.map(([a,b])=>a+"="+b).join(";");
      if(!intern.has(word))intern.set(word,nextId++);
      const value=intern.get(word);memo.set(stateKey,value);return value;
    };
    const short=[],long=[],zero=Array(m).fill(0);
    for(let mask=0;mask<2**m;mask++){
      short.push(sig(mask,zero,zero,0,false,H-1));
      long.push(sig(mask,zero,zero,0,false,H));
    }
    const t=Math.ceil(q/u);
    let expected=1;
    for(let j=t;j<=m;j++)expected+=binom(m,j);
    if(new Set(short).size!==1)failures.push([m,q,u,"horizon_before_threshold",new Set(short).size]);
    if(new Set(long).size!==expected)
      failures.push([m,q,u,"horizon_at_threshold",new Set(long).size,expected]);
    const groups=new Map();
    for(let mask=0;mask<2**m;mask++){
      const s=long[mask];if(!groups.has(s))groups.set(s,[]);groups.get(s).push(mask);
    }
    for(const group of groups.values()){
      const low=group.filter(mask=>popcount(mask)<t);
      if((group.length>1 && group.some(mask=>popcount(mask)>=t)) ||
         (low.length>0 && low.length!==group.length))
        failures.push([m,q,u,"wrong_equivalence_class",group]);
    }
    const witness=(mask,seq)=>{
      let credit=0;const seen=Array(m).fill(0);
      for(const i of seq){
        seen[i]++;
        if(seen[i]<=u && (mask&(1<<i)))credit=Math.min(q,credit+1);
      }
      return credit===q;
    };
    const enumerate=(seq,depth)=>{
      if(depth===q){
        for(let mask=0;mask<2**m;mask++){
          const success=witness(mask,seq);
          const expectedWord=seq.every(i=>(mask&(1<<i))!==0 &&
                                   seq.filter(j=>j===i).length<=u);
          if(success!==expectedWord)failures.push([m,q,u,"explicit_witness",mask,seq]);
          totalWitnesses++;
        }
        return;
      }
      for(let i=0;i<m;i++)enumerate([...seq,i],depth+1);
    };
    enumerate([],0);
    checks.push({m,q,u,h:H,classes:expected,bit_minimum:Math.ceil(Math.log2(expected)),
                 states_checked:memo.size,signature_nodes:intern.size,assignments:2**m});
    totalStates+=memo.size;totalRoots+=2**m;
  }
  return {
    schema:"X6_R24_RECURRENT_SHARED_CREDIT_BOOLEAN_BRC_V1",
    model:"two signed Port moves per credit cycle, per-source grant cap u, one consumer cost q",
    checked_parameter_sets:checks.length,
    total_root_assignments:totalRoots,
    total_memoized_labelled_states:totalStates,
    total_explicit_witness_replays:totalWitnesses,
    all_pass:failures.length===0,failures:failures.slice(0,30),
    notable:checks.filter(x=>x.m===4&&x.q===4).map(x=>({u:x.u,classes:x.classes,
        bit_minimum:x.bit_minimum,states_checked:x.states_checked})),
    scope:"m=1..4,q=1..min(m+1,4),u=1..q; source/signed Port labels; conditional event controller only",
    cases:checks
  };
}
if(typeof require!=="undefined" && require.main===module){
  const result=runR24();console.log(JSON.stringify(result,null,2));
  if(!result.all_pass)process.exitCode=1;
}
