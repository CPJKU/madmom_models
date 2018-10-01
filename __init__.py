# encoding: utf-8
"""
Models package.

Please see the LICENSE file for licensing details of this package.

"""

from __future__ import absolute_import, division, print_function

import os
import glob

path = os.path.dirname(__file__)

# beats
BEATS_LSTM = sorted(glob.glob('%s/beats/2016/beats_lstm_[1-8].pkl' % path))
BEATS_BLSTM = sorted(glob.glob('%s/beats/2015/beats_blstm_[1-8].pkl' % path))

# downbeats
DOWNBEATS_BLSTM = sorted(glob.glob(
    '%s/downbeats/2016/downbeats_blstm_[1-8].pkl' % path))
DOWNBEATS_BGRU = [
    sorted(glob.glob(
        '%s/downbeats/2016/downbeats_bgru_rhythmic_*.pkl' % path)),
    sorted(glob.glob(
        '%s/downbeats/2016/downbeats_bgru_harmonic_*.pkl' % path))]

# notes
NOTES_BRNN = sorted(glob.glob('%s/notes/2013/notes_brnn.pkl' % path))

# onsets
ONSETS_RNN = sorted(glob.glob('%s/onsets/2013/onsets_rnn_[1-8].pkl' % path))
ONSETS_BRNN = sorted(glob.glob('%s/onsets/2013/onsets_brnn_[1-8].pkl' % path))
ONSETS_BRNN_PP = sorted(glob.glob('%s/onsets/2014/onsets_brnn_pp_[1-8].pkl' %
                                  path))
ONSETS_CNN = sorted(glob.glob('%s/onsets/2013/onsets_cnn.pkl' % path))

# patterns
PATTERNS_BALLROOM = sorted(
    glob.glob('%s/patterns/2013/ballroom_pattern_[34]_4.pkl' % path))

# chroma
CHROMA_DNN = ['%s/chroma/2016/chroma_dnn.pkl' % path]

# chords
CHORDS_DCCRF = ['%s/chords/2016/chords_dccrf.pkl' % path]
CHORDS_CNN_FEAT = ['%s/chords/2016/chords_cnnfeat.pkl' % path]
CHORDS_CFCRF = ['%s/chords/2016/chords_cnncrf.pkl' % path]

# key
KEY_CNN = ['%s/key/2018/key_cnn.pkl' % path]

# keep namespace clean
del os, glob, path
