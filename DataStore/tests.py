from DiskStorage import DiskStorageCls
from FTPStorage import FtpStorageCls
from JsonFormatter import JsonFormatterCls
from XmlFormatter import XmlFormatterCls
from Y42Lib import DsLib
import unittest
unittest.TestLoader.sortTestMethodsUsing = None

ds = DsLib(JsonFormatterCls(), DiskStorageCls())

class TestDsLib(unittest.TestCase):
    
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

    def test_query(self):
        ds.BatchInsert([("age", 32), ("num1", 32), ("num2",32)])
        res = ds.Query(32)
        self.assertEqual(res, [("age", 32), ("num1", 32), ("num2",32)])

    def test_query_with_offset(self):
        res = ds.Query(32, offset=1)
        self.assertEqual(res, [("num1", 32), ("num2",32)])

    def test_query_with_limit(self):
        res = ds.Query(32, limit=1)
        self.assertEqual(res, [("age", 32)])

    def test_query_with_offset_and_limit(self):
        res = ds.Query(32, offset=1, limit=1)
        self.assertEqual(res, [("num1", 32)])

    def test_query_invalid_offset(self):
        res = ds.Query(32, offset=100)
        self.assertEqual(res, [])

    def test_query_over_limit(self):
        res = ds.Query(32, limit=100)
        self.assertEqual(res, [("age", 32), ("num1", 32), ("num2",32)])

    def test_query_offest_over_limit(self):
        res = ds.Query(32, offset=3, limit=1)
        self.assertEqual(res, [])

    def test_query_truncated(self):
        res = ds.Query(32, offset=1, limit=5)
        self.assertEqual(res, [("num1", 32), ("num2",32)])

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
