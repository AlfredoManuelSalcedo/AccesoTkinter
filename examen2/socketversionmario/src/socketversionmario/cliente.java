package socketversionmario;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;

public class cliente {
public static void main(String[] args) {
	 try {
         Socket socket = new Socket();
         InetSocketAddress addres = new InetSocketAddress ("localhost",8080);
         socket.connect(addres);
        socket.close();
     } catch (IOException e) {
         e.printStackTrace();
     }
}
}
