'use strict';
// Exact BigInt certificate for the coefficient-domain claims in R291.
function verify() {
  const N=48, MAX_M=3*N+5, DP_N=92;
  const zero=()=>Array(N+1).fill(0n);
  const at=(a,i)=>i<0||i>N?0n:a[i];
  const mult=(a,b)=>{const r=zero();for(let i=0;i<=N;i++)if(a[i]!==0n)for(let j=0;j+i<=N;j++)if(b[j]!==0n)r[i+j]+=a[i]*b[j];return r};
  function check(ok,msg){if(!ok)throw Error('FAIL: '+msg)}
  const h=zero();
  for(let n=1;n<=N;n++){
    let a=n===4?1n:0n;
    for(const [k,c] of [[1,1n],[2,2n],[3,1n],[4,1n]])a+=c*at(h,n-k);
    for(const [k,c] of [[1,1n],[2,2n],[3,1n]])
       for(let j=0;j<=n-k;j++)a+=c*h[j]*h[n-k-j];
    h[n]=a;
  }
  check(h.slice(0,4).every(x=>x===0n),"h order");
  check(h.slice(4).every(x=>x>=0n),"h positive");
  const w=zero();for(let i=0;i<=N;i++)w[i]=at(h,i)+at(h,i-1)+(i===0||i===1?1n:0n);
  const powers=[zero()];powers[0][0]=1n;
  for(let m=1;m<=MAX_M+2;m++)powers[m]=mult(powers[m-1],w);
  const gaps={'+':[],'-':[]};
  let coefficientTests=0, strictlyPositiveChecks=0;
  for(const s of ['+','-'])for(let m=s==='+'?1:2;m<=MAX_M;m++){
     const q=zero(),H=zero();
     for(let j=0;j<=N;j++){
       H[j]=s==='+'?at(powers[m+1],j)-at(powers[m+1],j-1)+at(powers[m+1],j-2)-at(powers[m+2],j-1):at(powers[m-1],j)-at(powers[m],j-1);
       q[j]=H[j]-at(q,j-1);
       const threshold=s==='+'?3*j-1:3*j;
       if(m>=threshold){check(q[j]>=0n,`uniform ${s} ${m} ${j}`);coefficientTests++;}
       if((s==='+'&&j>=1&&m>=3*j)||(s==='-'&&j>=2&&m>=3*j)){
          check(q[j]>0n,`strict ${s} ${m} ${j}`);strictlyPositiveChecks++;
       }
     }
     gaps[s][m]=q;
  }
  const sharp=[];
  for(let j=1;j<=3;j++){
    const plusM=3*j-2, minusM=3*j-1;
    const pv=gaps['+'][plusM][j], nv=gaps['-'][minusM][j];
    check(pv<0n&&nv<0n,'sharp j='+j);
    sharp.push({j,plus_below_m:plusM,plus_coefficient:pv.toString(),minus_below_m:minusM,minus_coefficient:nv.toString()});
  }
  const EDGES=[[[2,-1,-1],[2,1,-1]],[[0,-1,-1],[0,1,-1]],[[1,1,1],[2,1,-1]]];
  let states=new Map([['0,1,0,0',1n]]), sourceDPChecks=0, sourceDPEffectTerms=0;
  for(let n=0;n<=DP_N;n++){
    const effects=new Map();
    for(const [key,c] of states){const [q,e,k]=key.split(',').map(Number);if(q===0){const id=e+','+k;effects.set(id,(effects.get(id)||0n)+c)}}
    sourceDPEffectTerms+=effects.size;
    for(const s of ['+','-'])for(let m=s==='+'?1:2;m<=Math.min(n+2,MAX_M);m++){
      const e=s==='+'?1:-1, j=(n-m-2)/2;
      const p=(effects.get(e+','+(-m))||0n)-(effects.get(e+','+(-m-2))||0n);
      const exp=Number.isInteger(j)&&j>=0&&j<=N?gaps[s][m][j]:0n;
      check(p===exp,`raw-source ${n} ${s} ${m} j=${j}`);
      sourceDPChecks++;
    }
    const next=new Map();
    for(const [key,c] of states){const [q,e,k,prevZero]=key.split(',').map(Number);
      for(let b=0;b<2;b++){
        if(prevZero&&b===0)continue;
        const [q1,eta,d]=EDGES[q][b];
        const dest=[q1,eta*e,eta*k+d,b===0?1:0].join(',');
        next.set(dest,(next.get(dest)||0n)+c);
      }
    }
    states=next;
  }
  return {
    schema:'EM_R291_UNIFORM_MOVING_TAIL_CONES_V1',status:'PASS',
    input:{algebraic_source:'R288 author-side exact G_m forms; R286 h fixed point',h_equation:'h=y^4+(y+2y^2+y^3+y^4)h+y(1+y)^2*h^2',source_model:'ordered six-edge positive BRC clean-reset, full affine source effects'},
    proved_uniform_region:{plus:'forall j>=0,m>=max(1,3*j-1): [y^j]G^+_m>=0',minus:'forall j>=0,m>=max(2,3*j): [y^j]G^-_m>=0'},
    arithmetic:'JavaScript BigInt exact integer',algebraic_degree_end:N,max_m:MAX_M,
    uniform_nonnegative_coefficient_checks:coefficientTests,strict_positive_coefficient_checks:strictlyPositiveChecks,
    independent_source_dp_length_end:DP_N,independent_source_dp_effect_terms:sourceDPEffectTerms,
    independent_source_gap_checks:sourceDPChecks,below_boundary_negative_counterexamples:sharp,
    universal_proof:'coefficientwise binomial-h decomposition, positivity from ord_y h=4; see proof markdown',
    proof_dependencies_admitted:false,native_owner_verified:false,driver_review:'NOT_DONE'
  };
}
console.log(JSON.stringify(verify(),null,2));
