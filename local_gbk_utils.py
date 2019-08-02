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

def get_local_gb_handles(prot_accession_id, gbk_dir):