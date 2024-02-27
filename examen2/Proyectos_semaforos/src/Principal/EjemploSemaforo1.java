package Principal;

public class EjemploSemaforo1 {
public static void main(String[] args) {
	for(int i =0; i<10;i++) {
		new Thread(new Semaforo1("Proceso#" +i)).start();
	}
}
}
