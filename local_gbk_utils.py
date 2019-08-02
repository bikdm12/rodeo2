import socket
import time
import traceback
from Bio import Entrez, SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from My_Record import My_Record, Sub_Seq
import logging
from rodeo_main import VERBOSITY
from timeout_decorator import timeout, TimeoutError
from os import path

logger = logging.getLogger(__name__)
logger.setLevel(VERBOSITY)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(VERBOSITY)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

def get_local_gb_handles(prot_accession_id, gbk_dir):

    gbk_file_path = path.join(gbk_dir, prot_accession_id) + '.gbk'

    try:
        handles = [open(gbk_file_path, 'r')]
        return handles
    
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    
    except Exception as e:
        logger.error(e)
        if path.exists(gbk_dir):
            logger.error("No genbank file for %s." % (prot_accession_id))
            return -4
        else:
            logger.error("No such directory: %s" % (gbk_dir))
            return -5