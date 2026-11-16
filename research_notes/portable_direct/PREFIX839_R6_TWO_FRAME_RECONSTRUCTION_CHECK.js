// PREFIX-839 independent BigInt named-state Q branching and two-frame inversion.

// Use: node PREFIX839_R6_TWO_FRAME_RECONSTRUCTION_CHECK.js

function elem(w) {
  const p=w.length,e=Array(p+1).fill(0n); e[0]=1n;
  for(const x0 of w){const x=BigInt(x0); for(let d=p;d>=1;--d)e[d]+=x*e[d-1];}
  return e;
}

function bc(n,k) {
  if(k<0||k>n)return 0n;
  let z=1n;
  for(let i=1;i<=k;i++)z=z*BigInt(n+1-i)/BigInt(i);
  return z;
}

function fac(n){let a=1n;for(let j=2;j<=n;j++)a*=BigInt(j);return a;}

function popcnt(n){let a=0;while(n){a+=n&1;n>>=1;}return a;}

function trace(w,a0,b0,limit){
  const p=w.length,a=BigInt(a0),b=BigInt(b0),out=[];
  let states=new Map([[( ((1<<p)-1)<<1 ),1n]]);
  function add(mp,key,val){mp.set(key,(mp.get(key)||0n)+val);}
  for(let t=0;t<=limit;t++){
    const y=Array(p+1).fill(0n);
    for(const [key,mass] of states){const mask=key>>1,mark=key&1;y[popcnt(mask)+mark]+=mass;}
    out.push(y);
    const next=new Map();
    for(const [key,mass] of states){
      const mask=key>>1,mark=key&1;
      if(mark)add(next,mask<<1,mass*b);
      else if(popcnt(mask)<p)add(next,(mask<<1)|1,mass*a);
      for(let i=0;i<p;i++)if(mask&(1<<i))add(next,((mask^(1<<i))<<1)|mark,mass*BigInt(w[i]));
    }
    states=next;
  }
  return out;
}

function reconstruct(y,p,a0,b0,t){
  const a=BigInt(a0),b=BigInt(b0),lam=a*b,e=Array(p+2).fill(0n);
  for(let d=p;d>=1;--d){
    const tau=((t-d)%2===0)?t:t+1;
    if(tau<d)throw Error("insufficient horizon");
    const alpha=fac(d)*bc(tau-1,d-1)*lam**BigInt((tau-d)/2);
    const beta=(d<p&&tau>=d+2)?fac(d+1)*bc(tau-1,d)*a*lam**BigInt((tau-d-2)/2):0n;
    const numerator=y[tau][p-d]-beta*e[d+1];
    if(numerator%alpha)throw Error("nonexact integer inversion");
    e[d]=numerator/alpha;
  }
  return [1n,...e.slice(1,p+1)];
}

function check(){
  const stats={configs:0,inversions:0,formula_bins:0,permutation_tests:0,collision_cases:[],max_p:5,weights:"nondecreasing 1..4",a:"1,2,3",b:"1,2,4",t:"p-1 through p+5",status:"ALL_EXACT_ASSERTIONS_PASSED"};
  function assert(cond,msg){if(!cond)throw Error(msg);}
  function enumerate(p,min,arr,cb){
    if(arr.length===p){cb([...arr]);return;}
    for(let w=min;w<=4;w++)enumerate(p,w,[...arr,w],cb);
  }
  for(let p=1;p<=5;p++)enumerate(p,1,[],w=>{
    const e=elem(w);
    for(const a of [1,2,3])for(const b of [1,2,4]){
      const yy=trace(w,a,b,2*p+5);
      stats.configs++;
      for(let t=p-1;t<=p+5;t++){
        const r=reconstruct(yy,p,a,b,t);
        assert(r.every((v,i)=>v===e[i]),`reconstruction p=${p} w=${w} a=${a} b=${b} t=${t}`);
        stats.inversions++;
      }
      for(let t=1;t<yy.length;t++){
        const z=Array(p+1).fill(0n);
        for(let d=1;d<=p;d++)for(let mark=0;mark<=1;mark++){
          const r2=t-d-mark;
          if(r2<0||r2%2)continue;
          const r=r2/2;
          z[p-d+mark]+=fac(d)*bc(t-1,d-1)*e[d]*BigInt(a)**BigInt(r+mark)*BigInt(b)**BigInt(r);
        }
        for(let j=0;j<=p;j++){
          assert(z[j]===yy[t][j],`closed-form p=${p} t=${t} bin=${j}`);
          stats.formula_bins++;
        }
      }
      if(p>=2){
        const rev=[...w].reverse();
        const yrev=trace(rev,a,b,p+3),yorig=trace(w,a,b,p+3);
        assert(yrev.every((hist,i)=>hist.every((v,j)=>v===yorig[i][j])),"name-permutation invariance");
        stats.permutation_tests++;
      }
    }
  });
  for(const [w1,w2,t] of [[[1,7],[2,4],3],[[1,4,10],[2,2,11],4],[[1,16,16],[2,5,26],34]]){
    const y1=trace(w1,1,2,t+1),y2=trace(w2,1,2,t+1);
    assert(y1[t].every((v,j)=>v===y2[t][j]),"re-alias expected");
    assert(y1[t+1].some((v,j)=>v!==y2[t+1][j]),"adjacent frames expected distinct");
    const e1=reconstruct(y1,w1.length,1,2,t),e2=reconstruct(y2,w2.length,1,2,t);
    assert(e1.some((v,j)=>v!==e2[j]),"distinct recovered coordinates");
    stats.collision_cases.push({p:w1.length,t,A:w1,B:w2,common_at_t:y1[t].map(String),recovered_A:e1.map(String),recovered_B:e2.map(String)});
  }
  return stats;
}

const result = check();

process.stdout.write(JSON.stringify(result,null,2)+'\n');

