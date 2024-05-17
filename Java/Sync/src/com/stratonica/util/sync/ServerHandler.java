package com.stratonica.util.sync;
import java.net.*;
abstract class ServerHandler extends Thread{
	
	protected Socket socket;
	
	public ServerHandler(Socket socket) {
		this.socket = socket;
	};

}
