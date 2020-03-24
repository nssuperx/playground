using System;
 
class Program{
    static void Main(string[] args)
    {
        Console.WriteLine("Console.WriteLineで改行あり標準出力");
        Console.Write("Console.Write");
        Console.Write("で改行なし標準出力\n\n");
        int a = 1;
        double b = 1.0;
        var v1 = 1;
        var v2 = 1.0;
        var va = a;
        var vb = b;

        Console.WriteLine("int型 {0}, double型 {1:f4}",a,b);
        Console.WriteLine("var 整数 {0}, 少数 {1:f4}",v1,v2);
        Console.WriteLine("var型に代入したとき 整数 {0}, 少数 {1:f4}",va,vb);

        Console.WriteLine("int a = " + a.GetType());
        Console.WriteLine("double b = " + b.GetType());
        Console.WriteLine("varに整数代入 v1 = " + v1.GetType());
        Console.WriteLine("varに少数代入 v2 = " + v2.GetType());
        Console.WriteLine("varに整数の変数を代入 va = " + va.GetType());
        Console.WriteLine("varに少数の変数を代入 vb = " + vb.GetType());

        Console.WriteLine("\nConsole.WriteLineの詳しい書式は後で調べる");
    }
}
