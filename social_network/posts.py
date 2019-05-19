from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None,user=None):
        self.text = text
        self.timestamp = timestamp
        self.user = user

    def set_user(self, user):
        self.user = user
        
    def __str__(self):
        username = "@" + self.user.first_name + " " + self.user.last_name
        time = ''
        if self.timestamp:
            time = self.timestamp.strftime('%A') + ', ' + self.timestamp.strftime('%b') + ' ' + self.timestamp.strftime('%d') + ', ' + self.timestamp.strftime('%Y')
        return '{}: "{}"\n\t{}'.format(username,self.text,time)
    
    
class TextPost(Post):  # Inherit properly
    pass


class PicturePost(Post):  # Inherit properly
    def __init__(self,text,timestamp,image_url):
        self.text = text
        self.timestamp = timestamp
        self.image_url = image_url

    def __str__(self):
        textpost = super().__str__()
        ind = textpost.find('\n')
        picpost = textpost[:ind] +'\n\t'+ self.image_url + textpost[ind:]
        return picpost


class CheckInPost(Post):  # Inherit properly
    def __init__(self,latitude,longitude,text,timestamp):
        self.text = text
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude
        
    def __str__(self):
        textpost = super().__str__()
        firstname = textpost[:textpost.find(' ')]
        start = textpost.find(' ',len(firstname)+1)
        ind = textpost.find('\n')
        position = str(self.latitude) + ', ' + str(self.longitude)
        checkpost = firstname + ' Checked In:' + textpost[start:ind] + '\n\t' + position + textpost[ind:]
        print(checkpost)
        return checkpost
