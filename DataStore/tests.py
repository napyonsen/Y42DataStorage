from DiskStorage import DiskStorageCls
from FTPStorage import FtpStorageCls
from JsonFormatter import JsonFormatterCls
from XmlFormatter import XmlFormatterCls
from Y42Lib import DsLib
import unittest

ds = DsLib(JsonFormatterCls(), DiskStorageCls())

class TestInsertion(unittest.TestCase):
    
    def test_insertion(self):
        ds.Insert(("name", "mustafa"))
        name = ds.GetRecord("name")
        self.assertEqual(name, "mustafa")

    def test_batch_insertion(self):
        ds.BatchInsert([("age", 32), ("city","istanbul")])
        age = ds.GetRecord("age")
        city = ds.GetRecord("city")
        self.assertEqual(age, 32)
        self.assertEqual(city, "istanbul")

    def test_update(self):
        ds.UpdateRecord(("name", "osman"))
        name = ds.GetRecord("name")
        self.assertEqual(name, "osman")

    def test_delete(self):
        ds.DeleteRecord("name")
        name = ds.GetRecord("name")
        self.assertEqual(name, None)


    def test_does_exist(self):
        ds.Insert(("name", "mustafa"))
        self.assertEqual(ds.DoesExist("name"), True)
        self.assertEqual(ds.DoesExist("sex"), False)

    def test_FtpStorage(self):
        ds = DsLib(JsonFormatterCls(), FtpStorageCls())
        with self.assertRaises(NotImplementedError):
            ds.UpdateRecord(("name", "messi"))

    def test_XmlFormatter(self):
        ds = DsLib(XmlFormatterCls(), DiskStorageCls())
        with self.assertRaises(NotImplementedError):
            ds.UpdateRecord(("name", "messi"))



if __name__ == '__main__':
    unittest.main()
