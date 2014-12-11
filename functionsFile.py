import math
import datetime
import collections
import operator

class functions:

    def generateReport( self, filePath, info ):
        output = 'Generated on: ' + str( datetime.datetime.now() ) + '\n\r\n\r'
        for rowInfo in info:
            output += '** ' + rowInfo + '\n\r'
            output += ' Number of URL calls ' + str( info[ rowInfo ][ 'count' ] )
            output += ', Response time Mean/Avg: ' + str( self.mean( info[ rowInfo ][ 'process_time'] ) ) + 'ms'
            output += ', Response time Median: ' + str( self.meadian( info[ rowInfo ][ 'process_time'] ) ) + 'ms'
            output += ', Response time Mode: ' + str( self.mode( info[ rowInfo ][ 'process_time'] ) ) + 'ms'
            output += ', Dyno(s) responded the most: ' + str( self.dyno( info[ rowInfo ][ 'dyno'] ) )
            output += '\r\n'
        fob = open( filePath, 'w' )
        fob.write( output )
        fob.close()
        
    def mean( self, listVal ):
        return ( sum( listVal ) / len( listVal ) )

    def mode( self, listVal ):
        # Create category of repeated values then determine the MAX number
        listVal = collections.OrderedDict( sorted( collections.Counter(listVal).items() ) )
        listVal = dict( listVal )
        return max( listVal , key=listVal.get )

    def meadian( self, listVal ):
        
        listVal = collections.OrderedDict( sorted( collections.Counter(listVal).items() ) )
        listVal = dict( listVal )
        
        meadian = math.floor( ( len( listVal ) + 1 ) / 2 )
        listVal = sorted(listVal)

        #decrease meadian by one because index start from zero
        meadian = meadian - 1

        # if there are an even number of numbers. In this case, the median is the mean (the usual average) of the middle two values
        if( len( listVal ) % 2 == 0 ):
            return ( listVal[ meadian ] + listVal[ meadian + 1 ] ) / 2
        else: #if odd
            return listVal[ meadian ]

    def dyno(self, listVal):
        return max( listVal , key=listVal.get )
