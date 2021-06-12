# Monkey-Host 
Project made for Banana Hacks 2021
Award: Top 5 Finalists + Best Hardware Hack<br/>
Authors: Mostafa H, Amaar S, Shavaiz K, Shahnawaz K <br/> 
<br/>
1) Person counting system using ML based on a CNN trained using tensorflow library  <br/>
1a. Detects if person is there  <br/>
1b. paired with the hardware part and discord bot, we are able to save computational resources by having some idea of when to check  <br/>
<br/>
2) Discord bot allows user to enter their name, phone number, and time they will attend.  <br/>
2a. Once the user uses the command, the bot will send them a confirmation in chat and the bot will send a message to a channel that only moderators have access to.<br/>  
2b. User can also cancel their RSVP. Bot will again send confirmation in chat and will send a message to another private channel.  <br/>
<br/>
3) We use the arduino uno, paired with the ultrasonic sensor and motion sensor in order to detect any movement / people walking through the door  <br/>
3a. The ultrasonic sensor is placed on a door way or at the enterance to see if an object is near by, and so is the motion sensor. This gives the program an idea of when a person might be at the door  <br/>
3b. if the users are expecting someone at the door at that time, the user is notified (not urgently), however if they werent, a more urgent alarm is sent for the host to verify who is at the door  <br/>

4) We plan on having a database housing info like sign ups and how many people attended  <br/>
4a. Used to send on the discord server when the party is full  <br/>
4b. could be used later on to implement and application to the system it self  <br/>

Overall:  <br/>
ML model based on a conventional neural network (CNN) trained using the tensorflow library using data we personally collected using our image collection python script. This model was then saved allowing us to make predictions on weather the object at the door is a person or not<br/>
