#!/usr/bin/env node
'use strict';
// R762DU: direct cyclic convolution over F_3[C_(3^a)^3] and independent Lucas comparisons.
// Integer typed arrays, exact arithmetic. Run: node R762DU_VERIFY.js
const BRANCHES=[[0,0,0],[1,0,0],[0,0,1],[1,1,0],[0,1,1],[1,1,1]];
function localTable(power){
  let cur=new Map([['0,0,0',1]]);
  for(let t=0;t<power;t++){
    const next=new Map();
    for(const [key,v] of cur){
      const xyz=key.split(',').map(Number);
      for(const b of BRANCHES){
        const k=xyz.map((u,i)=>u+b[i]).join(',');
        next.set(k,((next.get(k)||0)+v)%3);
      }
    }
    cur=next;
  }
  return cur;
}
const local=[localTable(0),localTable(1),localTable(2)];
function digitCounts(n){
  let n1=0,n2=0;
  while(n){
    const r=n%3;
    if(r===1)n1++;
    if(r===2)n2++;
    n=Math.floor(n/3);
  }
  const support=6**n1*18**n2;
  const difference=6**n1*(-6)**n2;
  return {support,plus:(support+difference)/2,minus:(support-difference)/2};
}
function digitCoefficient(q,n,x,y,z){
  if(n>=q)return 0;
  let out=1;
  while(n||x||y||z){
    const digit=n%3;
    const k=[x%3,y%3,z%3].join(',');
    out=(out*(local[digit].get(k)||0))%3;
    n=Math.floor(n/3);
    x=Math.floor(x/3);y=Math.floor(y/3);z=Math.floor(z/3);
  }
  return out;
}
function verify(q){
  const volume=q*q*q,step=q*q;
  let coefficients=new Uint8Array(volume);
  coefficients[0]=1;
  const shifts=BRANCHES.map(([dx,dy,dz])=>{
    const destinations=new Uint32Array(volume);
    for(let x=0;x<q;x++)for(let y=0;y<q;y++)for(let z=0;z<q;z++){
      const src=x*step+y*q+z;
      destinations[src]=((x+dx)%q)*step+((y+dy)%q)*q+((z+dz)%q);
    }
    return destinations;
  });
  let coefficientChecks=0,residueChecks=0,stepChecks=0,plusMass=0,minusMass=0;
  const sample=[];
  for(let n=0;n<=q;n++){
    let plus=0,minus=0;
    for(let i=0;i<volume;i++){
      const v=coefficients[i];
      plus+=(v===1);minus+=(v===2);residueChecks++;
      if(q<=27 || i%4093===0){
        const x=Math.floor(i/step),y=Math.floor(i/q)%q,z=i%q;
        const want=digitCoefficient(q,n,x,y,z);
        if(v!==want)throw new Error('digit mismatch q='+q+' n='+n+' at '+[x,y,z].join(',')+': '+v+' != '+want);
        coefficientChecks++;
      }
    }
    const want=n<q?digitCounts(n):{support:0,plus:0,minus:0};
    if(plus+minus!==want.support||plus!==want.plus||minus!==want.minus)
      throw new Error('support/sign mismatch q='+q+' n='+n+' got '+plus+'/'+minus+' expected '+want.plus+'/'+want.minus);
    if(n===0||n===1||n===2||n===q-1||n===q)
      sample.push({n,support:plus+minus,plus,minus});
    plusMass+=plus;minusMass+=minus;stepChecks++;
    if(n===q)break;
    const next=new Uint16Array(volume);
    for(let i=0;i<volume;i++){
      const v=coefficients[i];
      if(v)for(const d of shifts)next[d[i]]+=v;
    }
    for(let i=0;i<volume;i++)coefficients[i]=next[i]%3;
  }
  let a=0,divisor=q;
  while(divisor>1){
    if(divisor%3)throw new Error('q is not a power of three');
    divisor/=3;a++;
  }
  if(plusMass!==(25**a+1)/2||minusMass!==(25**a-1)/2)
    throw new Error('aggregated sign count mismatch q='+q);
  return {q,checked_exponents:stepChecks,cyclic_residue_visits:residueChecks,digit_coefficient_comparisons:coefficientChecks,aggregated_plus:plusMass,aggregated_minus:minusMass,samples:sample};
}
function main(){
  if(local[0].size!==1||local[1].size!==6||local[2].size!==19)
    throw new Error('unexpected local table dimensions');
  const signs=[0,1,2].map(d=>{
    const vals=[...local[d].values()];
    return {digit:d,support:vals.filter(x=>x!==0).length,plus:vals.filter(x=>x===1).length,minus:vals.filter(x=>x===2).length};
  });
  const expected=[{digit:0,support:1,plus:1,minus:0},{digit:1,support:6,plus:6,minus:0},{digit:2,support:18,plus:6,minus:12}];
  if(JSON.stringify(signs)!==JSON.stringify(expected))throw new Error('local table mismatch');
  const qs=process.argv.includes('--short')?[3,9,27]:[3,9,27,81];
  const results=qs.map(verify);
  process.stdout.write(JSON.stringify({schema:'R762DU_EXACT_AUTHOR_CHECK_V1',arithmetic:'integer mod 3, no floating point',status:'PASS',local_digit_tables:signs,tests:results},null,2)+'\n');
}
main();
