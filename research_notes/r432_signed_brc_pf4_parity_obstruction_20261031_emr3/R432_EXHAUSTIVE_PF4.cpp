// R432: exact finite PF4 4x4 non-splitting minors, for 5<=r<=15.
// Input: r then all r-1 signed BRC coefficients a_0..a_(r-2)
// pre-divided by their positive row gcd. Use only r<=15:
// verify 24*(max a)^4 < 2^127 before passing; no floats in determinant.
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <array>
#include <algorithm>
#include <string>
#include <iostream>
#include <ctime>
using namespace std;
using i128=__int128_t;
static int perm[24][4],sgn[24],np=0;
void make_perm(){
 int p[4]={0,1,2,3};
 do{int s=1;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)if(p[i]>p[j])s=-s;
  for(int i=0;i<4;i++)perm[np][i]=p[i];sgn[np++]=s;
 }while(next_permutation(p,p+4));
}
string display(i128 v){
 if(v==0)return "0";bool neg=v<0;if(neg)v=-v;
 string out;while(v){out.push_back(char('0'+v%10));v/=10;}
 if(neg)out.push_back('-');reverse(out.begin(),out.end());return out;
}
struct Stat{
 long long checked=0,pos=0,neg=0,zero=0;
 vector<string> examples;
};
int main(int argc,char **argv){
 if(argc<2){cerr<<"Usage: ./R432_EXHAUSTIVE_PF4 r a0 ... a_(r-2)\n";return 1;}
 int r=atoi(argv[1]),n=r-2;
 if(r<5||r>15){cerr<<"This __int128 certificate only covers 5<=r<=15.\n";return 2;}
 if(argc!=n+3){cerr<<"Bad coefficient count.\n";return 1;}
 vector<long long>a(n+1);
 for(int i=0;i<=n;i++)a[i]=atoll(argv[i+2]);
 make_perm();
 auto at=[&](int h)->long long{return h<0||h>n?0:a[h];};
 int rows[4],cols[4];rows[0]=0;Stat st;
 auto det=[&]()->i128{
    long long M[4][4];
    for(int i=0;i<4;i++)for(int j=0;j<4;j++)M[i][j]=at(cols[j]-rows[i]);
    i128 sum=0;
    for(int t=0;t<24;t++){
        i128 x=M[0][perm[t][0]];
        if(!x)continue;
        x*=M[1][perm[t][1]];if(!x)continue;
        x*=M[2][perm[t][2]];if(!x)continue;
        x*=M[3][perm[t][3]];if(!x)continue;
        sum+=sgn[t]*x;
    }
    return sum;
 };
 clock_t start=clock();
 for(int g1=1;g1<=n;g1++)for(int g2=1;g2<=n;g2++)for(int g3=1;g3<=n;g3++){
    rows[1]=g1;rows[2]=g1+g2;rows[3]=g1+g2+g3;
    for(int j0=0;j0<=n;j0++){cols[0]=j0;
    for(int j1=max(rows[1],j0+1);j1<=rows[1]+n;j1++){cols[1]=j1;
    for(int j2=max(rows[2],j1+1);j2<=rows[2]+n;j2++){cols[2]=j2;
    for(int j3=max(rows[3],j2+1);j3<=rows[3]+n;j3++){cols[3]=j3;
        i128 d=det();st.checked++;
        if(d<0){
            st.neg++;
            if(st.examples.size()<12){
                string ex="{\"rows\":[";
                for(int z=0;z<4;z++){if(z)ex+=",";ex+=to_string(rows[z]);}
                ex+="],\"cols\":[";
                for(int z=0;z<4;z++){if(z)ex+=",";ex+=to_string(cols[z]);}
                ex+="],\"value\":\""+display(d)+"\"}";
                st.examples.push_back(ex);
            }
        }else if(d==0)st.zero++;else st.pos++;
    }}}}
 }
 double sec=double(clock()-start)/CLOCKS_PER_SEC;
 cout<<"{\"r\":"<<r<<",\"order\":4,\"checked\":"<<st.checked
     <<",\"positive\":"<<st.pos<<",\"negative\":"<<st.neg
     <<",\"zero\":"<<st.zero<<",\"negative_examples\":[";
 for(size_t z=0;z<st.examples.size();z++){if(z)cout<<",";cout<<st.examples[z];}
 cout<<"],\"cpu_seconds\":"<<sec<<"}"<<endl;
}
