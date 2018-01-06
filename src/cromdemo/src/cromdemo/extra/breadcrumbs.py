from zope import interface
from zope.interface import Interface
label='Label Needed'
from acquisition import Acquire,ParentalAcquire

def myParents(self):
    return parents(self.context)

def parents(self):
    return parentsUpTo(self,IApplicationRoot)

def reversedParents(self):
    return reversedParentsUpTo(self,IBreadcrumbsRoot)

def parentsUpTo(self,anInterface):
    return reversed(reversedParentsUpTo(self,anInterface))

def reversedParentsUpTo(self,anInterface):
        parents=[]
        item=self        
        while (item!=None):
           parents.append(item)
           if anInterface.providedBy(item):
              break
           item=item.__parent__      
        return parents


def parentWhichImplements(self,interface):
        item=self        
        while (item!=None):
           if interface.providedBy(item):
              return item
           item=item.__parent__      
        return None

def parentsWhichImplement(self,interface):
        item=self        
        result=[]
        while (item!=None):
           if interface.providedBy(item):
              result.append(item)
           item=item.__parent__      
        return result


def parentalMethod(self,method):
   for item in parents(self):
       if hasattr(item,method):
          return item.__getattr__(method)
   raise Exception("NO SUCH METHOD FOUND")


def getRoot(object):
        max = 9999
        context=object
        while context is not None:
            if IRoot.providedBy(context):
                return context
            context = context.__parent__
            max -= 1
            if max < 1:
                raise TypeError("Maximum location depth exceeded, "                                "probably due to a a location cycle.")
        raise TypeError("Parents needed to  determine location root")


class Breadcrumbs(object):  

  def parentalAcquire(self):
       return ParentalAcquire(self.context)

  def objectHref(self,object):
      return self.href(self.url(object),object.getTitle())

  def href(self,url,name):
           result ='<a href=\"'
           result += url
           result+='\">'
           if name != None:
              result += name
           result +='</a>'
           return result
  
  def urlPlusName(self,name):
      return self.url(target) + '/' + name
  
  def AqContext(self):
      return Acquire(self.context)

  def AqObject(self,anObject):
      return Acquire(anObject)

  def getRoot(self):
      return getRoot(self.context) 
 
  def parents(self):
      return parents(self.context)

  label='Label Needed'

  def authenticated(self):
      return not IUnauthenticatedPrincipal.providedBy(self.request.principal)

  def li(self,text):   
        result='<li>'
        result+=text
        result+='</li>'
        return result


  def liHref(self,url,name):   
        result='<li>'
        result+=self.href(url,name)
        result+='</li>'
        return result


  def className(self):
       return type(self.context).__name__





       

       



