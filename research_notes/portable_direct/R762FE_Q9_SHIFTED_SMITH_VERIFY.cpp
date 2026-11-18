// R762FE — shifted q=9 six-branch BRC 3-adic Smith certificate and explicit witness.
// Build: g++ -O3 -std=c++17 R762FE_Q9_SHIFTED_SMITH_VERIFY.cpp -lgmpxx -lgmp -o r762fe
// Run:   ./r762fe 140 > cert140.json && ./r762fe 180 > cert180.json
// Both precisions must return matching arrays e/b/penalties and witness valuations.
#include <gmpxx.h>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <chrono>
using namespace std;
constexpr int Q=9, D=729, R=126;
const int offsets[6][3]={{0,0,0},{1,0,0},{0,0,1},{1,1,0},{1,1,1},{0,1,1}};
// The order of the final two offsets does not change the named positive sum P.
// The six labelled steps are exactly {1,X,Z,XY,YZ,XYZ}.
int ix(int x,int y,int z){return (x*Q+y)*Q+z;}
int v3(const mpz_class&x,int prec){
 if(x==0)return prec;
 mpz_class t=x;int n=0;
 while(n<prec&&mpz_divisible_ui_p(t.get_mpz_t(),3)){
  mpz_divexact_ui(t.get_mpz_t(),t.get_mpz_t(),3);n++;
 }
 return n;
}
int main(int argc,char**argv){
 int prec=argc>1?atoi(argv[1]):140;
 if(prec<120){cerr<<"precision must be >=120 trits\n";return 2;}
 int steps=2*R;
 mpz_class modulus;mpz_ui_pow_ui(modulus.get_mpz_t(),3,prec);
 vector<vector<int>> src(6,vector<int>(D));
 for(int j=0;j<6;j++)for(int x=0;x<Q;x++)for(int y=0;y<Q;y++)for(int z=0;z<Q;z++)
  src[j][ix(x,y,z)]=ix((x-offsets[j][0]+Q)%Q,(y-offsets[j][1]+Q)%Q,(z-offsets[j][2]+Q)%Q);
 vector<mpz_class> state(D),temp(D),moments(steps+1);
 state[0]=1;
 vector<vector<mpz_class>> B(D,vector<mpz_class>(R));
 for(int n=0;n<=steps;n++){
  if(n>=1&&n<=R)for(int i=0;i<D;i++)B[i][n-1]=state[i];
  if(n>=1)moments[n]=state[0];
  if(n==steps)break;
  for(int i=0;i<D;i++){
   temp[i]=state[src[0][i]];
   for(int j=1;j<6;j++)temp[i]+=state[src[j][i]];
   mpz_mod(temp[i].get_mpz_t(),temp[i].get_mpz_t(),modulus.get_mpz_t());
  }
  swap(state,temp);
 }
 vector<vector<mpz_class>> H(R,vector<mpz_class>(R));
 for(int i=0;i<R;i++)for(int j=0;j<R;j++)H[i][j]=moments[i+j+1];
 auto H0=H;auto B0=B;
 vector<vector<mpz_class>> V(R,vector<mpz_class>(R));
 for(int i=0;i<R;i++)V[i][i]=1;
 vector<int> e(R),b(R),pen(R);
 auto start=chrono::steady_clock::now();
 for(int j=0;j<R;j++){
  int val=prec,ip=-1,kp=-1;
  for(int i=j;i<R;i++)for(int k=j;k<R;k++){
   int z=v3(H[i][k],prec);
   if(z<val){val=z;ip=i;kp=k;if(z==0)break;}
  }
  if(ip==-1){cerr<<"INSUFFICIENT precision at "<<j<<"\n";return 2;}
  if(ip!=j)swap(H[ip],H[j]);
  if(kp!=j){
   for(auto &row:H)swap(row[j],row[kp]);
   for(auto &row:B)swap(row[j],row[kp]);
   for(auto &row:V)swap(row[j],row[kp]);
  }
  mpz_class power;mpz_ui_pow_ui(power.get_mpz_t(),3,val);
  mpz_class quotient_mod=modulus/power;
  mpz_class pivot_unit=H[j][j]/power,inv;
  if(mpz_invert(inv.get_mpz_t(),pivot_unit.get_mpz_t(),quotient_mod.get_mpz_t())==0){cerr<<"inv fail";return 3;}
  for(int i=j+1;i<R;i++)if(H[i][j]!=0){
   assert(mpz_divisible_p(H[i][j].get_mpz_t(),power.get_mpz_t()));
   mpz_class factor=(H[i][j]/power)*inv % quotient_mod;
   H[i][j]=0;
   for(int k=j+1;k<R;k++){
    H[i][k]-=factor*H[j][k];
    mpz_mod(H[i][k].get_mpz_t(),H[i][k].get_mpz_t(),modulus.get_mpz_t());
   }
  }
  for(int k=j+1;k<R;k++)if(H[j][k]!=0){
   assert(mpz_divisible_p(H[j][k].get_mpz_t(),power.get_mpz_t()));
   mpz_class factor=(H[j][k]/power)*inv % quotient_mod;
   H[j][k]=0;
   for(auto &row:B){
    row[k]-=factor*row[j];
    mpz_mod(row[k].get_mpz_t(),row[k].get_mpz_t(),modulus.get_mpz_t());
   }
   for(auto &row:V){
    row[k]-=factor*row[j];
    mpz_mod(row[k].get_mpz_t(),row[k].get_mpz_t(),modulus.get_mpz_t());
   }
  }
  e[j]=val;int minv=prec;
  for(auto &row:B)minv=min(minv,v3(row[j],prec));
  b[j]=minv;pen[j]=e[j]-b[j];
  if(j%10==0||j==R-1)cerr<<"j="<<j<<" e="<<e[j]<<" b="<<b[j]
   <<" penalty="<<pen[j]<<" elapsed="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<" s\n";
 }
 // Directly test the *untransformed* matrices on the last column of V.
 int target=R-1,mh=prec,mb=prec,mi=-1;
 for(int i=0;i<R;i++){
  mpz_class z;
  for(int k=0;k<R;k++)z+=H0[i][k]*V[k][target];
  mpz_mod(z.get_mpz_t(),z.get_mpz_t(),modulus.get_mpz_t());
  mh=min(mh,v3(z,prec));
 }
 for(int i=0;i<D;i++){
  mpz_class z;
  for(int k=0;k<R;k++)z+=B0[i][k]*V[k][target];
  mpz_mod(z.get_mpz_t(),z.get_mpz_t(),modulus.get_mpz_t());
  int t=v3(z,prec);
  if(t<mb){mb=t;mi=i;}
 }
 if(mh!=e[target]||mb!=b[target]){cerr<<"WITNESS_FAIL mh="<<mh<<" mb="<<mb<<"\n";return 4;}
 int maxp=*max_element(pen.begin(),pen.end());
 int pos=max_element(pen.begin(),pen.end())-pen.begin();
 cout<<"{\"schema\":\"R762FE_SHIFTED_Q9_3ADIC_LATTICE_V1\",\"precision\":"<<prec
 <<",\"r\":"<<R<<",\"terminal_count\":"<<D<<",\"window_start\":1,\"moment_range\":[1,"<<2*R-1
 <<"],\"witness_Hvaluation\":"<<mh<<",\"witness_Bvaluation\":"<<mb
 <<",\"witness_Bcoordinate\":"<<mi<<",\"max_penalty\":"<<maxp
 <<",\"max_penalty_index\":"<<pos<<",\"max_exponent\":"<<*max_element(e.begin(),e.end())
 <<",\"sum_exponents\":";
 int total=0;for(int x:e)total+=x;
 cout<<total<<",\"e\":[";
 for(int j=0;j<R;j++)cout<<(j?",":"")<<e[j];
 cout<<"],\"b\":[";
 for(int j=0;j<R;j++)cout<<(j?",":"")<<b[j];
 cout<<"],\"penalties\":[";
 for(int j=0;j<R;j++)cout<<(j?",":"")<<pen[j];
 cout<<"]}"<<endl;
}
