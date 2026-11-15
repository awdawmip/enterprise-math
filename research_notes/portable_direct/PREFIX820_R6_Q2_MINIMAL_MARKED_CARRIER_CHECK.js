/* PREFIX-820 — exact named-state and eight-coordinate tests; run: node PREFIX820_R6_Q2_MINIMAL_MARKED_CARRIER_CHECK.js */
const result = (function verify(){
 const P=1009,bc=x=>{let c=0;while(x){c+=x&1;x>>=1;}return c;};
 const rank=rows=>{
  let a=rows.map(r=>r.map(v=>((Number(v)%P)+P)%P)),h=0,n=a[0].length;
  const pow=(u,v)=>{let w=1;while(v){if(v&1)w=w*u%P;u=u*u%P;v=Math.floor(v/2);}return w;};
  for(let j=0;j<n&&h<a.length;j++){
   let k=h;while(k<a.length&&!a[k][j])k++;
   if(k===a.length)continue;
   [a[k],a[h]]=[a[h],a[k]];
   let inv=pow(a[h][j],P-2);
   for(let z=j;z<n;z++)a[h][z]=a[h][z]*inv%P;
   for(let i=0;i<a.length;i++)if(i!==h&&a[i][j]){
    let f=a[i][j];for(let z=j;z<n;z++)a[i][z]=((a[i][z]-f*a[h][z])%P+P)%P;
   }h++;
  }return h;
 };
 const ix=[];for(let z=0;z<=1;z++)for(let k=0;k<=2-z;k++)for(let h=0;h<=k;h++)ix.push([z,k,h]);
 const key=(z,k,h)=>ix.findIndex(t=>t[0]===z&&t[1]===k&&t[2]===h);
 const operator=(a,b)=>{
  let T=Array.from({length:9},()=>Array(9).fill(0)),C=Array.from({length:3},()=>Array(9).fill(0));
  ix.forEach(([z,k,h],j)=>{if(h>0)T[key(z,k-1,h-1)][j]+=h;if(z===1)T[key(0,k,h)][j]+=b;if(z===0&&k<2)T[key(1,k,h)][j]+=a;if(h===0)C[k+z][j]=1;});
  return [T,C];
 };
 const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,v,i)=>s+v*B[i][j],0)));
 const orank=(a,b)=>{
  let [T,C]=operator(a,b),O=[],E=C;
  for(let h=0;h<9;h++){O.push(...E);E=mm(E,T);}
  return rank(O);
 };
 const full=(mask,beta)=>{
  let z=(mask&1)?1:0,other=[];for(let i=1;i<beta.length;i++)if(mask&(1<<i))other.push(i);
  let k=other.length,row=Array(9).fill(0);
  row[key(z,k,0)]=1;if(k>=1)row[key(z,k,1)]=other.reduce((s,i)=>s+beta[i],0);
  if(k>=2)row[key(z,k,2)]=beta[other[0]]*beta[other[1]];
  return row;
 };
 const basis=(mask,beta)=>{
  let marked=(mask&1)!==0,other=[];for(let i=1;i<beta.length;i++)if(mask&(1<<i))other.push(i);
  let k=other.length,b=BigInt(beta[0]),s=other.reduce((x,i)=>x+BigInt(beta[i]),0n);
  let x=!marked&&k===0?1n:0n,y=!marked&&k===1?1n:0n,z=!marked&&k===1?s:0n;
  let u=(!marked&&k===2?1n:0n)+(marked&&k===1?1n:0n);
  let v=(!marked&&k===2?s:0n)+(marked&&k===1?b:0n);
  let w=!marked&&k===2?BigInt(beta[other[0]])*BigInt(beta[other[1]]):0n;
  let p=marked&&k===0?1n:0n,r=marked&&k===1?s:0n;
  return [x,y,z,u,v,w,p,r];
 };
 const read=v=>[v[0],v[1]+v[6],v[3]];
 const Q=(v,a,b)=>{
  let [x,y,z,u,t,w,p,r]=v,A=BigInt(a),B=BigInt(b);
  return [z+B*p,t,2n*w+B*r,A*y,A*B*y,0n,A*x+r,A*z];
 };
 const R=(v,b)=>{
  let [x,y,z,u,t,w,p,r]=v,B=BigInt(b);
  return [z+B*p,t,2n*w+B*r,0n,0n,0n,r,0n];
 };
 const Add=(v,a,b)=>{
  let [x,y,z,u,t,w,p,r]=v,A=BigInt(a),B=BigInt(b);
  return [0n,0n,0n,A*y,A*B*y,0n,A*x,A*z];
 };
 const direct=(mass,beta,a,kind)=>{
  const out=new Map(),push=(k,v)=>out.set(k,(out.get(k)||0n)+v),m=beta.length;
  for(const [mask,num] of mass){
   if(kind!=="A")for(let i=0;i<m;i++)if(mask&(1<<i))push(mask^(1<<i),num*BigInt(beta[i]));
   if(kind!=="R"&&!(mask&1)&&bc(mask)<2)push(mask|1,num*BigInt(a));
  }return out;
 };
 const dr=mass=>{let y=[0n,0n,0n];for(const [mask,n] of mass)y[bc(mask)]+=n;return y;};
 const same=(u,v)=>u.length===v.length&&u.every((x,i)=>x===v[i]);
 const counts={parameter_cases:0,basis_states:0,exact_histogram_comparisons:0,observability_rank_checks:0,moment_surjectivity_checks:0,RA_word_histogram_comparisons:0};
 for(let m=4;m<=7;m++)for(const base of [1,3,5]){
  const beta=[0,...Array.from({length:m-1},(_,i)=>base+i)],masks=Array.from({length:1<<m},(_,i)=>i).filter(mask=>bc(mask)<=2);
  if(rank(masks.map(mask=>full(mask,beta)))!==9)throw Error("moment surjectivity "+m+" "+base);
  counts.moment_surjectivity_checks++;
  for(let b of [0,1,4])for(let a of [0,1,2,5]){
   beta[0]=b;counts.parameter_cases++;counts.observability_rank_checks++;
   if(orank(a,b)!==(a===0?6:8))throw Error("observer rank "+m+" "+base+" "+a+" "+b);
   for(const mask of masks){
    counts.basis_states++;
    let mass=new Map([[mask,1n]]),v=basis(mask,beta);
    for(let h=0;h<12;h++){
     if(!same(dr(mass),read(v)))throw Error("histogram "+[m,base,a,b,mask,h].join(","));
     counts.exact_histogram_comparisons++;
     mass=direct(mass,beta,a,"Q");v=Q(v,a,b);
    }
   }
  }
 }
 const beta=[4,1,2,3],a=2,masks=Array.from({length:16},(_,i)=>i).filter(i=>bc(i)<=2);
 for(const mask of masks)for(let length=0;length<=6;length++)for(let word=0;word<(1<<length);word++){
  let mass=new Map([[mask,1n]]),v=basis(mask,beta);
  for(let j=0;j<length;j++){
   let kind=(word&(1<<j))?"A":"R";
   mass=direct(mass,beta,a,kind);v=kind==="A"?Add(v,a,beta[0]):R(v,beta[0]);
  }
  if(!same(dr(mass),read(v)))throw Error("R/A word mismatch");
  counts.RA_word_histogram_comparisons++;
 }
 for(const b of [0,1,4,9])for(const a of [0,1,5]){
  const [T,C]=operator(a,b),v=[0,0,0,-1,-b,0,0,1,0];
  if([...T,...C].some(row=>row.reduce((s,x,i)=>s+x*v[i],0)!==0))throw Error("null-vector check");
 }
 return {result:"ALL_EXACT_ASSERTIONS_PASSED",counts,model:"Capacity-two named-source weighted removal and single marked addition",finite_domain:{m:[4,5,6,7],unmarked_beta_base:[1,3,5],marked_beta:[0,1,4],addition_a:[0,1,2,5],Q_horizons:"0..11",RA_word_lengths:"0..6 for beta=[4,1,2,3], a=2",arithmetic:"exact BigInt counts; finite rank tests modulo prime 1009"},theorem_scope:"Linear future-count dimension 8 for q=2, a>0, m>=4 and at least three pairwise distinct unmarked beta. Symbolic minor 2*a^2 independent of b is in paper."};
})();
console.log(JSON.stringify(result, null, 2));
