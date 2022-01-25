def getkey():
  r = open('gpgkey.html','r')
  content = r.read()
  r.close()
  return content

def gethome():
  r = open('home.html','r')
  content = r.read()
  r.close()
  return content

def getblog():
  r = open('blog.html','r')
  content = r.read()
  r.close()
  return content

def getresume():
  r = open('resume.html','r')
  content = r.read()
  r.close()
  return content