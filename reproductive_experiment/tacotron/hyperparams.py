
# -*- coding: utf-8 -*-
#/usr/bin/python3
'''
By kyubyong park. kbpark.linguist@gmail.com. 
https://www.github.com/kyubyong/tacotron
'''

# commit hash
# 6009936

class Hyperparams:
    '''Hyper parameters'''
    # mode
    sanity_check = True

    # data
    data_set = 'siwis' # 'bible', 'atr503', 'siwis', 'lj'
    bible_text_file = 'WEB/text.csv'
    bible_sound_fpath = 'WEB'
    lj_text_file = 'LJSpeech-1.0/metadata.csv'
    lj_sound_fpath = 'LJSpeech-1.0/wavs'
    atr503_text_file = 'atr503/source.csv'
    atr503_sound_fpath = 'atr503/wav_22050'
    siwis_text_file = 'The_SIWIS_French_Speech_Synthesis_Database/SiwisFrenchSpeechSynthesisDatabase/text.csv'
    siwis_sound_fpath = 'The_SIWIS_French_Speech_Synthesis_Database/SiwisFrenchSpeechSynthesisDatabase/wavs'
    max_len = 100 if not sanity_check else 30 # maximum length of text
    min_len = 10 if not sanity_check else 20
    preload_audio = True
    reverse_input = False

    # signal processing
    sr = 22050 # Sampling rate. Paper => 24000
    n_fft = 2048 # fft points (samples)
    frame_shift = 0.0125 # seconds
    frame_length = 0.05 # seconds
    hop_length = int(sr*frame_shift) # samples  This is dependent on the frame_shift.
    win_length = int(sr*frame_length) # samples This is dependent on the frame_length.
    n_mels = 80 # Number of Mel banks to generate
    power = 1.2 # Exponent for amplifying the predicted magnitude
    n_iter = 30 # Number of inversion iterations
    use_log_magnitude = True # if False, use magnitude

    # model
    embed_size = 256 # alias = E
    encoder_num_banks = 16
    decoder_num_banks = 8
    num_highwaynet_blocks = 4
    r = 5 # Reduction factor. Paper => 2, 3, 5
    norm_type = "ins" # a normalizer function. value: bn, ln, ins or None

    # training scheme
    lr = 0.0010 # Paper => Exponential decay
    logdir = "logdir_" + data_set if not sanity_check else "logdir_s_" + data_set
    outputdir = 'samples_' + data_set if not sanity_check else "samples_s_" + data_set
    batch_size = 32
    num_epochs = 10000 if not sanity_check else 40 # Paper => 2M global steps!
    loss_type = "l2" # Or you can test "l1"
    num_samples = 32
    decay_step = 300
    decay_rate=0.96

    max_iters=100

    # etc
    num_gpus = 1 # If you have multiple gpus, adjust this option, and increase the batch size
                 # and run `train_multiple_gpus.py` instead of `train.py`.
    target_zeros_masking = False # If True, we mask zero padding on the target, 
                                 # so exclude them from the loss calculation.