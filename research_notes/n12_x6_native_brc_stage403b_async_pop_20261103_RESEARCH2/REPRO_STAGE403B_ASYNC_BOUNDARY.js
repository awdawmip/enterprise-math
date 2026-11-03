// Stage403-B: exact asynchronous Q-POP counterexamples, for Node.js.
"use strict";
const result=(function(){
  const inv={A:"B",B:"A",C:"D",D:"C"};
  const axes={A:[1,0,0,0,0,0],B:[-1,0,0,0,0,0],C:[0,0,1,0,0,0],D:[0,0,-1,0,0,0]};
  const plus=(u,v)=>u.map((x,i)=>x+v[i]);
  const z=w=>[...w].reduce((u,x)=>plus(u,axes[x]),[0,0,0,0,0,0]);
  function adj(w){const d={};for(let i=0;i+1<w.length;i++){const e=w.slice(i,i+2);d[e]=(d[e]||0)+1;}return Object.fromEntries(Object.entries(d).sort());}
  const K=(p,q)=>[...p.slice(0,Math.min(p.length,q.length))].reduce((v,x,i)=>v+(x===q[i]?1:0),0);
  const obs=(p,q)=>JSON.stringify({mP:p.length,mQ:q.length,zP:z(p),zQ:z(q),JP:adj(p),JQ:adj(q),K:K(p,q)});
  function cancel(p,q){if(p.length<2||q.length<2||inv[p.at(-1)]!==p.at(-2)||inv[q.at(-1)]!==q.at(-2))throw Error("CANCEL disabled");return [p.slice(0,-2),q.slice(0,-2)];}
  const family=[];
  for(let c=0;c<=6;c++){
    const tail="AB".repeat(c)+"A";
    const p="CCCA"+"AB".repeat(c),q1="AAB"+tail,q2="ABA"+tail,L=2*c+2;
    if(p.length!==q1.length||q1.length!==q2.length||q1.slice(-(L-1))!==q2.slice(-(L-1)))throw Error("incorrect family");
    if(obs(p,q1)!==obs(p,q2)||K(p,q1)!==1)throw Error("current observer mismatch");
    let a=[p,q1.slice(0,-1)],b=[p,q2.slice(0,-1)];
    if(c>0 && obs(...a)!==obs(...b))throw Error("premature distinction on Q-POP");
    for(let k=0;k<c;k++){a=cancel(...a);b=cancel(...b);if(k+1<c&&obs(...a)!==obs(...b))throw Error("premature distinction");}
    if(obs(...a)===obs(...b)||a[0]!=="CCCA"||b[0]!=="CCCA"||a[1]!=="AAB"||b[1]!=="ABA")throw Error("final witness failure");
    family.push({C:c,m:p.length,K_initial:1,L_minus_1:L-1,L_sufficient:L,Q1:q1,Q2:q2,final_JQ_1:adj(a[1]),final_JQ_2:adj(b[1])});
  }
  let words=0;let groups=0;
  for(let n=1;n<=7;n++){
    const seen=new Map();
    for(let mask=0;mask<(1<<n);mask++){
      let w="";for(let i=0;i<n;i++)w+=mask&(1<<i)?"B":"A";
      const key=JSON.stringify([z(w),adj(w),w.slice(-5)]);
      if(seen.has(key)&&seen.get(key)!==w)throw Error("unexpected n<=7 collision");
      seen.set(key,w);words++;
    }
    groups+=seen.size;
  }
  const steps=[];for(let i=0;i<6;i++)for(const s of [1,-1]){const v=Array(6).fill(0);v[i]=s;steps.push(v);}
  let dp=new Map([["0,0,0,0,0,0",1n]]);
  for(let n=0;n<8;n++){
    const nd=new Map();
    for(const [key,weight] of dp)for(const step of steps){const next=plus(key.split(",").map(Number),step).join(",");nd.set(next,(nd.get(next)||0n)+weight);}
    dp=nd;
  }
  const Np=dp.get(z("CCCAABAB").join(",")),Nq=dp.get(z("AABABABA").join(","));
  if(Np!==68768n||Nq!==385056n)throw Error("native 12-direction BRC count error");
  return {marker:"STAGE403B_ASYNC_BOUNDARY_PASS",sample_C_range:"0..6",family,short_binary_words_checked:words,short_binary_groups:groups,native_X6_BRC_steps:12,BRC_n:8,N8_P:Np.toString(),N8_Q:Nq.toString(),
    operation_language:"arbitrary paired APPEND; at most one Q-only POP; at most C synchronized two-source inverse-pair CANCEL",
    K_rule:"sum of equal labels at shared absolute indices i <= min(mP,mQ)"};
})();
if (typeof console!=="undefined") console.log(JSON.stringify(result,null,2));
