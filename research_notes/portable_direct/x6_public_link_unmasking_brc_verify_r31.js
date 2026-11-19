// R31 exact Boolean-BRC finite-controller verifier; Node.js, standard JS, deterministic.
// Execute: node x6_public_link_unmasking_brc_verify_r31.js
function runR31(){
  const counts={controllers:0,pair_horizon_checks:0,pass:true,largest_class_count:0,random_controllers:0,explicit_chains:0};
  function check(n,N,m,links,trans,initial){
    const d=Array(n).fill(Infinity),seen=new Set([initial]),queue=[[initial,0]];
    for(let p=0;p<queue.length;p++){
      const [s,t]=queue[p];for(let i=0;i<n;i++)if(((links[s]>>i)&1)===0&&t<d[i])d[i]=t;
      for(let a=0;a<m;a++){const z=trans[s*m+a];if(z>=0&&!seen.has(z)){seen.add(z);queue.push([z,t+1])}}
    }
    const intern=new Map([["[]",1]]);let nextId=2;
    const memo=new Map();
    function sign(theta,s,phase,used,h){
      if(h===0)return 1;
      const key=[theta,s,phase,used,h].join(":");if(memo.has(key))return memo.get(key);
      const out=[];
      for(let a=0;a<m;a++){const z=trans[s*m+a];if(z>=0)out.push(["A"+a,sign(theta,z,phase,used,h-1)])}
      for(let i=0;i<n;i++){
        const base=3**i,st=Math.floor(phase/base)%3;
        if(st===0)out.push(["P"+i+"+",sign(theta,s,phase+base,used,h-1)]);
        if(st===1)out.push(["P"+i+"-",sign(theta,s,phase+base,used,h-1)]);
        if(st===2&&!(used&(1<<i))&&(((theta>>i)&1)||((links[s]>>i)&1)))
          out.push(["Q"+i,sign(theta,s,phase,used|(1<<i),h-1)]);
      }
      const repr=JSON.stringify(out);
      if(!intern.has(repr))intern.set(repr,nextId++);
      const id=intern.get(repr);memo.set(key,id);return id;
    }
    for(let h=0;h<=6;h++){
      const vals=Array.from({length:1<<n},(_,theta)=>sign(theta,initial,0,0,h));
      const unique=new Set(vals).size;counts.largest_class_count=Math.max(unique,counts.largest_class_count);
      const expected=2**d.filter(v=>v+3<=h).length;
      if(unique!==expected)throw Error("class count mismatch "+JSON.stringify({n,N,m,links,trans,initial,h,d,unique,expected,vals}));
      for(let a=0;a<(1<<n);a++)for(let b=a+1;b<(1<<n);b++){
        const same=d.every((v,i)=>v+3>h||((a>>i)&1)===((b>>i)&1));
        if((vals[a]===vals[b])!==same)throw Error("pair mismatch "+JSON.stringify({n,N,m,links,trans,initial,h,d,a,b}));
        counts.pair_horizon_checks++;
      }
    }
    counts.controllers++;
  }
  function exhaustive(N,n,m){
    const Lcount=(1<<n)**N,rad=N+1,size=N*m,tcount=rad**size;
    for(let L=0;L<Lcount;L++){
      const links=Array(N);let z=L;
      for(let s=0;s<N;s++){links[s]=z%(1<<n);z=Math.floor(z/(1<<n))}
      for(let T=0;T<tcount;T++){
        const trans=Array(size);let v=T;
        for(let k=0;k<size;k++){trans[k]=(v%rad)-1;v=Math.floor(v/rad)}
        for(let initial=0;initial<N;initial++)check(n,N,m,links,trans,initial);
      }
    }
  }
  for(let n=1;n<=2;n++)for(let N=1;N<=2;N++)for(let m=0;m<=2;m++)exhaustive(N,n,m);
  let rng=0x91c0ffe;
  function next(){rng^=rng<<13;rng^=rng>>>17;rng^=rng<<5;return rng>>>0}
  for(let j=0;j<256;j++){
    const N=3,n=3,m=j%3;
    const links=Array.from({length:N},()=>next()%(1<<n));
    const trans=Array.from({length:N*m},()=>next()%(N+1)-1);
    check(n,N,m,links,trans,next()%N);counts.random_controllers++;
  }
  for(let q=0;q<=5;q++){
    const N=q+1,n=1,m=1,links=Array(N).fill(1);links[q]=0;
    const trans=Array.from({length:N},(_,s)=>s<q?s+1:-1);
    check(n,N,m,links,trans,0);counts.explicit_chains++;
  }
  return counts;
}
console.log(JSON.stringify(runR31(),null,2));
