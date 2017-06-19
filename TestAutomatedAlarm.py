# TestAutomatedAlarm.py

# Import Statements
import unittest
import automatedAlarm

class KnownValues(unittest.TestCase):

    def test_automatedAlarmForWednesdayOff(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("wednesday", True)
        # Check for expected output
        self.assertEqual('8:30', result)

    def test_automatedAlarmForMondayOff(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("monday", True)
        # Check for expected output
        self.assertEqual('9:30', result)

    def test_automatedAlarmForMondaySchool(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("monday", False)
        # Check for expected output
        self.assertEqual('7:00', result)

    def test_automatedAlarmForWednesdaySchool(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("wednesday", False)
        # Check for expected output
        self.assertEqual('7:30', result)

    def test_automatedAlarmForSaturdayOff(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("saturday", True)
        # Check for expected output
        self.assertEqual('9:00', result)

    def test_automatedAlarmForSaturdaySchool(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("saturday", False)
        # Check for expected output
        self.assertEqual('9:00', result)

    def test_automatedAlarmForFridaySchool(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("friday", False)
        # Check for expected output
        self.assertEqual('7:00', result)

    def test_automatedAlarmForThursdaySchool(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("thursday", False)
        # Check for expected output
        self.assertEqual('7:00', result)

    def test_automatedAlarmForThursdayOff(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("thursday", True)
        # Check for expected output
        self.assertEqual('8:30', result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
