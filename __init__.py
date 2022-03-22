# encoding: utf-8
"""
Models package.

Please see the LICENSE file for licensing details of this package.

"""

from __future__ import absolute_import, division, print_function

import os
import glob

MODEL_PATH = os.path.dirname(__file__)


def models(pattern, path=MODEL_PATH):
    """
    Retrieve all models in path given a file name pattern.

    Parameters
    ----------
    pattern : str
        Pattern to be matched.
    path : str, optional
        Path to search for model files.

    Returns
    -------
    models : list
        Sorted list of matching model file names.

    """
    return sorted(glob.glob('%s/%s' % (path, pattern)))


# beats
BEATS_LSTM = models('beats/2016/beats_lstm_[1-8].pkl')
BEATS_BLSTM = models('beats/2015/beats_blstm_[1-8].pkl')
BEATS_TCN = models("beats/2019/beats_tcn_[1-8].pkl")

# downbeats
DOWNBEATS_BLSTM = models('downbeats/2016/downbeats_blstm_[1-8].pkl')
DOWNBEATS_BGRU = [models('downbeats/2016/downbeats_bgru_rhythmic_*.pkl'),
                  models('downbeats/2016/downbeats_bgru_harmonic_*.pkl')]
# notes
NOTES_BRNN = models('notes/2013/notes_brnn.pkl')
NOTES_CNN = models('notes/2019/notes_cnn.pkl')
NOTES_CNN_MIREX = models('notes/2018/notes_cnn_[12].pkl')

# onsets
ONSETS_RNN = models('onsets/2013/onsets_rnn_[1-8].pkl')
ONSETS_BRNN = models('onsets/2013/onsets_brnn_[1-8].pkl')
ONSETS_BRNN_PP = models('onsets/2014/onsets_brnn_pp_[1-8].pkl')
ONSETS_CNN = models('onsets/2013/onsets_cnn.pkl')

# patterns
PATTERNS_BALLROOM = models('patterns/2013/ballroom_pattern_[34]_4.pkl')

# chroma
CHROMA_DNN = models('chroma/2016/chroma_dnn.pkl')

# chords
CHORDS_DCCRF = models('chords/2016/chords_dccrf.pkl')
CHORDS_CNN_FEAT = models('chords/2016/chords_cnnfeat.pkl')
CHORDS_CFCRF = models('chords/2016/chords_cnncrf.pkl')

# key
KEY_CNN = models('key/2018/key_cnn.pkl')

# drums
DRUMS_CRNN = sorted(glob.glob('%s/drums/2017/drums_crnn5_[0-3].pkl' % path))
DRUMS_BRNN = sorted(glob.glob('%s/drums/2017/drums_brnn2_[0-3].pkl' % path))
DRUMS_CNN  = sorted(glob.glob('%s/drums/2017/drums_cnn3_[0-3].pkl' % path))

DRUMS_CRNN_R = sorted(glob.glob('%s/drums/2017/drums_crnn5_rand_[0-2].pkl' % path))
DRUMS_BRNN_R = sorted(glob.glob('%s/drums/2017/drums_brnn2_rand_[0-2].pkl' % path))
DRUMS_CNN_R  = sorted(glob.glob('%s/drums/2017/drums_cnn3_rand_[0-2].pkl' % path))  # '%s/drums/2017/drums_cnn3_rand_2.pkl' % path] #

DRUMS_CRNN_8  = sorted(glob.glob('%s/drums/2018/drums_crnn1_O8_S[0-4].pkl' % path))
DRUMS_CNN_8   = sorted(glob.glob('%s/drums/2018/drums_cnn0_O8_S[0-4].pkl' % path))
DRUMS_CRNN_18 = sorted(glob.glob('%s/drums/2018/drums_crnn1_O18_S[0-4].pkl' % path))
DRUMS_CNN_18  = sorted(glob.glob('%s/drums/2018/drums_cnn0_O18_S[0-4].pkl' % path))

# DRUMS_SUPER = DRUMS_CRNN + DRUMS_BRNN + DRUMS_CNN

# keep namespace clean
del os, glob
