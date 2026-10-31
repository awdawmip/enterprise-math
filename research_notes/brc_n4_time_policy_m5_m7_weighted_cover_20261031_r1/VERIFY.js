'use strict';
// Exact source-weighted S23 observer certificate, no numerical random sampling.
const verify=function verify(){
 const assert=(c,m)=>{if(!c)throw Error(m)};
 const Q=[[10,10],[20,20],[15,15],[15,15]];
 const P=[[9,11],[5,5],[3,27],[30,30]];
 for(const law of [Q,P]){let leaves=law.flatMap(v=>v.flatMap(w=>[w,w]));assert(leaves.length===16&&leaves.every(w=>w>0)&&leaves.reduce((a,b)=>a+b,0)===240,"positive law")}
 const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
 const source=[0,0,1,2,2,3],slot1=[0,0,1,1],slot2=[0,1,0,2];
 const bit=(x,i)=>(x>>i)&1;
 const time=(a,b,c)=>source.map((s,j)=>!bit(a,slot1[s])?1:(!bit(b,slot2[s])?2:(bit(c,j)?3:4)));
 const key=s=>s.join(",");
 const seen=new Map();let policies=0,checks=0,maxNum=0;
 for(let a=0;a<4;a++)for(let b=0;b<8;b++)for(let c=0;c<64;c++){
  const t=time(a,b,c);
  const laws=M.map(row=>[1,2,3,4].map(v=>row.reduce((acc,w,j)=>acc+(t[j]===v?w:0),0)));
  assert(laws.every(row=>row.reduce((u,v)=>u+v,0)===20),"row normal");
  let omit=-1;for(let h=0;h<4;h++)if(laws.every(row=>3*row[h]<=40)){omit=h;break}
  assert(omit>=0,"heavy time");
  for(const row of laws){
    let num=row.reduce((d,p,h)=>d+Math.abs(3*p-(h===omit?0:20)),0);
    assert(num<=80,"upper bound");maxNum=Math.max(maxNum,num);checks++;
  }
  if(t[0]===t[1]&&t[3]===t[4]){let s=[t[0],t[2],t[3],t[5]];seen.set(key(s),s)}
  policies++;
 }
 assert(policies===2048&&checks===12288&&maxNum===80,"policy census");
 const signatures=[...seen.values()];
 assert(signatures.length===64,"64 signatures");
 const H=[2,3,4],G=[3,4],blocks=[[[1,1,1,1]],[],[],[],[]];
 for(let x of H)for(let y of H){blocks[1].push([1,1,x,y]);blocks[2].push([x,y,1,1]);blocks[3].push([2,x,2,y]);}
 for(let x of G)for(let u of H)for(let y of G)for(let v of H)blocks[4].push([x,u,y,v]);
 assert(JSON.stringify(blocks.map(b=>b.length))==="[1,9,9,9,36]","class sizes");
 const weights=[16,5,5,6,2],weight=new Map();
 for(let j=0;j<5;j++)for(let s of blocks[j]){assert(!weight.has(key(s)),"class overlap");weight.set(key(s),weights[j])}
 assert(weight.size===64&&signatures.every(s=>weight.has(key(s))),"class union");
 const total=[...weight.values()].reduce((a,b)=>a+b,0);
 assert(total===232,"weight sum");
 const pairs=[];for(let a=1;a<=4;a++)for(let b=a+1;b<=4;b++)pairs.push([a,b]);
 const nh=X=>X.filter(x=>H.includes(x)).length,ng=X=>X.filter(x=>G.includes(x)).length;
 let max=0,countMax=0,count=0;
 for(let A of pairs)for(let B of pairs)for(let C of pairs)for(let D of pairs){
  const w=signatures.reduce((a,s)=>a+(A.includes(s[0])&&B.includes(s[1])&&C.includes(s[2])&&D.includes(s[3])?weight.get(key(s)):0),0);
  const f=16*(A.includes(1)&&B.includes(1)&&C.includes(1)&&D.includes(1)?1:0)
        +5*(A.includes(1)&&B.includes(1)?1:0)*nh(C)*nh(D)
        +5*nh(A)*nh(B)*(C.includes(1)&&D.includes(1)?1:0)
        +6*(A.includes(2)&&C.includes(2)?1:0)*nh(B)*nh(D)
        +2*ng(A)*nh(B)*ng(C)*nh(D);
  assert(w===f,"block sum identity");
  if(w>max){max=w;countMax=1}else if(w===max)countMax++;
  count++;
 }
 assert(count===1296&&max===32&&countMax===90&&total>7*max,"cover certificate");
 const wt=time(3,5,27);
 assert(wt[0]===3&&wt[2]===2&&wt[5]===4,"single-state 3-support witness");
 return {status:"PASS_BRC_N4_TIME_POLICY_M5_M7_WEIGHTED_COVER_20261031",arithmetic:"exact integer",laws:2,positive_leaves_per_law:16,prepared_rows:6,deterministic_policies:policies,upper_bound_checks:checks,max_upper_TV:"2/3",genuine_signatures:signatures.length,block_sizes:blocks.map(x=>x.length),block_weights:weights,total_weight:total,boxes:count,max_box_weight:max,boxes_at_max:countMax,minimum_labels_for_error_strictly_below_2_over_3_at_least:8,one_code_all_m_at_least_4:"2/3",theorem:"R_(k,m)=2/3 for all k>=1 and 4<=m<=7 in lawful S23 time-only model",scope:"full arbitrary randomized S23 upper via analytic predecessor; exact finite deterministic lower; S2/native X6 not asserted"};
};
console.log(JSON.stringify(verify(),null,2));
