using System;
 
class Program{
    static void Main(string[] args)
    {
        int x = 100;
        Console.WriteLine("値型の値渡し");
        Console.Write("{0} -> ",x);
        ValTest(x);
        Console.WriteLine("{0}",x);

        int[] xarray_a = new int[]{1,2,3};
        Console.WriteLine("参照型の値渡し:「参照」の書き換え");
        Console.Write("{0},{1},{2} -> ",xarray_a[0],xarray_a[1],xarray_a[2]);
        ArrayTestA(xarray_a);
        Console.WriteLine("{0},{1},{2}",xarray_a[0],xarray_a[1],xarray_a[2]);

        int[] xarray_b = new int[]{1,2,3};
        Console.WriteLine("参照型の値渡し:「参照先」の書き換え");
        Console.Write("{0},{1},{2} -> ",xarray_b[0],xarray_b[1],xarray_b[2]);
        ArrayTestB(xarray_b);
        Console.WriteLine("{0},{1},{2}",xarray_b[0],xarray_b[1],xarray_b[2]);
    }

    static void ValTest(int x){
        x = 10;
    }
    
    static void ArrayTestA(int[] xarray_a){
        xarray_a = new int[]{4,5,6};
    }

    static void ArrayTestB(int[] xarray_b){
        xarray_b[0] = 4;
        xarray_b[1] = 5;
        xarray_b[2] = 6;
    }
}
