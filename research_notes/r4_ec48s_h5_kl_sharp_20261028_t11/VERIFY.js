"use strict";
// EC48S exact support and positive-rational witness checker; run: node VERIFY.js
const verify=function verify(){
 const gcd=(a,b)=>b?gcd(b,a%b):Math.abs(a),fmt=(a,b)=>{let g=gcd(a,b);return b/g===1?String(a/g):`${a/g}/${b/g}`};
 const witness=l=>{
  const s=Math.ceil(Math.log2(l)),muD=4*l*s,words=Array.from({length:l},(_,h)=>Array.from({length:s},(_,j)=>(h>>(s-1-j))&1)),B=words.flat().reduce((a,b)=>a+b,0);
  let p=0,q=0,leaves=0;for(const w of words){p+=8*s+4*s;q+=4*s+8*s;leaves+=2;for(const bit of w){p+=4;q+=4;leaves+=bit?2:1}}if(p!==16*l*s||q!==16*l*s||leaves!==2*l+l*s+B)throw Error("source-mass mismatch");
  let sc=64*l*l*s, score=8*l*(2*s*l+B)-(16*l*s+B);
  return {l,s,B,mu:fmt(1,muD),leaf_count:leaves,p_total:fmt(p,16*l*s),q_total:fmt(q,16*l*s),alpha:fmt(8*l*s+3*B,16*l*s),beta:fmt(4*l*s+B,16*l*s),tau_full_each:fmt(16*l*s+B,4*l*s),tau_m_each:fmt(16*l*s+B+1,4*l*s),c:fmt(1,32*l),v_full:fmt(score,sc),v_m:fmt(score-1,sc),gap:fmt(1,sc)};
 };
 const cases=[[2,[0,0,1]],[3,[0,0,1,2]],[2,[0,1]],[4,[0,1,2,3]]].map(([k,group])=>{
   let l=group.length,s=Math.ceil(Math.log2(l)),m=l-1,words=Array.from({length:l},(_,h)=>Array.from({length:s},(_,j)=>(h>>(s-1-j))&1));
   let bestF=-1e50,bestM=-1e50,nF=0,nM=0;
   for(let gm=0;gm<(1<<k);gm++){
    let ng=group.reduce((sum,g)=>sum+((gm>>g)&1),0),tb=8*l*s+4*s*ng;
    for(let ac=0;ac<(1<<l);ac++){
     let on=[];for(let h=0;h<l;h++)if((gm>>group[h]&1)&&(ac>>h&1))on.push(h);
     let a0=2*s*on.length,t0=tb+4*s*on.length;
     for(let mask=0;mask<(1<<(l*s));mask++){
      let a=a0,t=t0;for(let h of on)for(let j=0;j<s;j++)if(mask>>(h*s+j)&1){t++;a+=words[h][j]}
      let z=8*l*a-t;if(z>bestF)bestF=z;nF++;
     }
    }
    for(let code=0;code<Math.pow(m+1,l);code++){
      let x=code,ids=[];for(let h=0;h<l;h++){ids.push(x%(m+1)-1);x=Math.floor(x/(m+1))}
      let on=[];for(let h=0;h<l;h++)if((gm>>group[h]&1)&&ids[h]>=0)on.push(h);
      let a0=2*s*on.length,t0=tb+4*s*on.length;
      for(let mask=0;mask<(1<<(m*s));mask++){
        let a=a0,t=t0;for(let h of on)for(let j=0;j<s;j++)if(mask>>(ids[h]*s+j)&1){t++;a+=words[h][j]}
        let z=8*l*a-t;if(z>bestM)bestM=z;nM++;
      }
    }
   }
   let rootStop=-4*l*s;bestF=Math.max(bestF,rootStop);bestM=Math.max(bestM,rootStop);
   const B=words.flat().reduce((a,b)=>a+b,0),expected=8*l*(2*s*l+B)-(16*l*s+B),scale=64*l*l*s;
   if(bestF!==expected||bestM!==expected-1)throw Error(`exact maximization mismatch k=${k},l=${l}: ${bestF},${bestM},${expected}`);
   return {k,l,groups:group,m,full_normal_forms:nF,compressed_normal_forms:nM,relaxed_early_group_masks_when_k_eq_l:k===l,V_full:fmt(bestF,scale),V_m:fmt(bestM,scale),gap:fmt(1,scale),assertions:"PASS"};
 });
 return {schema:"ENTERPRISE_MATH_EC48S_EXACT_V1",arithmetic:"integer exhaustive scores; rational fraction outputs reduced by GCD",test_cost:"c=1/(32*l)",normal_form_extrema:cases,normalizations_and_RAW_vectors:[2,3,4,5,8,11].map(witness),analytic_cost_range:"0<c<=1/(32*l)",analytic_gap:"c/(2*l*ceil(log2(l)))",remark:"k=l compressed group early-stop masks form an upper-bound relaxation; explicit merged-parent witness attains it",status:"AUTHOR_PROVED / EXACT_COMPUTATION_PASS / UNREVIEWED / NOT_ADMITTED"};
};
console.log(JSON.stringify(verify(),null,2));
