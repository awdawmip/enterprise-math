function factorBoundary(M){
 const h=new Map(), Q=[];
 for(let q=0;q<=M-2;q++){
  const n=q*M+1;
  for(let r=1;r<=M-1;r++){
   if(n%r!==0)continue;
   const s=n/r,v=M-r-s+q;
   if(s<1||s>M-1||v<1||v>=M)continue;
   const t=M*(M-r)*(M-s);
   h.set(t,(h.get(t)||0)+2);
   if(q===1)Q.push({r,s,a:M-r,d:M-s,u:M,v,threshold:t});
  }
 }
 return {bins:[...h].sort((x,y)=>y[0]-x[0]),q1:Q};
}

function directBoundary(M){
 const h=new Map();
 for(let a=1;a<=M;a++)for(let d=1;d<=M;d++){
   if((a*d-1)%M!==0)continue;
   const v=(a*d-1)/M;
   if(v<1||v>=M)continue;
   const t=M*a*d;
   h.set(t,(h.get(t)||0)+2);
 }
 return [...h].sort((x,y)=>y[0]-x[0]);
}

function verify(){
 let comparisons=0, squareExamples=0;const sample={};
 for(let M=2;M<=128;M++){
   const f=factorBoundary(M),d=directBoundary(M);
   if(JSON.stringify(f.bins)!==JSON.stringify(d))throw Error("boundary mismatch M="+M);
   comparisons++;
   if([10,11,15,20,24,32,35,64].includes(M)){
     sample[M]={positive_boundary_count:f.bins.reduce((s,[,c])=>s+c,0),distinct_thresholds:f.bins.length,top_bins:f.bins.slice(0,7),q1:f.q1.slice(0,8)};
   }
 }
 for(let t=4;t<=100;t++){
   const M=t*t-1, a=M-t, d=a, u=M,v=t*(t-2);
   const threshold=u*a*d;
   const k=a, standard=(k+1)*k*k;
   if(a*d-u*v!==1 || !(v>=1&&v<M) || !(2*threshold>M**3) || !(threshold>standard)){
     throw Error("infinite family finite check failed t="+t);
   }
   squareExamples++;
 }
 return {status:"PASS",scope:"Exact integer tests on bounded M and square-minus-one family; infinite claims from symbolic identities",comparisons,squareExamples,sample};
}

console.log(JSON.stringify(verify(),null,2));
