

## Raw data tree

```
project
│   children.csv
│
└───recordings
│   │   recordings.csv
│   │   recording1.wav
│
└───extra
    │   notes.txt
``` 

## children notebook

Can be either `children.csv`, `children.xls` or `children.xslx`.

| Name | Description | Required ? | Format |
|------|-------------|------------|--------|
| **experiment** | one word to capture the unique ID of the data collection effort; for instance Tsimane_2018, solis-intervention-pre | **required** | - |
| **child_id** | unique child ID -- unique within the experiment (Id could be repeated across experiments to refer to different children) | **required** | - |
| **child_dob** | child's date of birth | **required** | `%Y-%m-%d` (date/time) |
| **location_id** | Unique location ID -- only specify here if children never change locations in this culture; otherwise, specify in the recordings metadata | optional | - |
| **child_sex** | f= female, m=male | optional | `(m\|f\|M\|F)` (regex) |
| **language** | language the child is exposed to if child is monolingual; small caps, indicate dialect by name or location if available; eg "france french"; "paris french" | optional | - |
| **languages** | list languages child is exposed to separating them with ; and indicating the percentage if one is available; eg: "french 35%; english 65%" | optional | - |
| **mat_ed** | maternal years of education | optional | - |
| **fat_ed** | paternal years of education | optional | - |
| **car_ed** | years of education of main caregiver (if not mother or father) | optional | - |
| **monoling** | whether the child is monolingual (Y) or not (N) | optional | `(Y\|N)` (regex) |
| **monoling_criterion** | how monoling was decided; eg "we asked families which languages they spoke in the home" | optional | - |
| **normative** | whether the child is normative (Y) or not (N) | optional | `(Y\|N)` (regex) |
| **normative_criterion** | how normative was decided; eg "unless the caregivers volunteered information whereby the child had a problem, we consider them normative by default" | optional | - |
| **mother_id** | unique ID of the mother | optional | - |
| **father_id** | unique ID of the father | optional | - |
| **daytime** | yes (Y) means recording launched such that most or all of the audiorecording happens during daytime; no (N) means at least 30% of the recording may happen at night | optional | `(Y\|N)` (regex) |




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
