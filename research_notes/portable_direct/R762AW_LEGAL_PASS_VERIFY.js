'use strict';
// Reconstruct exact integer conditional V29/V25 selector and legal three-PASS branch counts. Run: node R762AW_LEGAL_PASS_VERIFY.js
const calculate = function calculate(){
 const ck=(v,m)=>{if(!v)throw Error("R762AW fail "+m)};
 const match=[[[0,1],[2,3],[4,5]],[[0,2],[1,4],[3,5]],[[0,3],[1,5],[2,4]],[[0,4],[1,3],[2,5]]];
 const events=[[0,1],[1,2],[2,0]], states=[];
 for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)states.push([i,j,k]);
 const name=s=>s.join(""), codes={};for(const s of states)codes[name(s)]=match.map(p=>p.every(([a,b])=>s.includes(a)!==s.includes(b))?p.reduce((v,[a,b])=>v*(s.includes(b)?-1:1),1):0);
 const nbr={};for(const s of states)nbr[name(s)]=states.filter(t=>s.filter(x=>t.includes(x)).length===2).map(name);
 function val(s,t,n,m){
  let M=Array.from({length:4},()=>Array(4).fill(0));
  events.forEach(([a,b],i)=>M[a][b]=n+((m>>i)&1));
  let u=[-2,-4,-3,10].map((z,i)=>z+M[i].reduce((a,b)=>a+b,0)-M.reduce((a,row)=>a+row[i],0)),cs=codes[s],ct=codes[t],v=0;
  for(let i=0;i<4;i++){v+=u[i]*ct[i];for(let j=0;j<4;j++)v+=cs[i]*(M[i][j]-M[j][i])*ct[j]}
  return v;
 }
 const win=(s,n,m)=>{const a=nbr[s].map(t=>[t,val(s,t,n,m)]), mx=Math.max(...a.map(p=>p[1]));return a.filter(p=>p[1]===mx).map(p=>p[0]).sort()};
 const cycle=["012","123","234","034","035","025"];
 const permutations=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
 const words=permutations.map(p=>p.map((_,j)=>p.slice(0,j+1).reduce((z,i)=>z|(1<<i),0)));
 ck(JSON.stringify(words)===JSON.stringify([[1,3,7],[1,5,7],[2,3,7],[2,6,7],[4,5,7],[4,6,7]]),"six permutation masks");
 for(const n of [16,17,23,100])for(let i=0;i<6;i++)for(let m=0;m<8;m++)ck(JSON.stringify(win(cycle[i],n,m))===JSON.stringify([cycle[(i+1)%6]]),"unique cycle");
 let results={};
 for(const s of states.map(name)){
  let hist=[];
  for(let ix=0;ix<6;ix++){
    let track=[{last:s,states:[s],mask:[]}];
    for(const m of words[ix]){
      let next=[];
      for(const t of track)for(const last of win(t.last,16,m))next.push({last,states:[...t.states,last],mask:[...t.mask,m]});
      track=next;
    }
    hist.push(...track);
  }
  ck(hist.every(h=>cycle.includes(h.last)),"cycle absorption");
  const count=hist.length, paths=new Set(hist.map(h=>h.states.join(">"))).size;
  const ends=cycle.map(x=>hist.filter(h=>h.last===x).length);
  results[s]={B1:count,unlabeled_state_paths:paths,end_vector:ends};
 }
 const exceptional=["013","014","024","135","235","245"];
 const doubled=["013","014","023","024","135","145","235","245"];
 for(const [s,r] of Object.entries(results)){
  ck(r.B1===(exceptional.includes(s)?8:6),"B1 "+s);
  ck(r.unlabeled_state_paths===(doubled.includes(s)?2:1),"paths "+s);
 }
 ck(JSON.stringify(results["145"].end_vector)==="[2,0,4,0,0,0]","145 ends");
 ck(JSON.stringify(results["013"].end_vector)==="[0,0,6,0,0,2]","013 ends");
 const checks=[];
 for(const [s,v] of Object.entries(results)){
  let d=v.end_vector;
  for(let r=1;r<=5;r++){
    if(r>1){let e=[0,0,0,0,0,0];for(let i=0;i<6;i++)e[(i+3)%6]+=6*d[i];d=e}
    const k=d.reduce((a,b)=>a+b,0);ck(k===v.B1*6**(r-1),"macro recurrence "+s+","+r);
    checks.push([s,r,k]);
  }
 }
 return {schema:"R762AW_LEGAL_3PASS_BRC_CERT_V1",status:"PASS",start_n:"any integer n>=16 by independent R762AU affine-dominance theorem",base_model:"frozen P000 with conditional V23/V25/V29 active-triad selector",source:"R762AU PR #2451; R762AV PR #2453",states:20,permutations,mask_words:words,cycle,one_macro:results,exceptional_B1_8:exceptional,twopath_initials:doubled,count_law:"B_r(s)=B1(s)*6^(r-1), integer r>=1; B1=8 on exceptional set, B1=6 otherwise",root145:"B_r(145)=6^r",root013:"B_r(013)=8*6^(r-1)",first_macro_20_state_checks:20,legal_order_words_checked:6,cycle_uniqueness_sanity_n:[16,17,23,100],recurrence_checks:checks,proof_scope:"Mathematical induction on all r once every first-macro branch reaches C; affine dominance inherited from R762AU for all integer n>=16; model conditional and independent review pending"};
};
console.log(JSON.stringify(calculate(),null,2));
