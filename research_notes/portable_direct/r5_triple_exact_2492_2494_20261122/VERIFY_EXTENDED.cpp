// R5 frozen five-event scalar model: exact finite-field jet witnesses at large thresholds.
// Research code: independent rational threshold generating-function implementation.
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
struct J{int v=0,d=0;};
int MOD;
J add(J a,J b){return {int((ll(a.v)+b.v)%MOD),int((ll(a.d)+b.d)%MOD)};}
J neg(J a){return {a.v ? MOD-a.v:0,a.d?MOD-a.d:0};}
J sub(J a,J b){return add(a,neg(b));}
J mul(J a,J b){return {int(ll(a.v)*b.v%MOD),int((ll(a.d)*b.v+ll(a.v)*b.d)%MOD)};}
int pw(int a,int k){ll z=1,x=a;while(k){if(k&1)z=z*x%MOD;x=x*x%MOD;k>>=1;}return int(z);}
J inv(J a){int b=pw(a.v,MOD-2);return {b,int((MOD-ll(a.d)*b%MOD*b%MOD)%MOD)};}
bool isprime(int a){if(a<2)return false;for(int i=2;ll(i)*i<=a;i++)if(a%i==0)return false;return true;}
vector<int> factors(int x){vector<int> a;for(int i=2;i*i<=x;i++)if(x%i==0){a.push_back(i);while(x%i==0)x/=i;}if(x>1)a.push_back(x);return a;}
int primitive(int n){auto f=factors(n);for(int k=2;k<MOD;k++){int x=pw(k,(MOD-1)/n);if(pw(x,n)!=1)continue;bool ok=true;for(int d:f)if(pw(x,n/d)==1)ok=false;if(ok)return x;}throw runtime_error("no primitive root");}
J ONE{1,0}, ZERO{0,0};
vector<J> gf(const vector<pair<int,J>>& factors,int N){vector<J> a(N+1);a[0]=ONE;for(auto [shift,z]:factors){for(int i=shift;i<=N;i++)a[i]=add(a[i],mul(z,a[i-shift]));}return a;}
J product(const vector<J>& x,const vector<int>& p){J z=ONE;for(int k:p)z=mul(z,sub(ONE,x[k]));return z;}
vector<J> single(const vector<J>& x,const vector<int>& p,int M){vector<J> out(M+1);J D=product(x,p);if(D.v==0 && D.d==0)return out;vector<pair<int,J>> den{{1,ONE}};for(int k:p)den.push_back({1,x[k]});auto a=gf(den,M-1);for(int m=1;m<=M;m++)out[m]=mul(D,a[m-1]);return out;}
vector<J> core(const vector<J>& x,int M){
 vector<int> U;for(int p=214;p<=221;p++)U.push_back(p);
 J D=product(x,U);J X=x[214],Y=x[215];
 vector<J> alpha(3),beta(3);
 for(int i=0;i<3;i++){
    alpha[i]=ONE;beta[i]=ONE;
    for(int j=0;j<3;j++)if(j!=i){
        alpha[i]=mul(alpha[i],inv(sub(ONE,mul(x[216+j],inv(x[216+i])))));
        beta[i]=mul(beta[i],inv(sub(ONE,mul(x[219+j],inv(x[219+i])))));
    }
 }
 vector<J> A(M+1);
 for(int s=0;s<3;s++)for(int r=0;r<3;r++){
    J V=x[216+s], Jv=x[219+r], w[3]={X,Y,Jv};
    J coef=mul(D,mul(alpha[s],beta[r]));
    for(int mask=1;mask<8;mask++){
       int k=__builtin_popcount((unsigned)mask);J Q=ONE;
       for(int i=0;i<3;i++)if(mask>>i&1)Q=mul(Q,w[i]);
       vector<pair<int,J>> den={{1,ONE},{1,V},{1,X},{1,Y},{1,Jv}};
       if(k>=2)den.push_back({k-1,Q});
       J sc=coef;
       if(k==1){
          if(Q.v==1){
             int special=0;for(int i=0;i<3;i++)if(mask>>i&1)special=(i==0?214:(i==1?215:219+r));
             J quotient=ONE;for(int t:U)if(t!=special)quotient=mul(quotient,sub(ONE,x[t]));
             sc=mul(quotient,mul(alpha[s],beta[r]));
          }else sc=mul(sc,inv(sub(ONE,Q)));
       }
       if(k%2)sc=neg(sc);
       vector<J> a=gf(den,M-1);
       for(int m=1;m<=M;m++){
         J v=neg(a[m-1]);
         if(m-1>=k)v=add(v,mul(Q,a[m-1-k]));
         A[m]=add(A[m],mul(sc,v));
       }
    }
 }
 return A;
}
int main(){
 vector<int> targets={1,4,37,43,54,60,64,112,113,114,115,116,124,125,126,127,128,2492,2493,2494,4988,6144,8638,8639,8640,11132,11133,11134,11135,11136,13628,13629,13630,16124,17280,19774,19775,19776};
 int M=*max_element(targets.begin(),targets.end());
 const vector<int> W={7,9,11,13,16,17,19,23,25,27,29,31,32,37,43};
 vector<int> S3,S4;for(int p=223;p<=290;p++)S3.push_back(p);for(int p=296;p<=312;p++)S4.push_back(p);
 cout<<"m,d,prime,root,R0,DR0,pole,witness\n";
 for(int d:W){
    MOD=10007;while(MOD%d!=1||!isprime(MOD))MOD++;
    int w=primitive(d);
    vector<J> x(315);for(int p=0;p<=314;p++){int v=pw(w,p%d);x[p]={v,int(ll(p)*v%MOD)};}
    auto A=core(x,M),B=single(x,S3,M),C=single(x,S4,M);
    int pole=0;for(int p=214;p<=314;p++)if(p%d==0)pole++;
    // Independent source anchors from the original joint-event integer DP,
    // published at enterprise-math@74c74c94d7971bdd8594824b734e574f85d43fd2.
    const vector<tuple<int,int,int,int>> anchors={
       {112,7,0,2421},{124,7,0,9953},
       {60,16,7049,9435},{124,16,3921,9189},
       {112,29,0,2537},{116,29,0,2876},
       {124,32,0,201},{128,32,0,5610},
       {112,43,952,6862},{124,43,0,8367},{128,43,0,7663},
       {124,37,4778,10024},{128,31,0,3657}
    };
    for(auto [m,ad,expected0,expected1]:anchors)if(ad==d){
       J R=sub(ONE,mul(mul(sub(ONE,A[m]),sub(ONE,B[m])),sub(ONE,C[m])));
       if(R.v!=expected0||R.d!=expected1){
          cerr<<"ANCHOR FAIL d="<<d<<" m="<<m<<" got="<<R.v<<","<<R.d<<" expected="<<expected0<<","<<expected1<<"\n";
          return 2;
       }
    }
    for(int m:targets){
       J R=sub(ONE,mul(mul(sub(ONE,A[m]),sub(ONE,B[m])),sub(ONE,C[m])));
       bool witness=pole>=3 && (R.v!=0 || (pole>=4 && R.d!=0));
       cout<<m<<','<<d<<','<<MOD<<','<<w<<','<<R.v<<','<<R.d<<','<<pole<<','<<(witness?1:0)<<'\n';
    }
    cerr<<"completed order "<<d<<" p="<<MOD<<" anchors PASS\n";
 }
}
