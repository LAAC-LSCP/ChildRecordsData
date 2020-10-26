

- [Source data formatting guidelines](#source-data-formatting-guidelines)
  - [Raw data tree](#raw-data-tree)
  - [children notebook](#children-notebook)
  - [recording notebook](#recording-notebook)
- [Annotations formatting](#annotations-formatting)
  - [Annotations format](#annotations-format)
  - [Annotations index](#annotations-index)
  - [Annotation importation input format](#annotation-importation-input-format)

# Source data formatting guidelines

Projects must pass the [the validation script](https://laac-lscp.github.io/ChildRecordsData/#validate-raw-data) with no error and as few warnings as possible before submission.

## Raw data tree

Before submission, data should comply with the following structure :

```
project
│   children.csv
│
└───recordings
│   │   recordings.csv
│   │   recording1.wav
│
└───raw_annotations
│   │   child1.rttm
│   │   child1_3600.TextGrid
│
└───extra
    │   notes.txt
```

The children and recordings notebooks should be formatted according to the standards detailed right below.

## children notebook

Can be either `children.csv`, `children.xls` or `children.xslx`.

| Name | Description | Required ? | Format |
|------|-------------|------------|--------|
| **experiment** | one word to capture the unique ID of the data collection effort; for instance Tsimane_2018, solis-intervention-pre | **required** | - |
| **child_id** | unique child ID -- unique within the experiment (Id could be repeated across experiments to refer to different children) | **required** | - |
| **child_dob** | child's date of birth | **required** | `%Y-%m-%d` (date/time) |
| **location_id** | Unique location ID -- only specify here if children never change locations in this culture; otherwise, specify in the recordings metadata | optional | - |
| **child_sex** | f= female, m=male | optional | `(m|f|M|F)` (regex) |
| **language** | language the child is exposed to if child is monolingual; small caps, indicate dialect by name or location if available; eg "france french"; "paris french" | optional | - |
| **languages** | list languages child is exposed to separating them with ; and indicating the percentage if one is available; eg: "french 35%; english 65%" | optional | - |
| **mat_ed** | maternal years of education | optional | - |
| **fat_ed** | paternal years of education | optional | - |
| **car_ed** | years of education of main caregiver (if not mother or father) | optional | - |
| **monoling** | whether the child is monolingual (Y) or not (N) | optional | `(Y|N)` (regex) |
| **monoling_criterion** | how monoling was decided; eg "we asked families which languages they spoke in the home" | optional | - |
| **normative** | whether the child is normative (Y) or not (N) | optional | `(Y|N)` (regex) |
| **normative_criterion** | how normative was decided; eg "unless the caregivers volunteered information whereby the child had a problem, we consider them normative by default" | optional | - |
| **mother_id** | unique ID of the mother | optional | - |
| **father_id** | unique ID of the father | optional | - |
| **daytime** | yes (Y) means recording launched such that most or all of the audiorecording happens during daytime; no (N) means at least 30% of the recording may happen at night | optional | `(Y|N)` (regex) |


## recording notebook

Can be either `recordings/recordings.csv`, `recordings/recordings.xls` or `recordings/recordings.xslx`.

| Name | Description | Required ? | Format |
|------|-------------|------------|--------|
| **experiment** | one word to capture the unique ID of the data collection effort; for instance Tsimane_2018, solis-intervention-pre | **required** | - |
| **child_id** | unique child ID -- unique within the experiment (Id could be repeated across experiments to refer to different children) | **required** | - |
| **date_iso** | date in which recording was started in ISO (eg 2020-09-17) | **required** | `%Y-%m-%d` (date/time) |
| **start_time** | local time in which recording was started in format 24-hour (H)H:MM; if minutes are unknown, use 00. Set as ‘NA’ if unknown. | **required** | `%H:%M` (date/time) |
| **recording_device_type** | lena, usb, olympus, babylogger (lowercase) | **required** | `(lena|usb|olympus|babylogger)` (regex) |
| **filename** | the path to the file from the root of “recordings”), set to ‘NA’ if no valid recording available. It is unique (two recordings cannot point towards the same file). | **required** | filename |
| **recording_device_id** | unique ID of the recording device | optional | - |
| **experimenter** | who collected the data (could be anonymized ID) | optional | - |
| **location_id** | unique location ID -- can be specified at the level of the child (if children do not change locations) | optional | - |
| **its_filename** | its_filename | optional | filename |
| **upl_filename** | upl_filename | optional | filename |
| **lena_id** |  | optional | - |
| **age** | age in months (rounded) | optional | `^[0-9]+$` (regex) |
| **notes** | free-style notes about individual recordings (avoid tabs and newlines) | optional | - |


# Annotations formatting

## Annotations format

The package provides functions to convert any annotation into the following csv format, with one row per segment :

| Name | Description | Format |
|------|-------------|--------|
| **annotation_file** | raw annotation path relative to /raw_annotations/ | - |
| **segment_onset** | segment start time in seconds | `(\d+(\.\d+)?)` (regex) |
| **segment_offset** | segment end time in seconds | `(\d+(\.\d+)?)` (regex) |
| **speaker_id** | identity of speaker in the annotation | - |
| **speaker_type** | class of speaker (FEM, MAL, CHI, OCH) | `(FEM|MAL|CHI|OCH|SPEECH|NA)` (regex) |
| **ling_type** | 1 if the vocalization contains at least a vowel (ie canonical or non-canonical), 0 if crying or laughing | `(1|0|NA)` (regex) |
| **vcm_type** | vocal maturity defined as: C (canonical), N (non-canonical), Y (crying) L (laughing), J (junk) | `(C|N|Y|L|J|NA)` (regex) |
| **lex_type** | W if meaningful, 0 otherwise | `(W|0|NA)` (regex) |
| **mwu_type** | M if multiword, 1 if single word -- only filled if lex_type==W | `(M|1|NA)` (regex) |
| **addresseee** | T if target-child-directed, C if other-child-directed, A if adult-directed, U if uncertain or other | `(T|C|A|U|NA)` (regex) |
| **transcription** | orthographic transcription of the speach | - |


## Annotations index

Annotations are indexed in one unique dataframe located at `/annotations/annotations.csv`, with the following format :

| Name | Description | Format |
|------|-------------|--------|
| **set** | name of the annotation set (e.g. VTC, annotator1, etc.) | - |
| **recording_filename** | recording filename as specified in the recordings index | - |
| **time_seek** | reference time in seconds, e.g: 3600, or 3600.500. All times expressed in the annotations are relative to this time. | `[0-9]{1,}(\.[0-9]{3})?` (regex) |
| **range_onset** | covered range start time in seconds, measured since `time_seek` | `[0-9]{1,}(\.[0-9]{3})?` (regex) |
| **range_offset** | covered range end time in seconds, measured since `time_seek` | `[0-9]{1,}(\.[0-9]{3})?` (regex) |
| **raw_filename** | annotation input filename location (relative to raw_annotations/) | filename |
| **format** | input annotation format | `(TextGrid|eaf|vtc_rttm)` (regex) |
| **annotation_filename** | output formatted annotation location (automatic column, don't specify) | filename |
| **imported_at** | importation date (automatic column, don't specify) | `%Y-%m-%d %H:%M:%S` (date/time) |
| **error** | error message in case the annotation could not be imported | - |


## Annotation importation input format

The annotations importation script and function take a dataframe of the following format as an input :

| Name | Description | Required ? | Format |
|------|-------------|------------|--------|
| **set** | name of the annotation set (e.g. VTC, annotator1, etc.) | **required** | - |
| **recording_filename** | recording filename as specified in the recordings index | **required** | - |
| **time_seek** | reference time in seconds, e.g: 3600, or 3600.500. All times expressed in the annotations are relative to this time. | **required** | `[0-9]{1,}(\.[0-9]{3})?` (regex) |
| **range_onset** | covered range start time in seconds, measured since `time_seek` | **required** | `[0-9]{1,}(\.[0-9]{3})?` (regex) |
| **range_offset** | covered range end time in seconds, measured since `time_seek` | **required** | `[0-9]{1,}(\.[0-9]{3})?` (regex) |
| **raw_filename** | annotation input filename location (relative to raw_annotations/) | **required** | filename |
| **format** | input annotation format | **required** | `(TextGrid|eaf|vtc_rttm)` (regex) |
| **filter** | source file to filter in (for rttm only) | optional | - |

