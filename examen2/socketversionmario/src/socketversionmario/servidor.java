package socketversionmario;
import java.io.*;
import java.net.*;

	public class servidor {
	    public static void main(String[] args) throws IOException {
	        ServerSocket serverSocket = new ServerSocket(8080);
	        System.out.println("Servidor iniciado en el puerto 8080");
	 
	        while (true) {
	            Socket clientSocket = serverSocket.accept();
	            System.out.println("Cliente conectado");
	            clientSocket.close();
	        }
	    }
	}


