// Exact-integer audit of the full causal BRC N=4 time-only R1 theorem.
// Run: node VERIFY.js  (Node 18+; no libraries).
// Eight preparations; time 1/2/3/4; first-stage A/B decisions are included.
"use strict";
function verify() {
  const ok=(x,m)=>{if(!x) throw new Error("CHECK_FAILED: "+m);};
  const bit=(n,j)=>(n>>j)&1;
  const raw={
    Q:{AU:[10,10],AV:[20,20],BU:[15,15],BV:[15,15]},
    P:{AU:[9,11],AV:[5,5],BU:[3,27],BV:[30,30]}
  };
  const rows=[
    {id:"AU_Q",S:"AU",p:"A",j:[10,10],lr:[0,1]},
    {id:"AU_P",S:"AU",p:"A",j:[9,11],lr:[0,1]},
    {id:"AV_Q",S:"AV",p:"A",j:[10,10],lr:[2,2]},
    {id:"AV_P",S:"AV",p:"A",j:[10,10],lr:[2,2]},
    {id:"BU_Q",S:"BU",p:"B",j:[10,10],lr:[3,4]},
    {id:"BU_P",S:"BU",p:"B",j:[2,18],lr:[3,4]},
    {id:"BV_Q",S:"BV",p:"B",j:[10,10],lr:[5,5]},
    {id:"BV_P",S:"BV",p:"B",j:[10,10],lr:[5,5]}
  ];
  let leaves=0;
  for(const law of ["Q","P"]){
    let sum=0;
    for(const S of ["AU","AV","BU","BV"]){
      const [a,b]=raw[law][S];ok(a>0&&b>0,"positive leaf");
      sum+=2*(a+b);leaves+=4;
      const r=rows.find(x=>x.id===S+"_"+law);
      ok(r.j[0]*(a+b)===20*a&&r.j[1]*(a+b)===20*b,"conditional preparation");
    }
    ok(sum===240,"P/Q sixteen-leaf normalization");
  }
  const g=S=>S==="AV"?1:S==="BV"?2:0;
  // Each center has exact denominator 120, ordered (T1,T2,T3,T4).
  function center(first,second,third){
    const a=bit(first,0),b=bit(first,1);
    if(!a&&!b)return [120,0,0,0];
    if(a&&b)return [0,40,40,40];
    const live=a?"A":"B", remaining=live==="A"?"AV":"BV";
    const x=bit(second,0),y=bit(second,g(remaining));
    if(!x&&!y)return [60,60,0,0];
    if(x&&y)return [40,0,40,40];
    if(!x&&y){const t=bit(third,live==="A"?2:5);return [40,40,40*t,40*(1-t)];}
    // The surviving AU/BU sibling has two P/Q conditional J distributions.
    // Reference common submeasure of mass 1/3, pushed through the time kernel.
    const w=live==="A"?[19,21]:[8,32],j=live==="A"?0:3;
    const t3=w[0]*bit(third,j)+w[1]*bit(third,j+1);
    return [40,40,t3,40-t3];
  }
  function truth(row,first,second,third){
    if(!bit(first,row.p==="A"?0:1))return [120,0,0,0];
    if(!bit(second,g(row.S)))return [0,120,0,0];
    const t3=row.j[0]*bit(third,row.lr[0])+row.j[1]*bit(third,row.lr[1]);
    return [0,0,6*t3,120-6*t3];
  }
  const L1=(a,b)=>a.reduce((s,x,i)=>s+Math.abs(x-b[i]),0);
  let rowsChecked=0,maxAdaptiveL1=0,maxFixedL1=0,sharpAdaptiveRows=0,splitPolicies=0;
  for(let f=0;f<4;f++)for(let s=0;s<8;s++)for(let t=0;t<64;t++){
    const d=center(f,s,t);ok(d.reduce((a,b)=>a+b,0)===120,"decoder normalized");
    if(f===1||f===2)splitPolicies++;
    for(const row of rows){
      const p=truth(row,f,s,t),ad=L1(p,d),fixed=L1(p,[30,30,30,30]);
      ok(p.reduce((a,b)=>a+b,0)===120,"truth normalized");
      ok(ad<=160,"adaptive decoder total variation <= 2/3");
      ok(fixed<=180,"fixed decoder total variation <= 3/4");
      maxAdaptiveL1=Math.max(maxAdaptiveL1,ad);
      maxFixedL1=Math.max(maxFixedL1,fixed);
      if(ad===160)sharpAdaptiveRows++;
      rowsChecked++;
    }
  }
  const witness=[
    truth(rows[2],3,5,27),truth(rows[0],3,5,27),truth(rows[6],3,5,27)
  ];
  ok(JSON.stringify(witness)===JSON.stringify([[0,120,0,0],[0,0,120,0],[0,0,0,120]]),"lawful three-time lower witness");
  const pureTimes=[
    truth(rows[0],0,0,0),truth(rows[0],3,0,0),
    truth(rows[0],3,7,63),truth(rows[0],3,7,0)
  ];
  ok(JSON.stringify(pureTimes)===JSON.stringify([[120,0,0,0],[0,120,0,0],[0,0,120,0],[0,0,0,120]]),"four fixed-decoder policy witnesses");
  ok(maxAdaptiveL1===160&&maxFixedL1===180,"sharp radii");
  return {
    marker:"PASS_BRC_N4_TIME_ONLY_FULL_CAUSAL_R1_20261031",
    exact_source_leaves:leaves,deterministic_S23_timing_policies:2048,
    total_preparation_comparisons:rowsChecked,one_first_prefix_continues_cases:splitPolicies,
    maximal_TV_with_policy_dependent_decoder:"160/240=2/3",
    maximal_TV_with_policy_independent_decoder:"180/240=3/4",
    sharp_policy_dependent_rows:sharpAdaptiveRows,
    three_time_lower_witness:witness,four_policy_fixed_decoder_witness:pureTimes,
    scope:"deterministic S23 timing enumeration; all randomized S23/S2 proved by analytic behavioral mixture and domination arguments"
  };
}
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(verify(),null,2));
