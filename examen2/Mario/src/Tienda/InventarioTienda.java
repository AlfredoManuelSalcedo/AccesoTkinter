package Tienda;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.util.HashMap;

public class InventarioTienda {
	public static PrintStream flujo = System.out;
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static int menu (String[] opciones) throws NumberFormatException, IOException {
		int op;
		do {
			for (String string : opciones) System.out.println(string);
			flujo.println("Opcion a ejecutar:");
			op = Integer.valueOf(br.readLine());
		}while(op < 1 || op > opciones.length);
		return op;
	}
	
	
	public static void agregar(HashMap<String, Producto> inv) throws IOException {
		String Nombre="";
		double precio;
		int cantidad;
		System.out.println("¿Como se llama el producto?");
		Nombre=br.readLine().toLowerCase();
		try {
			System.out.println("¿Cual sera su precio");
			precio=Double.valueOf(br.readLine());
			System.out.println("¿Cuanto stock se  tiene del producto?");
			cantidad=Integer.valueOf(br.readLine());
			Producto Nproducto = new Producto(precio, cantidad);
			inv.put(Nombre, Nproducto);
		}catch(IOException e) {
			System.out.println("Error al crear el producto: "+e.getMessage());
		}
		
	}

public static void actualizar(HashMap<String, Producto> inv) throws IOException {
	System.out.println("¿Que producto desea actualizar?");
	String Nombre = br.readLine().toLowerCase();
	if(inv.containsKey(Nombre)) {
		System.out.println("¿Cual es el nuevo Stock?");
		int cantidad=Integer.valueOf(br.readLine());
		try {
			Producto modificable= inv.get(Nombre);
			modificable.setStock(cantidad);
		}catch(Exception e) {
			e.getStackTrace();
		}
	}else {
		System.out.println("No existe ese producto");
	}
}

public static void consultaprecio(HashMap<String, Producto> inv) throws IOException {
	System.out.println("¿Que producto quieres consultar?");
	String Nombre=br.readLine().toLowerCase();
	if(inv.containsKey(Nombre)) {
		try {
			Producto consulta = inv.get(Nombre);
			double precio = consulta.getPrecio();
			System.out.println("El precio de: "+Nombre+" es: "+precio+"€");
		}catch(Exception e) {
			e.getStackTrace();
		}
	}
}

public static void listar(HashMap<String, Producto> inv) {
	for(String pro : inv.keySet()) {
		Producto uso = inv.get(pro);
		System.out.println(pro + "= Precio: " + uso.getPrecio() + "Stock: " + uso.getStock());
	}
}

public static void eliminar(HashMap<String, Producto> inv) {
	try {
		String porelim="";
		System.out.println("¿Que producto desea eliminar?");
	porelim=br.readLine().toLowerCase();
	inv.remove(porelim);
	}catch(Exception e) {
		e.printStackTrace();
	}
}
	

	public static void main(String[] args) throws NumberFormatException, IOException {
		HashMap <String, Producto> inventario = new HashMap <String, Producto> ();
		int op;
		String[]opciones= {"1.-Agregar un nuevo producto al inventario","2.-Actualizar la cantidad en stock de un producto existente", "3.-Consultar el precio de un producto por su nombre.",
				"4.-Listar todos los productos en el inventario con sus nombres, precios y cantidades en stock","5.-Eliminar un producto del inventario por su nombre","6.-Salir"};	
		try {
			do {
				System.out.println("Que desea relizar:");
				op=menu(opciones);
				switch (op) {
				case 1:
					agregar(inventario);
					break;
				case 2:
					actualizar(inventario);
					break;
				case 3:
					consultaprecio(inventario);
					break;
				case 4:
					listar(inventario);
					break;
				case 5:	
					eliminar(inventario);
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
            System.out.println("Ingreso mal las cantidades");
        }
		
		
	}

}