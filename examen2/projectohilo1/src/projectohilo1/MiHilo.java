package projectohilo1;

public class MiHilo extends Thread {

	    public void run() {
	        System.out.println("Hola desde el hilo");
	    }

	public static void main(String[] args) {
		MiHilo miHilo = new MiHilo();
        miHilo.start();
	}

}
