
''' This class manupulates data as a dcitionary of items. Underlying data
    on the actual storage environment is converted to it and from it. '''

"Record is assumed to be (key,value) tuple" 

"Keys are assumed to be strings and values are assumed primitive types"

"No perfromance consideration is made here. No caching is done. A real implementation would do that"

"We could implement a syncronization decorator here. Although it makes code shorter, it breaks dowwn the simplicity principle."

from threading import Lock

class DsLib:
    def __init__(self, formatterObj, storageObj):
        self.formatterObj = formatterObj
        self.storageObj = storageObj
        self.lock = Lock()

    def _readAll(self):
        rawdata = self.storageObj.Load()
        data = self.formatterObj.Decode(rawdata)
        return data

    def _writeAll(self,data):
        rawdata = self.formatterObj.Encode(data)
        self.storageObj.Save(rawdata)

    def Insert(self,record):
        self.lock.acquire()
        data = self._readAll()
        data[record[0]] = record[1]
        self._writeAll(data)
        self.lock.release()

    def BatchInsert(self,records):
        self.lock.acquire()
        data = self._readAll()

        for record in records:
            data[record[0]] = record[1]
        
        self._writeAll(data)
        self.lock.release()

    def DoesExist(self,key):
        self.lock.acquire()
        data = self._readAll()
        self.lock.release()
        return key in data

    def GetRecord(self,key):
        self.lock.acquire()
        data = self._readAll()
        self.lock.release()
        if key in data: return data[key]
        else: return None
        
    def UpdateRecord(self,record):
        self.Insert(record)

    def DeleteRecord(self,key):
        self.lock.acquire()
        data = self._readAll()
        del data[key]
        self._writeAll(data)
        self.lock.release()