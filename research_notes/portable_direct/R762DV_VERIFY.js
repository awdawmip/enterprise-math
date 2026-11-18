#!/usr/bin/env node
'use strict';
// R762DV: independent cyclic ring convolution modulo 9 and full first-layer quotient check.
const B=[[0,0,0],[1,0,0],[0,0,1],[1,1,0],[0,1,1],[1,1,1]];
function make(q){
  const len=q**3,step=q*q;
  const shifts=B.map(([dx,dy,dz])=>{
    const map=new Uint32Array(len);
    for(let x=0;x<q;x++)for(let y=0;y<q;y++)for(let z=0;z<q;z++){
      const i=x*step+y*q+z;
      map[i]=((x+dx)%q)*step+((y+dy)%q)*q+(z+dz)%q;
    }
    return map;
  });
  return {len,shifts};
}
function multiply(a,shape,mod){
  const tmp=new Uint16Array(shape.len);
  for(let i=0;i<shape.len;i++){
    const v=a[i];if(v)for(const sh of shape.shifts)tmp[sh[i]]+=v;
  }
  const out=new Uint8Array(shape.len);
  for(let i=0;i<shape.len;i++)out[i]=tmp[i]%mod;
  return out;
}
function verify(q){
  const d=q/3,shape=make(q),small=make(d);
  const base=[];
  let a=new Uint8Array(shape.len),b=new Uint8Array(small.len);
  a[0]=1;b[0]=1;
  for(let r=0;r<d;r++){base.push(b);b=multiply(b,small,3);}
  let checked=0,firstLayerNonzero=0;
  const samples=[];
  for(let n=0;n<q+d;n++){
    if(n>=q){
      const r=n-q;let plus=0,minus=0;
      for(let x=0;x<q;x++)for(let y=0;y<q;y++)for(let z=0;z<q;z++){
        const idx=x*q*q+y*q+z;
        const observed=a[idx];
        if(observed%3)throw new Error('undivided count '+[q,n,idx].join(','));
        const quotient=observed/3;
        const expected=(3-base[r][(x%d)*d*d+(y%d)*d+(z%d)])%3;
        if(quotient!==expected)throw new Error('first-layer mismatch '+[q,n,idx].join(','));
        plus+=(quotient===1);minus+=(quotient===2);checked++;
      }
      firstLayerNonzero+=plus+minus;
      if(r===0||r===d-1)samples.push({n,nonzero:plus+minus,plus,minus});
    }
    if(n+1<q+d)a=multiply(a,shape,9);
  }
  return {q,d,range:'Q<=n<Q+d',tested_exponents:d,first_layer_coefficient_checks:checked,first_layer_nonzero_total:firstLayerNonzero,samples};
}
const qs=process.argv.includes('--short')?[3,9,27]:[3,9,27,81];
const tests=qs.map(verify);
console.log(JSON.stringify({schema:'R762DV_FIRST_LAYER_EXACT_AUTHOR_CHECK_V1',status:'PASS',arithmetic:'integer cyclic convolution modulo 9 and independent modulo 3 quotient',tests},null,2));
