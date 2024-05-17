package com.stratonica.util.sync;

import com.stratonica.util.Conversion;

/**
 * SyncClient based upon client example at:
 *
 * @author www.codejava.net
 */
public class SyncClient extends SyncClientBase implements Runnable {

	private static final long MAX_SLEEP_TIME = 50;
	String groupID = "group";
	private int repeatCount;

	public SyncClient(String host, int port, String groupID) {
		super(host, port);
		this.groupID = groupID;
	}

	public static void main(String[] args) {

		String groupID = SyncBase.DEFAULT_GROUP;
		int port = SyncBase.DEFAULT_PORT;
		String host = SyncBase.DEFAULT_HOST;

		// test parameters
		int clientCount = 1;
		int repeatCount = 10;

		if (args.length > 0) {
			host = args[0];
		}
		if (args.length > 1) {
			port = Conversion.toInteger(args[1]);
		}

		SyncClient client = new SyncClient(host, port, groupID);
		
		// do this once, in one thread, before starting test
		client.deleteGroup(groupID);
		client.setClientCount(groupID, clientCount);
		
		for (int n = 0; n < clientCount; n++) {
			String instanceID1 = client.registerUser(groupID);
			System.out.println("NEW **& user id:" + instanceID1);
		}

		// client.waitForGroup();
		while (repeatCount-- > 0) {
			for (int n = 0; n < clientCount; n++) {
				client.sendWaiting(groupID);
			}
			for (int n = 0; n < clientCount; n++) {
				client.waitingToRun();
			}
			for (int n = 0; n < clientCount; n++) {
				client.updateRunning();
				;
			}
			for (int n = 0; n < clientCount; n++) {
				client.waitingOthers();
			}
		}

		client.deleteGroup(groupID);
	}

	public String setClientCount(int clientCount) {
		return getResponse("total " + this.groupID + " " + clientCount);
	}

	public Object sync(Object obj) {
		sendWaiting(groupID);
		waitingToRun();
		updateRunning();
		waitingOthers();
		return obj;
	}

	public void deleteGroup() {
		System.out.println(getResponse("delete " + this.groupID));
	}
	public void deleteGroup(String group) {
		System.out.println(getResponse("delete " + group));
	}

	private void sendWaiting(String group) {

		System.out.println(getResponse("waiting " + group));

	}

	private void sendRunning(String group) {
		System.out.println(getResponse("running " + group));
	}

	private String registerUser(String group) {
		return getResponse("new " + group);
	}

	public String setClientCount(String group, int i) {
		return getResponse("total " + group + " " + i);
	}

	public void sleep(long time) {
		try {
			Thread.sleep(time);
		} catch (InterruptedException e) {
		}
	}

	public void waitToRun() {
		String resp = null;

		do {
			resp = getResponse("status " + groupID);
			sleep(MAX_SLEEP_TIME);
		} while (!resp.toLowerCase().contentEquals("status " + SyncBase.GROUP_STATUS_GO));

		resp = getResponse("running " + groupID);

	}

	public void waitForOthers() {

		String resp = null;
		do {
			resp = getResponse("status " + groupID);
			sleep(MAX_SLEEP_TIME);
		} while (!resp.toLowerCase().contentEquals("status " + SyncBase.GROUP_STATUS_RUN));

		resp = getResponse("waiting " + groupID);

	}

	private void waitingToRun() {
		System.out.println("Waiting to run");
		sleep(MAX_SLEEP_TIME);

		waitToRun();

		System.out.println("Running...");

	}

	private void updateRunning() {
		System.out.println("Update running");

		sendRunning(groupID);
		System.out.println("Update Running complete");
		sleep(MAX_SLEEP_TIME);
	}

	private void waitingOthers() {
		System.out.println("... Run Done, Waiting for others");
		waitForOthers();
		System.out.println("Restarting");
	}

	public void setRepeatCount(int count) {
		this.repeatCount = count;
	}

	// Now this exists to simulate a parallel testNG run
	// In actual testNG, you would put these method calls in
	// using a client instance
	@Override
	public void run() {

		String instanceID1 = registerUser(groupID);
		System.out.println("NEW **& user id:" + instanceID1);

		while (repeatCount-- > 0) {
			System.out.println("**Sending Status Waiting");
			sendWaiting(groupID);
			System.out.println("**I am Waiting To Run");
			waitingToRun();
			System.out.println("**Updating status running");
			updateRunning();
			System.out.println("**Waiting for others");
			waitingOthers();
		}

	}

	public String pingServer() {
		return getResponse("ack");
	}

}
