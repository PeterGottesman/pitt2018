import secrets
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

def getURI():
    URI = "mysql+pymysql://" + secrets.username + ":" + secrets.password + "@" + \
          secrets.url + "/" + secrets.db
    return URI
