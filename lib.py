

def getkey():
  r = open('gpgkey.html','r')
  content = r.read()
  r.close()
  return content

def gethome():
  r = open('gpgkey.html','r')
  content = r.read()
  r.close()
  return content
