package proyectohilo4;

public class HiloLambda extends Thread{
public static void main(String[] args) {
	Thread hilo = new Thread(() -> System.out.println("Hola desde el hilo"));
	hilo.start();
}
}
