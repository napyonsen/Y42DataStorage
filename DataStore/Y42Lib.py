
''' This class manupulates data as a dcitionary of items. Underlying data
    on the actual storage environment is converted to it and from it. '''

"Record is assumed to be (key,value) tuple" 

"Keys are assumed to be strings and values are assumed primitive types"

"No perfromance consideration is made here. No caching is done. A real implementation would do that"

class DsLib:
    def __init__(self, formatterObj, storageObj):
        self.formatterObj = formatterObj
        self.storageObj = storageObj

    def _readAll(self):
        rawdata = self.storageObj.Load()
        data = self.formatterObj.Decode(rawdata)
        return data

    def _writeAll(self,data):
        rawdata = self.formatterObj.Encode(data)
        self.storageObj.Save(rawdata)

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
        del data[key]
        self._writeAll(data)