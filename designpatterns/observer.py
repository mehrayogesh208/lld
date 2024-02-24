from abc import ABC

#Interface
class Observable(ABC):
    def add(self,observer):
        pass
    def remove(self,observer):
        pass
    def noitfy(self):
        pass
    def getData(self):
        pass
    def setData(self,data):
        pass

#concrete of observable class
class IphoneObservable(Observable):
    def __init__(self):
        self._subscribedList = []
        self._stockCount = 0
    def add(self,observer):
        self._subscribedList.append(observer)
    def remove(self,observer):
        newList = []
        for item in self._subscribedList:
            if item is not observer:
                newList.append(item)
        self._subscribedList = newList
    def noitfy(self):
        for item in self._subscribedList:
            item.update()
    def getData(self):
        return self._stockCount
    def setData(self, newStockCount):
        if self._stockCount == 0:
            self._stockCount = newStockCount
            self.noitfy()
        self._stockCount = newStockCount

#interface for Observer
class Observer(ABC):
    def update(self):
        pass
#concrete class
class EmailObserver(Observer):
    def __init__(self,observable,email):
        self._observableObj = observable
        self.emailId = email
    def update(self):
        self.sendEmail()
    def sendEmail(self):
        print("Sending Email to {} for stock count {}".format(self.emailId,self._observableObj.getData()))

class SMSObserver(Observer):
    def __init__(self,observable):
        self._observableObj = observable
    def update(self):
        self.sendSMS()
    def sendSMS(self):
        print("Sending SMS for stock count",self._observableObj.getData())


if __name__ == '__main__':
    iphoneObservableObj = IphoneObservable()
    store:Observable = iphoneObservableObj
    store.add(EmailObserver(iphoneObservableObj,"test@gmail.com"))
    store.add(SMSObserver(iphoneObservableObj))
    store.setData(5)
    store.setData(0)
    store.setData(2)

        

