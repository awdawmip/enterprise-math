const verify = function verify() {
  const T = {
    0: [[2,-1,-1],[2,1,-1]],
    1: [[0,-1,-1],[0,1,-1]],
    2: [[1,1,1],[2,1,-1]]
  };
  const S = [[0,1,"++--",2],[1,1,"---+",0],[2,1,"----",-2],
             [0,-1,"++-+",4],[1,-1,"-++-",2],[2,-1,"+--+",2]];
  const sync="+++--+";
  function ck(p,m) {if(!p) throw new Error("CHECK_FAILED: "+m);}
  function dec(q,e,word) {
    let t=0,prev=-1,dirty=false,bits="";
    for(const s of word) {
      const d=s==="+"?1:-1;
      const matches=[0,1].filter(b=>e*T[q][b][1]*T[q][b][2]===d);
      ck(matches.length===1,"unique inverse delta");
      const b=matches[0], [qn,eta]=T[q][b];
      if (b===0 && prev===0) dirty=true;
      bits+=b;prev=b;t+=d;q=qn;e*=eta;
    }
    return {q,e,t,dirty,bits};
  }
  for(const [q,e] of [[0,1],[0,-1],[1,1],[1,-1],[2,1],[2,-1]]) {
    const a=dec(q,e,"+++"),b=dec(q,e,sync);
    ck(a.q===2&&a.e===-1,"triple synchronization");
    ck(b.q===2&&b.e===-1&&b.dirty&&b.bits.endsWith("000"),"dirty synchronizer");
    for(const [q2,e2,route,sum] of S) {
      const x=dec(q,e,sync+route);
      ck(x.q===q2&&x.e===e2&&x.t===sum&&x.dirty,"target route");
    }
  }
  function binom(n,r) {
    if(!Number.isInteger(r)||r<0||r>n)return 0n;
    r=Math.min(r,n-r);
    let z=1n;
    for(let i=1;i<=r;i++) z=z*BigInt(n-r+i)/BigInt(i);
    return z;
  }
  function add(m,k,v) {m.set(k,(m.get(k)||0n)+v);}
  const F=[0n,1n];
  for(let j=2;j<160;j++) F[j]=F[j-1]+F[j-2];
  let state=new Map([["0,1,0,0,0",1n]]);
  let pointwise=0,certified=0,observed=0;
  for(let n=0;n<=150;n++) {
    const total=new Map(),C=new Map(),D=new Map();
    for(const [key,v] of state) {
      const [q,e,t,d]=key.split(",").map(Number);
      add(total,t,v);
      add(d?D:C,q+","+e+","+t,v);
    }
    for(let t=-n;t<=n;t++) {
      const target=((n-t)%2===0)?binom(n,(n+t)/2):0n;
      ck((total.get(t)||0n)===target,"total binomial n="+n+" t="+t);
    }
    if(n>=10) for(const [q,e,route,sum] of S) for(let t=-8;t<=8;t++) {
      if((n-t)%2) continue;
      const b=binom(n-10,(n-10+t-sum)/2);
      ck((D.get(q+","+e+","+t)||0n)>=b,"dirty lower n="+n);
      pointwise++;
    }
    if(n>=9) {
      let peak=0n,best=0n;
      const active=[...C].filter(([key])=>key.startsWith("0,"));
      for(const [,value] of active)if(value>peak)peak=value;
      for(const [key] of active) {
        const [,e,t]=key.split(",").map(Number);
        let mn=null;
        for(let q=0;q<=2;q++) for(const m of [C,D]) {
          const v=m.get(q+","+e+","+t)||0n;
          if(mn===null||v<mn)mn=v;
        }
        if(mn>best)best=mn;
      }
      if(best===peak)observed++;
    }
    if((n>=46&&n%2===0)||(n>=43&&n%2===1)) {
      const e=n%2===0?1:-1,k=n%2===0?-4:-3,t=e*k;
      const b=n%2===0?binom(n-10,(n-16)/2):binom(n-10,(n-11)/2);
      ck(b>=F[n+2],"Fibonacci threshold n="+n);
      for(let q=0;q<3;q++)ck((D.get(q+","+e+","+t)||0n)>=b,"dirty candidate");
      certified++;
    }
    if(n===150)break;
    const next=new Map();
    for(const [key,v] of state) {
      const [q,e,t,d,last]=key.split(",").map(Number);
      for(let bit=0;bit<=1;bit++) {
        const [qn,eta,b]=T[q][bit],en=e*eta,tn=t+en*b;
        ck(tn-t===(bit===0?e:-e),"delta code");
        const dn=(d||(last&&bit===0))?1:0;
        add(next,qn+","+en+","+tn+","+dn+","+(bit===0?1:0),v);
      }
    }
    state=next;
  }
  ck(binom(36,15)===5567902560n&&binom(33,16)===1166803110n,"exact bases");
  for(let m=2;m<150;m++)ck(4*(m+1)>=3*(m+2),"ratio inequality");
  return {
    result_id:"R282_DIRTY_SYNCHRONIZING_SUFFIX_20261025_T3",
    status:"PASS",
    model:"R281 exact 6-edge positive-weight ordered BRC auxiliary",
    source_commit:"d5fa39cebe5fcd6cda0e19759f23bbcb77bd023a",
    synchronizer:sync,
    routes:S,
    max_integer_DP_n:150,
    exact_pointwise_dirty_checks:pointwise,
    certified_dirty_candidate_layers:certified,
    observed_B_equals_Lambda_layers_n9_to150:observed,
    even_dirty_sufficient_threshold:46,
    odd_dirty_sufficient_threshold:43,
    even_base:{binomial:binom(36,15).toString(),fibonacci:F[48].toString()},
    odd_base:{binomial:binom(33,16).toString(),fibonacci:F[45].toString()},
    math_status:"AUTHOR_SIDE_PROVED_EXACT_SYNCHRONIZING_SUFFIX_AND_BINOMIAL_BOUND; CONDITIONAL_COROLLARY_REQUIRES_R274_R275_R281; NOT_ADMITTED"
  };
};
console.log(JSON.stringify(verify(),null,2));
