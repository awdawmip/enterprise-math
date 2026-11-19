function researchCheck161() {
  const choose=(n,k)=>{if(k<0||k>n)return 0n;let v=1n;for(let i=1;i<=k;i++)v=v*BigInt(n-i+1)/BigInt(i);return v};
  const S=Array.from({length:17},()=>Array(7).fill(0n)); S[0][0]=1n;
  for(let n=1;n<=16;n++)for(let k=1;k<=Math.min(n,6);k++)S[n][k]=S[n-1][k-1]+BigInt(k)*S[n-1][k];
  const fact=k=>{let v=1n;for(let i=2;i<=k;i++)v*=BigInt(i);return v};
  const nativeSurj=n=>{let s=0n;for(let k=0;k<=Math.min(6,n);k++)s+=choose(6,k)*(2n**BigInt(k))*fact(k)*S[n][k];return s};
  const nativeIE=n=>{let s=0n;for(let j=0;j<=6;j++)s+=(j%2===0?1n:-1n)*choose(6,j)*(2n**BigInt(6-j))*(BigInt(6-j)**BigInt(n));return s};
  const pow3=[1,3,9,27,81,243];
  const nativeDP=n=>{let a=new Map([[0,1n]]);for(let step=0;step<n;step++){let b=new Map();const add=(k,v)=>b.set(k,(b.get(k)||0n)+v);for(const [mask,count] of a){for(let i=0;i<6;i++){let p=pow3[i],digit=Math.floor(mask/p)%3;if(!digit){add(mask+p,count);add(mask+2*p,count)}else add(mask,count)}}a=b;}return [...a.values()].reduce((x,y)=>x+y,0n)};
  const positiveMod=(x,m)=>((x%m)+m)%m;
  const layer=(r,k,pattern)=>{const v=Math.abs(k);if(v>r)return 0n;if(r===0)return k===0?1n:0n;if(v===r)return 3n**BigInt(v);let plus=0,minus=0;for(let t=0;t<v;t++){const interfaceIndex=k>=0?t:-(t+1);const sign=pattern[positiveMod(interfaceIndex,pattern.length)]*(k>=0?1:-1);if(sign>0)plus++;else minus++}const c=Math.min(plus,minus),d=Math.abs(plus-minus),h=r-v;const boundary=3n*(2n**BigInt(c+h))*(1n+2n**BigInt(d))-6n;return choose(r,h)*boundary};
  const barlow=(r,pattern)=>{let s=0n;for(let k=-r;k<=r;k++)s+=layer(r,k,pattern);return s};
  const patterns=[];for(let L=1;L<=4;L++)for(let mask=0;mask<(1<<L);mask++)patterns.push(Array.from({length:L},(_,i)=>(mask>>i)&1?1:-1));
  const table=[];
  for(let r=0;r<=16;r++){const d=nativeDP(r),f=nativeSurj(r),g=nativeIE(r);if(d!==f||f!==g)throw Error("Native discrepancy r="+r);if(r<=10)table.push({r, native:d.toString(),fcc:barlow(r,[-1]).toString(),hcp:barlow(r,[-1,1]).toString()})}
  const allAtR2=[...new Set(patterns.map(p=>barlow(2,p).toString()))];
  if(allAtR2.length!==1||allAtR2[0]!=="84"||table[1].native!=="12"||table[2].native!=="132"||table[2].fcc!=="84")throw Error("Barlow witness mismatch");
  return {schema:"X6_UNIT161_FROZEN_P022_NATIVE_BRC_TYPED_CONSUMER_CHECK_V1",date:"2026-11-19",historical_pin:"fd2bcff10ca6e147348b6c1236027fc0d2877df3",task:"RS-X6-LEGACY-PLANE-RECONCILIATION",dimension:6,methods:["native three-state per axis word DP","native Stirling surjection sum","native inclusion-exclusion exponential sum","P022 frozen layer-shell closed formula"],native_validation_radii:"0..16",barlow_all_patterns_length_1_to_4:patterns.length,barlow_r2_totals:allAtR2,table,scope:"P022 derived periodic close-packed contact graph versus signed six-axis primitive native Cell adjacency; unrelated to original R063 benchmark",not_executed:["historical P022 pytest suite","original R063 six-file benchmark"],result:"PASS",review:"UNREVIEWED/NOT_ADMITTED"};
}
const certificate = researchCheck161();
console.log(JSON.stringify(certificate, null, 2));
