package com.stratonica.util;

import java.util.HashMap;
import java.util.List;

public class Conversion {

	public static Integer toInteger(String data) {
		try {
			return Integer.parseInt(data);
		} catch(Exception e) {
			return null;
		}
	}
	
	public static Boolean toBoolean(String data) {
		if (data.length() == 0) return false;
		char ch = data.trim().toLowerCase().charAt(0);
		if (ch == 'y' || ch == 't') return true;
		return false;
	}
	
	public static String removeNonAlphanumeric(String str) {
	    if (str == null) {
	        return "";
	    }
	    StringBuilder sb = new StringBuilder();
	    for (char c : str.toCharArray()) {
	        if (Character.isLetterOrDigit(c) || c == '_') {
	            sb.append(c);
	        }
	    }
	    return sb.toString();
	}
	public static HashMap<String, String> toMap(List<String> elementAttributes) {

		HashMap<String, String> rtn = new HashMap<String, String>();
		for (String attr : elementAttributes) {
			
			String[] items = attr.split("=", 2);
			String key = attr;
			String value = null;
			if (items.length > 1) {
				 key = items[0];
				 value = items[1];
			} 
			rtn.put(key, value);
		}	
		return rtn;
	}


}
