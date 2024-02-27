package Principal;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.Month;

public class ejer01 {

	public static void main(String[] args) throws IOException {
		System.out.println("Año?");
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String añostr = br.readLine();
		int año = Integer.parseInt(añostr);
		
		for(Month mes : Month.values()) {
			LocalDate fecha = LocalDate.of(año, mes, mes.maxLength());
			
			while (fecha.getDayOfWeek() != DayOfWeek.FRIDAY) {
				fecha = fecha.minusDays(1);
			}
			System.out.println("El último viernes de: "+ mes+ " del "+ año+ " fue el dia "+ fecha.getDayOfMonth());
		}
		
		
	}

}
