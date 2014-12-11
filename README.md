log-analyzer-using-python
=========================

log-analyzer-using-python calculates the following:

<ul>
<li>The number of times the URL was called.</li>
<li>The mean (average), median and mode of the response time (connect time + service time).</li>
<li>The "dyno" that responded the most.</li>
</ul>
<h3>Defined Endpoints:</h3>

GET /api/users/{user_id}/count_pending_messages <br>
GET /api/users/{user_id}/get_messages <br>
GET /api/users/{user_id}/get_friends_progress <br>
GET /api/users/{user_id}/get_friends_score <br>
POST /api/users/{user_id} <br>
GET /api/users/{user_id} <br>

<h3> How to run:</h3>
python run.py log-file-path output-file-path generate the data from target file and export the analyst data to the output file.

python run.py will generate the ouput to report.txt file.

