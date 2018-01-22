class YACRS(object):
    """
    A potential Python API for YACRS.
    
    ---
    This just lists the calls I would like to be able to make. All of this functionality
    is already available via the web interface (I think), although not in a convenient form.
    
    """
    

    def __init__(self):
        # starts in disconnected form
        pass
    
    def connect(self, user, password, server="https://learn.gla.ac.uk"):
        """Connect to YACRS, logging in with the given username
        and password. Optionally, a server can be specified.                
        """
        pass # store the token
    
    def disconnect(self):
        """Disconnect from the YACRS server. Calls to a
        disconnected server throw a NoServerConnection exception.
        """
        pass
    
    ###
    # The following calls require that a connection be active
    ###
    
    def list_sessions(self):
        """Return a list of sessions for the logged in user, in the form
        [
            {"number":integer, "title":string},
            {"number":integer, "title":string},
            ...
        ]
        
        
        """
        pass
    
    def new_session(self, title=None, course_id=None, guests=False,
                   display_on_list=False, teacher_led=False,
                   time_limit=0, allow_review=True,
                   microblog=False, max_text_length=0):
        """Create a new session. Returns the session number.
        Any of the YACRS session parameters can be specified on
        session creation.        
        
        Returns session number.
        """
        pass
    
    def set_session_settings(self, number, **kwargs):
        """Adjust an existing session with any of the keyword
        arguments from create session. Takes an existing session number
        
        number: session to adjust
        **kwargs: keyword arguments, any of the keys from new_session().
        
        NoSuchSession exception if this session doesn't exist
        
        Returns None
        """
        pass
    
    
    def get_session_settings(self, number):
        """Return the full properties of a session, in 
        a dictionary with the same fields
        as new_session() would take them as keyword arguments.
        
        number: number of the session to query
        
        NoSuchSession exception if this session doesn't exist
        
        Returns dictionary of settings, same format as new_session().
        """
        pass
        
    def start_session(self, number):
        """Start a specific session. Stops the current session if one is active.
        before starting the new session.
        
        NoSuchSession exception if this session doesn't exist.
        
        Returns None.
        """
        pass
    
    def stop_session(self):
        """Stop the current session, if one is running. 
        Does nothing if no session running.
        
        Returns True if a session stopped, and False if no session was running
        """
        pass
    
    def get_active_session(self):
        """Return the active session number, or None if no session active."""
        pass
    
 
    def get_session_category_scores(self, session):
        """Return the category scores for the whole session
        
        session: session number
        
        in the format
        {
            "id":student_id
            [
                {"category":category, "score":int}                
            ]        
        }        
        """
        pass
    
    def get_session_categories(self, session):
        """Return the categories, along with a list
        of questions for each category
        [
            {"category":category, "questions":[list of ints]},
            ...
        ]
        """
    
    def get_session_results(self, session):
        """Return all question responses for a whole session
        Format:
        [
         {
         question:
             {title:string,
             start_time:timestamp question started,             
             end_time:timestamp question ended
             mcq: True/False,
             category:string,
             options:list of strings or integer
             correct:string or number or list of strings/numbers
             multi_option:true or false
             confidence: true/false             
             }
         results:
             {
                 results list as returned from get_results
             }
         }
        
        ]
        
        """
        pass
    

    
    ###
    ### The following calls require that a session be active
    ###
    
    def get_active_question(self):
        """Return the active question number in the active session, or None if no question open.
        
        NoActiveSession exception if no session is active
        """
        pass
    
    def get_responses(self, question_number=None):
        """Return the number of users and number of responses to the question as tuple (users, responses)
        
        NoActiveSession exception if no session is active
        """
        pass
    
    def start_mcq(self, title=None, options=None, title_shown=True,
                  correct=None, category=None,
                  multi_option=False, confidence=False):
        """Start a new multiple choice question. 
        title: title of question
        title_shown: if True, show title on student devices
        options: list of options to be chosen. 
                If a number, offer a list of unnamed options (e.g. A-F)
                If a list of strings, offer a list of options with titles                
        correct: The correct answer, either as a numerical index or
                 as a string, if the options were a list of strings
                 If None, no option marked as correct.
                 Can be list of strings or list of numbers if this
                 is a multi_option question.
        category: String category to assign this question to.
        multi_option: if True, more than one answer can be selected (MRQ)
        confidence: if True, allow students to specify their confidence level
        
        Returns the question number.
        
        NoActiveSession exception if no session is active.
        """
        pass
        
    def start_freetext(self, title=None, category=None):
        """Start a free text question.
            title: title to be displayed
            category: category of this question

            Returns the question number.
            
            NoActiveSession exception if no session is active.
        """
        pass
    
    def get_question_results(self, question_number=None):
        """Return the full results to a question, 
        as list of dictionaries:
        [{id:student_id, 
        name:student name,
        time:timestamp, 
        response:string/integer, 
        correct:boolean,
        confidence:integer}]        
        
        Works while questions are open as well as afterwards.   
        
        NoActiveSession exception if no session is active.
        """
        pass
    
    def get_question_histogram(self, question_number=None):
        """Return the results histogram, as a list of counts. Only
        works if the question is an MCQ/MRQ question or a True/False/Don't Know.        
            For example: [10,5,0,1,0]
            If confidences are enabled, includes a confidence breakdown instead of a simple count.
            For example: [[0,4,5,1], [0,0,3,2], [0,0,0,0], [1,0,0,0], [0,0,0,0]]
            Each sublist is a number of counts at each of the confidence categories.
        
        Works while questions are open.
        
        NoActiveSession exception if no session is active.
        """        
        pass
        
    def end_question(self):
        """End the current question. Returns the results of that question.
        
        Returns the same format as get_question_results()
        
        NoActiveSession exception if no session is active.
        """
        pass
    
    
#####################################################################    

# properties to make the API a bit nicer to work with

    @property(self):
    def connected(self):
        """Return True if connected, or False otherwise"""
    pass
        
    @property 
    def sessions(self):
        """Return the session list (same as .list_sessions()). """
        pass

    @property
    def active_session(self):
        """Active session number, or None if no session active."""
        pass
        
    @property
    def session_data(self):
        """Conveneince for query_session(self.active_session).
        None if no session"""
        pass
    
    @property
    def n_users(self):
        """Number of active users in this session, or None"""
        pass
        
    @property
    def question(self):
        """Number of current question, if active, or None"""
        pass
    
    @property
    def n_responses(self):
        """Number of responses to current question, or None"""
        pass
    
    @property
    def categories(self):
        """Convenience for get_session_categories(self.active_session)
        None if no active session.
        """
        pass
    




# some basic exceptions 
class NoActiveSession(Exception):
    pass

class NoSuchSession(Exception):
    pass

class NoServerConnection(Exception):
    pass

