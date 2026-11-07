"use strict";
function validate(){
 const C=(n,k)=>{if(n<0||k<0||k>n)return 0n;let z=1n;for(let j=1;j<=k;j++)z=z*BigInt(n-j+1)/BigInt(j);return z;};
 const norm=a=>{while(a.length>1&&a[a.length-1]===0n)a.pop();return a;};
 const add=(a,b)=>{const r=Array(Math.max(a.length,b.length)).fill(0n);for(let i=0;i<a.length;i++)r[i]+=a[i];for(let i=0;i<b.length;i++)r[i]+=b[i];return norm(r);};
 const mul=(a,b)=>{const r=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]+=a[i]*b[j];return norm(r);};
 const scale=(a,x)=>norm(a.map(v=>v*x));
 const coeff=(a,i)=>(i>=0&&i<a.length)?a[i]:0n;
 const mono=(n,v,shift)=>n<0?[0n]:[...Array(shift).fill(0n),...Array.from({length:n+1},(_,h)=>v*C(n,h))];
 const K=i=>{const d=[-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)];let z=[0n];for(let j=1;j<=4;j++)if(d[j-1]!==0n)z=add(z,mono(i+1-j,-d[j-1],i-1));return z;};
 const J=s=>{let z=[0n];for(const [v,n] of [[-C(3,s-1),s],[-C(6,s-1),s-1],[C(8,s-2),s-2]])if(v!==0n)z=add(z,mono(n,v,s));return z;};
 const eq=(a,b)=>JSON.stringify(a.map(String))===JSON.stringify(b.map(String));
 const fail=(b,msg)=>{if(!b)throw Error(msg);};
 const KS=Array.from({length:13},(_,i)=>i?K(i):[0n]),B0=[1n,1n],top=8;
 fail(eq(KS[1],[2n,3n])&&eq(KS[2],[0n,-1n,4n,4n])&&coeff(KS[3],2)===-8n,"frozen K mismatch");
 const U=[new Map([["",B0]])],B=[B0];let expanded=1,augChecks=0,parikhChecks=0;
 const parse=w=>w===""?[]:w.split(",").map(Number);
 for(let s=1;s<=top;s++){
  const row=new Map([["",J(s)]]);let b=J(s);
  for(let i=1;i<=Math.min(s,12);i++){
   b=add(b,mul(KS[i],B[s-i]));
   for(const [word,p] of U[s-i]){
    const key=String(i)+(word?","+word:"");
    row.set(key,add(row.get(key)||[0n],mul(KS[i],p)));
   }
  }
  U.push(row);B.push(b);expanded+=row.size;
  let a=[0n];for(const p of row.values())a=add(a,p);
  fail(eq(a,b),"augmentation s="+s);augChecks++;
  const groups=new Map();
  for(const [word,p] of row){
   const m=Array(12).fill(0);for(const i of parse(word))m[i-1]++;
   const key=m.join(",");groups.set(key,add(groups.get(key)||[0n],p));
  }
  for(const [key,p] of groups){
   const m=key.split(",").map(Number),steps=m.reduce((a,b)=>a+b,0),weight=m.reduce((a,b,i)=>a+(i+1)*b,0),r=s-weight;
   fail(r>=0,"word weight overflow");let ways=1n,n=steps;
   for(const v of m){ways*=C(n,v);n-=v;}
   let expected=(r===0?B0:J(r));
   for(let i=1;i<=12;i++)for(let j=0;j<m[i-1];j++)expected=mul(expected,KS[i]);
   fail(eq(p,scale(expected,ways)),"parikh s="+s+" m="+key);parikhChecks++;
  }
 }
 const newState=g=>{const a=[B0];for(let s=1;s<=top;s++){let b=J(s);for(let i=1;i<=Math.min(s,12);i++){const v=g(s,i);if(v!==0n)b=add(b,scale(mul(KS[i],a[s-i]),v));}a.push(b);}return a;};
 let typeChecks=0;
 for(const u1 of [-1,0,1,2])for(const u2 of [-1,0,1,2])for(const u3 of [-1,0,1,2]){
  const u=[1n,BigInt(u1),BigInt(u2),BigInt(u3)],states=newState((s,i)=>i<=3?u[i]:1n);
  for(let s=0;s<=top;s++){
   let z=[0n];for(const [word,p] of U[s]){let a=1n;for(const i of parse(word))a*=i<=3?u[i]:1n;z=add(z,scale(p,a));}
   fail(eq(z,states[s]),"type eval "+[s,u1,u2,u3]);typeChecks++;
  }
 }
 const address=[[3,1],[3,2],[2,1],[2,2]];let levelChecks=0;
 for(let mask=0;mask<16;mask++){
  const g=(s,i)=>{const pos=address.findIndex(v=>v[0]===s&&v[1]===i);return pos<0?1n:BigInt((mask>>pos)&1);};
  const st=newState(g);
  for(let s=0;s<=top;s++){
   let z=[0n];for(const [word,p] of U[s]){let a=1n,level=s;for(const i of parse(word)){a*=g(level,i);level-=i;}z=add(z,scale(p,a));}
   fail(eq(z,st[s]),"level eval "+s+" mask "+mask);levelChecks++;
  }
 }
 const D=(q,k)=>{let v=0n;for(let w=0;w<=k;w++)v+=((k-w)%2?-1n:1n)*C(k,w)*2n**BigInt(q-w)*coeff(B[q+w],q);return v;};
 const lifted=(q,k)=>{const v=new Map();for(let w=0;w<=k;w++){const fac=((k-w)%2?-1n:1n)*C(k,w)*2n**BigInt(q-w);for(const [word,p] of U[q+w])v.set(word,(v.get(word)||0n)+fac*coeff(p,q));}return v;};
 let dChecks=0;
 for(let q=0;q<=4;q++)for(let k=0;k<=q;k++){const v=lifted(q,k);let sum=0n;for(const c of v.values())sum+=c;fail(sum===D(q,k),"D lift mismatch "+[q,k]);dChecks++;}
 const dw=lifted(2,1);
 fail(D(2,1)===60n&&dw.get("1,2")===6n&&dw.get("2,1")===6n,"ordered D witness");
 fail(eq(U[3].get("1,2"),U[3].get("2,1"))&&coeff(U[3].get("1,2"),2)===3n,"order pair witness");
 return {schema:"R616_SIGNED_BRC_GRADED_WORD_LIFT_V1",scientific_pin:"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",source_path:"research_notes/r388_signed_k3_corank16_20261029_emr3/r388_exact.py",source_blob:"7fa7a762f758b30c6090468ac43487daa34abad8",theta:"0",arithmetic:"exact BigInt integers, no floating-point BRC update",scope:"auxiliary signed K/J -> graded noncommutative word-source lift and D readout; no native X6 correspondence",verified_levels:"s=0..8",branch_count:12,word_terms:expanded,augmentation_checks:augChecks,parikh_aggregation_checks:parikhChecks,formal_type_evaluation_checks:typeChecks,layer_address_gate_checks:levelChecks,D_lift_checks:dChecks,D_2_1:String(D(2,1)),ordered_D_2_1:{"1,2":String(dw.get("1,2")),"2,1":String(dw.get("2,1"))},nonunit_K1:"2+3t",endpoint_group_factorization:"OBSTRUCTED under the multiplicative group-homomorphism hypothesis",native_bridge:"UNVERIFIED",terminal_marker:"R616_EXACT_GRADED_WORD_LIFT_PASS"};
}
if(typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs"),out=validate();
 fs.writeFileSync("R616_EVIDENCE.json",JSON.stringify(out,null,2)+"\n","utf8");
 console.log(out.terminal_marker);
 console.log("counts",out.word_terms,out.augmentation_checks,out.parikh_aggregation_checks,out.formal_type_evaluation_checks,out.layer_address_gate_checks,out.D_lift_checks);
}
