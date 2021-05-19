@client.event
async def on_message(message) :
    # This is called whenever a message is sent, possibly our webhook
    if message.channel.id == 837726339586195457: # Make sure that this is the dedicated channel id, in an integer format
        data = message.content.split(" ") # Split the contents of the webhook message
        

        user = re.sub("\D", "", data[4]) # Reducing a ping to just a user id, see above

        # print(user)
        # This is for debugging, make sure you choose the right index
         # Call the method to add it to database or something
        user_object = client.get_user(int(user)) or await client.fetch_user(int(user))
        
        user=user_object #This is basically getting user id so we can send him the dm

        #Now do whatever u want to here ie if you want to reward him any coins or any type of stuff here. If its a simple message which says Thankyou then ignore this
        
        await user_object.send("Thanks for voting!")
    
    await client.process_commands(message) 
