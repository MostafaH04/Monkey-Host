# Banana-Hacks-Submition  
Project made for Banana Hacks 2021  
Authors: Mostafa H, Amaar S, Shavaiz K, Shahnawaz K  

1) Person counting system using ML based on a CNN trained using tensorflow library  
1a. Detects if person is there  
1b. paired with the hardware part and discord bot, we are able to save computational resources by having some idea of when to check  

2) Discord bot used to schedule party time, send notifications, rsvp and notify friends when party is full  
2a. uses the Discord API and is run using python    
2b. allows the user to RSVP by giving their Name, phone number (to reach them on) and the time they are arriving  

3) We use the arduino uno, paired with the ultrasonic sensor and motion sensor in order to detect any movement / people walking through the door  
3a. The ultrasonic sensor is placed on a door way or at the enterance to see if an object is near by, and so is the motion sensor. This gives the program an idea of when a person might be at the door  
3b. if the users are expecting someone at the door at that time, the user is notified (not urgently), however if they werent, a more urgent alarm is sent for the host to verify who is at the door  

4) We plan on having a database housing info like sign ups and how many people attended  
4a. Used to send on the discord server when the party is full  
4b. could be used later on to implement and application to the system it self  

Overall:  
ML model based on a conventional neural network (CNN) trained using the tensorflow library using data we personally collected using our image collection python script. This model was then saved allowing us to make predictions on weather the object at the door is a person or not
