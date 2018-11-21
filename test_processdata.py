import unittest
from   processdata import process_input, get_order_dob, get_order_gender, get_order_reverse_lastname, get_recordcount, get_failcount, get_flist

class TestFields(unittest.TestCase):
    def test_norecords(self):

    	#no input, we expect no records
        self.assertEqual(get_recordcount(), 0)
        self.assertEqual(get_failcount()  , 0)

        #empty input, we expect 1 failure, no records
        with self.assertRaises(ValueError):
	        process_input('')
        self.assertEqual(get_recordcount(), 0)
        self.assertEqual(get_failcount()  , 1)

        #adding too many fields, we expect another failure
        with self.assertRaises(ValueError):
	        process_input('firstname|lastname|gender|favoritecolor|09/22/1987|extrafield')
        self.assertEqual(get_recordcount(), 0)
        self.assertEqual(get_failcount()  , 2)

       	#adding too few fields, we expect another failure
        with self.assertRaises(ValueError):
	        process_input('firstname|lastname|gender|favoritecolor')
        self.assertEqual(get_recordcount(), 0)
        self.assertEqual(get_failcount()  , 3)


       	#giving a 2 digit year
        with self.assertRaises(ValueError):
	        process_input('firstname|lastname|gender|favoritecolor|10/22/80')
        self.assertEqual(get_recordcount(), 0)
        self.assertEqual(get_failcount()  , 4)

   		#giving more than 4 digit year
        with self.assertRaises(ValueError):
	        process_input('firstname|lastname|gender|favoritecolor|10/22/80808080')
        self.assertEqual(get_recordcount(), 0)
        self.assertEqual(get_failcount()  , 5)

        #proper input, we expect 1 new record and no failures
        process_input('thoma|michael|m|red|09/22/1987')
        self.assertEqual(get_recordcount(), 1)
        self.assertEqual(get_failcount()  , 5)