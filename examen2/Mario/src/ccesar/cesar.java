package ccesar;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;

public class cesar {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static PrintStream flujo = System.out;
	public static int menu (String[] opciones) throws NumberFormatException, IOException {
		int op;
		do {
			for (String string : opciones) System.out.println(string);
			flujo.println("Opcion a ejecutar:");
			op = Integer.valueOf(br.readLine());
		}while(op < 1 || op > opciones.length);
		return op;
	}	
	
	public static String codificar(String letr, String txt, int despl) {
		String textocodificado="";
		char caracter;
		for (int i =0;i<txt.length();i++) {
			caracter=txt.charAt(i);
			int pos = letr.indexOf(caracter);
			if (pos==-1) {
				textocodificado+=caracter;
			}else {
				textocodificado+=letr.charAt((pos+despl)%letr.length());
			}
		}
		return textocodificado;
	}
	
	public static String descodificar(String letr,String txt, int despl) {
		String textodescodificado="";
		char caracter;
		for (int i =0;i<txt.length();i++) {
			caracter=txt.charAt(i);
			int pos = letr.indexOf(caracter);
			if (pos==-1) {
				textodescodificado+=caracter;
			}else {
				if(pos-3<0) {
					textodescodificado+=letr.charAt(letr.length()+(pos-3));
			}else {
				textodescodificado+=letr.charAt((pos-despl)%letr.length());
			}
		}
	}
		return textodescodificado;
	}
	
	
	public static void main(String[] args) throws IOException {
		String letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
		int desplazamiento=0;
		int op;
		String[]opciones= {"1.-Codificar","2.-Descodificar","3.-Salir"};	
		try {
			do {
				System.out.println("Que desea relizar:");
				op=menu(opciones);
				switch (op) {
				case 1:
					System.out.println("¿Texto a codificar?");
					String original=br.readLine().toUpperCase();
					System.out.println("¿De cuanto sera el desplazamiento?");
					try {
						desplazamiento=Integer.valueOf(br.readLine());
					}catch(NumberFormatException e) {
			            System.out.println("Ingreso mal el numero");
			        }
					String txtcod=codificar(letras,original,desplazamiento);
					System.out.println("Su texto codificado seria: "+txtcod);
					;
					break;
				case 2:
					System.out.println("¿Texto a descodificar?");
					String codificado=br.readLine().toUpperCase();
					System.out.println("¿De cuanto sera el desplazamiento?");
					try {
						desplazamiento=Integer.valueOf(br.readLine());
					}catch(NumberFormatException e) {
			            System.out.println("Ingreso mal el numero");
			        }
					String txtdes=descodificar(letras,codificado,desplazamiento);
					System.out.println("Su texto descodificado seria: "+txtdes);
					break;
				
				}
				if(op!=opciones.length) {
					System.out.println("Presione una tecla para continuar");
					String basura =br.readLine();
				}
				else {
					break;
				}
			}while(op!= opciones.length);
		
		
	}catch(NumberFormatException e) {
        System.out.println("Error");
    }

}
}
