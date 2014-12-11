import os.path
import sys
from parserFile import parser
from functionsFile import functions

#Check if user enter the path to log file, I use sys.argv[1] because the first argument is the name of current file
try:    
    logFilePath = sys.argv[1]
    if( not os.path.isfile( logFilePath )  ):
        print( 'Log file does\'t exist in PAHT: ' + logFilePath )
        sys.exit()
        
except IndexError:
    logFilePath = 'sample.log'

    if( not os.path.isfile( logFilePath )  ):
        print( 'Log file does\'t exist in PATH: ' + logFilePath )
        sys.exit()

#Check if user enter the path to the report file
try:
    reportFilePath = sys.argv[2]
    #No need to check if Text file exist because it will be created if not exist
except IndexError:
    reportFilePath = 'report.txt'

print ('Start Procissing...')

objParser = parser(logFilePath)

objFunc = functions()
objFunc.generateReport( reportFilePath , objParser.info )

print( '\n\rReport file Generated!' )
