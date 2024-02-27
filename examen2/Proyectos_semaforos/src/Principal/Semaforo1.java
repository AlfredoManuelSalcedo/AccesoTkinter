package Principal;

import java.util.concurrent.Semaphore;

public class Semaforo1 implements Runnable {
private static final Semaphore S1 = new Semaphore(2);
private final String nombre;

public Semaforo1(String nombre) {
	super();
	this.nombre = nombre;
}
 public void run() {
	 try {
		 S1.acquire();
		 System.out.println("Proceso: "+this.nombre+" dormido");
		 Thread.sleep(5000);
		 System.out.println("Proceso: "+this.nombre+" finalizado");
		 S1.release();
	 }catch(InterruptedException ex) {
		 ex.printStackTrace();
	 }
 }
}
