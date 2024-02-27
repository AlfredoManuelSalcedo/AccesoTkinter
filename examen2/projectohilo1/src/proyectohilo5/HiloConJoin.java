package proyectohilo5;

public class HiloConJoin extends Thread {
	public void run() {
        System.out.println("Hola desde el hilo "+(int)(Thread.currentThread().getId()));
    }
	public static void main(String[] args) throws InterruptedException {
		HiloConJoin hilo1 =new HiloConJoin();
		HiloConJoin hilo2 =new HiloConJoin();
		HiloConJoin hilo3 =new HiloConJoin();
		HiloConJoin hilo4 =new HiloConJoin();
		hilo1.start();
		hilo1.join();
		hilo2.start();
		hilo2.join();
		hilo3.start();
		hilo3.join();
		hilo4.start();
		hilo4.join();
		
	}
}
