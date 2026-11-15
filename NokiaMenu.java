
 
import java.util.Scanner;
	public class NokiaMenu{
		public static void main(String[] args){
	Scanner input= new Scanner(System.in);
	
	
	String mainMenu="""
	
	Main menu
	  1.Phone book
	  2.Messages
	  3.Chat
	  4.Call register
	  5.Tones
	  6.Settings
	  7.Call divert
	  8.Music
	  9.Games
	  10.Calculators
	  11.Reminders
	  12.Clock
	  13.Profile
	  14.Services
	  15.SIM services
	    """;
	    
	    System.out.println(mainMenu);
	    
	int mainMenuOption=input.nextInt();
	
	switch(mainMenuOption){
	  case 1:
	          String phonebookMenu= """
	          
	          Phone book Menu
	          1. Search
            2. Service Nos.
            3. Add name
            4. Erase
            5. Edit
            6. Copy
            7. Assign tone
            8. Send b’card
            9. Options
            10.Speed dials
            11. Voice tags
	  """;
	  
	   System.out.println(phonebookMenu);
	   
	   
	   
	   
	   
	   
	   int phonebookMenuOption=input.nextInt();
	   
	   switch(phonebookMenuOption){
	   case 1:
	          System.out.println("Search a number and name");
	           break;
	    
	    
	    case 2: 
	          System.out.println("Call Service number");
	           break;
	    case 3:
	           System.out.println("Save a number and name");
	           break;
	    case 4:
	           System.out.println("Delete phone number");
	            break;
	    case 5:
	          System.out.println("Edit phone number");
	            break;
	    case 6:
	          System.out.println("Copy name and  phone number");
	            break;
	    case 7:
	          System.out.println("Assign desired tone");
	            break;
	    case 8:
	          System.out.println("Send business card");
	            break;
	    case 9:
	            String optionMenu ="""
	              
	              Option menu
	              1.Memory in use
	              2.Type of view
	              3.Memory status
	              """;
	              System.out.println(optionMenu);
	              
	              int optionMenuOption = input.nextInt();
	              switch(optionMenuOption){
	                case 1:
	                  System.out.println("Memory in use checked");
	                case 2:
	                  System.out.println("Type of view checked");
	               case 3:
	                  System.out.println("Memory status checked");
	                  }
	                  
	              break;
	      case 10:
	             
	                  System.out.println("Set number 2-9 to speed dial");
	              break;
	              
	      case 11:
	                
	                  System.out.println("Dial a number by saying 1 or more word ");
	                  break;
	              
	              
	                   	   
	   
	   }
	   break;
case 2:
	          String messageMenu= """
	          
	          Messages menu
	          1. Write messages
            2. Inbox
            3. Outbox
            4. Picture messages
            5. Templates
            6. Smileys
            7. Message settings
            """;
            
            System.out.println(messageMenu);
            
            int messageMenuOption=input.nextInt();
            
            
switch(messageMenuOption){
case 1:
    System.out.println("Start message");
      break;
case 2:
    System.out.println("Save messages in inbox ");
      break;
case 3:
    System.out.println("view messages in outbox");
      break;
case 4:
    System.out.println("scroll to a picture message");
      break;
case 5:
    System.out.println("view, edit, or erase the preset template");
     break;
case 6:
    System.out.println("create smileys");
     break;
  case 7:
  String mesaggeSettingsMenu="""
  
  1.Set
  2.Common
  """;
  
      System.out.println(mesaggeSettingsMenu);    
      
      int mesaggeSettingsMenuOption= input.nextInt();
 switch(mesaggeSettingsMenuOption){
      case 1:  
      
          String setMenu ="""
          
          Set Menu
          
          1. Message centre number
          2. Messages sent as
          3. Message validity
          """;
          System.out.println(setMenu); 
          
          int setMenuOption= input.nextInt();
 switch (setMenuOption){
     case 1:      
          System.out.println("Use a center messages to text and  pictures messages");
          break;
      case 2:  
          System.out.println("Request the network to convert your message into E-mail, Fax, or Paging format");
          break;
      case 3:  
          System.out.println("Select the time period during which the message centre keeps and attempts to resend your message"); 
          break;
      }
        break;
           case 2:  
      
          String commonMenu ="""
          
          Set Common Menu
          
         1. Delivery reports
         2. Reply via same centre
         3. Character support
          """;
          System.out.println(commonMenu); 
          
          int commonMenuOption= input.nextInt();
          
               switch (commonMenuOption){
     case 1:      
          System.out.println("request the network to send delivery reports of your messages to keep track of the messages");
            break;
          
      case 2:  
          System.out.println("allow the recipient to reply using your message centre");
            break;
      case 3:  
          System.out.println("send messages using special characters"); 
            break;
      }
      break;
      }
      
      
      case 8: 
      System.out.println("service provider info");
      break;
 
case 9:
System.out.println("Type number to save to your voicemail box");
break;
 
case 10:
System.out.println("send service requests to your service provider");
break;
}
break;
 
 
  case 3: 
    System.out.println("Chat");
    break;
    
   case 4:
    String callRegisterMenu= """
	          
	          Call Register menu
	          1. Missed calls
            2. Received calls
            3. Dialled numbers
            4. Erase recent call lists
            5. Show call duration
            6. Show call costs
            7. Call cost settings
            """;
            
            System.out.println(callRegisterMenu);
            
            int callRegisterMenuOption=input.nextInt();
            
            
            switch(callRegisterMenuOption){
            
            case 1:
                  System.out.println("Missed calls");
                  break;
            case 2:
                  System.out.println("Received calls");
                   break;
            case 3:
                  System.out.println("Dialled numbers");
                   break;
            case 4:
                  System.out.println("Delete recent call lists");
                   break;
            case 5:
               String callDurationMenu= """
	          
	          Call Duration Menu
	          1. Last call duration
            2. All calls’ duration
            3. Received calls’ duration
            4. Dialled calls’ duration
            5. Clear timers
            """;
            
            System.out.println(callDurationMenu);
            
            int callDurationMenuOption=input.nextInt();
            
            switch(callDurationMenuOption){
            
            case 1: 
              System.out.println("call duration");
              break;
            case 2: 
              System.out.println("All calls’ duration");
              break;
            case 3: 
              System.out.println("Received calls’ duration");
              break;
            case 4: 
              System.out.println("Dialled calls’  duration"); 
              break;
             case 5:
              System.out.println("Clear timers");  
              break;
            
                }
                break;
 
  case 6:
              String callCostMenu= """
	          
	          Call Cost Menu
	        1. Last call cost
          2. All calls’ cost
          3. Clear counters
            """;
            
            System.out.println(callCostMenu);
            
            int callCostMenuOption=input.nextInt();
            
            switch(callCostMenuOption){
            
            case 1: 
              System.out.println("Last call cost");
              break;
            case 2: 
              System.out.println("All calls’ cost");
              break;
           case 3: 
              System.out.println("Clear counters");
              break;
                  
                  }
                break;
     case 7:
     
        String callCostSettingsMenu= """
	          
	          Call Cost Settings Menu
	       1. Call cost limit
         2. Show costs in
            """;
            
            System.out.println(callCostSettingsMenu);
            
            int callCostSettingsMenuOptions=input.nextInt();
            
            switch(callCostSettingsMenuOptions){
            
            case 1: 
              System.out.println("Call cost limit");
              break;
            case 2: 
              System.out.println("Show costs");
              break;
                  
                  }
                break;
                
                
          case 8:
          
                System.out.println("Use prepaid credit for calls");
                break;
                }
                
                
                
                
        case 5:
        
           String tonesMenu= """
            Tones menu
            1. Ringing tone
            2. Ringing volume
            3. Incoming call alert
            4. Message alert tone
            5. Keypad tones
            6. Warning tones
            7. Vibrating alert
            8. Screen saver
            """;
            
            System.out.println(tonesMenu);
            
            int tonesMenuOptions= input.nextInt();
            switch (tonesMenuOptions){
            
            case 1:
            System.out.println("select the tone that you hear when you receive a call");
            break;
 
 
            case 2:
            System.out.println("set the volume level for the ringing and message alert tones");
            break;
 
 
            case 3:
            System.out.println("select the way the phone notifies you of incoming voice calls");
            break;
 
 
            case 4:
            System.out.println("set the tone that you hear when you receive a text message.");
            break;
 
 
            case 5:
            System.out.println("set the volume for keypad tones.");
            break;
 
 
            case 6:
            System.out.println("set the phone to sound tones");
            break;
 
 
            case 7:
            System.out.println("set the phone to vibrate when you receive a call or a text message");
            break;
 
 
            case 8:
            System.out.println("select the picture that is displayed in standby mode after a specified time");
            break;
            
            
            
            
            
            
            }
            
        
      break;
      
      
case 6:
String settingsMenu="""
 SETTINGS MENU 
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
""";
 
System.out.println(settingsMenu);
int settingsMenuOption = input.nextInt();
 
 
switch(settingsMenuOption){
 
case 1:
 
String callSettingsMenu="""
 
 CALL SETTINGS OPTIONS
 
1.Automatic redial
 
2.Speed dialling
 
3.Call waiting options
 
4.Own number sendng
 
5.Phone line in use
 
6.Automatic answer
 
""";
 
System.out.println(callSettingsMenu);
int callSettingsMenuOptions= input.nextInt();
 
switch(callSettingsMenuOptions){
 
case 1:
  System.out.println("Set automatic redial");
  break;
case 2:
  System.out.println("Set speed dial");
  break;
case 3:
  System.out.println("Set call waiting settings");
  break;
case 4:
  System.out.println("Dislay your own number");
  break;
case 5:
  System.out.println("select the phone line");
  break;
case 6:
  System.out.println("set Automatic answer");
  break;
 
 
 
}
 break;
 
 
 
case 2:
 
String phoneSettingsMenu="""
 
 PHONE SETTINGS OPTIONS
 
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
""";
 
System.out.println(phoneSettingsMenu);
int phoneSettingsMenuOption= input.nextInt();
 
switch(phoneSettingsMenuOption){
 
case 1:
  System.out.println("Select language");
  break;
case 2:
  System.out.println("set the phone to indicate  cellular network based");
  break;
case 3:
  System.out.println("Write welcome note");
   break;
case 4:
  System.out.println("Select network");
   break;
case 5:
  System.out.println("set to show or hide confirmation messages");
   break;
  
  }
   break;
 
 
case 3:
 
String securitySettingsMenu="""
 
 SECURITY SETTINGS OPTIONS
 
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes
""";
 
System.out.println(securitySettingsMenu);
int securitySettingsMenuOption= input.nextInt();
 
switch(securitySettingsMenuOption){
 
case 1:
  System.out.println("Request pin");
  break;
case 2:
  System.out.println("restrict the making and receiving of calls");
  break;
case 3:
  System.out.println("restrict your outgoing calls to selected phone numbers");
   break;
case 4:
  System.out.println("specify a group of people whom you can call and who can call you");
   break;
case 5:
  System.out.println("set the phone to ask for the security code");
   break;
case 6:
  System.out.println("change the security code, PIN code, PIN2 code, or barring password");
   break;   
}
  break;
  
case 4:
      System.out.println("reset the menu settings to their original values");
}
break;
 
case 7:
      System.out.println(" Set Call divert");
      break;
case 8:
      String musicMenu="""
      MUSIC MENU
1. Music player
2. Radio
3. Recorder
4. Track list
 
""";
 
 
 
System.out.println(musicMenu);
 
 
int musicMenuOption=input.nextInt();
 
switch(musicMenuOption){
 
case 1:
System.out.println("Play music tracks");
break;
 
case 2:
System.out.println("Listen to radio");
break;
case 3:
System.out.println("Record music");
break;
 
case 4:
System.out.println("Make track lists");
break;
 
}
      break;
      
case 9:
 System.out.println(" Select Games");
 break;
case 10:
System.out.println("Calculator");
break;
case 11:
System.out.println("save short text notes with an alarm for reminders");
break;     
 
case 12 :
  String clockMenu="""
CLOCK MENU
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
""";
System.out.println(clockMenu);
int clockMenuOption= input.nextInt();
 
switch(clockMenuOption){
 
 case 1:
 System.out.println("set the alarm to go off at the desired time");
 break;
 case 2:
 System.out.println("set the phone to show the current time");
 break;
 case 3:
 System.out.println("set the correct date");
 break;
 case 4:
 System.out.println("set stopwatch");
 break;
 case 5:
 System.out.println("set a countdown");
 break;
 case 6:
 System.out.println("set to auto update date and time");
 break;
 
 
}
  break;
  
case 13:
System.out.println("edit, manage, and create profile");
  break;
  
case 14:
System.out.println("access various WAP");
  break;
case 15:
System.out.println("SIM Services Menu");
break; 
}
            
            
            
            
            
            
            
            
            
            }
  
      }
            
            
	          
	   
	  
	  
	  
	
 
 
 
