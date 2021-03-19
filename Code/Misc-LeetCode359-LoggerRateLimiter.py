class Logger:

    def __init__(self):
        self.data = dict()

    def shouldPrintMessage(self, timestamp: 'int', message: 'str') -> 'bool':
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.data or timestamp - self.data[message] >= 10:
            self.data[message] = timestamp
            return True
        else:
            return False

logger = Logger();
print(logger.shouldPrintMessage(1,'foo'))
print(logger.shouldPrintMessage(2,'bar'))
print(logger.shouldPrintMessage(3,'foo'))
print(logger.shouldPrintMessage(8,'bar'))
print(logger.shouldPrintMessage(10,'fo'))
print(logger.shouldPrintMessage(11,'foo'))
