package Principal;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.util.ArrayList;

public class Buffer {
	public static PrintStream flujo = System.out;
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 ArrayList<Integer> elementos = new ArrayList<Integer>();
 public synchronized void poner(int elemento) throws InterruptedException {    
     elementos.add(elemento);
     System.out.println("Productor: Se ha producido el elemento " + elemento);
     notify();
 }
 public synchronized void tomar(int elemento) throws InterruptedException {    
     elementos.remove(elemento);
     System.out.println("Productor: Se ha tomado el elemento " + elemento);
     notify();
 }
 
	public static int menu (String[] opciones) throws NumberFormatException, IOException {
		int op;
		do {
			for (String string : opciones) System.out.println(string);
			flujo.println("Opcion a ejecutar:");
			op = Integer.valueOf(br.readLine());
		}while(op < 1 || op > opciones.length);
		return op;
	}
 
 public static void main(String[] args) throws IOException, InterruptedException {
	Buffer buffer = new Buffer();
	final int []numero= {0};
	Runnable productor = () -> {
		System.out.println("Numero a añadir?");		
			try {
				numero[0]=Integer.valueOf(br.readLine());
				buffer.poner(numero[0]);
			} catch (NumberFormatException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
	};
	Runnable consumidor = () -> {
		System.out.println("Numero a quitar?");		
			try {
				numero[0]=Integer.valueOf(br.readLine());
				buffer.tomar(numero[0]);
			} catch (NumberFormatException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
	};
	int op;
	String[]opciones= {"1.-Productor", "2.-Consumidor", "3.-Salir"};
	try {
		do {
		    System.out.println("Quien eres? :");
		    op = menu(opciones);
		    switch (op) {
		        case 1:
		            Thread productorThread = new Thread(productor);
		            productorThread.start();		           
		            break;
		        case 2:
		            Thread consumidorThread = new Thread(consumidor);
		            consumidorThread.start();
		            break;
		    }
		    if (op != opciones.length) {
		        System.out.println("Presione una tecla para continuar");
		        String basura = br.readLine();
		    } else {
		        break;
		    }
		} while (op != opciones.length);
		
	}catch(NumberFormatException e) {
        System.out.println("Ingreso mal las cantidades");
    }
	
}
}
 