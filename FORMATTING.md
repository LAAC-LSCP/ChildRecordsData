

- [Datasets structure](#datasets-structure)
  - [Dataset tree](#dataset-tree)
  - [Metadata](#metadata)
    - [children notebook](#children-notebook)
    - [recording notebook](#recording-notebook)
- [Annotations](#annotations)
  - [Annotations format](#annotations-format)
  - [Annotations index](#annotations-index)
  - [Annotation importation input format](#annotation-importation-input-format)

# Datasets structure

ChildRecordsData assumes your data is structured in a specific way before it is imported. This structure is necessary to check, for instance, that there are no unreferenced files, and no referenced files that are actually missing. The data curator therefore needs to organize their data in a specific way (respecting the dataset tree, with all specified metadata files, and all specified columns within the metadata files) before their data can be imported.

To be imported, datasets must pass the [the validation routine](https://laac-lscp.github.io/ChildRecordsData/#validate-raw-data) with no error. We also recommend you pay attention to the warnings, and try to sort as many of those out as possible before submission.

## Dataset tree

All datasets should have this structure before import (so you need to organize your files into this structure):

```
project
│   
│
└───metadata
│   │   children.csv
│   │   recordings.csv
│   │   annotations.csv
|
└───recordings
│   └───raw
│   │   │   recording1.wav
│
└───annotations
│   └───vtc
│   │   └───raw
│   │   │   │   child1.rttm
│   └───annotator1
│   │   └───raw
│   │   │   │   child1_3600.TextGrid
│
└───extra
    │   notes.txt
```

The children and recordings notebooks should be formatted according to the standards detailed right below.

## Metadata


### children notebook

Located in the `metadata` folder. Can be named either `children.csv`, `children.xls` or `children.xslx`.

| Name | Description | Required ? | Format |
|------|-------------|------------|--------|
| **experiment** | one word to capture the unique ID of the data collection effort; for instance Tsimane_2018, solis-intervention-pre | **required** | - |
| **child_id** | unique child ID -- unique within the experiment (Id could be repeated across experiments to refer to different children) | **required** | - |
| **child_dob** | child's date of birth | **required** | `%Y-%m-%d` (date/time) |
| **location_id** | Unique location ID -- only specify here if children never change locations in this culture; otherwise, specify in the recordings metadata | optional | - |
| **child_sex** | f= female, m=male | optional | m, M, f, F |
| **language** | language the child is exposed to if child is monolingual; small caps, indicate dialect by name or location if available; eg "france french"; "paris french" | optional | - |
| **languages** | list languages child is exposed to separating them with ; and indicating the percentage if one is available; eg: "french 35%; english 65%" | optional | - |
| **mat_ed** | maternal years of education | optional | - |
| **fat_ed** | paternal years of education | optional | - |
| **car_ed** | years of education of main caregiver (if not mother or father) | optional | - |
| **monoling** | whether the child is monolingual (Y) or not (N) | optional | Y, N |
| **monoling_criterion** | how monoling was decided; eg "we asked families which languages they spoke in the home" | optional | - |
| **normative** | whether the child is normative (Y) or not (N) | optional | Y, N |
| **normative_criterion** | how normative was decided; eg "unless the caregivers volunteered information whereby the child had a problem, we consider them normative by default" | optional | - |
| **mother_id** | unique ID of the mother | optional | - |
| **father_id** | unique ID of the father | optional | - |
| **order_of_birth** | child order of birth | optional | `(\d+(\.\d+)?)` (regex) |
| **n_of_siblings** | amount of siblings | optional | `(\d+(\.\d+)?)` (regex) |
| **household_size** | number of people living in the household (adults+children) | optional | `(\d+(\.\d+)?)` (regex) |
| **dob_criterion** | determines whether the date of birth is known exactly or extrapolated e.g. from the age. Dates of birth are assumed to be known exactly if this column is NA or unspecified. | optional | extrapolated, exact |
| **dob_accuracy** | date of birth accuracy | optional | extact, week, month, year, other |


### recording notebook

Located in the `metadata` folder.  Can be named either `recordings.csv`, `recordings.xls` or `recordings.xslx`.

| Name | Description | Required ? | Format |
|------|-------------|------------|--------|
| **experiment** | one word to capture the unique ID of the data collection effort; for instance Tsimane_2018, solis-intervention-pre | **required** | - |
| **child_id** | unique child ID -- unique within the experiment (Id could be repeated across experiments to refer to different children) | **required** | - |
| **date_iso** | date in which recording was started in ISO (eg 2020-09-17) | **required** | `%Y-%m-%d` (date/time) |
| **start_time** | local time in which recording was started in format 24-hour (H)H:MM; if minutes are unknown, use 00. Set as ‘NA’ if unknown. | **required** | `%H:%M` (date/time) |
| **recording_device_type** | lena, usb, olympus, babylogger (lowercase) | **required** | lena, usb, olympus, babylogger |
| **filename** | the path to the file from the root of “recordings”), set to ‘NA’ if no valid recording available. It is unique (two recordings cannot point towards the same file). | **required** | filename |
| **duration** | duration of the audio | optional | `(\d+(\.\d+)?)` (regex) |
| **recording_device_id** | unique ID of the recording device | optional | - |
| **experimenter** | who collected the data (could be anonymized ID) | optional | - |
| **location_id** | unique location ID -- can be specified at the level of the child (if children do not change locations) | optional | - |
| **its_filename** | its_filename | optional | filename |
| **upl_filename** | upl_filename | optional | filename |
| **trs_filename** | trs_filename | optional | filename |
| **lena_id** |  | optional | - |
| **might_feature_gaps** | 1 if the audio cannot be guaranteed to be a continuous block with no time jumps, 0 or NA or undefined otherwise. | optional | is_boolean (function) |
| **start_time_accuracy** | Accuracy of start_time for this recording. If not specified, assumes minute-accuray. | optional | minute, hour, reliable |
| **noisy_setting** | 1 if the audio may be noisier than the childs usual day, 0 or undefined otherwise | optional | is_boolean (function) |
| **notes** | free-style notes about individual recordings (avoid tabs and newlines) | optional | - |


# Annotations

## Annotations format

The package provides functions to convert any annotation into the following csv format, with one row per segment :

| Name | Description | Format |
|------|-------------|--------|
| **annotation_file** | raw annotation path relative, relative to `annotations/<set>/raw` | - |
| **segment_onset** | segment start time in seconds | `(\d+(\.\d+)?)` (regex) |
| **segment_offset** | segment end time in seconds | `(\d+(\.\d+)?)` (regex) |
| **speaker_id** | identity of speaker in the annotation | - |
| **speaker_type** | class of speaker (FEM, MAL, CHI, OCH) | FEM, MAL, CHI, OCH, SPEECH, TVN, TVF, FUZ, FEF, MAF, SIL, CXF, NON, OLN, OLF, CHF, NA |
| **ling_type** | 1 if the vocalization contains at least a vowel (ie canonical or non-canonical), 0 if crying or laughing | 1, 0, NA |
| **vcm_type** | vocal maturity defined as: C (canonical), N (non-canonical), Y (crying) L (laughing), J (junk) | C, N, Y, L, J, NA |
| **lex_type** | W if meaningful, 0 otherwise | W, 0, NA |
| **mwu_type** | M if multiword, 1 if single word -- only filled if lex_type==W | M, 1, NA |
| **addresseee** | T if target-child-directed, C if other-child-directed, A if adult-directed, U if uncertain or other | T, C, A, U, NA |
| **transcription** | orthographic transcription of the speach | - |
| **phonemes** | amount of phonemes | `(\d+(\.\d+)?)` (regex) |
| **syllables** | amount of syllables | `(\d+(\.\d+)?)` (regex) |
| **words** | amount of words | `(\d+(\.\d+)?)` (regex) |
| **lena_block_type** | whether regarded as part as a pause or a conversation by LENA | pause, CM, CIC, CIOCX, CIOCAX, AMF, AICF, AIOCF, AIOCCXF, AMM, AICM, AIOCM, AIOCCXM, XM, XIOCC, XIOCA, XIC, XIOCAC |
| **lena_block_number** | number of the LENA pause/conversation the segment belongs to | `(\d+(\.\d+)?)` (regex) |
| **lena_conv_status** | LENA conversation status | BC, RC, EC |
| **lena_response_count** | LENA turn count within block | `(\d+(\.\d+)?)` (regex) |
| **lena_conv_floor_type** | (FI): Floor Initiation, (FH): Floor Holding | FI, FH |
| **lena_conv_turn_type** | LENA turn type | TIFI, TIMI, TIFR, TIMR, TIFE, TIME, NT |
| **utterances_count** | utterances count | `(\d+(\.\d+)?)` (regex) |
| **utterances_length** | utterances length | `(\d+(\.\d+)?)` (regex) |
| **non_speech_length** | non-speech length | `(\d+(\.\d+)?)` (regex) |
| **average_db** | average dB level | `(\-?)(\d+(\.\d+)?)` (regex) |
| **peak_db** | peak dB level | `(\-?)(\d+(\.\d+)?)` (regex) |
| **child_cry_vfx_len** | childCryVfxLen | `(\d+(\.\d+)?)` (regex) |
| **utterances** | LENA utterances details (json) | - |
| **cries** | cries (json) | - |
| **vfxs** | Vfx (json) | - |


## Annotations index

Annotations are indexed in one unique dataframe located at `/metadata/annotations.csv`, with the following format :

| Name | Description | Format |
|------|-------------|--------|
| **set** | name of the annotation set (e.g. VTC, annotator1, etc.) | - |
| **recording_filename** | recording filename as specified in the recordings index | - |
| **time_seek** | reference time in seconds, e.g: 3600, or 3600.500. All times expressed in the annotations are relative to this time. | `(\-?)(\d+(\.\d+)?)` (regex) |
| **range_onset** | covered range start time in seconds, measured since `time_seek` | `(\d+(\.\d+)?)` (regex) |
| **range_offset** | covered range end time in seconds, measured since `time_seek` | `(\d+(\.\d+)?)` (regex) |
| **raw_filename** | annotation input filename location, relative to `annotations/<set>/raw` | filename |
| **annotation_filename** | output formatted annotation location (automatic column, don't specify) | filename |
| **imported_at** | importation date (automatic column, don't specify) | `%Y-%m-%d %H:%M:%S` (date/time) |
| **error** | error message in case the annotation could not be imported | - |


## Annotation importation input format

The annotations importation script and function take a dataframe of the following format as an input :

| Name | Description | Required ? | Format |
|------|-------------|------------|--------|
| **set** | name of the annotation set (e.g. VTC, annotator1, etc.) | **required** | - |
| **recording_filename** | recording filename as specified in the recordings index | **required** | - |
| **time_seek** | reference time in seconds, e.g: 3600, or 3600.500. All times expressed in the annotations are relative to this time. | **required** | `(\-?)(\d+(\.\d+)?)` (regex) |
| **range_onset** | covered range start time in seconds, measured since `time_seek` | **required** | `(\d+(\.\d+)?)` (regex) |
| **range_offset** | covered range end time in seconds, measured since `time_seek` | **required** | `(\d+(\.\d+)?)` (regex) |
| **raw_filename** | annotation input filename location, relative to `annotations/<set>/raw` | **required** | filename |
| **format** | input annotation format | optional | TextGrid, eaf, vtc_rttm, alice, its |
| **filter** | source file to filter in (for rttm and alice only) | optional | - |

