"use strict";
const __EM_REPORT = (function(){
  const J=[1,2,3,4], SCALE=80;
  function assert(c,message){if(!c)throw Error(message);}
  function gcd(a,b){a=Math.abs(a);b=Math.abs(b);while(b){const t=a%b;a=b;b=t;}return a||1;}
  function norm(x){const g=gcd(x[0],x[1]);return [x[0]/g,x[1]/g];}
  function maxfrac(a,b){return a[0]*b[1]>=b[0]*a[1]?a:b;}
  function eqfrac(a,b){return a[0]*b[1]===b[0]*a[1];}
  function totals(a){return [a.reduce((x,y)=>x+y,0),a.reduce((x,y,i)=>x+y*J[i],0)];}
  function admissible(m,n){const a=totals(m),b=totals(n);return a[0]===b[0]&&a[1]===b[1];}
  function formula(m,n){
    assert(admissible(m,n),"moment mismatch");
    let best=[0,1];
    for(let j=0;j<J.length;j++){
      let S=0;
      for(let i=0;i<J.length;i++)S+=(m[i]-n[i])*Math.max(0,J[i]-J[j]);
      best=maxfrac(best,[2*S,2+J[j]]);
    }
    return norm(best);
  }
  function direct(m,n){
    assert(admissible(m,n),"moment mismatch");
    let ns=[[1,0],[-1,0],[0,1],[0,-1]];
    for(let j of J){ns.push([-j,2],[j,-2]);}
    let best=[0,1];
    for(let bits=0;bits<(1<<J.length);bits++){
      let Q=0,P=0;
      for(let i=0;i<J.length;i++)if(bits&(1<<i)){Q+=2*m[i];P+=m[i]*J[i];}
      for(const [a,b] of ns){
        let h=0;
        for(let i=0;i<J.length;i++)h+=n[i]*Math.max(0,2*a+b*J[i]);
        best=maxfrac(best,[a*Q+b*P-h,Math.abs(a)+Math.abs(b)]);
      }
    }
    return norm(best);
  }
  function physical(x){return norm([x[0],x[1]*SCALE]);}
  let profiles=[];
  for(let a=1;a<=4;a++)for(let b=1;b<=4;b++)
  for(let c=1;c<=4;c++)for(let d=1;d<=4;d++)
    profiles.push([a,b,c,d]);
  const classes=new Map();
  for(const m of profiles){const k=totals(m).join(":");if(!classes.has(k))classes.set(k,[]);classes.get(k).push(m);}
  let checked=0,positive=0,zero=0;
  for(const group of classes.values())for(let i=0;i<group.length;i++)
    for(let j=0;j<group.length;j++)if(i!==j){
      const f=formula(group[i],group[j]),v=direct(group[i],group[j]);
      assert(eqfrac(f,v),"formula/direct disagreement "+JSON.stringify([group[i],group[j],f,v]));
      checked++;if(f[0]>0)positive++;else zero++;
    }
  const n=[3,3,3,3],m1=[4,1,4,3],m2=[3,4,1,4],m12=[4,2,2,4];
  const d1=physical(formula(m1,n)),d2=physical(formula(m2,n)),d12=physical(formula(m12,n));
  assert(eqfrac(d1,[1,160])&&eqfrac(d2,[1,200])&&eqfrac(d12,[1,160]),"specific distances");
  assert(eqfrac(formula(n,m1),[0,1]),"convex order inclusion");
  assert(d1[0]*d2[1]*d12[1]+d2[0]*d1[1]*d12[1]>d12[0]*d1[1]*d2[1],"strict subadditivity");
  const result={
    status:"PASS_EXACT_INTEGER_RATIONAL",
    likelihood_ratios:["1/2","1","3/2","2"],
    mass_unit:"1/40",physical_coordinate_scale:80,
    number_of_positive_mass_profiles:profiles.length,
    equal_moment_classes:classes.size,
    independently_cross_checked_ordered_pairs:checked,
    positive_directed_distances:positive,
    zero_directed_distances:zero,
    check:"finite_call_deficit_formula_vs_exact_zonotope_vertex_facet_optimization",
    examples:{left:d1[0]+"/"+d1[1],right:d2[0]+"/"+d2[1],combined:d12[0]+"/"+d12[1],reverse_inclusion_distance:"0"}
  };
  return JSON.stringify(result,null,2);
})();
console.log(__EM_REPORT);
