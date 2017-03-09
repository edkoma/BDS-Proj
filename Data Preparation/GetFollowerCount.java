import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;

import twitter4j.ResponseList;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import twitter4j.User;
import twitter4j.conf.ConfigurationBuilder;

public class GetFollowerCount {
	public static void main(String[] args) throws TwitterException, FileNotFoundException{
	ConfigurationBuilder cf = new ConfigurationBuilder();
    //Auth info redacted. Contact Edward if you want access to the accout, or you can make your 
    //own Twitter dev account.
	cf.setDebugEnabled(true)
	    .setOAuthConsumerKey()
	    .setOAuthConsumerSecret()
	    .setOAuthAccessToken()
	    .setOAuthAccessTokenSecret();
	
	TwitterFactory tf = new TwitterFactory(cf.build());
	twitter4j.Twitter twitter = tf.getInstance();
	int counter = 26;
	File file = new File("/Users/edkoma/Documents/workspace/GetFollowerCount/src/actorsnew.csv");
    @SuppressWarnings("resource")
	Scanner scanner = new Scanner(file,"UTF-8");

    ArrayList<String> actors = new ArrayList<String>();
    for (int k = 0; k < 200*(counter-1); k++){
    	String str = scanner.nextLine();
    }
    for (int j = 200*(counter-1)+1; j <= 5043 ; j++){
    	String str = scanner.nextLine();
    	String[] ar=str.split(",");
    	for( int i = 0; i <3; i ++){
    		if(!actors.contains(ar[i])){
        		actors.add(ar[i]);
        	}
    	}
    }

    
    Map<String,Integer> followersCount = new HashMap<String,Integer>();
    Iterator<String> iter = actors.iterator();
    
    while (iter.hasNext()) {
    	String actor = iter.next();
    	ResponseList<User> users = twitter.searchUsers(actor, 1);
    	String username = "@";
        for (User user : users) {
        		if(user.isVerified()){
        			username = "@" + user.getScreenName();
        			break;
        		}
        }
        int result;
        if (username.equals("@")){
        	result = 0;
        }
        else{    
    	    User user = twitter.showUser(username);
    	    result = user.getFollowersCount();
        }
        followersCount.put(actor, result);
        System.out.println(actor + " " + result);
    }
    
    Scanner scanner2 = new Scanner(file,"UTF-8");
    PrintWriter pw = new PrintWriter(new FileOutputStream(new File("/Users/edkoma/Documents/workspace/GetFollowerCount/src/result.csv"),true));
    StringBuilder sb = new StringBuilder();
    for (int g = 0; g < 200*(counter-1); g++){
    	String str = scanner2.nextLine();
    } 
   for (int j = 200*(counter-1)+1; j <= 5043; j++){
    	String str = scanner2.nextLine();
    	String[] ar=str.split(",");
    	for( int i = 0; i <2; i ++){
    		sb.append(followersCount.get(ar[i])+",");
    	}
    	sb.append(followersCount.get(ar[2])+"\n");
    }
   
    pw.write(sb.toString());
    pw.close();
    System.out.println("done!");
    }
}
