class Info:
    '''
    clsass that generates instances of the users credentials
    '''
    info_list = []

    def _init_(self,facebookp,emailp,instagramps,twitterps,facebookusername,twitusername,instagramusername):
        self.facebookp = facebookp
        self.emailp = emailp
        self.instagramps = instagramps
        self.twitterps = twitterps
        self.facebookusername = facebookusername
        self.twitusername = twitusername
        self.instagramusername = instagramusername

    def save_info(self):
            '''
            method created to save credentials
            '''
            Info.info_list.append(self)

    def delete_info(self):
                '''
                method that deletes credentials
                '''
                Info.info_list.remove(self)

    @classmethod


    def display_info(cls):
        '''
        a class method involves the whole class the display info
        '''

        return cls.info_list