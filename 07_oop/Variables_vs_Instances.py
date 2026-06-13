#Every time you create an account or a character its data belongs strictly to that individual object
#Those are called Instance Variables (defined using self)
#But what if you want a variable that is shared across every single object built from that blueprint?
#For example tracking the total number of users registered on your streaming service?
#For that we use a Class Variable

class StreamingAccount: #Belongs to the whole class, not an individual object
    total_users = 0 

    def __init__(self, email):
        self.email = email # Instance variable (unique to each user)
        # Every time a new account is made, increase the master counter by 1
        StreamingAccount.total_users += 1

# Testing it out:
user_1 = StreamingAccount("anna@email.com")
user_2 = StreamingAccount("barbie@email.com")
user_3 = StreamingAccount("jamie@email.com")

print(StreamingAccount.total_users)  # Prints: 3