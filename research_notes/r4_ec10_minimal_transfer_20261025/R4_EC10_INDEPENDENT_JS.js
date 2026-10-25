function verifyR4EC10() {
  const p=1000003;
  const mod=x=>((x%p)+p)%p;
  function pow(a,n){let v=1;while(n>0){if(n%2)v=v*a%p;a=a*a%p;n=Math.floor(n/2);}return v;}
  const inv2=pow(2,p-2);
  const states=[];for(const [q,r] of [[0,0],[0,2],[1,1],[1,2],[2,0],[2,1],[2,2]])for(const e of [1,-1])states.push([q,r,e]);
  const outputs=[];for(let q=0;q<3;q++)for(let c=0;c<2;c++)for(const e of [1,-1])outputs.push([q,c,e]);
  const fidx=(q,r,e)=>{const k=states.findIndex(s=>s[0]===q&&s[1]===r&&s[2]===e);if(k<0)throw Error("invalid state");return k;};
  const oidx=(q,c,e)=>{const k=outputs.findIndex(s=>s[0]===q&&s[1]===c&&s[2]===e);if(k<0)throw Error("invalid output");return k;};
  const edge=(q,a)=>q===0?(a?[2,1,-1]:[2,-1,-1]):q===1?(a?[0,1,-1]:[0,-1,-1]):(a?[2,1,-1]:[1,1,1]);
  function advance(v) {
    const w=Array(14).fill(0);
    states.forEach(([q,r,e],i)=>{
      for(let a=0;a<=1;a++){
        const [nq,eta,b]=edge(q,a);const nr=r===2?2:a===1?0:r===0?1:2;const ne=e*eta;
        const wt=(ne*b===1?2:inv2);const j=fidx(nq,nr,ne);
        w[j]=(w[j]+wt*v[i])%p;
      }
    });return w;
  }
  function observe(v) {
    const y=Array(12).fill(0);
    states.forEach(([q,r,e],i)=>{const k=oidx(q,r===2?1:0,e);y[k]=(y[k]+v[i])%p;});
    return y;
  }
  const ys=[],init=Array(14).fill(0);init[fidx(0,0,1)]=1;
  let v=init;
  for(let n=0;n<=13;n++){ys.push(observe(v));v=advance(v);}
  let count=0;
  for(let n=0;n<=12;n++){
    const exhaustive=Array(12).fill(0);
    for(let word=0;word<(1<<n);word++){
      let q=0,r=0,e=1,t=0;
      for(let j=0;j<n;j++){
        const a=(word>>j)&1;const [nq,eta,b]=edge(q,a);r=r===2?2:a===1?0:r===0?1:2;
        e=e*eta;t+=e*b;q=nq;
      }
      const k=oidx(q,r===2?1:0,e);let wt=1;
      if(t>0)wt=pow(2,t);else if(t<0)wt=pow(inv2,-t);
      exhaustive[k]=(exhaustive[k]+wt)%p;count++;
    }
    if(exhaustive.some((x,i)=>x!==ys[n][i]))throw Error("raw word enumeration failed n="+n);
  }
  function determinant(source){
    let a=source.map(r=>r.slice()),d=1,N=a.length;
    for(let j=0;j<N;j++){
      let k=j;while(k<N&&a[k][j]===0)k++;
      if(k===N)return 0;
      if(k!==j){[a[k],a[j]]=[a[j],a[k]];d=mod(-d);}
      const pivot=a[j][j];d=d*pivot%p;const inv=pow(pivot,p-2);
      for(let i=j+1;i<N;i++){
        const b=a[i][j]*inv%p;
        for(let h=j+1;h<N;h++)a[i][h]=mod(a[i][h]-b*a[j][h]);
        a[i][j]=0;
      }
    }return d;
  }
  const rows13=[...Array.from({length:11},(_,k)=>[0,k]),[1,4],[1,5]];
  const rows12=[...[0,1,2,4,5,6,7,8,9,10].map(k=>[0,k]),[1,4],[1,5]];
  const d13=determinant(rows13.map(([lag,o])=>Array.from({length:13},(_,j)=>ys[lag+j][o])));
  const d12=determinant(rows12.map(([lag,o])=>Array.from({length:12},(_,j)=>ys[1+lag+j][o])));
  if(d13!==739682||d12!==684922)throw Error("modular minor disagreement "+d13+","+d12);
  const S=(2+inv2)%p;
  let P=[1];
  function multiply(B){const C=Array(P.length+B.length-1).fill(0);P.forEach((a,i)=>B.forEach((b,j)=>{C[i+j]=(C[i+j]+a*b)%p;}));P=C;}
  multiply([1,0,1]);multiply([1,mod(-S),0,0,2,0,mod(-1)]);
  multiply([1,mod(-S)]);multiply([1,0,1,mod(-S)]);
  if(P.length!==13)throw Error("invalid denominator");
  const defect=e=>P.reduce((sum,c,j)=>(sum+c*ys[12-j][oidx(0,1,e)])%p,0);
  if(defect(1)!==p-5||defect(-1)!==5)throw Error("defect mismatch");
  return {status:"PASS",p,z:2,det_initial:d13,det_shifted:d12,defect_positive:mod(-5),defect_negative:5,raw_words_enumerated:count};
}
const report=verifyR4EC10();
console.log(JSON.stringify(report));
