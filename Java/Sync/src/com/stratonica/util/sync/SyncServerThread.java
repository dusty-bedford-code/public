package com.stratonica.util.sync;

import java.io.*;
import java.net.*;

import com.stratonica.util.Conversion;

/**
 * This thread is responsible to handle client connection.
 *
 * @author www.codejava.net
 */
public class SyncServerThread extends ServerHandler {

	SyncServer theServer = null;
	SyncServerProcessor theProcessor;
	
	public SyncServerThread(Socket socket, SyncServer server) {
		super(socket);
		this.theServer = server;
		this.theProcessor = new SyncServerProcessor();
	}

	private String getClientMessage() {
		try {
			InputStream input = socket.getInputStream();
			BufferedReader reader = new BufferedReader(new InputStreamReader(input));
			return reader.readLine();
		} catch (IOException ex) {
			System.out.println("Server exception: " + ex.getMessage());
			ex.printStackTrace();
		}
		return "exception";
	}

	public void run() {

		String msg = getClientMessage();
		
		processMessage(msg);
		

	}

	private void processMessage(String msg) {
		
		theServer.log("Message:(" + msg + ")");
		String[] items = msg.split(" ");

		if (items.length < 1) {
			items = new String[2];
			items[0] = "status";
			items[1] = "default";
		}

		switch (items[0]) {
		case "clear":  // do this during test preparation
			clearGroup(items[1]);
			response(SyncBase.SUCCESS + " " + items[1]);
			break;
		case "delete":  // do this during test preparation
			deleteGroup(items[1]);
			response(SyncBase.SUCCESS + " " + items[1]);
			break;
		case "new":
			addGroup(items[1]);
			Integer nextID = getNextID(items[1]);
			response(SyncBase.SUCCESS + " " + items[1] + nextID);
			break;
		case "total":
			addGroup(items[1]);
			setTotal(items[1], Conversion.toInteger(items[2]));
			respSuccess();
			break;
		case "waiting":
			addWaitingUser(items[1]);
			respSuccess();
			break;
		case "running":
			addRunningUser(items[1]);
			respSuccess();
			break;
		case "status":
			response(SyncBase.STATUS + " " + groupStatus(items[1]));
			break;
		case "exception":
			break;
		case "groups":
			respSuccess();
			break;
		default:
			respAck();
			break;

		}
		
	}

	private synchronized void clearGroup(String group) {
		if (theServer.groupMap.get(group) != null) {
			theServer.groupMap.remove(group);
		}
		addGroup(group);
	}

	private synchronized void deleteGroup(String group) {
		if (theServer.groupMap.get(group) != null) {
			theServer.groupMap.remove(group);
		}
	}

	private synchronized GroupInfo addGroup(String group) {
		if (theServer.groupMap.get(group) == null) {
			theServer.groupMap.put(group, new GroupInfo());
		}
		return theServer.groupMap.get(group);
	}

	private synchronized void addRunningUser(String group) {
		GroupInfo grp = theServer.groupMap.get(group);
		grp.addRunning();

	}

	private synchronized void addWaitingUser(String group) {
		GroupInfo grp = theServer.groupMap.get(group);
		grp.addWaiting();
	}

	private synchronized String groupStatus(String group) {
		GroupInfo grp = theServer.groupMap.get(group);
		if (grp != null) {
			return grp.getGroupStatus();
		}
		return "no_such_group_" + group;

	}

	private synchronized Integer getNextID(String group) {

		GroupInfo grpInfo = theServer.groupMap.get(group);
		++grpInfo.groupLastID;
		grpInfo = theServer.groupMap.get(group);
		System.out.println("** Last ID" + grpInfo.groupLastID);
		return grpInfo.groupLastID;
	}

	private void respAck() {
		response(SyncBase.ACK);

	}

	private void respSuccess() {
		response(SyncBase.SUCCESS);

	}

	private void response(String msg) {
		try {
			OutputStream output = socket.getOutputStream();
			PrintWriter writer = new PrintWriter(output, true);
			writer.println(msg);
			socket.close();
		} catch (IOException ex) {
			System.out.println("Server exception: " + ex.getMessage());
			ex.printStackTrace();
		}

	}

	private synchronized void setTotal(String group, Integer count) {
		GroupInfo groupInfo = theServer.groupMap.get(group);
		if (groupInfo == null) {
			addGroup(group);
			groupInfo = theServer.groupMap.get(group);
		}
		groupInfo.setGroupCount(count);
	}

}
