// D25 reflected 2304-tail certificate through p^3; exact modular integer arithmetic.
// Node.js: node research_notes/portable_direct/d25_reflected_tail_second_digit_check_20261106.js
// Source pin c47e13e4aba0e006366f989d6334d443f6333ae3.
// Research author side only; no native H0/B0 computation or formal acceptance.
"use strict";
function mod(a,m){return (a%m+m)%m;}
function inv(a,m){let t=0,u=1,r=m,s=mod(a,m);while(s){const q=Math.floor(r/s);[t,u]=[u,t-q*u];[r,s]=[s,r-q*s];}if(r!==1)throw Error("nonunit inverse");return mod(t,m);}
function mpow(a,e,m){let v=1;a=mod(a,m);while(e){if(e%2)v=v*a%m;a=a*a%m;e=Math.floor(e/2);}return v;}
function assert(ok,label){if(!ok)throw Error("FAILED "+label);}
function isPrime(p){if(p<2)return false;for(let d=2;d*d<=p;d++)if(p%d===0)return false;return true;}
function check(p){
  assert(isPrime(p)&&p>3&&p<1000,"prime-bound");
  const m=p*p,h=(p-1)/2,L=Math.floor((2*p-1)/3);
  const k0=Math.floor(2*L/3),K=k0-(2*L-3*k0===1?1:0),J=h-K-1;
  const f=[1];for(let i=1;i<p;i++)f[i]=f[i-1]*i%m;
  const Wilson=mod(f[p-1]+1,m)/p;
  const H4=mod(mpow(f[h],4,m)-1,m)/p;
  const q48=mod(mpow(48,p-1,m)-1,m)/p;
  const beta=mod(2*Wilson-2+H4+q48,p);
  // Independent factorial-shell calculation (4k<2p, omit the single p).
  function directUnit(k){
    let n=1;for(let z=1;z<=4*k;z++)if(z!==p)n=n*z%m;
    const den=mpow(2304,k,m)*mpow(f[k],4,m)%m;
    return n*inv(den,m)%m;
  }
  assert(mod(directUnit(h)+1,m)/p===beta,"top-shell-beta");
  let direct=0, S0=0, S1=0, q=1, D=0;
  for(let j=0;j<=J;j++){
    const k=h-j,w=8*j+3;
    assert(4*j+1<p && p<=4*k && 4*k<2*p,"unit-window");
    direct=mod(direct+(8*k+1)*directUnit(k),m);
    S0=mod(S0+w*q,m);
    S1=mod(S1+mod(w*(D-beta)-4,p)*(q%p),p);
    if(j<J){
      const R=18*mpow(2*j+1,3,m)%m*
         inv((j+1)*(4*j+3)*(4*j+5)%m,m)%m;
      const lambda=mod(-4*inv(2*j+1,p)+[2,3,4,5].
        reduce((a,r)=>a+2*inv(4*j+r,p),0),p);
      q=q*R%m;D=mod(D+lambda,p);
    }
  }
  const reflected=mod(S0+p*S1,m);
  assert(reflected===direct,"reflected-vs-independent-factorial-"+p);
  return {p,h,K,J,tail_terms:J+1,Wilson,H4,q48,beta,
    S0_mod_p2:S0,S1_mod_p:S1,tail_over_p_mod_p2:direct,verified:true};
}
const primes=[5,7,11,13,17,19,23,31,37,43,61,67,139,211,373,997];
const rows=primes.map(check);
const expected={13:89,19:98,67:835,373:120175};
for(const [key,value] of Object.entries(expected)){
  const x=rows.find(z=>z.p===Number(key));
  assert(x.tail_over_p_mod_p2===value,"fixed-witness-"+key);
}
console.log(JSON.stringify({schema:"D25_REFLECTED_TAIL_SECOND_DIGIT_CHECK_V1",
 source_pin:"c47e13e4aba0e006366f989d6334d443f6333ae3",
 classification:"AUTHOR_EXACT_FINITE_VERIFIED_UNREVIEWED_NOT_ADMITTED",
 sample_count:rows.length, failures:0, native_H0B0:"NOT_RUN",rows},null,2));
