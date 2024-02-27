package Principal;

import java.io.BufferedReader;
import java.io.InputStreamReader;



public class DemoContador {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Contador contador = new Contador();
        boolean opcion = true;
        while (opcion) {
        	 System.out.println("Inrementar o Decrementar");
             String opcionID = br.readLine().toUpperCase();
             final int[] incremento = {0};
             final int[] decremento = {0};
             if (opcionID.equals("INCREMENTAR")) {
            	 System.out.println("¿Cuanto va a incrementar?");
            	 incremento[0] = Integer.valueOf(br.readLine());
            	 Thread hiloIncrementar = new Thread(() -> {
            		    for (int i = 0; i < incremento[0]; i++) {
            		        contador.incrementar();
            		        System.out.println("Incrementando: " + contador.getCuenta());
            		    }
            		});
            	 hiloIncrementar.start();
            	 opcion =false;
             }
             else if(opcionID.equals("DECREMENTAR")) {
            	 System.out.println("¿Cuanto va a decrementar?");
            	 decremento[0] = Integer.valueOf(br.readLine());
            	 Thread hiloIncrementar = new Thread(() -> {
            		    for (int i = 0; i < decremento[0]; i++) {
            		    	 contador.decrementar();
            		         System.out.println("Decrementando: " + contador.getCuenta());
            		    }
            		});
            	 hiloIncrementar.start();
            	 opcion =false;
             }
             else {
            	 System.out.println("OPCION NO VALIDA");
             }
        }
       
    }
}