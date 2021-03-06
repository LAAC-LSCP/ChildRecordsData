from ChildProject.projects import ChildProject
from ChildProject.pipelines.conversion import ConversionPipeline
import numpy as np
import os
import pandas
import shutil

def test_convert():
    shutil.copytree(src = "examples/valid_raw_data", dst = "output/convert")

    profile = ConversionPipeline().run(
        path = 'output/convert',
        name = 'test',
        format = 'wav',
        codec = 'pcm_s16le',
        sampling = 16000
    )

    project = ChildProject("output/convert")
    project.read()

    recordings = project.recordings
    converted_recordings = profile.recordings

    assert np.isclose(4000, project.compute_recordings_duration()['duration'].sum()), "audio duration equals expected value"
    assert os.path.exists(os.path.join("output/convert/", ChildProject.CONVERTED_RECORDINGS, "test")), "missing converted recordings folder"
    assert recordings.shape[0] == converted_recordings.shape[0], "conversion table is incomplete"
    assert all(converted_recordings['success'].tolist()), "not all recordings were successfully converted"
    assert all([
        os.path.exists(os.path.join("output/convert/", ChildProject.CONVERTED_RECORDINGS, "test", f))
        for f in converted_recordings['converted_filename'].tolist()
    ]), "recording files are missing"


