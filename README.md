# Y42DataStorage


DsLib class gets its data formatter and storager objects as an argument when creation. All data formatter objects should have Decode() and Encode()
methods while all storage objects passed should have Save() and Load() methods. By this way, real implementation of this methods leaved to the user of the 
library. In order this class to be work properly, this objects must be supplied by the user when creating the DsLib object.

Note that since python is Duck typed, we do not need to define a common base class for formatter objects neither for storage objects
to implement the polimorphic behavior here. 
