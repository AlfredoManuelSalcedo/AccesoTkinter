package Principal;

public class Contador {
	private int cuenta;

    public Contador() {
        this.cuenta = 0;
    }

    public synchronized void incrementar() {
        cuenta++;
    }

    public synchronized void decrementar() {
        cuenta--;
    }

    public int getCuenta() {
        return cuenta;
    }

}
