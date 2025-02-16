"""
* Create a Printer class that has two functions:
   notify_low_ink()
   notify_out_of_paper()
* notify_low_ink() should print a message saying ink is low.
* notify_out_of_paper() should print a message saying printer is out of paper.
* Create an instance of the printer, then call each of the instance methods
  to test the messages.
"""


class Printer:
    def notify_low_ink(self):
        print("Ink is low!")

    def notify_out_of_paper(self):
        print("Out of paper!")

inkjet_printer = Printer()

inkjet_printer.notify_low_ink()
inkjet_printer.notify_out_of_paper()