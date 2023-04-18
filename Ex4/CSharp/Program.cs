using System;
using System.ComponentModel;
using System.Diagnostics.Metrics;
using System.Drawing;
using System.Reflection;
using System.Text;
using System.Threading.Tasks.Dataflow;
using System.Linq;
using System.Net.Cache;
using System.Reflection.Metadata;
using System.Collections.Generic;
using System.Collections;
using static MainClass;
using System.Runtime.CompilerServices;
using System.Text.RegularExpressions;
using System.Numerics;
using System.Xml.Linq;
using System.Runtime.Intrinsics.Arm;
using Microsoft.VisualBasic;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Threading;


public class MainClass
{
    static void Main(string[] args)
    {
        double[][] A = ReadMatrixFromCsv("C:\\Users\\daion\\OneDrive\\Документы\\Practice01\\Ex4\\Python\\matrix_a.csv");
        double[][] B = ReadMatrixFromCsv("C:\\Users\\daion\\OneDrive\\Документы\\Practice01\\Ex4\\Python\\matrix_b.csv");
        double[][] C = ReadMatrixFromCsv("C:\\Users\\daion\\OneDrive\\Документы\\Practice01\\Ex4\\Python\\matrix_c.csv");

        var stopwatch = new Stopwatch();
        stopwatch.Start();
        double[][] C1 = MatMul(A, B);
        C1 = C1.Select(row1 => C.Select(row2 => 2.0 * row1.Zip(row2, (x, y) => x * y).Sum()).ToArray()).ToArray();
        stopwatch.Stop();
        string resWithoutMultithreading = $"Time without multithreading: {stopwatch.Elapsed.TotalSeconds:F4} seconds";
        Console.WriteLine(resWithoutMultithreading);
        WriteResultToFile(resWithoutMultithreading);


        stopwatch.Reset();
        stopwatch.Start();
        double[][] C2 = MatMulThreaded(A, B, 4);
        C2 = C2.Select(row1 => C.Select(row2 => 2.0 * row1.Zip(row2, (x, y) => x * y).Sum()).ToArray()).ToArray();
        stopwatch.Stop();
        string resWithMultithreading = $"Time with multithreading: {stopwatch.Elapsed.TotalSeconds:F4} seconds";
        Console.WriteLine(resWithMultithreading);
        WriteResultToFile(resWithMultithreading);

        WriteMatrixToCsv(C2, "C_result.csv");

    }
    static double[][] ReadMatrixFromCsv(string filename)
    {
        var matrix = new double[0][];
        using (var reader = new StreamReader(filename))
        {
            while (!reader.EndOfStream)
            {
                var row = reader.ReadLine().Split(',');
                var newRow = new double[row.Length];
                for (int i = 0; i < row.Length; i++)
                {
                    newRow[i] = double.Parse(row[i], CultureInfo.InvariantCulture);
                }
                Array.Resize(ref matrix, matrix.Length + 1);
                matrix[matrix.Length - 1] = newRow;
            }
        }
        return matrix;
    }

    static void WriteMatrixToCsv(double[][] matrix, string filename)
    {
        using (var writer = new StreamWriter(filename))
        {
            foreach (var row in matrix)
            {
                writer.WriteLine(string.Join(",", row));
            }
        }
    }

    static void WriteResultToFile(string result)
    {
        using (var writer = new StreamWriter("C:\\Users\\daion\\OneDrive\\Документы\\Practice01\\Ex4\\Python\\results.csv", true))
        {
            writer.WriteLine("In C#");
            writer.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));
            writer.WriteLine(result);
        }
    }

    static double[][] MatMul(double[][] a, double[][] b)
    {
        int m = a.Length;
        int n = b[0].Length;
        int p = b.Length;
        double[][] c = new double[m][];
        for (int i = 0; i < m; i++)
        {
            c[i] = new double[n];
            for (int j = 0; j < n; j++)
            {
                double sum = 0.0;
                for (int k = 0; k < p; k++)
                {
                    sum += a[i][k] * b[k][j];
                }
                c[i][j] = sum;
            }
        }
        return c;
    }

    static void MatMulWorker(double[][] a, double[][] b, double[][] c, int startRow, int endRow)
    {
        int n = b[0].Length;
        int p = b.Length;
        for (int i = startRow; i < endRow; i++)
        {
            c[i] = new double[n];
            for (int j = 0; j < n; j++)
            {
                double sum = 0.0;
                for (int k = 0; k < p; k++)
                {
                    sum += a[i][k] * b[k][j];
                }
                c[i][j] = sum;
            }
        }
    }

    static double[][] MatMulThreaded(double[][] a, double[][] b, int numThreads)
    {
        int m = a.Length;
        int n = b[0].Length;
        double[][] c = new double[m][];
        Thread[] threads = new Thread[numThreads];
        for (int i = 0; i < numThreads; i++)
        {
            int startRow = i * m / numThreads;
            int endRow = (i + 1) * m / numThreads;
            threads[i] = new Thread(() => MatMulWorker(a, b, c, startRow, endRow));
            threads[i].Start();
        }
        foreach (Thread thread in threads)
        {
            thread.Join();
        }
        return c;
    }

}





