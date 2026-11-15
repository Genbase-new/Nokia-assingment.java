main_menu = """
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
"""

print(main_menu)

main_menu_option = int(input())

match main_menu_option:

    case 1:
        phone_book_menu = """
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
"""
        print(phone_book_menu)

        phone_book_menu_option = int(input())

        match phone_book_menu_option:
            case 1:
                print("Search a number and name")
            case 2:
                print("Call Service number")
            case 3:
                print("Save a number and name")
            case 4:
                print("Delete phone number")
            case 5:
                print("Edit phone number")
            case 6:
                print("Copy name and  phone number")
            case 7:
                print("Assign desired tone")
            case 8:
                print("Send business card")
            case 9:
                option_menu = """
Option menu
1.Memory in use
2.Type of view
3.Memory status
"""
                print(option_menu)

                option_menu_option = int(input())

                match option_menu_option:
                    case 1:
                        print("Memory in use checked")
                    case 2:
                        print("Type of view checked")
                    case 3:
                        print("Memory status checked")
            case 10:
                print("Set number 2-9 to speed dial")
            case 11:
                print("Dial a number by saying 1 or more word ")

    case 2:
        message_menu = """
Messages menu
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
"""
        print(message_menu)

        message_menu_option = int(input())

        match message_menu_option:
            case 1:
                print("Start message")
            case 2:
                print("Save messages in inbox ")
            case 3:
                print("view messages in outbox")
            case 4:
                print("scroll to a picture message")
            case 5:
                print("view, edit, or erase the preset template")
            case 6:
                print("create smileys")
            case 7:
                message_settings_menu = """
1.Set
2.Common
"""
                print(message_settings_menu)

                message_settings_menu_option = int(input())

                match message_settings_menu_option:
                    case 1:
                        set_menu = """
Set Menu

1. Message centre number
2. Messages sent as
3. Message validity
"""
                        print(set_menu)

                        set_menu_option = int(input())

                        match set_menu_option:
                            case 1:
                                print("Use a center messages to text and  pictures messages")
                            case 2:
                                print("Request the network to convert your message into E-mail, Fax, or Paging format")
                            case 3:
                                print("Select the time period during which the message centre keeps and attempts to resend your message")
                    case 2:
                        common_menu = """
Set Common Menu

1. Delivery reports
2. Reply via same centre
3. Character support
"""
                        print(common_menu)

                        common_menu_option = int(input())

                        match common_menu_option:
                            case 1:
                                print("request the network to send delivery reports of your messages to keep track of the messages")
                            case 2:
                                print("allow the recipient to reply using your message centre")
                            case 3:
                                print("send messages using special characters")
            case 8:
                print("service provider info")
            case 9:
                print("Type number to save to your voicemail box")
            case 10:
                print("send service requests to your service provider")

    case 3:
        print("Chat")

    case 4:
        call_register_menu = """
Call Register menu
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
"""
        print(call_register_menu)

        call_register_menu_option = int(input())

        match call_register_menu_option:
            case 1:
                print("Missed calls")
            case 2:
                print("Received calls")
            case 3:
                print("Dialled numbers")
            case 4:
                print("Delete recent call lists")
            case 5:
                call_duration_menu = """
Call Duration Menu
1. Last call duration
2. All calls’ duration
3. Received calls’ duration
4. Dialled calls’ duration
5. Clear timers
"""
                print(call_duration_menu)

                call_duration_menu_option = int(input())

                match call_duration_menu_option:
                    case 1:
                        print("call duration")
                    case 2:
                        print("All calls’ duration")
                    case 3:
                        print("Received calls’ duration")
                    case 4:
                        print("Dialled calls’  duration")
                    case 5:
                        print("Clear timers")
            case 6:
                call_cost_menu = """
Call Cost Menu
1. Last call cost
2. All calls’ cost
3. Clear counters
"""
                print(call_cost_menu)

                call_cost_menu_option = int(input())

                match call_cost_menu_option:
                    case 1:
                        print("Last call cost")
                    case 2:
                        print("All calls’ cost")
                    case 3:
                        print("Clear counters")
            case 7:
                call_cost_settings_menu = """
Call Cost Settings Menu
1. Call cost limit
2. Show costs in
"""
                print(call_cost_settings_menu)

                call_cost_settings_menu_options = int(input())

                match call_cost_settings_menu_options:
                    case 1:
                        print("Call cost limit")
                    case 2:
                        print("Show costs")
            case 8:
                print("Use prepaid credit for calls")

    case 5:
        tones_menu = """
Tones menu
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver
"""
        print(tones_menu)

        tones_menu_options = int(input())

        match tones_menu_options:
            case 1:
                print("select the tone that you hear when you receive a call")
            case 2:
                print("set the volume level for the ringing and message alert tones")
            case 3:
                print("select the way the phone notifies you of incoming voice calls")
            case 4:
                print("set the tone that you hear when you receive a text message.")
            case 5:
                print("set the volume for keypad tones.")
            case 6:
                print("set the phone to sound tones")
            case 7:
                print("set the phone to vibrate when you receive a call or a text message")
            case 8:
                print("select the picture that is displayed in standby mode after a specified time")

    case 6:
        settings_menu = """
SETTINGS MENU
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
"""
        print(settings_menu)

        settings_menu_option = int(input())

        match settings_menu_option:
            case 1:
                call_settings_menu = """
CALL SETTINGS OPTIONS

1.Automatic redial

2.Speed dialling

3.Call waiting options

4.Own number sendng

5.Phone line in use

6.Automatic answer
"""
                print(call_settings_menu)

                call_settings_menu_options = int(input())

                match call_settings_menu_options:
                    case 1:
                        print("Set automatic redial")
                    case 2:
                        print("Set speed dial")
                    case 3:
                        print("Set call waiting settings")
                    case 4:
                        print("Dislay your own number")
                    case 5:
                        print("select the phone line")
                    case 6:
                        print("set Automatic answer")
            case 2:
                phone_settings_menu = """
PHONE SETTINGS OPTIONS

1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
"""
                print(phone_settings_menu)

                phone_settings_menu_option = int(input())

                match phone_settings_menu_option:
                    case 1:
                        print("Select language")
                    case 2:
                        print("set the phone to indicate  cellular network based")
                    case 3:
                        print("Write welcome note")
                    case 4:
                        print("Select network")
                    case 5:
                        print("set to show or hide confirmation messages")
            case 3:
                security_settings_menu = """
SECURITY SETTINGS OPTIONS

1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes
"""
                print(security_settings_menu)

                security_settings_menu_option = int(input())

                match security_settings_menu_option:
                    case 1:
                        print("Request pin")
                    case 2:
                        print("restrict the making and receiving of calls")
                    case 3:
                        print("restrict your outgoing calls to selected phone numbers")
                    case 4:
                        print("specify a group of people whom you can call and who can call you")
                    case 5:
                        print("set the phone to ask for the security code")
                    case 6:
                        print("change the security code, PIN code, PIN2 code, or barring password")
            case 4:
                print("reset the menu settings to their original values")

    case 7:
        print(" Set Call divert")

    case 8:
        music_menu = """
MUSIC MENU
1. Music player
2. Radio
3. Recorder
4. Track list
"""
        print(music_menu)

        music_menu_option = int(input())

        match music_menu_option:
            case 1:
                print("Play music tracks")
            case 2:
                print("Listen to radio")
            case 3:
                print("Record music")
            case 4:
                print("Make track lists")

    case 9:
        print(" Select Games")

    case 10:
        print("Calculator")

    case 11:
        print("save short text notes with an alarm for reminders")

    case 12:
        clock_menu = """
CLOCK MENU
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
"""
        print(clock_menu)

        clock_menu_option = int(input())

        match clock_menu_option:
            case 1:
                print("set the alarm to go off at the desired time")
            case 2:
                print("set the phone to show the current time")
            case 3:
                print("set the correct date")
            case 4:
                print("set stopwatch")
            case 5:
                print("set a countdown")
            case 6:
                print("set to auto update date and time")

    case 13:
        print("edit, manage, and create profile")

    case 14:
        print("access various WAP")

    case 15:
        print("SIM Services Menu")

