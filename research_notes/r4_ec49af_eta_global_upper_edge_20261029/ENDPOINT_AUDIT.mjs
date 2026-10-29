// EC49AF endpoint-only causal skip-cost audit; run: node ENDPOINT_AUDIT.mjs
// All 288 enumerated prefixes are exactly checked using BigInt rationals.
const endpointAudit = function endpointAudit() {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;};
  const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(d===0n)throw Error("zero denom");let g=gcd(n,d);return {n:n/g,d:d/g};};
  const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d);
  const sub=(a,b)=>R(a.n*b.d-b.n*a.d,a.d*b.d);
  const mul=(a,b)=>R(a.n*b.n,a.d*b.d);
  const div=(a,b)=>R(a.n*b.d,a.d*b.n);
  const cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0;
  const eq=(a,b)=>cmp(a,b)===0;
  const max=(a,b)=>cmp(a,b)>=0?a:b;
  const min=(a,b)=>cmp(a,b)<=0?a:b;
  const s=a=>a.d===1n?String(a.n):String(a.n)+"/"+String(a.d);
  const ok=(b,msg)=>{if(!b)throw Error("endpoint audit: "+msg);};
  const Z=R(0),O=R(1),ETA=R(1,4),RR=R(177,172);
  const t=(w,u)=>add(R(1,2),mul(R((2*u-1)*(1-w)),ETA));
  const raw=(name,w,u,z)=>mul(t(w,u),name==="P"?(w===z?R(1,6):R(1,12)):R(1,9));
  const prefix=(iw,jw,labels,bl,b)=>{
    const h=add(R(5,16),b);
    const X=Array.from({length:3},()=>[Z,Z,Z,Z]);
    for(let w=0;w<3;w++){
      const H=w===iw?h:Z, B=w===jw?b:Z;
      X[w][labels[w]]=sub(sub(O,H),B);
      X[w][2+bl]=add(X[w][2+bl],B);
      ok(cmp(X[w][labels[w]],Z)>=0,"row mass");
    }
    return X;
  };
  const evaluate=(X,b)=>{
    const atom={}, mass={}, gain={};
    let full=Z;
    let stop=Z;
    for(let w=0;w<3;w++){
      let paid=Z;for(let c=0;c<4;c++)paid=add(paid,X[w][c]);
      stop=add(stop,div(sub(O,paid),R(3)));
    }
    full=mul(stop,max(Z,sub(O,RR)));
    for(let c=0;c<4;c++)for(let u=0;u<2;u++){
      let pp=Z,qq=Z, sensed=Z;
      for(let z=0;z<3;z++){
        let p=Z,q=Z;
        for(let w=0;w<3;w++){
          p=add(p,mul(X[w][c],raw("P",w,u,z)));
          q=add(q,mul(X[w][c],raw("Q",w,u,z)));
        }
        pp=add(pp,p);qq=add(qq,q);
        sensed=add(sensed,max(Z,sub(p,mul(RR,q))));
      }
      mass[c+","+u]=pp;
      gain[c+","+u]=sub(sensed,max(Z,sub(pp,mul(RR,qq))));
      ok(cmp(gain[c+","+u],Z)>=0,"refinement gain nonnegative");
      full=add(full,sensed);
    }
    let rem=div(sub(R(1,16),b),R(3)),loss=Z;
    let groups=Object.keys(mass).filter(k=>cmp(mass[k],Z)>0)
      .sort((a,b)=>cmp(div(gain[a],mass[a]),div(gain[b],mass[b])));
    for(let k of groups){
      let take=min(rem,mass[k]);
      loss=add(loss,mul(take,div(gain[k],mass[k])));
      rem=sub(rem,take);
    }
    ok(eq(rem,Z),"skip mass coverage");
    return {legal:sub(full,loss),full,loss};
  };
  const Xstar=[[O,Z,Z,Z],[Z,O,Z,Z],[R(9,16),Z,R(1,16),Z]];
  const HX=evaluate(Xstar,R(1,16));
  ok(eq(HX.legal,R(3461,33024))&&eq(HX.loss,Z),"universal prefix support");
  let c0=0,c1=0,max0=null,max1=null,maxRelax0=null, best0=null;
  for(const b of [Z,R(1,16)])
    for(let iw=0;iw<3;iw++)for(let jw=0;jw<3;jw++)
      for(let mask=0;mask<8;mask++)for(let bl=0;bl<2;bl++){
        let labels=[mask&1,(mask>>1)&1,(mask>>2)&1];
        let X=prefix(iw,jw,labels,bl,b);
        const v=evaluate(X,b);
        if(eq(b,Z)){
          c0++;
          if(max0===null||cmp(v.legal,max0)>0){max0=v.legal;best0={stop_history:iw,B_history:jw,A_labels:labels,B_label:bl,skip_loss:s(v.loss)};}
          if(maxRelax0===null||cmp(v.full,maxRelax0)>0)maxRelax0=v.full;
        }else{
          c1++;
          if(max1===null||cmp(v.legal,max1)>0)max1=v.legal;
        }
      }
  ok(c0===144&&c1===144,"288 complete endpoint enumeration");
  ok(eq(maxRelax0,R(27,256)),"relaxed b0 max");
  ok(eq(max0,R(168127,1618176)),"legal b0 max");
  ok(eq(max1,HX.legal),"legal b1 max");
  ok(eq(sub(maxRelax0,HX.legal),R(11,16512)),"relaxed gap");
  ok(eq(sub(HX.legal,max0),R(17,18816)),"legal deficit");
  return {
    schema:"EC49AF_ENDPOINT_SKIP_COST_AUDIT_V1",
    eta:"1/4",support_direction:"alpha-(177/172)*beta",
    endpoint_prefixes:288,b_zero_count:c0,b_one_sixteenth_count:c1,
    exact_prefix_X_support:s(HX.legal),
    b_zero_relaxed_always_S_max:s(maxRelax0),
    b_zero_legal_max_after_optimal_skip:s(max0),
    b_one_sixteenth_legal_max:s(max1),
    relaxed_b_zero_surplus_over_X:s(sub(maxRelax0,HX.legal)),
    legal_b_zero_deficit_from_X:s(sub(HX.legal,max0)),
    example_optimal_b_zero_endpoint:best0,
    scope:"Finite 288 specified endpoint prefixes at this eta and r; not a universal all-real-prefix statement.",
    status:"AUTHOR_EXACT_FINITE_ENUMERATION / BIGINT_CHECK_PASS / UNREVIEWED / NOT_ADMITTED"
  };
};
console.log(JSON.stringify(endpointAudit(),null,2));
