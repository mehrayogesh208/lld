class LogProcessor:
    def __init__(self,logProcesssor=None):
        self.logProcessor = logProcesssor
    def log(self,level,message):
        if self.logProcessor is not None:
            self.logProcessor.log(level,message)

class InfoLogProcessor(LogProcessor):
    def __init__(self,logProcessor=None):
        super().__init__(logProcessor)
    def log(self,level,message):
        if level == 'INFO':
            print(message)
        else:
            super().log(level,message)

class ErrorLogProcessor(LogProcessor):
    def __init__(self,logProcessor=None):
        super().__init__(logProcessor)
    def log(self,level,message):
        if level == 'ERROR':
            print(message)
        else:
            super().log(level,message)

class DebugLogProcessor(LogProcessor):
    def __init__(self,logProcessor=None):
        super().__init__(logProcessor)
    def log(self,level,message):
        if level == 'DEBUG':
            print(message)
        else:
            super().log(level,message)

obj = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor()))
obj.log("ERROR","test")
    


