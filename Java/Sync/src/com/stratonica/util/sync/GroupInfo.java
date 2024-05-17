package com.stratonica.util.sync;

public class GroupInfo {
	
	Integer groupLastID = 0;
	Integer groupCount = null;
	Integer waiting = 0;
	Integer running = 0;
	String groupStatus = "init";
	
	public synchronized void addWaiting() {
		--running;
		++waiting;
		if (waiting == groupCount) {
			setGroupStatus(SyncBase.GROUP_STATUS_GO);
		}
	}
	public synchronized void addRunning() {
		++running;
		--waiting;
		if (waiting == 0) {
			setGroupStatus(SyncBase.GROUP_STATUS_RUN);
		}
	}

	public synchronized void setGroupStatus(String status) {
		groupStatus = status;
	}
	
	public synchronized Integer getNextID() {
		return ++groupLastID;
	}
	
	public synchronized Integer getGroupCount() {
		return groupCount;
	}
	
	public synchronized void setGroupCount(Integer count) {
		if (groupCount == null) {
			groupCount = count;
			running = count;
		}
	}

	public synchronized String getGroupStatus() {
		return groupStatus;
	}

}
