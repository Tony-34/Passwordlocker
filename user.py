class User:
    '''
    class  that generates instances for the user
    '''
    save_userlist = []
    def _init_(self,fname,lname,email,):

        self.fname = fname
        self.lname = lname
        self.email = email

    def save_user (self):
        '''
        save_user method saves a new user objectto the user list
        '''
        User.save_userlist.append(self)