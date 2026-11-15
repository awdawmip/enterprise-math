#!/usr/bin/env node
"use strict";
function verifyR762AY(){
  const fac=[1];for(let n=1;n<=8;n++)fac[n]=fac[n-1]*n;
  const allPerms=(n)=>{let a=[];const rec=(p,left)=>{if(!left.length){a.push(p);return}for(let i=0;i<left.length;i++)rec(p.concat(left[i]),left.slice(0,i).concat(left.slice(i+1)))};rec([],Array.from({length:n},(_,i)=>i));return a};
  const count=(m,mask)=>{const s=Array.from({length:m},(_,i)=>i).filter(i=>(mask>>i)&1);if(!s.length)return 0;let d=1;for(let i=0;i<s.length;i++){let g=(s[(i+1)%s.length]-s[i]+m)%m||m;d*=fac[g]}return fac[m]/d};
  const pop=(x)=>{let c=0;while(x){x&=x-1;c++}return c};
  const apply=(mask,sig)=>sig.reduce((acc,dest,i)=>acc|(((mask>>i)&1)<<dest),0);
  const gcd=(a,b)=>b?gcd(b,a%b):a,lcm=(a,b)=>a/gcd(a,b)*b;
  const ord=(sig)=>{let seen=new Set(),out=1;for(let i=0;i<sig.length;i++){if(seen.has(i))continue;let j=i,len=0;do{seen.add(j);j=sig[j];len++}while(j!==i);out=lcm(out,len)}return out};
  let fullCases=0,individualPerms=0,extremeCases=0,frames=0,pairChecks=0,countPeriods=0;
  const extremeRecords={};
  for(let m=2;m<=7;m++){
   const words=allPerms(m);fullCases+=(1<<m);
   let byH=Array.from({length:m+1},()=>[]);
   for(let mask=0;mask<(1<<m);mask++){
     let n=0;
     for(const word of words){const K=Array.from({length:m},(_,i)=>(mask>>i)&1);let ok=true;for(const e of word){if(!K[e]){ok=false;break}K[e]--;K[(e+1)%m]++}if(ok){n++;if(K.some((x,i)=>x!==((mask>>i)&1)))throw Error("inventory not restored")}}
     individualPerms+=words.length;
     if(n!==count(m,mask))throw Error(`direct count m=${m} mask=${mask} n=${n} expected=${count(m,mask)}`);
     byH[pop(mask)].push(n)
   }
   extremeRecords[m]={};
   for(let h=0;h<=m;h++){
    const a=h?Math.floor(m/h):0,b=h?m%h:0;
    const mn=h?fac[m]/fac[m-h+1]:0,mx=h?fac[m]/(fac[a]**(h-b)*fac[a+1]**b):0;
    const actual=[Math.min(...byH[h]),Math.max(...byH[h])];
    if(actual[0]!==mn||actual[1]!==mx)throw Error(`extreme m=${m} h=${h}`);
    if(m===4||m===6)extremeRecords[m][h]={min:mn,max:mx};
    extremeCases++;
   }
  }
  for(let m=2;m<=5;m++){
   for(const sig of allPerms(m)){
    frames++;const d=ord(sig);
    const sequences=[],prefixes=[];
    for(let mask=0;mask<(1<<m);mask++){let cur=mask,prod=1n,seq=[],pre=[];for(let j=0;j<d;j++){let v=count(m,cur);seq.push(v);prod*=BigInt(v);pre.push(prod.toString());cur=apply(cur,sig)}if(cur!==mask)throw Error("frame orbit mismatch");sequences.push(seq.join(","));prefixes.push(pre.join(","));countPeriods++}
    for(let s=0;s<(1<<m);s++)for(let t=s;t<(1<<m);t++){if((sequences[s]===sequences[t])!==(prefixes[s]===prefixes[t]))throw Error(`count-residual classification m=${m}`);pairChecks++}
   }
  }
  const sigma=[0,2,1,3],sign=(mask)=>{let s=[];for(let i=0;i<2;i++){s.push(count(4,mask));mask=apply(mask,sigma)}return s};
  const witnesses={"adjacent_01":sign(3),"adjacent_12":sign(6),"adjacent_23":sign(12)};
  if(JSON.stringify(witnesses)!==JSON.stringify({"adjacent_01":[4,6],"adjacent_12":[4,4],"adjacent_23":[4,6]}))throw Error("witness");
  return {schema:"EM_R762AY_EXACT_FINITE_EVIDENCE_V1",scope:"conditional named token-PASS directed cycle, external frame permutation of inventory only; NOT native P000 triadic event admission",all_assertions:"PASS",arithmetic:"exact integer numbers for factorial m<=7 and BigInt horizon products",m_range:"2..7",frame_m_range:"2..5",full_support_cases:fullCases,fully_enumerated_named_permutation_tests:individualPerms,sharp_extrema_cases:extremeCases,frame_permutations_tested:frames,frame_support_orbits_tested:countPeriods,signature_vs_all_horizon_pairs_tested:pairChecks,extrema:extremeRecords,example_sigma:"(1 2) on m=4",example_signatures:witnesses};
}
const evidence=verifyR762AY();
if (typeof process !== "undefined" && require.main===module) console.log(JSON.stringify(evidence,null,2));
module.exports={verifyR762AY};
