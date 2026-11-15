/* PREFIX-821 exact BigInt verifier; standard Node.js: node PREFIX821_R6_Q3_OBSERVER_LANGUAGE_CHECK.js */
const result=(function evaluate(){
 const mod=1009, modexp=(x,n)=>{let a=1;while(n){if(n&1)a=a*x%mod;x=x*x%mod;n>>=1;}return a;};
 const rank=rows=>{
  let B=rows.map(row=>row.map(v=>((v%mod)+mod)%mod)),h=0,n=B[0].length;
  for(let j=0;j<n&&h<B.length;j++){
   let p=h;while(p<B.length&&!B[p][j])p++;
   if(p===B.length)continue;
   [B[h],B[p]]=[B[p],B[h]];
   let inv=modexp(B[h][j],mod-2);
   for(let k=j;k<n;k++)B[h][k]=B[h][k]*inv%mod;
   for(let i=0;i<B.length;i++)if(i!==h&&B[i][j]){let c=B[i][j];for(let k=j;k<n;k++)B[i][k]=(B[i][k]-c*B[h][k]%mod+mod)%mod;}
   h++;
  }return h;
 };
 const det=rows=>{
  let B=rows.map(row=>row.map(v=>((v%mod)+mod)%mod)),prod=1,n=B.length;
  for(let j=0;j<n;j++){
   let p=j;while(p<n&&!B[p][j])p++;
   if(p===n)return 0;
   if(p!==j){[B[j],B[p]]=[B[p],B[j]];prod=(mod-prod)%mod;}
   let v=B[j][j];prod=prod*v%mod;
   let inv=modexp(v,mod-2);
   for(let i=j+1;i<n;i++)if(B[i][j]){let c=B[i][j]*inv%mod;for(let k=j;k<n;k++)B[i][k]=(B[i][k]-c*B[j][k]%mod+mod)%mod;}
  }return prod;
 };
 const q=3,ix=[];for(let z=0;z<2;z++)for(let k=0;k<=q-z;k++)for(let h=0;h<=k;h++)ix.push([z,k,h]);
 const key=(z,k,h)=>ix.findIndex(p=>p[0]===z&&p[1]===k&&p[2]===h);
 const bc=x=>{let n=0;for(;x;x&=x-1)n++;return n;};
 const zeros=n=>Array(n).fill(0n);
 const matrix=(a,b)=>{
  let R=Array.from({length:16},()=>Array(16).fill(0)),A=Array.from({length:16},()=>Array(16).fill(0)),C=Array.from({length:4},()=>Array(16).fill(0));
  ix.forEach(([z,k,h],j)=>{
   if(h>0)R[key(z,k-1,h-1)][j]+=h;
   if(z===1)R[key(0,k,h)][j]+=b;
   if(z===0&&k<q)A[key(1,k,h)][j]+=a;
   if(h===0)C[k+z][j]=1;
  });
  return {R,A,C,Q:R.map((row,i)=>row.map((v,j)=>v+A[i][j]))};
 };
 const mul=(B,T)=>B.map(row=>T[0].map((_,j)=>row.reduce((s,v,i)=>s+v*T[i][j],0)));
 const apply=(M,T)=>M.map(row=>row.reduce((s,v,i)=>s+BigInt(v)*T[i],0n));
 const basis=(mask,beta)=>{
  let marked=mask&1,other=[];for(let i=1;i<beta.length;i++)if(mask>>i&1)other.push(beta[i]);
  let k=other.length,es=[1n];for(const v of other){let e=Array(es.length+1).fill(0n);for(let j=0;j<es.length;j++){e[j]+=es[j];e[j+1]+=es[j]*BigInt(v);}es=e;}
  let M=zeros(16);for(let h=0;h<=k;h++)M[key(marked,k,h)]=es[h];return M;
 };
 const direct=(mass,beta,a,kind)=>{
  let out=new Map(),push=(k,v)=>out.set(k,(out.get(k)||0n)+v);
  for(const [mask,weight] of mass){
   if(kind!=="A")for(let i=0;i<beta.length;i++)if(mask>>i&1)push(mask^(1<<i),weight*BigInt(beta[i]));
   if(kind!=="R"&&!(mask&1)&&bc(mask)<q)push(mask|1,weight*BigInt(a));
  }return out;
 };
 const counts=mass=>{
  let Y=zeros(4);for(const [mask,v] of mass)Y[bc(mask)]+=v;return Y;
 };
 const equal=(x,y)=>x.length===y.length&&x.every((v,i)=>v===y[i]);
 const assertions={parameter_cases:0,named_basis_states:0,exact_histogram_comparisons:0,q_only_rank_tests:0,RA_rank_tests:0,symbolic_minor_numeric_specializations:0,witness_Q_horizons:0,witness_distinguishing_words:0};
 for(let m=5;m<=7;m++)for(const base of [1,3,5]){
  let beta=[0,...Array.from({length:m-1},(_,i)=>base+i)];
  let masks=Array.from({length:1<<m},(_,i)=>i).filter(mask=>bc(mask)<=q);
  for(const b of [1,2,4])for(const a of [1,2,5]){
   beta[0]=b;
   const {R,A,C,Q}=matrix(a,b);
   const O=[],E0=C;
   let E=E0;
   for(let t=0;t<4;t++){O.push(...E);E=mul(E,Q);}
   if(rank(O)!==14)throw Error("Q rank "+[m,base,b,a]);
   if(rank(O.concat(mul(C,R)))!==15)throw Error("R/A rank "+[m,base,b,a]);
   const piv=[...Array(13).keys(),14],minor=piv.map(i=>piv.map(j=>O[i][j]));
   let target=96*(a**5)*b%mod;
   if(det(minor)!==target)throw Error("14x14 minor "+[m,base,b,a,det(minor),target]);
   const v1=zeros(16),v2=zeros(16);
   v1[key(0,3,0)]=-1n;v1[key(0,3,1)]=-BigInt(b);v1[key(1,2,0)]=1n;
   v2[key(0,1,0)]=-6n;v2[key(0,1,1)]=-6n*BigInt(b);
   v2[key(0,3,2)]=-3n*BigInt(a*b);v2[key(0,3,3)]=-BigInt(a*b*b);
   v2[key(1,0,0)]=6n;v2[key(1,2,1)]=6n*BigInt(a);v2[key(1,2,2)]=3n*BigInt(a*b);
   if(!equal(apply(C,v1),zeros(4))||!equal(apply(Q,v1),zeros(16))||!equal(apply(C,v2),zeros(4))||!equal(apply(Q,v2),zeros(16)))throw Error("Kernel check "+[m,base,b,a]);
   let cR=apply(C,apply(R,v2));
   if(!equal(cR,[0n,0n,6n*BigInt(a),0n]))throw Error("CR witness check");
   assertions.parameter_cases++;assertions.q_only_rank_tests++;assertions.RA_rank_tests++;assertions.symbolic_minor_numeric_specializations++;
   for(const mask of masks){
    let mass=new Map([[mask,1n]]),mom=basis(mask,beta);
    assertions.named_basis_states++;
    for(let t=0;t<=8;t++){
     if(!equal(counts(mass),apply(C,mom)))throw Error("Named path mismatch "+[m,base,b,a,mask,t]);
     assertions.exact_histogram_comparisons++;
     mass=direct(mass,beta,a,"Q");mom=apply(Q,mom);
    }
   }
  }
 }
 // Explicit nonnegative named-state witness; exact Q trajectories.
 const beta=[1,1,2,3,4],a=1;
 let mu=new Map([[1,36n],[11,54n],[22,24n],[28,2n]]),
 nu=new Map([[2,36n],[7,45n],[13,9n],[14,11n],[26,15n]]);
 if(!equal(counts(mu),[0n,36n,0n,80n])||!equal(counts(nu),[0n,36n,0n,80n]))throw Error("Wrong initial witness");
 for(let h=0;h<=12;h++){
  if(!equal(counts(mu),counts(nu)))throw Error("Q witness gap at "+h);
  assertions.witness_Q_horizons++;
  mu=direct(mu,beta,a,"Q");nu=direct(nu,beta,a,"Q");
 }
 mu=new Map([[1,36n],[11,54n],[22,24n],[28,2n]]);
 nu=new Map([[2,36n],[7,45n],[13,9n],[14,11n],[26,15n]]);
 const diff=(kind)=>{const x=counts(direct(mu,beta,a,kind)),y=counts(direct(nu,beta,a,kind));return x.map((v,i)=>v-y[i]);};
 if(!equal(diff("R"),[0n,0n,36n,0n])||!equal(diff("A"),[0n,0n,-36n,0n]))throw Error("R/A witness mismatch");
 assertions.witness_distinguishing_words+=2;
 return {status:"ALL_EXACT_ASSERTIONS_PASSED",model:"q=3, one marked branch, nonnegative weighted named states, combined Q versus individually selected R and A",arithmetic:"exact BigInt count paths; modulo-1009 finite nonzero-minor/rank checks",tests:assertions,domain:{m:[5,6,7],unmarked_beta_base:[1,3,5],marked_beta:[1,2,4],addition_a:[1,2,5],Q_histogram_horizons:"0..8",witness_horizons:"0..12"},witness:{m:5,beta:[1,1,2,3,4],a:1,mu:{"1":36,"11":54,"22":24,"28":2},nu:{"2":36,"7":45,"13":9,"14":11,"26":15},initial_histogram:[0,36,0,80],R_hist_difference:[0,0,36,0],A_hist_difference:[0,0,-36,0]},general_theorems:"symbolic two-dimensional Q-only kernel, rank-14 observability minor 96*a^5*b, and R/A-word rank 15 for a,b>0 with >=4 distinct unmarked removal weights; finite tests illustrate proof scope",review:"AUTHOR_PROVED_NOT_INDEPENDENTLY_REVIEWED"};
})();
console.log(JSON.stringify(result,null,2));
