<pre>
<code>
import re

class parser:
    info = {}

    user_id_replacement = '([0-9]+)'
    look_for_pattern = re.compile('(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2})\sheroku\[router]:\sat=info\smethod=(GET|POST)\spath=(\/api\/users\/[0-9]+\/?[a-zA-Z0-9_\-]*)\shost=([a-zA-Z0-9\-\._:]+)\sfwd="([0-9\.]+)"\sdyno=([a-zA-Z0-9\-\.]+)\sconnect=(\d+)ms\sservice=(\d+)ms\sstatus=(\d+)\sbytes=(\d+)')

    parse_index_dict = { 'timestamp':0 , 'method':1 , 'path':2 , 'host':3 , 'fwd':4 , 'dyno':5 , 'connect':6 , 'service':7 , 'status':8 , 'bytes':9 }

    end_points = ['GET /api/users/{user_id}/count_pending_messages',
                  'GET /api/users/{user_id}/get_messages',
                  'GET /api/users/{user_id}/get_friends_progress',
                  'GET /api/users/{user_id}/get_friends_score',
                  'POST /api/users/{user_id}',
                  'GET /api/users/{user_id}' ]
        
    def __init__( self , logFilePath ):

        #Open the log file
        fobj = open( logFilePath , 'r' )

        #Get all lines in the file
        with fobj as lines:
            flines = lines.readlines()

        for line in flines:

            #Get all matches pattern
            gotten_matches = self.look_for_pattern.findall( line )
            
            if ( gotten_matches ):

                #Resave gotten_matches becasue it be direction in list
                gotten_matches = gotten_matches[0]
            
                if( len( gotten_matches ) == len( self.parse_index_dict ) ):

                    #Get matches pattern in path
                    url_path = gotten_matches[ self.parse_index_dict['path'] ]

                    if( url_path ):

                        #Replace orignal user id with {user_id}
                        replaced_url_path = re.sub( self.user_id_replacement , "{user_id}" , url_path )
                        replaced_url_path = gotten_matches[ self.parse_index_dict['method'] ] + ' ' + replaced_url_path
                
                        if( replaced_url_path in self.end_points ):
                            if( not self.info or not ( replaced_url_path in self.info ) ):
                                self.info[ replaced_url_path ] = {}
                                self.info[ replaced_url_path ]['count'] = None
                                self.info[ replaced_url_path ]['process_time'] = []

                            #Count number of time that URL called
                            self.info[ replaced_url_path ]['count'] = self.counter( self.info[ replaced_url_path ]['count'] )

                            #Calculate process time using ( connect time + service time )
                            self.info[ replaced_url_path ]['process_time'].append( int( gotten_matches[ self.parse_index_dict['connect'] ] + gotten_matches[ self.parse_index_dict['service'] ] ) )

                            #Get the index of dyno that represented in gotten_matches
                            dyno = gotten_matches[ self.parse_index_dict['dyno'] ]
                    
                            if( not ( 'dyno' in self.info[ replaced_url_path ] ) ):
                                self.info[ replaced_url_path ]['dyno'] = {}
                                self.info[ replaced_url_path ]['dyno'][dyno] = 1
                            elif( not dyno in self.info[ replaced_url_path ]['dyno'] ):
                                self.info[ replaced_url_path ]['dyno'][dyno] = 1
                            elif( dyno in self.info[ replaced_url_path ]['dyno'] ):
                                self.info[ replaced_url_path ]['dyno'][dyno] = self.counter( self.info[ replaced_url_path ]['dyno'][dyno] )
            
    def counter( self , value ):
        if( value is None ):
            return 1
        else:
            return value + 1
</code>
</pre>

