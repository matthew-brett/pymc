###
# no_trace database backend
# No memory whatsoever of the samples.
###

from numpy import zeros,shape
import base
import PyMC2

class Trace(base.Trace):
    """The no-trace backend provides a minimalistic backend where no
    trace of the values sampled is kept. This may be useful for testing 
    purposes.
    """ 
    
class Database(base.Database):
    """The no-trace backend provides a minimalistic backend where no
    trace of the values sampled is kept. This may be useful for testing 
    purposes.
    """ 
    def __init__(self):
        """Get the Trace from the local scope."""
        self.Trace = Trace
