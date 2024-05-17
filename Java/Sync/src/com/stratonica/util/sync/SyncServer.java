package com.stratonica.util.sync;

import java.io.*;
import java.net.*;
import java.util.HashMap;
import java.util.Date;

import com.stratonica.util.Conversion;
 
/**
 * Sync Server, based upon server code at:
 * 
 * @author www.codejava.net
 */
public class SyncServer {
	
	private int port;
	// List<ClientStatus> clientStatus = new ArrayList<ClientStatus>();
	HashMap<String, GroupInfo> groupMap = new HashMap<String, GroupInfo>();

	public SyncServer(int port) {
		this.port = port;
	}
 
    public static void main(String[] args) {

   		int port = SyncBase.DEFAULT_PORT;
   	    	
    	if (args.length > 0) {
       		port = Conversion.toInteger(args[0]);
    	}
    	
    	(new SyncServer(port)).runServer();
    }

	private void runServer() {
       try (ServerSocket serverSocket = new ServerSocket(port)) {
        	 
            System.out.println("Server is listening on port " + port);
 
            while (true) {
                Socket socket = serverSocket.accept();
                new SyncServerThread(socket, this).start();
            }
 
        } catch (IOException ex) {
            System.out.println("Server exception: " + ex.getMessage());
            ex.printStackTrace();
        }
		
	}
	public void log(String msg) {
		System.out.println(curTime() + ": " + msg);
	}

	private long curTime() {
	     return (new Date()).getTime();
	}
}