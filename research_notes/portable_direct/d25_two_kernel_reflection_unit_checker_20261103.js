// D25 216/2304 reflection-unit congruence; p>=5. Exact modular integer arithmetic.
// Author-side check: not native H0/B0, not independent mathematical review.
"use strict";
function primes(N) {
  const s = new Uint8Array(N + 1).fill(1);
  s[0]=s[1]=0;
  for(let i=2;i*i<=N;i++) if(s[i]) for(let j=i*i;j<=N;j+=i) s[j]=0;
  return Array.from({length:N+1},(_,i)=>i).filter(i=>i>=5 && s[i]);
}
function modPow(a,n,p) {
  let x=1; a=((a%p)+p)%p;
  for(;n>0;n=Math.floor(n/2),a=a*a%p) if(n%2) x=x*a%p;
  return x;
}
function inv(a,p) {return modPow(a,p-2,p);}
const smallFactorial=[1,1,2,6];
function verify(p) {
  const U=new Array(4*p+1); U[0]=1;
  for(let n=1;n<U.length;n++) U[n]=U[n-1]*(n%p || 1)%p;
  const valuation=[0], hunit=[1], classes=[0,0,0],base=3*inv(32,p)%p;
  // Independent recurrence for h_k=c_k/b_k, retaining stripped p-factors.
  for(let k=0;k<p-1;k++) {
    const a=[4*k+1,4*k+2,4*k+3],b=[16,2*k+1,3*k+1,3*k+2];
    let x=1,y=1,d=0;
    for(let z of a) {if(z%p===0){z/=p;d++;}x=x*(z%p)%p;}
    for(let z of b) {if(z%p===0){z/=p;d--;}y=y*(z%p)%p;}
    valuation.push(valuation[valuation.length-1]+d);
    hunit.push(hunit[hunit.length-1]*x%p*inv(y,p)%p);
  }
  const examples=[];
  for(let k=1;k<p;k++) {
    const f4=Math.floor(4*k/p),f2=Math.floor(2*k/p),f3=Math.floor(3*k/p);
    const d=f4-f2-f3;
    if(valuation[k]!==d || valuation[p-k]!==-d) throw Error("valuation "+p+","+k);
    const den=U[2*k]*U[3*k]%p*smallFactorial[f2]*smallFactorial[f3]%p;
    const factorialUnit=U[4*k]*U[k]%p*smallFactorial[f4]%p
      *inv(den,p)%p*modPow(base,k,p)%p;
    if(hunit[k]!==factorialUnit) throw Error("factorial/recurrence "+p+","+k);
    const band=(4*k<p || 4*k>3*p) ? 0 : ((3*k<p || 3*k>2*p) ? 1 : 2);
    const target=((([3,-1,2][band]%p)+p)%p)*inv(16,p)%p;
    const actual=hunit[k]*hunit[p-k]%p;
    if(actual!==target) throw Error("reflection "+p+","+k);
    classes[band]++;
    if([1,Math.ceil(p/4),Math.floor(p/3)+1,Math.floor(2*p/3)+1,p-1].includes(k))
      examples.push({k,valuation:d,actual,target});
  }
  if(hunit[p-1]!==1) throw Error("terminal ratio "+p);
  return {p,classes,examples};
}
function main() {
  const ps=primes(2000), results=ps.map(verify);
  return {
    result:"PASS", primes:ps.length, index_checks:ps.reduce((s,p)=>s+p-1,0),
    interval:"all prime 5<=p<=2000", arithmetic:"exact modular integers",
    selected:results.filter(x=>[5,7,13,19,37,373].includes(x.p)),
    native_H0_B0:"NOT_EXECUTED", review:"NOT_ADMITTED"
  };
}
const report=main();
if(typeof console!=="undefined") console.log(JSON.stringify(report,null,2));
