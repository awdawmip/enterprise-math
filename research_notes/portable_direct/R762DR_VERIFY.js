#!/usr/bin/env node
// R762DR exact integer BRC verifier. No dependencies or floating-point operations in residue convolution.
// Generated from and identical to the executed function body below.
function verifyR762DR() {
  const MOD=2187, all=[], notable=[3,5,7], aVals=[2,3,4];
  let configurations=0, visited=0, checks=0, q9Cert=null;
  function gcd(a,b) {while(b){const t=a%b;a=b;b=t;}return a;}
  function comb(n,k){let v=1; for(let i=1;i<=k;i++)v=v*(n-i+1)/i;return Math.round(v);}
  function advance(a,q){const b=new Array(q*q).fill(0);for(let x=0;x<q;x++){let t=x*q,p=((x+1)%q)*q;for(let z=0;z<q;z++){const v=a[t+z];if(v===0)continue;const zz=(z+1)%q;b[t+z]+=v;b[p+z]+=2*v;b[t+zz]+=2*v;b[p+zz]+=v;}}return b.map(v=>v%MOD);}
  function powMod6(n){let v=1;for(let i=0;i<n;i++)v=v*6%MOD;return v;}
  function convert9(a){const o=Array.from({length:9},()=>new Array(9).fill(0));for(let x=0;x<9;x++)for(let z=0;z<9;z++){let v=a[x*9+z];if(!v)continue;for(let i=0;i<=x;i++)for(let j=0;j<=z;j++)o[i][j]=(o[i][j]+v*comb(x,i)*comb(z,j))%3;}const m=[];for(let i=0;i<9;i++)for(let j=0;j<9;j++)if(o[i][j])m.push([i,j,o[i][j]]);return m;}
  for(let exponent=2;exponent<=4;exponent++){
    const d=3**(exponent-1),q=3*d;let v=new Array(q*q).fill(0);v[0]=1;
    const transitions=[],witnesses={};
    for(let n=1;n<9*d;n++){
      v=advance(v,q);configurations++;visited+=q*q;
      let content=MOD,total=0;for(const x of v){content=gcd(content,x);total=(total+x)%MOD;}
      let expected=n<3*d?1:n<5*d?9:n<7*d?81:729;
      if(content!==expected)throw Error(`content error Q=${q} n=${n} got=${content} expected=${expected}`);
      checks++;
      if(total!==powMod6(n))throw Error(`mass error Q=${q} n=${n}`);
      checks++;
      if(notable.some(k=>n===k*d))transitions.push({n,gcd_mod_2187:content});
      if(n===7*d){
        const idx=v.findIndex(x=>x!==0);
        if(idx<0 || v[idx]%729!==0 || v[idx]%2187===0)throw Error("missing witness");
        witnesses.i=Math.floor(idx/q);witnesses.j=idx%q;witnesses.coeff_mod_2187=v[idx];
        if(q===9){
          if(v.some(x=>x%729!==0))throw Error("q9 divisibility missing");
          const monomials=convert9(v.map(x=>(x/729)%3));
          const expectedMonomials=[[3,3,1],[3,7,1],[3,8,1],[7,3,1],[7,7,1],[7,8,1],[8,3,1],[8,7,1]];
          if(JSON.stringify(monomials)!==JSON.stringify(expectedMonomials))throw Error("q9 exact polynomial certificate mismatch:"+JSON.stringify(monomials));
          q9Cert={Q:9,n:21,all_81_coefficients_divisible_by_729:true,quotient_mod_3_in_x_z_basis:monomials};
        }
      }
    }
    all.push({a:exponent,Q:q,d,n_checked:[1,9*d-1],transitions,witness_7d:witnesses,status:"PASS"});
  }
  return {schema:"R762DR_POSITIVE_BRC_INTEGER_CERTIFICATE_V1",result:"PASS",model:"F=1+2X+2Z+XZ in Z[C_Q^2], Q=3^a, a=2,3,4",arithmetic:"exact integer modular cyclic convolution, modulus 2187",configurations,coefficients_visited:visited,step_assertions:checks,verified_content:"1 (n<3d); 9 (3d<=n<5d); 81 (5d<=n<7d); 729 (7d<=n<9d)",run:all,Q9_exact_finite_polynomial_certificate:q9Cert,independent_review:"NOT_REVIEWED",native_TRIADIC_CLOSURE_E:"NOT_ESTABLISHED"};
}
console.log(JSON.stringify(verifyR762DR(),null,2));
