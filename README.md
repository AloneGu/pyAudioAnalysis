## Audio process play box

some examples of audio process

## Dependencies

pyAudioAnalysis: https://github.com/tyiannak/pyAudioAnalysis

and its requirements: follow this page: https://github.com/tyiannak/pyAudioAnalysis/wiki/2.-General

## Note

The sklearn version is 0.16 as hmm is removed in latest version:

pip install scikit-learn==0.16

source xxx

## Example to do speaker diarization

        python audioAnalysis.py speakerDiarization -i data/test.wav --num 0 --flsd