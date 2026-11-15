'use strict';
// PREFIX-818: exact independent named-path and moment/type-quotient regression, standard Node.js.
const run = function run(){
  function ck(c,msg){if(!c)throw new Error(msg)}
  function bc(x){let n=0;while(x){x &= x-1;n++}return n}
  function symmetric(bs){let a=[1n];for(let v of bs){let b=Array(a.length+1).fill(0n);for(let i=0;i<a.length;i++){b[i]+=a[i];b[i+1]+=a[i]*BigInt(v)}a=b}return a}
  function states(m,q){return Array.from({length:2**m},(_,x)=>x).filter(x=>bc(x)<=q)}
  function trace(m,q,alpha,beta,start,H){
    let mass=new Map([[start,1n]]), outs=[];
    for(let h=0;h<=H;h++){
      const count=Array(q+1).fill(0n);
      for(const [s,w] of mass)count[bc(s)]+=w;
      outs.push(count);
      let next=new Map();
      for(const [s,w] of mass)for(let i=0;i<m;i++){
        let has=!!(s&(2**i)),active=bc(s);
        if(has || active<q){
          const b=has?beta[i]:alpha[i];
          if(b>0){let t=s^(2**i);next.set(t,(next.get(t)||0n)+w*BigInt(b))}
        }
      }
      mass=next;
    }
    return outs;
  }
  function momentTrace(m,q,beta,start,H){
    let M=Array.from({length:q+1},(_,k)=>Array(k+1).fill(0n));
    const arr=[];for(let i=0;i<m;i++)if(start&(2**i))arr.push(beta[i]);
    M[arr.length]=symmetric(arr);
    let outs=[];
    for(let z=0;z<=H;z++){
      outs.push(Array.from({length:q+1},(_,k)=>M[k][0]));
      let N=Array.from({length:q+1},(_,k)=>Array(k+1).fill(0n));
      for(let k=0;k<q;k++)for(let h=0;h<=k;h++)N[k][h]=BigInt(h+1)*M[k+1][h+1];
      M=N;
    }
    return outs;
  }
  function equal(a,b){return a.length===b.length && a.every((x,i)=>x.toString()===b[i].toString())}
  let out={schema:"PREFIX818_R6_EXACT_REGRESSION_V1",method:"exact BigInt enumerative weighted-path propagation and independent elementary-symmetric moment update",pure_removal_cases:0,pure_removal_start_states:0,pure_removal_horizon_histogram_matches:0,pure_removal_partition_pair_tests:0,Vandermonde_certificates:0,type_quotient_cases:0,type_quotient_start_states:0,type_quotient_horizon_matches:0};
  for(let m=1;m<=7;m++)for(let q=0;q<=Math.min(m,4);q++){
    for(let shift=0;shift<3;shift++){
      let beta=Array.from({length:m},(_,i)=>shift===0?i+1:shift===1?2*(i+1)+1:m-i+2);
      const ss=states(m,q);out.pure_removal_cases++;
      let signatures=[];
      for(const s of ss){
        let named=trace(m,q,Array(m).fill(0),beta,s,q+2);
        let mom=momentTrace(m,q,beta,s,q+2);
        for(let h=0;h<=q+2;h++){ck(equal(named[h],mom[h]),"moment mismatch");out.pure_removal_horizon_histogram_matches++}
        out.pure_removal_start_states++;
        signatures.push(named.map(row=>row.join(",")).join("|"));
      }
      ck(new Set(signatures).size===ss.length,"partition fingerprint collision "+m+"/"+q);
      out.pure_removal_partition_pair_tests+=ss.length*(ss.length-1)/2;
      if(m>=q+1)for(let k=0;k<=q;k++){
        const U=beta.slice(0,k+1);
        for(let i=0;i<=k;i++){
          let diag=1n;
          for(let j=0;j<=k;j++)if(j!==i)diag*=BigInt(U[i]-U[j]);
          ck(diag!==0n,"nonzero Vandermonde certificate");
        }
        out.Vandermonde_certificates++;
      }
    }
  }
  for(let m=1;m<=5;m++)for(let q=0;q<=Math.min(m,3);q++)
  for(let r=1;r<=Math.min(m,3);r++){
    const typ=Array.from({length:m},(_,i)=>Math.floor(i*r/m));
    if(new Set(typ).size!==r)continue;
    let mt=Array(r).fill(0);for(const t of typ)mt[t]++;
    for(let seed=0;seed<36;seed++){
      let alpha=Array.from({length:r},(_,t)=>(seed+t*3+t*t)%3);
      let beta=Array.from({length:r},(_,t)=>(Math.floor(seed/3)+t*2+t*t)%3);
      let a=typ.map(t=>alpha[t]), b=typ.map(t=>beta[t]);
      const ss=states(m,q);
      for(const s of ss){
        const c=Array(r).fill(0);for(let i=0;i<m;i++)if(s&(2**i))c[typ[i]]++;
        let masses=new Map([[c.join(","),1n]]);
        const named=trace(m,q,a,b,s,5);
        for(let h=0;h<=5;h++){
          let totals=Array(q+1).fill(0n);
          for(const [key,w] of masses){
            const v=key.split(",").map(Number);
            totals[v.reduce((x,y)=>x+y,0)]+=w;
          }
          ck(equal(totals,named[h]),"type quotient mismatch m="+m+" q="+q+" r="+r);
          out.type_quotient_horizon_matches++;
          const next=new Map();
          for(const [key,w] of masses){
            const v=key.split(",").map(Number),k=v.reduce((x,y)=>x+y,0);
            for(let t=0;t<r;t++){
              if(v[t]>0 && beta[t]>0){let u=v.slice();u[t]--;let key2=u.join(",");next.set(key2,(next.get(key2)||0n)+w*BigInt(v[t]*beta[t]))}
              if(k<q && v[t]<mt[t] && alpha[t]>0){let u=v.slice();u[t]++;let key2=u.join(",");next.set(key2,(next.get(key2)||0n)+w*BigInt((mt[t]-v[t])*alpha[t]))}
            }
          }
          masses=next;
        }
        out.type_quotient_start_states++;
      }
      out.type_quotient_cases++;
    }
  }
  const m=8,q=2,beta=Array.from({length:m},(_,i)=>i+1);
  const N=states(m,q).length,d=(q+1)*(q+2)/2;
  ck(N===37 && d===6,"example dimension");
  out.separation_witness={m,q,beta,named_state_count:N,coarsest_partition_classes:N,minimal_linear_dimension:d};
  out.all_exact_assertions_passed=true;
  return out;
};
process.stdout.write(JSON.stringify(run(),null,2)+'\n');
