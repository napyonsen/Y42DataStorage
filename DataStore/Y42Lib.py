
''' This class manupulates data as a dcitionary of items. Underlying data
    on the actual storage environment is converted to it and from it. '''

"Record is assumed to be (key,value) tuple" 

"Keys are assumed to be strings and values are assumed primitive types"

"No perfromance consideration is made here. No caching is done. A real implementation would do that"

"Note that we could implement a syncronization decorator here."

from threading import Lock

class DsLib:
    def __init__(self, formatterObj, storageObj):
        self.formatterObj = formatterObj
        self.storageObj = storageObj
        self.lock = Lock()

    def _readAll(self):
        self.lock.acquire()
        rawdata = self.storageObj.Load()
        data = self.formatterObj.Decode(rawdata)
        self.lock.release()
        return data

    def _writeAll(self,data):
        self.lock.acquire()
        rawdata = self.formatterObj.Encode(data)
        self.storageObj.Save(rawdata)
        self.lock.release()

    def Insert(self,record):
        data = self._readAll()
        data[record[0]] = record[1]
        self._writeAll(data)
        

    def BatchInsert(self,records):
        data = self._readAll()

        for record in records:
            data[record[0]] = record[1]
        
        self._writeAll(data)

    def DoesExist(self,key):
        data = self._readAll()
        return key in data

    def GetRecord(self,key):
        data = self._readAll()
        if key in data: return data[key]
        else: return None
        
    def UpdateRecord(self,record):
        self.Insert(record)

    def DeleteRecord(self,key):
        data = self._readAll()
        if key in data: del data[key]
        self._writeAll(data)

    def Query(self,query, offset = 0, limit = 100):
        data = self._readAll()
        res = [(k,v) for k, v in data.items() if  v == query]
        n = len(res)
        if offset >= n: return []
        if offset + limit >= n: return res[offset:]

        return res[offset:offset+limit]

