#!/usr/bin/env node
// PREFIX-453 executable exact integer certificate. Node.js; no packages.
function runCertificate(){
  const Q=3,N=4,P=1000003,DIM=6,logs=[];
  const check=(v,msg)=>{if(!v)throw Error(msg)};
  const coords=(d,m)=>m===1?Array.from({length:d+1},(_,i)=>[i]):Array.from({length:d+1},(_,i)=>coords(d-i,m-1).map(a=>[i,...a])).flat();
  const idx=coords(2,6).sort((a,b)=>a.reduce((p,x)=>p+x,0)-b.reduce((p,x)=>p+x,0)||cmp(a,b));
  function cmp(a,b){for(let i=0;i<a.length;i++){if(a[i]!==b[i])return a[i]-b[i]}return 0}
  check(idx.length===28,"dimension");
  const key=(r,x)=>JSON.stringify([r,x]);
  const parse=k=>JSON.parse(k);
  const val=(x,a)=>a.reduce((v,t,i)=>v*x[i]**t,1);
  const vec=x=>idx.map(a=>val(x,a));
  const canonical=(r,a)=>[2-2*r+a[0],a[1],a[2],a[3],a[4],-2+a.slice(0,5).reduce((p,x)=>p+x,0)+2*a[5]];
  const selected=new Map();
  for(let r=0;r<Q;r++)for(let a of idx){
    const k=key(r,canonical(r,a));
    check(!selected.has(k),"duplicate canonical state");
    selected.set(k,1);
  }
  check(selected.size===84,"84 source points");
  const mod=v=>((v%P)+P)%P;
  const pow=(x,n)=>{let r=1;for(;n>0;n=Math.floor(n/2)){if(n%2)r=mod(r*x);x=mod(x*x)}return r};
  function determinant(A){
    A=A.map(row=>row.map(mod)); const n=A.length;let det=1;
    for(let j=0;j<n;j++){
      let k=j;while(k<n&&A[k][j]===0)k++;
      if(k===n)return 0;
      if(k!==j){let t=A[j];A[j]=A[k];A[k]=t;det=mod(-det)}
      const p=A[j][j];det=mod(det*p);const inv=pow(p,P-2);
      for(let i=j+1;i<n;i++)if(A[i][j]!==0){
        const scale=mod(A[i][j]*inv);
        for(let t=j+1;t<n;t++)A[i][t]=mod(A[i][t]-scale*A[j][t]);
        A[i][j]=0;
      }
    }
    return det;
  }
  for(let r=0;r<Q;r++){
    const points=idx.map(a=>canonical(r,a));
    const det=determinant(points.map(vec));
    check(det!==0,"dictionary rank failure");
    logs.push(`PASS full-rank 28-point native sector ${r}: determinant_mod_${P}=${det}`);
  }
  function allWords(n){
    let h=new Map([[key(0,[0,0,0,0,0,0]),1]]);
    for(let t=0;t<n;t++){
      const next=new Map();
      for(let [k,mass] of h){
        const [r,x]=parse(k);
        for(let axis=0;axis<DIM;axis++)for(let sign of [-1,1]){
          const y=[...x];y[axis]+=sign;
          const s=(r+(axis===0&&sign===-1?1:0))%Q;
          const z=key(s,y);next.set(z,(next.get(z)||0)+mass);
        }
      }h=next;
    }
    let sum=0;for(let w of h.values())sum+=w;
    check(sum===12**n,"native word conservation");
    return h;
  }
  const dense=allWords(N);
  check(dense.size===1059,"joint support mismatch");
  check([...selected.keys()].every(k=>dense.has(k)),"canonical word unreachable");
  logs.push("PASS native X6 q=3 N=4, 12^4=20736 words, 1059 reachable joint bins, canonical 84 legal bins");
  const plus=[
    [[-2,-2,0,0,0,0],1],
    [[-2,1,0,0,0,-1],4],
    [[-2,1,0,0,0,1],4]
  ];
  const minus=[
    [[-2,0,0,0,0,-2],1],
    [[-2,0,0,0,0,0],4],
    [[-2,0,0,0,0,2],1],
    [[-2,2,0,0,0,0],3]
  ];
  function obs(h){let res=Array.from({length:Q},()=>Array(28).fill(0));for(let [k,w] of h){const [r,x]=parse(k),v=vec(x);for(let j=0;j<28;j++)res[r][j]+=w*v[j]}return res}
  const hplus=new Map(plus.map(([x,w])=>[key(2,x),w]));
  const hminus=new Map(minus.map(([x,w])=>[key(2,x),w]));
  check(plus.reduce((s,x)=>s+x[1],0)===9&&minus.reduce((s,x)=>s+x[1],0)===9,"mass mismatch");
  check(JSON.stringify(obs(hplus))===JSON.stringify(obs(hminus)),"quadratic observer differs");
  for(let H of [hplus,hminus])for(let[k,w]of H)check(dense.get(k)>=w,"not enough distinct ordered native paths");
  const cubic=h=>[...h].reduce((s,[k,w])=>s+w*parse(k)[1][1]**3,0);
  check(cubic(hplus)===0&&cubic(hminus)===24,"cubic separator");
  logs.push("PASS 9-vs-9 distinct unit-weight native word certificate, all 84 quadratic entries equal, cubic x2^3 = 0 vs 24");
  const ordered=[...selected.keys()].sort((a,b)=>{const [r,x]=parse(a),[s,y]=parse(b);return r-s||cmp(x,y)});
  const sorted=h=>[...h].sort((a,b)=>{const [r,x]=parse(a[0]),[s,y]=parse(b[0]);return r-s||cmp(x,y)});
  function histBytes(h,n=N){const bins=sorted(h).map(([k,w])=>{const[r,x]=parse(k);return [r,x,w,1]});return JSON.stringify({bins,codec:"HIST",n,q:Q}).length}
  function momentBytes(h,n=N){const moments=obs(h).map((row,r)=>[r,row.map(w=>[w,1])]);return JSON.stringify({codec:"MOMENT2_AFFINE",moments,n,q:Q}).length}
  const sample=(z)=>new Map(ordered.slice(0,z).map(k=>[k,1]));
  for(let [label,h] of [["single",sample(1)],["four",sample(4)],["twenty_eight",sample(28)],["eighty_four",selected],["full_dense",dense]]){
    const a=histBytes(h),b=momentBytes(h);
    logs.push(`BYTES ${label}: bins=${h.size}, hist=${a}, moment=${b}, chosen=${a<=b?"HIST":"MOMENT2_AFFINE"}`);
  }
  const lengths=Array.from({length:84},(_,i)=>{let h=sample(i+1);return [histBytes(h),momentBytes(h)]});
  const cross=lengths.findIndex(([a,b])=>b<a)+1;
  check(cross>1&&lengths.slice(cross-1).every(([a,b])=>b<a),"crossover not monotone in this family");
  logs.push(`PASS 84-prefix exact JSON crossover at ${cross} bins, previous=${lengths[cross-2]}, current=${lengths[cross-1]}`);
  for(let n=2;n<=6;n++){
    const h=allWords(n);
    logs.push(`BYTES dense_length_${n}: bins=${h.size}, hist=${histBytes(h,n)}, moment=${momentBytes(h,n)}`);
  }
  logs.push("PASS PREFIX-453 JS exact integer certificate");
  return logs;
}
for (const line of runCertificate()) console.log(line);
