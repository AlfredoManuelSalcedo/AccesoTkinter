package Tienda;

public class Producto {

	double precio;
	int stock;
	public Producto(double precio, int stock) {
		super();
		this.precio = precio;
		this.stock = stock;
	}
	public double getPrecio() {
		return precio;
	}
	public void setPrecio(double precio) {
		this.precio = precio;
	}
	public int getStock() {
		return stock;
	}
	public void setStock(int stock) {
		this.stock = stock;
	}
	@Override
	public String toString() {
		return "Producto [precio=" + precio + ", stock=" + stock + "]";
	}
	
	
}