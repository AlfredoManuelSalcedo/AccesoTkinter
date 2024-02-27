package uno;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Palindromo {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static String reves(String derecho) {
		String atseupser= "";
		for(int i=derecho.length()-1;i>=0;i--) {
			char letra=derecho.charAt(i);
			atseupser += letra;
		}
		return atseupser;
	}
	
	public static void palindromo(String derecho, String reves) {
		if (derecho.equals(reves)) {
			System.out.println("La palabra si es un palindromo");
		}else {
			System.out.println("La palabra no es un palindromo");
		}
	}
	
	public static boolean verificarpalabra(String pal) {
		boolean lat= false;
		if(pal.matches("[a-zA-Z]+")) {
			lat=true;
		}
		return lat;
	};
	
	public static void main(String[] args) throws IOException {
		boolean latino=false;
		System.out.println("Dime su palabra: ");
		String respuesta = br.readLine().toLowerCase();
		latino = verificarpalabra(respuesta);
		if (latino) {
			String atseupser= reves(respuesta);
			palindromo(respuesta,atseupser);
		}else {
			System.out.println("Caracter no latino en la palabra");
		}
		
	}

}