// R762FA: exact 729-coordinate q9 positive BRC trit-7/trit-8 checks.
// g++ -O3 -std=c++17 R762FA_Q9_H7_H8_VERIFY.cpp -lgmp -o r762fa_verify
// ./r762fa_verify 7 && ./r762fa_verify 8
#include <gmp.h>
#include <vector>
#include <array>
#include <iostream>
#include <fstream>
#include <chrono>
#include <cstdint>
#include <cassert>
#include <cstdlib>
using namespace std;
constexpr int Q=9, D=Q*Q*Q;
constexpr int NLO=8, NHI=190;
int f(int n){return n<9 ? 0 : n/3-2;}
int ix(int x,int y,int z){return (x*Q+y)*Q+z;}
int main(int argc,char**argv){
  if(argc!=2){cerr<<"usage: ./verify <h=7 or 8>\n";return 2;}
  int H=atoi(argv[1]); if(H!=7&&H!=8)return 2;
  int T=18; for(int j=1;j<H;j++)T*=3;
  int PREV=T/3, MODSMALL=1;for(int j=0;j<H;j++)MODSMALL*=3;
  int LAST=T+NHI;
  auto t0=chrono::steady_clock::now();
  vector<array<int,D>> perm(6);
  const int branch[6][3]={{0,0,0},{1,0,0},{0,0,1},{1,1,0},{0,1,1},{1,1,1}};
  for(int j=0;j<6;j++)for(int x=0;x<Q;x++)for(int y=0;y<Q;y++)for(int z=0;z<Q;z++)
    perm[j][ix(x,y,z)]=ix((x-branch[j][0]+Q)%Q,(y-branch[j][1]+Q)%Q,(z-branch[j][2]+Q)%Q);
  mpz_t M,scale,tmp,q;
  mpz_inits(M,scale,tmp,q,NULL);mpz_ui_pow_ui(M,3,f(LAST)+H);mpz_set_ui(scale,1);
  mpz_t *v=new mpz_t[D],*w=new mpz_t[D];
  for(int i=0;i<D;i++){mpz_init_set_ui(v[i],i==0?1:0);mpz_init(w[i]);}
  vector<vector<uint16_t>> small(NHI+1),medium(NHI+1),longer(NHI+1);
  int snapcount=0;
  for(int n=0;n<=LAST;n++){
    bool a=n>=NLO && n<=NHI;
    bool b=n>=PREV+NLO && n<=PREV+NHI;
    bool c=n>=T+NLO && n<=T+NHI;
    if(a||b||c){
      int k=a?n:b?n-PREV:n-T;
      auto &dest=a?small[k]:b?medium[k]:longer[k];
      dest.resize(D);
      mpz_ui_pow_ui(scale,3,f(n));
      for(int i=0;i<D;i++){
        if(!mpz_divisible_p(v[i],scale)){cerr<<"FAIL integrality n="<<n<<" i="<<i<<endl;return 2;}
        mpz_divexact(q,v[i],scale);
        dest[i]=mpz_fdiv_ui(q,MODSMALL);
      }
      snapcount++;
    }
    if(n<LAST){
      for(int i=0;i<D;i++){
        mpz_set(w[i],v[perm[0][i]]);
        for(int j=1;j<6;j++)mpz_add(w[i],w[i],v[perm[j][i]]);
      }
      swap(v,w);
      if(n%12==11)for(int i=0;i<D;i++)mpz_mod(v[i],v[i],M);
    }
    if(n && n%2000==0)cerr<<"n="<<n<<" time="<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"s\n";
  }
  // Every post-window mod 3^h equality is checked on all 729 distinct coordinates.
  auto diff=[](const vector<uint16_t>&a,const vector<uint16_t>&b){for(int i=0;i<D;i++)if(a[i]!=b[i])return i;return -1;};
  vector<int> fail(NHI+1),lower_fail(NHI+1);
  for(int n=NLO;n<=NHI;n++){
    fail[n]=diff(small[n],longer[n]);
    lower_fail[n]=diff(small[n],medium[n]);
  }
  int N=-1;
  for(int n=NLO;n+126<=NHI;n++){
    bool ok=true;for(int j=n;j<n+127;j++)if(fail[j]>=0){ok=false;break;}
    if(ok){N=n;break;}
  }
  cout<<"{\"schema\":\"R762FA_Q9_EXACT_CERT_V1\",\"model\":\"full 729-terminal six-named positive BRC\",\"h\":"<<H<<",\"modulus\":"<<MODSMALL<<",\"period_candidate\":"<<T<<",\"prior_period\":"<<PREV<<",\"last_power\":"<<LAST<<",\"fixed_modulus_exponent\":"<<f(LAST)+H<<",\"snapshots\":"<<snapcount<<",\"first_127_equalities_start\":"<<N<<",\"full_coefficient_equalities\":"<<(N==-1?0:127*D)<<",\"first_lower_period_failure\":";
  int lower=-1;for(int n=max(N,NLO);n<=NHI;n++)if(lower_fail[n]>=0){lower=n;break;}
  if(lower==-1)cout<<"null";else cout<<"{\"n\":"<<lower<<",\"index\":"<<lower_fail[lower]<<",\"left\":"<<small[lower][lower_fail[lower]]<<",\"right\":"<<medium[lower][lower_fail[lower]]<<"}";
  cout<<",\"last_before_start_failure\":";
  if(N>NLO&&fail[N-1]>=0){int i=fail[N-1];cout<<"{\"n\":"<<N-1<<",\"index\":"<<i<<",\"left\":"<<small[N-1][i]<<",\"right\":"<<longer[N-1][i]<<"}";}else cout<<"null";
  cout<<"}\n";
  for(int i=0;i<D;i++){mpz_clear(v[i]);mpz_clear(w[i]);}delete[]v;delete[]w;mpz_clears(M,scale,tmp,q,NULL);
  return N==-1?1:0;
}
