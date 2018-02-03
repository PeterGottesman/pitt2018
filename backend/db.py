from pitt2018.backend.database import secrets


def getURI():
    URI = "mysql+pymysql://" + secrets.username + ":" + secrets.password + "@" + \
          secrets.url + "/" + secrets.db
    return URI
