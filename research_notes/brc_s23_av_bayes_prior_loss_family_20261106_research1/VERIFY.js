// Exact rational S23 AV prior-loss family verification; requires JS BigInt (Node >= 12).
function verify() {
  "use strict";
  let checks = 0, pairCount = 0, riskPoints = 0;
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b!==0n){const t=a%b;a=b;b=t;}return a;}
  class Q {
    constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const z=gcd(n,d);this.n=n/z;this.d=d/z;}
    add(v){return new Q(this.n*v.d+v.n*this.d,this.d*v.d);}
    sub(v){return new Q(this.n*v.d-v.n*this.d,this.d*v.d);}
    mul(v){return new Q(this.n*v.n,this.d*v.d);}
    div(v){return new Q(this.n*v.d,this.d*v.n);}
    cmp(v){const n=this.n*v.d-v.n*this.d;return n<0n?-1:n>0n?1:0;}
    abs(){return this.n<0n?new Q(-this.n,this.d):this;}
    toString(){return this.d===1n?String(this.n):`${this.n}/${this.d}`;}
  }
  const f=(n,d=1n)=>new Q(n,d),zero=f(0),one=f(1),half=f(1,2),bound=f(1,14);
  function eq(a,b,label){checks++;if(a.cmp(b)!==0)throw Error(`${label}: ${a} != ${b}`);}
  function test(flag,label){checks++;if(!flag)throw Error(label);}
  function sum(v){return v.reduce((z,x)=>z.add(x),zero);}
  function min(a,b){return a.cmp(b)<=0?a:b;}
  function risk(u,v,t){return sum(u.map((x,i)=>min(one.sub(t).mul(x),t.mul(v[i]))));}
  function tv(u,v){return sum(u.map((x,i)=>x.sub(v[i]).abs())).div(f(2));}
  const avals=[f(1,2),f(5,8),f(3,4),f(7,8)];
  const xvals=[f(1,2),f(5,8),f(3,4)];
  const yvals=[f(5,8),f(3,4),f(7,8)];
  for(const a of avals)for(const x of xvals)for(const y of yvals){
    if(x.cmp(y)>=0)continue;
    pairCount++;
    const q=one.sub(a),r=q.mul(x),s=q.mul(y),delta=y.sub(x);
    const A0=[a,zero,r,q.sub(r)],A1=[a,zero,s,q.sub(s)];
    const B0=[r,one.sub(r)],B1=[s,one.sub(s)];
    const k=one.sub(r).div(f(2).sub(r.add(s)));
    const h=one.sub(x).div(f(2).sub(x.add(y)));
    const m=a.mul(q).mul(delta).div(f(2).sub(q.mul(x.add(y))));
    eq(sum(A0),one,"A0 normalization");eq(sum(A1),one,"A1 normalization");
    eq(sum(B0),one,"B0 normalization");eq(sum(B1),one,"B1 normalization");
    eq(tv(A0,A1),q.mul(delta),"TV AV");
    eq(tv(B0,B1),q.mul(delta),"TV compressed");
    test(half.cmp(k)<0 && k.cmp(h)<0 && h.cmp(one)<0,"strict knot order");
    eq(m,a.mul(f(2).mul(k).sub(one)),"peak identity");
    test(m.cmp(bound)<=0,"family global upper bound");
    const knots=[zero,half,k,h,one];
    const pts=[...knots];
    for(let i=0;i<knots.length-1;i++)pts.push(knots[i].add(knots[i+1]).div(f(2)));
    for(const t of pts){
      const loss=risk(B0,B1,t).sub(risk(A0,A1,t));
      let expected;
      if(t.cmp(half)<=0)expected=zero;
      else if(t.cmp(k)<=0)expected=a.mul(f(2).mul(t).sub(one));
      else if(t.cmp(h)<=0)expected=q.mul(one.sub(x).sub(f(2).sub(x.add(y)).mul(t)));
      else expected=zero;
      eq(loss,expected,`loss piece (${a},${x},${y}; ${t})`);
      test(loss.cmp(zero)>=0,"data processing");
      test(loss.cmp(m)<=0,"peak upper envelope");
      riskPoints++;
    }
    eq(risk(B0,B1,half),risk(A0,A1,half),"equal-prior risk equality");
  }
  const a=half,x=half,y=f(7,8),q=one.sub(a),r=q.mul(x),s=q.mul(y);
  const k=one.sub(r).div(f(2).sub(r.add(s)));
  const peak=a.mul(q).mul(y.sub(x)).div(f(2).sub(q.mul(x.add(y))));
  eq(k,f(4,7),"sharp prior");eq(peak,bound,"sharp gap");
  for(const z of [f(1,8),f(1,4),f(3,8),half]){
    const derivative=f(16).sub(f(32).mul(z)).add(f(11).mul(z.mul(z)));
    test(derivative.cmp(zero)>0,"q envelope derivative positive");
  }
  return `PASS_EXACT_S23_AV_PRIOR_LOSS_FAMILY_20261106; pairs=${pairCount}; evaluated_priors=${riskPoints}; exact_assertions=${checks}; max=1/14 at (a,x,y,t)=(1/2,1/2,7/8,4/7)`;
}
console.log(verify());
