/* R285: exact BigInt/rational cone certificate for ordered positive clean-reset six-edge auxiliary BRC.
 * Node 18+: node R285_verify_effective_gap.js
 * No native X6 physics, no Source/Driver admission.
 */
const R285_RESULT = (function () {
  const BASE=2600, TAIL=2612, MAX=2620, DPMAX=160;
  const P=[1,-2,1,-8,6,-3,7,-5,1].map(BigInt);
  const P7=[-1,1,-8,4,-6,11,-6,1].map(BigInt);
  const p=[1,-1,0,-2,1].map(BigInt);
  function must(ok,msg){if(!ok)throw Error("FAILED "+msg);}
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a||1n;}
  function F(n,d=1n){n=BigInt(n);d=BigInt(d);must(d!==0n,"zero denominator");if(d<0n){n=-n;d=-d;}const z=gcd(n,d);return {n:n/z,d:d/z};}
  const add=(x,y)=>F(x.n*y.d+y.n*x.d,x.d*y.d);
  const neg=x=>F(-x.n,x.d);
  const sub=(x,y)=>add(x,neg(y));
  const mul=(x,y)=>F(x.n*y.n,x.d*y.d);
  const div=(x,y)=>F(x.n*y.d,x.d*y.n);
  const pow=(x,k)=>{let z=F(1),v=x,m=k;while(m){if(m%2)z=mul(z,v);v=mul(v,v);m=Math.floor(m/2);}return z;};
  const cmp=(x,y)=>x.n*y.d<y.n*x.d?-1:(x.n*y.d>y.n*x.d?1:0);
  const repr=x=>({numerator:x.n.toString(),denominator:x.d.toString()});
  const at=(v,i)=>i>=0&&i<v.length?v[i]:0n;
  const conv=(u,v)=>{const w=Array(u.length+v.length-1).fill(0n);for(let i=0;i<u.length;i++)for(let j=0;j<v.length;j++)w[i+j]+=u[i]*v[j];return w;};
  const A=conv([-1n,1n],P7), B=conv(p,P);
  must(B.join(",")==="1,-3,3,-11,19,-13,27,-32,18,-18,17,-7,1","filter product");

  const g=[1n];
  for(let n=0;n<=MAX+1;n++){
    const N=BigInt(n);
    const num=(2n*N-2n)*at(g,n)+(N-1n)*at(g,n-1)
       +(2n*N-2n)*at(g,n-2)-(N-3n)*at(g,n-3);
    must(num%(N+1n)===0n,"integrality g "+n);
    g.push(num/(N+1n));
  }
  must(g.slice(0,10).join(",")==="1,-2,0,0,-2,-2,-4,-10,-20,-44","g base");
  const f=g.map(x=>-x);
  const k=[];
  for(let m=0;m<=MAX;m++){
    let num=at(A,m+1);
    for(let i=0;i<P.length;i++)num-=P[i]*at(g,m+1-i);
    must(num%2n===0n,"K parity "+m);
    k.push(num/2n-at(k,m-1));
  }
  const t=k.map((_,m)=>p.reduce((s,c,i)=>s+c*at(k,m-i),0n));
  must(k.slice(0,12).join(",")==="1,1,-2,-3,1,2,-2,-3,-2,-6,-13,-24","K base");

  const a=F(523,200),b=F(131,50),ONE=F(1), TWO=F(2);
  for(let n=BASE-2;n<=MAX+1;n++){
    must(f[n-1]>0n&&f[n]>0n,"f positivity "+n);
    const ratio=F(f[n],f[n-1]);
    must(cmp(ratio,a)>=0&&cmp(ratio,b)<=0,"finite ratio "+n);
  }
  function lower(n){
    const N=F(n), nm1=F(n-1),twoNm2=F(2*n-2);
    return div(sub(add(add(twoNm2,div(nm1,b)),div(twoNm2,pow(b,2))),div(F(n-3),pow(a,3))),F(n+1));
  }
  function upper(n){
    const nm1=F(n-1),twoNm2=F(2*n-2);
    return div(sub(add(add(twoNm2,div(nm1,a)),div(twoNm2,pow(a,2))),div(F(n-3),pow(b,3))),F(n+1));
  }
  const loInf=sub(add(add(TWO,div(ONE,b)),div(TWO,pow(b,2))),div(ONE,pow(a,3)));
  const upInf=sub(add(add(TWO,div(ONE,a)),div(TWO,pow(a,2))),div(ONE,pow(b,3)));
  must(cmp(lower(BASE),a)>0&&cmp(loInf,lower(BASE))>0,"permanent lower ratio");
  must(cmp(upInf,b)<0&&cmp(upper(BASE),upInf)<0,"permanent upper ratio");

  function bands(C){
    let L=F(0),U=F(0);
    for(let i=0;i<C.length;i++){
      const z=F(C[i]);
      L=add(L,div(z,pow(C[i]>=0n?b:a,i)));
      U=add(U,div(z,pow(C[i]>=0n?a:b,i)));
    }
    must(cmp(L,F(0))>0&&cmp(mul(a,L),U)>0,"signed cone band");
    return {L,U,margin:sub(mul(a,L),U)};
  }
  const bp=bands(P), bb=bands(B);
  const H=(C,n)=>C.reduce((s,c,i)=>s+c*at(f,n-i),0n);
  for(let n=TAIL;n<MAX;n++){
    for(const [C,band,v] of [[P,bp,k],[B,bb,t]]){
      const hn=H(C,n), hn1=H(C,n+1);
      must(cmp(mul(band.L,F(f[n])),F(hn))<=0,"filter lower "+n);
      must(cmp(F(hn),mul(band.U,F(f[n])))<=0,"filter upper "+n);
      must(hn1>hn,"filter monotonic "+n);
      must(2n*(v[n]-v[n-2])===hn1-hn,"two-step exact "+n);
      must(v[n]>v[n-2],"strict two-step "+n);
    }
  }

  let lastK=-1,lastT=-1;
  for(let m=0;m<TAIL;m++){
    if(k[m]<=0n)lastK=m;
    if(t[m]<=0n)lastT=m;
  }
  must(lastK===36&&lastT===34,"finite last nonpositive");
  for(let m=37;m<TAIL;m++)must(k[m]>0n,"finite K positivity "+m);
  for(let m=35;m<TAIL;m++)must(t[m]>0n,"finite T positivity "+m);
  must(k[36]===-727277462n&&k[37]===1985689179n,"even boundary");
  must(t[34]===-120708721n&&t[35]===3814120n,"odd boundary");

  const EDGES={
    "0,0":[2,-1,-1],"0,1":[2,1,-1],
    "1,0":[0,-1,-1],"1,1":[0,1,-1],
    "2,0":[1,1,1],"2,1":[2,1,-1]
  };
  let dp=new Map([["0,2,1,0",1n]]),crossE=0,crossO=0;
  for(let n=0;n<=DPMAX;n++){
    const d=new Map();
    for(const [key,w] of dp){
      const [q,prev,eps,dsp]=key.split(",").map(Number);
      if(q===0){
        const target=[eps,dsp].join(",");
        d.set(target,(d.get(target)||0n)+w);
      }
    }
    if(n%2===0&&n>=8){
      must((d.get("1,-4")||0n)-(d.get("-1,-4")||0n)===k[(n-8)/2],"DP E "+n);
      crossE++;
    }
    if(n%2===1&&n>=5){
      must((d.get("-1,-3")||0n)-(d.get("1,-5")||0n)===t[(n-5)/2],"DP O "+n);
      crossO++;
    }
    const nx=new Map();
    for(const [key,w] of dp){
      const [q,prev,eps,dsp]=key.split(",").map(Number);
      for(const bit of [0,1]){
        if(prev===0&&bit===0)continue;
        const [q2,eta,c]=EDGES[q+","+bit];
        const dest=[q2,bit,eps*eta,eta*dsp+c].join(",");
        nx.set(dest,(nx.get(dest)||0n)+w);
      }
    }
    dp=nx;
  }
  return {
    status:"PASS",schema:"EM_R285_EFFECTIVE_CENTRAL_GAP_JS_BIGINT_V1",
    scope:"positive ordered six-edge clean reset BRC auxiliary, not P000 native physics",
    prior_kernel:"R284@ce4ad0aab996c6310bccb112796325149f75884b",
    global_snapshot:"124e158e394e597af0212115d43a38edc164e6bb",
    ratio_cone:{a:repr(a),b:repr(b),base_start:BASE,base_indices:[BASE-2,BASE-1,BASE],
      lower_at_base:repr(lower(BASE)),lower_margin:repr(sub(lower(BASE),a)),
      upper_limit:repr(upInf),upper_limit_margin:repr(sub(b,upInf))},
    signed_filter:{P:P.map(String),pP:B.map(String),
      P_lower:repr(bp.L),P_upper:repr(bp.U),P_margin:repr(bp.margin),
      pP_lower:repr(bb.L),pP_upper:repr(bb.U),pP_margin:repr(bb.margin)},
    strict_two_step_from:TAIL,
    finite_coefficient_check_end:TAIL-1,
    last_nonpositive_K_index:lastK,last_nonpositive_pK_index:lastT,
    all_even_strict_from_length:82,all_odd_strict_from_length:75,
    boundary:{E80:k[36].toString(),E82:k[37].toString(),
      O73:t[34].toString(),O75:t[35].toString()},
    independent_original_path_DP_end:DPMAX,crosschecked_even:crossE,crosschecked_odd:crossO,
    arithmetic:"exact BigInt, reduced rational cross-products",
    mathematically_admitted:false,native_owner_verified:false,driver_review:"NOT_DONE"
  };
})();
if (typeof module !== "undefined" && require.main===module) {
  console.log(JSON.stringify(R285_RESULT,null,2));
}
