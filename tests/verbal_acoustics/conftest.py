from pytest import fixture

test_path = "tests/test_data/"
path_mp4 = test_path + "facial_speech_verbal_video_test.mp4"
path_wav = test_path + "facial_speech_verbal_audio_test.wav"


@fixture(scope="class")
def processing_verbal_acoustics_mp4(get_model):
    m = get_model.verbal_acoustics
    m.fit(path_mp4)
    yield m


@fixture(scope="class")
def processing_verbal_acoustics_wav(get_model):
    m = get_model.verbal_acoustics
    m.fit(path_wav)
    yield m
