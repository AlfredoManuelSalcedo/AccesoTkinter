package Principal;

class Semaforo {
    private String color;

    public Semaforo() {
        this.color = "Rojo";
    }

    public synchronized void cambiarColor(String nuevoColor, int tiempo) {
        System.out.println("Color: " + nuevoColor);
        this.color = nuevoColor;

        try {
            Thread.sleep(tiempo * 1000);  // Convierte segundos a milisegundos
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void iniciarSemaforo() {
        while (true) {
            cambiarColor("Rojo", 5);
            cambiarColor("Amarillo", 2);
            cambiarColor("Verde", 4);
        }
    }
}

public class SimulacionSemafaro {
    public static void main(String[] args) {
        Semaforo semaforo = new Semaforo();

        // Crear hilos para cada color
        Thread hiloRojo = new Thread(new Runnable() {
            @Override
            public void run() {
                semaforo.iniciarSemaforo();
            }
        });

        Thread hiloAmarillo = new Thread(new Runnable() {
            @Override
            public void run() {
                semaforo.iniciarSemaforo();
            }
        });

        Thread hiloVerde = new Thread(new Runnable() {
            @Override
            public void run() {
                semaforo.iniciarSemaforo();
            }
        });

        // Iniciar los hilos
        hiloRojo.start();
        hiloAmarillo.start();
        hiloVerde.start();
    }
}