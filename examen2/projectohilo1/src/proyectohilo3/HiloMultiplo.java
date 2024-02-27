package proyectohilo3;

public class HiloMultiplo extends Thread{
	public void run() {
        System.out.println("Hola desde el hilo "+(int)(Thread.currentThread().getId()));
    }
	public static void main(String[] args) {
		HiloMultiplo miHilo = new HiloMultiplo();
		HiloMultiplo miHilo1 = new HiloMultiplo();
		HiloMultiplo miHilo2 = new HiloMultiplo();
		HiloMultiplo miHilo3 = new HiloMultiplo();
		HiloMultiplo miHilo4 = new HiloMultiplo();
        miHilo.start();
        miHilo1.start();
        miHilo2.start();
        miHilo3.start();
        miHilo4.start();
	}
}
