# autoLogGenerator
This script generates logs very quickly. Its useful for generating workloads for data ingest and/or analytics applications.
It can write log lines to console, to log files.

### Pre-Requisites
- Python 2.7

### Execution
-  git clone https://github.com/jainpayal12/autoLogGenerator.git
-  set the Environment variable LOG_GENERATOR_DIR to cloned repository path.
   For Example : If you have cloned the git repository in Desktop folder. Then,
   LOG_GENERATOR_DIR=<home_directory>/Desktop/autoLogGenerator
   - gedit ~/.bashrc
     export LOG_GENERATOR_DIR=<home_directory>/Desktop/autoLogGenerator
-  run the python file
   
### Basic Usage
- Generating log on console.
  run : python $LOG_GENERATOR_DIR/lib/logGenerator.py
  
- Generating log in file
  run : python $LOG_GENERATOR_DIR/lib/logGenerator.py  >  $LOG_GENERATOR_DIR/logs/logFile
  
   
