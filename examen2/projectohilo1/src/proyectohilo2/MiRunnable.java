package proyectohilo2;

public class MiRunnable implements Runnable {

	public void run() {
		  System.out.println("Hola desde el hilo");
	}

	public static void main(String[] args) {
		MiRunnable mirunable = new MiRunnable();
		Thread Hilo = new Thread(mirunable);
		Hilo.start();
	}
}
