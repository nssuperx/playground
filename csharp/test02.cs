using System;
using System.Collections.Generic;

class Program{
    static void Main(string[] args){
        Console.WriteLine("標準入力頑張ります");
        string str1;
        int a;
        str1 = Console.ReadLine();
        Console.WriteLine("普通のConsole.ReadLine:"+str1);

        Console.WriteLine("整数1つだけ入力してね");
        a = int.Parse(Console.ReadLine());
        Console.WriteLine("int.Parseした" + a + "\n");
        Console.WriteLine("splitしてみる");
        Console.WriteLine("stringにぶち込む");
        string[] str = Console.ReadLine().Split(' ');
        Console.WriteLine("文字配列そのまま表示:");
        for(int i = 0;i < str.Length; i++){
            Console.WriteLine(str[i]);
        }

        Console.WriteLine("次は文字配列から数値だけ取り出してみる");
        string[] rawstr = Console.ReadLine().Split(' ');
        List<int> list = new List<int>();
        Console.WriteLine("int配列そのまま表示:");
        for(int i = 0;i < rawstr.Length; i++){
            int t;
            if(int.TryParse(rawstr[i], out t)){
                list.Add(t);
            }
        }
        
        Console.WriteLine("リストを配列に変換");
        int[] b = list.ToArray();

        for(int i = 0;i < b.Length; i++){
            Console.WriteLine(b[i]);
        }

        Console.WriteLine("foreachを使ってみる");
        foreach(int i in list){
            Console.WriteLine(i);
        }

        Console.WriteLine("やっぱりfor文でもやりたい\nlist.Countで要素数を取得できる");
        int lc = list.Count;
        for(int i = 0;i<lc;i++){
            Console.WriteLine(list[i]);
        }
        Console.WriteLine("C#標準入力,標準出力完全に理解した。");
    }
}