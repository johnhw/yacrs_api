# yacrs_api
Outline of a Python YACRS API

[yacrs_api.py] suggests a basic API that I would like to implement. It should give some insight into the functionality required of a REST API.

## Priorities

* **Simple** RESTful API
  * No additional features required; just a simple way of getting at existing functionality quickly via the API
* **Low latency**
  * <3s for setting a question, getting full question response
  * <1s update time for getting number of responses to question
  * This suggests different endpoints for requests like "number of responses", "graph of responses", "all responses to this question" and "all responses to all questions", even though all of the preceding could be worked out from the last
* Ideally all data as JSON blocks
* Ideally some protection against shooting yourself in the foot (make destructive operations reversible!)

  
