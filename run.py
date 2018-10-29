from datetime import datetime
users_list = [
    {       
            "userid":0,
            "username":'admin',
            "password":'admin',
            "role":'admin'
    }
]
comments = []

class Auth():
    def signup(self):
        """user register
                
        Keyword Arguments:
            role {user} -- [all users registereing will automatically be users] (default: {'user'})
        
        Returns:
            [message] -- [successful registered]
        """

        print('Enter your username')
        username = input()
        self.username = username
        name = [name for name in users_list if name['username'] == self.username]
        if name:
            return 'User already exist'
        print('Enter your password')
        password = input()
        self.password = password
        print('Please Password again')
        confirm = input()
        self.confirm = confirm
        if self.password != self.confirm:
            print('Passwords should match')
            return
        self.role = 'user'
        user_dict = {
            "userid": len(users_list) + 1,
            "username":self.username,
            "password":self.password,
            "role":self.role
        }
        
        users_list.append(user_dict)
        print("Successsfully registered in")
        return 'Successfully registered'
    
    def login(self):
        """user login 
        
        Arguments:
            username {nic} -- [unique username]
            password {nicki} -- [secret key to account]
        
        Returns:
            success message
        """
        
        print('Enter your username')
        username=   input()
        self.username = username
        print('Enter your password')
        password = input()
        self.password = password
        self.timestamp = datetime.now()
        passw = [passw for passw in users_list if passw['password'] == self.password 
                                          and passw['username'] == self.username]
        if not passw:
            print( 'Error logging in, check your credentials')
            return
        self.logged_in_status = True
        print(f"logged in at {self.timestamp}")

    def logout(self):
        if self.logged_in_status:
            self.logged_in_status = False
            return 'Successfully logged out' 
        print("Please log in first")

        return  self.login()

Auth().login()