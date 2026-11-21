#!/usr/bin/env node
'use strict';
// Exact modular verifier for EC49FWE: generated from the executed function body.
function verify(){
  "use strict";
  const mod=(x,m)=>((x%m)+m)%m;
  const inv=(a,p)=>{for(let j=1;j<p;j++)if(mod(a*j,p)===1)return j;throw Error("inverse absent")};
  const pow=(a,e,p)=>{let t=1;for(let j=0;j<e;j++)t=mod(t*a,p);return t};
  const gcd=(a,b)=>{while(b){let t=a%b;a=b;b=t}return a};
  const U=mod(4822040484*inv(mod(8132285009,11),11),11);
  const gamma=mod(141024*inv(mod(1653649,11),11),11);
  const I=inv(mod(637,11),11),C=mod(-3*I,11),D=mod(U*gamma,11);
  if(U!==4||gamma!==6||C!==3||D!==2)throw Error("BRC16943 constants");
  const rows=Array.from({length:11},(_,z)=>{
    const l=mod((637-3*z)*I,11),r=mod(U*(1+gamma*z),11);
    return {z,l,r,A:mod(1-(1-z)*l,11),B:mod(1-(1-z)*r,11)};
  });
  const P=new Set();
  for(let h=0;h<10;h++)for(let n=0;n<10;n++){
    const nonconfluent=rows.filter(x=>x.z!==3).every(x=>mod(pow(x.A,h,11)*pow(x.l,n,11)-pow(x.B,h,11)*pow(x.r,n,11),11)!==0);
    if(nonconfluent&&mod(pow(C,h+n,11)-pow(D,h+n,11),11)!==0)P.add(h*10+n);
  }
  if(P.size!==44)throw Error("P10 size");
  const fibers={"00":[3],"01":[0,3,4,"inf"],"10":[2,3,4,"inf"],"11":[2,3]};
  const proj=(h,n)=>{
    h=mod(h,5);n=mod(n,5);
    return h===0?(n===0?"zero":"inf"):mod(n*inv(h,5),5);
  };
  for(let h=0;h<10;h++)for(let n=0;n<10;n++){
    const truth=P.has(h*10+n);
    const predicted=fibers[`${h%2}${n%2}`].includes(proj(h,n));
    if(truth!==predicted)throw Error(`fiber discrepancy ${h},${n}`);
  }
  for(const u of [1,3,7,9])for(let h=0;h<10;h++)for(let n=0;n<10;n++)
    if(P.has(h*10+n)!==P.has(10*mod(u*h,10)+mod(u*n,10)))throw Error("unit symmetry");
  const phi=(s,q)=>s==="inf"?q:q==="inf"?0:inv(mod(q-s,5),5);
  const subset=(tag,s)=>new Set(fibers[tag].filter(q=>q!==s).map(q=>phi(s,q)));
  const sym=(X,Y)=>{let count=0;for(const x of X)if(!Y.has(x))count++;for(const y of Y)if(!X.has(y))count++;return count};
  const reflected=(X,c,m)=>new Set([...X].map(x=>mod(c-x,m)));
  const exact=(X,Y)=>{
    const even=[],odd=[];
    for(let c=0;c<5;c++){
      even.push(sym(X,reflected(X,c,5))+sym(Y,reflected(Y,c,5)));
      odd.push(2*sym(X,reflected(Y,c,5)));
    }
    const minimum=Math.min(...even,...odd);
    return [minimum,even.filter(v=>v===minimum).length,odd.filter(v=>v===minimum).length];
  };
  const pairs={"10":["10","01"],"01":["10","11"],"11":["01","11"]};
  const lambdas=[0,1,2,3,4,"inf"];
  const expected={
    "10":[[2,1,0],[2,2,2],[0,0,1],[2,2,2],[2,1,0],[0,0,1]],
    "01":[[2,2,2],[2,1,0],[2,1,0],[2,1,0],[2,1,0],[2,2,2]],
    "11":[[2,1,1],[2,1,1],[2,2,0],[2,2,0],[2,2,0],[2,0,2]]
  };
  const table={};
  for(const e of Object.keys(pairs)){
    table[e]={};
    for(let j=0;j<6;j++){
      const lambda=lambdas[j],s=lambda==="inf"?"inf":mod(lambda-1,5);
      const X=subset(pairs[e][0],s),Y=subset(pairs[e][1],s);
      const got=exact(X,Y);
      if(JSON.stringify(got)!==JSON.stringify(expected[e][j]))throw Error(`parity table ${e},${lambda}`);
      table[e][String(lambda)]={defect:got[0],even_minimizers:got[1],odd_minimizers:got[2]};
    }
  }
  const originalMask=(a,b)=>{
    let anchor=null;
    outer:for(let h=0;h<10;h++)for(let n=0;n<10;n++)
      if(mod((b-a)*h-a*n+1,10)===0){anchor=[h,n];break outer}
    if(!anchor)throw Error("affine anchor");
    const S=new Set();
    for(let t=0;t<10;t++)if(P.has(10*mod(anchor[0]+a*t,10)+mod(anchor[1]+(b-a)*t,10)))S.add(t);
    return S;
  };
  const histogram={}, total={directions:0,crt_classes:18};
  for(let a=0;a<10;a++)for(let b=0;b<10;b++){
    if(gcd(gcd(a,b),10)!==1)continue;
    total.directions++;
    const S=originalMask(a,b);
    const dvals=Array.from({length:10},(_,c)=>sym(S,reflected(S,c,10)));
    const d=Math.min(...dvals),e=dvals.filter((v,c)=>c%2===0&&v===d).length,o=dvals.filter((v,c)=>c%2===1&&v===d).length;
    const lambda=a%5===0?"inf":String(mod(b*inv(mod(a,5),5),5));
    const exp=table[`${a%2}${b%2}`][lambda];
    if(d!==exp.defect||e!==exp.even_minimizers||o!==exp.odd_minimizers)throw Error(`direction ${a},${b}`);
    const key=`D${d}_E${e}_O${o}`;histogram[key]=(histogram[key]||0)+1;
  }
  const expectedHist={D0_E0_O1:8,D2_E1_O0:24,D2_E2_O2:16,D2_E2_O0:12,D2_E1_O1:8,D2_E0_O2:4};
  if(total.directions!==72||JSON.stringify(Object.keys(histogram).sort().map(k=>[k,histogram[k]]))!==JSON.stringify(Object.keys(expectedHist).sort().map(k=>[k,expectedHist[k]])))throw Error("census");
  return {status:"ALL PASS",scientific_pin:"BRC16943",model_scope:"frozen nonconfluent mod-10 auxiliary P10 only",arithmetic:"exact finite integers",P10_cells:P.size,fiber_check:100,unit_covariance_check:400,projective_classes:18,primitive_direction_checks:total.directions,fibers,table,histogram,limitations:"Not a full mod-11 certificate, Farey global bound, native X6 realization, formal proof checker or independent review."};
}
console.log(JSON.stringify(verify(),null,2));
