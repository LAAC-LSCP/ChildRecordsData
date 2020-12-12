import datetime
import glob
import numpy as np
import os
import pandas as pd
import re
import shutil
import subprocess

from .tables import IndexTable, IndexColumn, is_boolean
from .utils import get_audio_duration

class ChildProject:
    REQUIRED_DIRECTORIES = [
        'recordings',
        'extra'
    ]

    CHILDREN_COLUMNS = [
        IndexColumn(name = 'experiment', description = 'one word to capture the unique ID of the data collection effort; for instance Tsimane_2018, solis-intervention-pre', required = True),
        IndexColumn(name = 'child_id', description = 'unique child ID -- unique within the experiment (Id could be repeated across experiments to refer to different children)', unique = True, required = True),
        IndexColumn(name = 'child_dob', description = "child's date of birth", required = True, datetime = '%Y-%m-%d'),
        IndexColumn(name = 'location_id', description = 'Unique location ID -- only specify here if children never change locations in this culture; otherwise, specify in the recordings metadata'),
        IndexColumn(name = 'child_sex', description = 'f= female, m=male', choices = ['m', 'M', 'f', 'F']),
        IndexColumn(name = 'language', description = 'language the child is exposed to if child is monolingual; small caps, indicate dialect by name or location if available; eg "france french"; "paris french"'),
        IndexColumn(name = 'languages', description = 'list languages child is exposed to separating them with ; and indicating the percentage if one is available; eg: "french 35%; english 65%"'),
        IndexColumn(name = 'mat_ed', description = 'maternal years of education'),
        IndexColumn(name = 'fat_ed', description = 'paternal years of education'),
        IndexColumn(name = 'car_ed', description = 'years of education of main caregiver (if not mother or father)'),
        IndexColumn(name = 'monoling', description = 'whether the child is monolingual (Y) or not (N)', choices = ['Y', 'N']),
        IndexColumn(name = 'monoling_criterion', description = 'how monoling was decided; eg "we asked families which languages they spoke in the home"'),
        IndexColumn(name = 'normative', description = 'whether the child is normative (Y) or not (N)', choices = ['Y', 'N']),
        IndexColumn(name = 'normative_criterion', description = 'how normative was decided; eg "unless the caregivers volunteered information whereby the child had a problem, we consider them normative by default"'),
        IndexColumn(name = 'mother_id', description = 'unique ID of the mother'),
        IndexColumn(name = 'father_id', description = 'unique ID of the father'),
        IndexColumn(name = 'order_of_birth', description = 'child order of birth', regex = r'(\d+(\.\d+)?)', required = False),
        IndexColumn(name = 'n_of_siblings', description = 'amount of siblings', regex = r'(\d+(\.\d+)?)', required = False),
        IndexColumn(name = 'household_size', description = 'number of people living in the household (adults+children)', regex = r'(\d+(\.\d+)?)', required = False),
        IndexColumn(name = 'dob_criterion', description = "determines whether the date of birth is known exactly or extrapolated e.g. from the age. Dates of birth are assumed to be known exactly if this column is NA or unspecified.", choices = ['extrapolated', 'exact'], required = False),
        IndexColumn(name = 'dob_accuracy', description = "date of birth accuracy", choices = ['extact', 'week', 'month', 'year', 'other'])
    ]

    RECORDINGS_COLUMNS = [
        IndexColumn(name = 'experiment', description = 'one word to capture the unique ID of the data collection effort; for instance Tsimane_2018, solis-intervention-pre', required = True),
        IndexColumn(name = 'child_id', description = 'unique child ID -- unique within the experiment (Id could be repeated across experiments to refer to different children)', required = True),
        IndexColumn(name = 'date_iso', description = 'date in which recording was started in ISO (eg 2020-09-17)', required = True, datetime = '%Y-%m-%d'),
        IndexColumn(name = 'start_time', description = 'local time in which recording was started in format 24-hour (H)H:MM; if minutes are unknown, use 00. Set as ‘NA’ if unknown.', required = True, datetime = '%H:%M'),
        IndexColumn(name = 'recording_device_type', description = 'lena, usb, olympus, babylogger (lowercase)', required = True, choices = ['lena', 'usb', 'olympus', 'babylogger']),
        IndexColumn(name = 'filename', description = 'the path to the file from the root of “recordings”), set to ‘NA’ if no valid recording available. It is unique (two recordings cannot point towards the same file).', required = True, filename = True, unique = True),
        IndexColumn(name = 'duration', description = 'duration of the audio', regex = r'(\d+(\.\d+)?)'),
        IndexColumn(name = 'recording_device_id', description = 'unique ID of the recording device'),
        IndexColumn(name = 'experimenter', description = 'who collected the data (could be anonymized ID)'),
        IndexColumn(name = 'location_id', description = 'unique location ID -- can be specified at the level of the child (if children do not change locations)'),
        IndexColumn(name = 'its_filename', description = 'its_filename', filename = True),
        IndexColumn(name = 'upl_filename', description = 'upl_filename', filename = True),
        IndexColumn(name = 'trs_filename', description = 'trs_filename', filename = True),
        IndexColumn(name = 'lena_id', description = ''),
        IndexColumn(name = 'might_feature_gaps', description = '1 if the audio cannot be guaranteed to be a continuous block with no time jumps, 0 or NA or undefined otherwise.', function = is_boolean),
        IndexColumn(name = 'start_time_accuracy', description = 'Accuracy of start_time for this recording. If not specified, assumes minute-accuray.', choices = ['minute', 'hour', 'reliable']),
        IndexColumn(name = 'noisy_setting', description = '1 if the audio may be noisier than the childs usual day, 0 or undefined otherwise', function = is_boolean),
        IndexColumn(name = 'notes', description = 'free-style notes about individual recordings (avoid tabs and newlines)')
    ]

    PROJECT_FOLDERS = [
        'raw_annotations',
        'annotations',
        'metadata',
        'converted_recordings',
        'doc',
        'scripts'
    ]

    def __init__(self, path):
        self.path = path
        self.errors = []
        self.warnings = []
        self.children = None
        self.recordings = None
    
    def read(self):
        self.ct = IndexTable('children', os.path.join(self.path, 'metadata/children'), self.CHILDREN_COLUMNS)
        self.rt = IndexTable('recordings', os.path.join(self.path, 'metadata/recordings'), self.RECORDINGS_COLUMNS)

        self.children = self.ct.read(lookup_extensions = ['.csv', '.xls', '.xlsx'])
        self.recordings = self.rt.read(lookup_extensions = ['.csv', '.xls', '.xlsx'])

    def validate_input_data(self, ignore_files = False):
        self.errors = []
        self.warnings = []

        path = self.path

        directories = [d for d in os.listdir(path) if os.path.isdir(path)]

        for rd in self.REQUIRED_DIRECTORIES:
            if rd not in directories:
                self.errors.append("missing directory {}.".format(rd))

        # check tables
        self.read()
        
        errors, warnings = self.ct.validate()
        self.errors += errors
        self.warnings += warnings

        errors, warnings = self.rt.validate()
        self.errors += errors
        self.warnings += warnings

        if ignore_files:
            return self.errors, self.warnings

        for index, row in self.recordings.iterrows():
            # make sure that recordings exist
            for column_name in self.recordings.columns:
                column_attr = next((c for c in self.RECORDINGS_COLUMNS if c.name == column_name), None)

                if column_attr is None:
                    continue

                if column_attr.filename and row[column_name] != 'NA' and not os.path.exists(os.path.join(path, 'recordings', str(row[column_name]))):
                    self.errors.append("cannot find recording '{}'".format(str(row[column_name])))

            # child id refers to an existing child in the children table
            if row['child_id'] not in self.children['child_id'].tolist():
                self.errors.append("child_id '{}' in recordings on line {} cannot be found in the children table.".format(row['child_id'], index))

        # detect un-indexed recordings and throw warnings
        files = [
            self.recordings[c.name].tolist()
            for c in self.RECORDINGS_COLUMNS
            if c.filename and c.name in self.recordings.columns
        ]

        indexed_files = [
            os.path.abspath(os.path.join(path, 'recordings', str(f)))
            for f in pd.core.common.flatten(files)
        ]

        recordings_files = glob.glob(os.path.join(path, 'recordings', '**/*.*'), recursive = True)

        for rf in recordings_files:
            if len(os.path.splitext(rf)) > 1 and os.path.splitext(rf)[1] in ['.csv', '.xls', '.xlsx']:
                continue

            ap = os.path.abspath(rf)
            if ap not in indexed_files:
                self.warnings.append("file '{}' not indexed.".format(rf))

        return self.errors, self.warnings

    def import_data(self, destination, follow_symlinks = True):
        errors, warnings = self.validate_input_data()

        if len(errors) > 0:
            raise Exception('cannot import data: validation failed')

        # perform copy
        shutil.copytree(src = self.path, dst = destination, symlinks = follow_symlinks)

        # create folders
        for folder in self.PROJECT_FOLDERS:
            os.makedirs(
                name = os.path.join(destination, folder),
                exist_ok = True
            )

    def get_stats(self):
        stats = {}
        recordings = self.recordings.merge(self.compute_recordings_duration(), left_on = 'filename', right_on = 'filename')
        recordings['exists'] = recordings['filename'].map(lambda f: os.path.exists(os.path.join(self.path, 'recordings', f)))

        stats['total_recordings'] = recordings.shape[0]
        stats['total_existing_recordings'] = recordings[recordings['exists'] == True].shape[0]
        stats['audio_duration'] = recordings['duration'].sum()
        stats['total_children'] = self.children.shape[0]

        return stats

    def compute_recordings_duration(self, profile = None):
        recordings = self.recordings[['filename']]

        recordings['duration'] = recordings['filename'].map(lambda f:
            get_audio_duration(os.path.join(self.path, 'converted_recordings', profile, f)) if profile
            else get_audio_duration(os.path.join(self.path, 'recordings', f))
        )

        return recordings
