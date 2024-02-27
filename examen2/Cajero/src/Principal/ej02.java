package Principal;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ej02 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void comprar(String base) throws IOException, SQLException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	    System.out.println("¿De cuánto es tu compra?");
	    String costoStr = br.readLine();
	    double costo = Double.parseDouble(costoStr);

	    System.out.println("¿Cómo vas a pagarlo?");
	    String compra = br.readLine();

	    String tb[] = compra.split("#");
	    String separador[];
	    double cantidad_total = 0.00;
	    int numeros[] = { 5, 2, 1 };

	    for (String i : tb) {
	        separador = i.split("-");
	        cantidad_total += Double.parseDouble(separador[1]) * Integer.parseInt(separador[0]);
	    }

	    double resta_cantidad = cantidad_total - costo;

	    if (costo <= cantidad_total) {
	        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/"+base, "root", "root");
	             PreparedStatement ps = conn.prepareStatement("SELECT * FROM CAJERO WHERE CANTIDAD > 0 ORDER BY MONEDA DESC;")) {

	            boolean cambio = false;

	            for (String i : tb) {
	                separador = i.split("-");
	                String SQL_UPDATE = "UPDATE CAJERO SET CANTIDAD = CANTIDAD + " + separador[0] + " WHERE MONEDA = " + separador[1];
	                try (PreparedStatement preparedStatement = conn.prepareStatement(SQL_UPDATE)) {
	                    preparedStatement.executeUpdate();
	                }
	            }

	            do {
	                ResultSet resultSet = ps.executeQuery();
	                while (resultSet.next()) {
	                    double bbdd_moneda = resultSet.getDouble("MONEDA");
	                    int bbdd_cantidad = resultSet.getInt("CANTIDAD");

	                    if (bbdd_moneda <= resta_cantidad) {
	                        int resto = (int) (resta_cantidad / bbdd_moneda);

	                        if (resto <= bbdd_cantidad) {
	                            resta_cantidad = resta_cantidad - (bbdd_moneda * resto);
	                            String SQL_UPDATE2 = "UPDATE CAJERO SET CANTIDAD = CANTIDAD - " + resto + " WHERE MONEDA = " + bbdd_moneda;
	                            try (PreparedStatement ps1 = conn.prepareStatement(SQL_UPDATE2)) {
	                                ps1.executeUpdate();
	                                cambio = true;
	                            }
	                        } else {
	                            resta_cantidad = resta_cantidad - (bbdd_moneda * bbdd_cantidad);
	                            String SQL_UPDATE2 = "UPDATE CAJERO SET CANTIDAD = CANTIDAD - " + bbdd_cantidad + " WHERE MONEDA = " + bbdd_moneda;
	                            try (PreparedStatement ps1 = conn.prepareStatement(SQL_UPDATE2)) {
	                                ps1.executeUpdate();
	                                cambio = true;
	                            }
	                        }
	                    }
	                }

	                if (!cambio) {
	                    break;
	                }

	            } while (resta_cantidad > 0.01);

	        } catch (SQLException e) {
	            System.out.println(e);
	        }
	    } else {
	        System.out.println("Debe ingresar " + resta_cantidad + " a la compra");
	    }
	}
	
	
	public static void traspasar(String base) throws IOException {
		System.out.println("A que banco quieres transferir");
		 String bbdd2 = br.readLine();
		 verificar(bbdd2);
		 verificartbl(bbdd2);
		 String SQL_UPDATE2 = "update "+base+".cajero set cantidad =0"; 
		 String SQL_UPDATE = "update "+bbdd2+".cajero A set cantidad = (select A.cantidad+B.cantidad from "+base+".cajero B where B.moneda=A.moneda);";
			try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/sys","root","root");
					PreparedStatement preparedStatement = conn.prepareStatement(SQL_UPDATE)){
				PreparedStatement preparedStatement2 = conn.prepareStatement(SQL_UPDATE2);
				preparedStatement.execute();
				preparedStatement2.execute();
			}	catch (SQLException e) {
				System.err.format("SQL State: %s\n%s", e.getSQLState(),e.getMessage());
			} catch (Exception e) {
				e.printStackTrace();
			}
		 
	}
	
	public static void introducir(String base) throws IOException{
		System.out.println("Cuantas monedas vas a ingresar");
		String monedas = br.readLine();
		String spl1[]= monedas.split("#");
		try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/"+base,"root","root");)
				{
		for(String i: spl1) {
			String spl2[]=i.split("-");
			String SQL_UPDATE="UPDATE CAJERO set cantidad = cantidad + "+spl2[0]+" where moneda= "+spl2[1];
			PreparedStatement preparedStatement = conn.prepareStatement(SQL_UPDATE);
			preparedStatement.executeUpdate();
		}
			
			
		}	catch (SQLException e) {
			System.err.format("SQL State: %s\n%s", e.getSQLState(),e.getMessage());
			System.out.println("Error al introducir las monedas, intente de nuevo");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void verificar (String res) {
		String SQL_CREATE="CREATE DATABASE "+res;
		
		try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/","root","root");
				PreparedStatement preparedStatement = conn.prepareStatement(SQL_CREATE)){
			preparedStatement.execute();
			System.out.println("Base de datos creada creada");
			
		}	catch (SQLException e) {
			System.out.println("Banco seleccionado");
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	public static void verificartbl(String nom) {
		String SQL_CREATE="CREATE TABLE CAJERO("+
				"MONEDA DECIMAL(10,2) PRIMARY KEY,"+
				" CANTIDAD INT CHECK(CANTIDAD>=0)"+
				")";
		String SQL_INSERT="INSERT INTO CAJERO VALUES (?,?)";
		int[] numeros =  {5,2,1};
		int row=0;
		try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/"+nom,"root","root");
				PreparedStatement preparedStatement = conn.prepareStatement(SQL_CREATE);
						PreparedStatement otra = conn.prepareStatement(SQL_INSERT)){
			preparedStatement.execute();
for (int i=-2;i<=2;i++) {
	for (int j=0;j<numeros.length;j++) {
		otra.setDouble(1, (Math.pow(10, i)*numeros[j]));
		otra.setInt(2, 10);
		row += otra.executeUpdate();
	}
}
			
		}catch (SQLException e) {
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}
	
	public static void listar(String base){
		String SQL_SELECT = "select * from CAJERO";
		try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/"+base,"root","root");
				PreparedStatement preparedStatement = conn.prepareStatement(SQL_SELECT)){
			ResultSet resultSet = preparedStatement.executeQuery();
			
			while(resultSet.next()) {
				Double mnd= resultSet.getDouble ("Moneda");
				int qnt= resultSet.getInt("Cantidad");
				
				System.out.printf("%7.2f %s\n", mnd,qnt);
			}
		} catch (SQLException e) {
			System.err.format("SQL State: %s\n%s", e.getSQLState(),e.getMessage());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static int menu(String[] m) throws NumberFormatException, IOException {
		int opc;
		do {
			for(String c: m)System.out.println(c);
			 System.out.println("Introduzca su opcion");
			 opc=Integer.valueOf(br.readLine());
		}while(opc<1 || opc>m.length);
		return opc;
	}

	public static void main(String[] args) throws IOException, SQLException {
		System.out.println("¿Que banco vas a usar?");
		String bbdd=br.readLine();
		verificar(bbdd);
		verificartbl(bbdd);
		String opciones[]= {"1. -Listar banco","2. -Realizar compra", "3. -Introducir monedas", 
				"4. -Cambio banco", "5. -Traspasar Dinero", "6. -Salir"};
		int op;
	while(true){
		System.out.println("Usando la BBDD: "+bbdd);
		op=menu(opciones);
		switch(op) {
		case 1: //listar banco
			listar(bbdd);
			break;
		case 2: //Realizar compra
			comprar(bbdd);
			break;
		case 3: //Introducir monedas
			introducir(bbdd);
			break;
		case 4: //Cambio banco
			System.out.println("¿A que banco quieres cambiar?");
			String bbdd2 = br.readLine();
			verificar(bbdd2);
			verificartbl(bbdd2);
			bbdd= bbdd2;
			break;
		case 5: //Traspasar dinero
			traspasar(bbdd);
			break;
		}
		if(op!=opciones.length) {
			System.out.println("Presione una tecla para continuar");
			String basura =br.readLine();
		}
		else {
			break;
		}
	}
	}

}