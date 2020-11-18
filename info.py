class Info:
    '''
    clsass that generates instances of the users information
    '''
    info_list = []

    def _init_(self,facebookp,emailp,instagramps,twitterpas,facebookusername,twitusername,instagramusername):
        self.facebookp = facebookp
        self.emailp = emailp
        self.instagramps = instagramps
        self.twitterpas = twitterpas
        self.facebookusername = facebookusername
        self.twitusername = twitusername
        self.instagramusername = instagramusername
        def save_info(self):
            '''
            method created to save information
            '''
            Info.info_list.append(self)

            def delete_info(self):
                '''
                method that deletes information
                '''
                Info.info_list.remove(self)