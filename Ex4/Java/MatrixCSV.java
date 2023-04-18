package Dgemm;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;
import java.util.stream.DoubleStream;
import java.util.stream.IntStream;

public class Main {

    public static void main(String[] args) throws IOException, InterruptedException {
        double[][] A = MatrixCSV
                .readMatrixFromCsv("C:\\Users\\daion\\OneDrive\\Документы\\Practice01\\Ex4\\Python\\matrix_a.csv");
        double[][] B = MatrixCSV
                .readMatrixFromCsv("C:\\Users\\daion\\OneDrive\\Документы\\Practice01\\Ex4\\Python\\matrix_b.csv");
        double[][] C = MatrixCSV
                .readMatrixFromCsv("C:\\Users\\daion\\OneDrive\\Документы\\Practice01\\Ex4\\Python\\matrix_c.csv");

        long startTime = System.nanoTime();
        double[][] C1 = MatrixCSV.matMul(A, B);
        for (int i = 0; i < C1.length; i++) {
            for (int j = 0; j < C.length; j++) {
                double sum = 0.0;
                for (int k = 0; k < C.length; k++) {
                    sum += C1[i][k] * C[k][j];
                }
                C1[i][j] = 2.0 * sum;
            }
        }

        long elapsedTime = System.nanoTime() - startTime;
        String resWithoutMultithreading = String.format("Time without multithreading: %.4f seconds",
                TimeUnit.NANOSECONDS.toSeconds(elapsedTime)
                        + (double) TimeUnit.NANOSECONDS.toNanos(elapsedTime % TimeUnit.SECONDS.toNanos(1))
                                / TimeUnit.SECONDS.toNanos(1));
        System.out.println(resWithoutMultithreading);
        MatrixCSV.writeResultToFile(resWithoutMultithreading);

        // Matrix multiplication with multithreading
        startTime = System.nanoTime();
        double[][] C2 = MatrixCSV.matMulThreaded(A, B, 4);
        for (int i = 0; i < C2.length; i++) {
            for (int j = 0; j < C.length; j++) {
                double sum = 0.0;
                for (int k = 0; k < C.length; k++) {
                    sum += C2[i][k] * C[k][j];
                }
                C2[i][j] = 2.0 * sum;
            }
        }

        elapsedTime = System.nanoTime() - startTime;
        String resWithMultithreading = String.format("Time with multithreading: %.4f seconds",
                TimeUnit.NANOSECONDS.toSeconds(elapsedTime)
                        + (double) TimeUnit.NANOSECONDS.toNanos(elapsedTime % TimeUnit.SECONDS.toNanos(1))
                                / TimeUnit.SECONDS.toNanos(1));
        System.out.println(resWithMultithreading);
        MatrixCSV.writeResultToFile(resWithMultithreading);

        MatrixCSV.writeMatrixToCsv(C2, "C_result.csv");
    }

}
