"use strict";
// PREFIX-495 exact BRC image rank/unrank and joint finite-state coding.
// Run: node prefix495_rank_certificate.js
function certificate() {
 const N=64, letters="aAbBcCdDeE", fail=(s)=>{throw Error(s)};
 const ok=(b,s)=>{if(!b)fail(s)};
 const eq=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
 const binom=(n,k)=>{if(n<k||k<0)return 0n;let a=1n;for(let i=1;i<=k;i++)a=a*BigInt(n-k+i)/BigInt(i);return a};
 const polygon=m=>BigInt(m+1)*BigInt(3*m+2)/2n;
 const F=Array.from({length:6},()=>Array(N+1).fill(0n));
 const S=Array.from({length:6},()=>Array(N+1).fill(0n));
 for(let t=0;t<=N;t++){F[0][t]=t%2?0n:polygon(t/2);S[0][t]=F[0][t]+(t?S[0][t-1]:0n)}
 for(let j=1;j<=5;j++)for(let t=0;t<=N;t++){
   F[j][t]=F[j-1][t]+(t?2n*S[j-1][t-1]:0n);
   S[j][t]=F[j][t]+(t?S[j][t-1]:0n);
 }
 const pref=(j,t)=>t<0?0n:S[j][t];
 const before=(j,R,v)=>{
   ok(Math.abs(v)<=R&&Number.isInteger(v),"bad y");
   if(v<0)return pref(j,R+v-1);
   if(v===0)return pref(j,R-1);
   return 2n*pref(j,R-1)+F[j][R]-pref(j,R-v);
 };
 const obs=c=>{
   const y=[],p=[];for(let i=0;i<5;i++){y.push(c[2*i]-c[2*i+1]);p.push(Math.min(c[2*i],c[2*i+1]))}
   return {n:c.reduce((a,b)=>a+b,0),y,V:p[1]+2*p[3]+p[4],W:p[2]+p[4]};
 };
 const rank=o=>{
   let {n,y,V,W}=o,R=n,r=0n;ok(n>=0&&n<=N&&y.length===5,"bad n");
   for(let i=0;i<5;i++){ok(Math.abs(y[i])<=R,"bad coordinate");r+=before(4-i,R,y[i]);R-=Math.abs(y[i])}
   ok(R%2===0,"bad parity");const m=R/2;
   ok(W>=0&&W<=m&&V>=0&&V<=2*m-W,"outside polygon");
   r+=BigInt(W)*BigInt(2*m+1)-BigInt(W)*BigInt(W-1)/2n+BigInt(V);
   ok(r<F[5][n],"rank overflow");return r;
 };
 const unrank=(n,r0)=>{
   ok(n>=0&&n<=N&&r0>=0n&&r0<F[5][n],"invalid unrank");let R=n,r=r0,y=[];
   for(let i=0;i<5;i++){let j=4-i,lo=-R,hi=R;
     while(lo<hi){let mid=Math.floor((lo+hi+1)/2);if(before(j,R,mid)<=r)lo=mid;else hi=mid-1}
     let v=lo,b=before(j,R,v);ok(r-b<F[j][R-Math.abs(v)],"empty rank block");
     y.push(v);r-=b;R-=Math.abs(v);
   }
   ok(R%2===0,"bad last parity");let m=R/2,row=w=>BigInt(w)*BigInt(2*m+1)-BigInt(w)*BigInt(w-1)/2n;
   let lo=0,hi=m;while(lo<hi){let mid=Math.floor((lo+hi+1)/2);if(row(mid)<=r)lo=mid;else hi=mid-1}
   let W=lo,V=Number(r-row(W));ok(V>=0&&V<=2*m-W,"bad V");return {n,y,V,W};
 };
 const analytic=n=>[1,2,3,4,2].reduce((x,c,j)=>x+BigInt(c)*binom(n-j+7,7),0n);
 for(let n=0;n<=N;n++)ok(F[5][n]===analytic(n),"closed form n="+n);
 const compositions=[];
 for(let n=0;n<=8;n++){
   let counts=Array(10).fill(0),images=new Map(),used=new Set(),raw=0;
   const rec=(i,left)=>{
     if(i===9){counts[i]=left;raw++;let o=obs(counts),key=o.y+"/"+o.V+"/"+o.W;
       if(!images.has(key)){let r=rank(o);ok(eq(unrank(n,r),o),"roundtrip");
         images.set(key,r);used.add(r.toString())}return;
     }
     for(let x=0;x<=left;x++){counts[i]=x;rec(i+1,left-x)}
   };rec(0,n);
   ok(BigInt(images.size)===F[5][n]&&used.size===images.size,"image mismatch at n="+n);
   compositions.push({n,occupancies:raw,fibers:images.size});
 }
 const kmp=(g,q,ch)=>{
   let s=g.slice(0,q)+ch;for(let i=g.length;i>=0;i--)if(s.endsWith(g.slice(0,i)))return i;fail("KMP");
 };
 const tagStep=(t,ch)=>t!=="N"?t:(ch==="b"||ch==="B"?"B":ch==="c"||ch==="C"?"C":"N");
 const controls=[];
 for(let g of ["aab","aba"]){
   let state=new Map([["0,N",0]]),queue=[[0,"N"]];
   for(let p=0;p<queue.length;p++){let [q,t]=queue[p];for(let ch of letters){
     let q2=kmp(g,q,ch),t2=tagStep(t,ch),key=q2+","+t2;
     if(!state.has(key)){state.set(key,queue.length);queue.push([q2,t2])}
   }}
   let k=state.size;ok(k===(g==="aab"?11:10),"controller size");
   let words=0,appends=0,seen=new Set();
   const walk=(c,q,t,depth)=>{
     let o=obs(c),r=rank(o),idx=state.get(q+","+t),joint=r*BigInt(k)+BigInt(idx);
     ok(idx!==undefined&&Number(joint%BigInt(k))===idx&&eq(unrank(depth,joint/BigInt(k)),o),"joint inverse");
     seen.add(depth+"/"+joint);words++;
     if(depth===4)return;
     for(let h=0;h<10;h++){
       let d=c.slice();d[h]++;let actual=obs(d),y=o.y.slice(),axis=Math.floor(h/2),eps=h%2===0?1:-1;
       let delta=eps*o.y[axis]<0?1:0;c;
       y[axis]+=eps;let alpha=[0,1,0,2,1],beta=[0,0,1,0,1];
       let updated={n:depth+1,y,V:o.V+alpha[axis]*delta,W:o.W+beta[axis]*delta};
       ok(eq(updated,actual)&&rank(updated)===rank(actual),"append closure");
       appends++;walk(d,kmp(g,q,letters[h]),tagStep(t,letters[h]),depth+1);
     }
   };
   walk(Array(10).fill(0),0,"N",0);
   ok(words===11111&&appends===11110,"coverage");
   controls.push({gate:g,states:k,ordered_words:words,append_updates:appends,distinct_joint_codes:seen.size});
 }
 const bits=x=>x<=1n?0:(x-1n).toString(2).length;
 const examples=[];
 for(let n of [8,16,32,64]){
   for(let r of [0n,F[5][n]/3n,F[5][n]/2n,F[5][n]-1n])ok(rank(unrank(n,r))===r,"large inverse");
   let field=5*Math.ceil(Math.log2(2*n+1))+Math.ceil(Math.log2(n+1))+Math.ceil(Math.log2(Math.floor(n/2)+1))+4;
   examples.push({n,fibers:F[5][n].toString(),aab_joint_bits:bits(11n*F[5][n]),field_bits:field});
 }
 return {date:"2026-11-05",scientific_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",precompute_max_n:N,
  compositions,controls,examples,variable_joint_positions_64:(11n*S[5][64]).toString(),status:"ALL_CHECKS_PASS"};
}
console.log(JSON.stringify(certificate(),null,2));
