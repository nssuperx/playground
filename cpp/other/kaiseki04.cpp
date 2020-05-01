#include<iostream>
#include<vector>
#include<numeric>
#include<cmath>
using namespace std;

int main(){
    vector<double> data{1.224,1.222,1.220,1.225,1.223,1.222,1.220,1.227,1.227,1.223};
    double e=0.0,ans=0.0,s=0.0,heikin;
    heikin = accumulate(data.begin(),data.end(),0.0) / data.size();
    for(int i=0;i<data.size();i++){
        s += pow(data.at(i) - heikin, 2.0);
    }
    s = sqrt(s / ((double)data.size() - 1.0));
    e = s / sqrt(data.size());
    ans = heikin + e;
    printf("heikin:%f\n",heikin);
    printf("gosa:%f\n",e);
    printf("ans:%f\n",ans);


    for(int i=0;i<data.size();i++){
        data.at(i) -= 0.015;
    }
    heikin = accumulate(data.begin(),data.end(),0.0) / data.size();
    for(int i=0;i<data.size();i++){
        s += pow(data.at(i) - heikin, 2.0);
    }
    s = sqrt(s / ((double)data.size() - 1.0));
    e = s / sqrt(data.size());
    ans = heikin + e;
    printf("heikin:%f\n",heikin);
    printf("gosa:%f\n",e);
    printf("ans:%f\n",ans);

}