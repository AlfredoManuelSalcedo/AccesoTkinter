package Principal;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramSocket;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;

public class Ej1 {
	private static ServerSocket serverSocket;
public static void main(String[] args) {
	String line;
	try {
		serverSocket = new  ServerSocket();
		System.out.println("Esperando conexion");
		InetSocketAddress addr =new InetSocketAddress("localhost",5678);
		serverSocket.bind(addr);
		Socket s = serverSocket.accept();
		System.out.println("Conexion establecida");
		BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream(),"UTF-8"));
		try {
			line=br.readLine();
			while(!line.equals("FIN")&& line !=null) {
				System.out.println(line);
				line=br.readLine();
			}
		}catch(NullPointerException ex) {
			System.out.println("Finalizada transmision...");
		}
		s.close();
		System.out.println("FIN");
	}catch(Exception e) {
		e.printStackTrace();
	}
}
}

