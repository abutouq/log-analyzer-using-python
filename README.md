log-analyzer-using-python
=========================

log-analyzer-using-python calculates the following:

-The number of times the URL was called.
-The mean (average), median and mode of the response time (connect time + service time).
-The "dyno" that responded the most.

Defined Endpoints:

GET /api/users/{user_id}/count_pending_messages
GET /api/users/{user_id}/get_messages
GET /api/users/{user_id}/get_friends_progress
GET /api/users/{user_id}/get_friends_score
POST /api/users/{user_id}
GET /api/users/{user_id}

How to run:
python run.py log-file-path output-file-path generate the data from target file and export the analyst data to the output file.

python run.py will generate the ouput to report.txt file.

