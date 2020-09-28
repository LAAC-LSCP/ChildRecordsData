

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

| Name | Description | Required ? | Format |
|------|-------------|------------|--------|
| experiment | one word to capture the unique ID of the data collection effort; for instance Tsimane_2018, solis-intervention-pre | required | none |
| child_id | unique child ID -- unique within the experiment (Id could be repeated across experiments to refer to different children) | required | none |
| child_dob | child's date of birth | required | none |
| location_id | Unique location ID -- only specify here if children never change locations in this culture; otherwise, specify in the recordings metadata | optional | none |
| child_sex | f= female, m=male | optional | none |
| language | language the child is exposed to if child is monolingual; small caps, indicate dialect by name or location if available; eg "france french"; "paris french" | optional | none |
| languages | list languages child is exposed to separating them with ; and indicating the percentage if one is available; eg: "french 35%; english 65%" | optional | none |
| mat_ed | maternal years of education | optional | none |
| fat_ed | paternal years of education | optional | none |
| car_ed | years of education of main caregiver (if not mother or father) | optional | none |
| monoling | whether the child is monolingual (Y) or not (N) | optional | none |
| monoling_criterion | how monoling was decided; eg "we asked families which languages they spoke in the home" | optional | none |
| normative | whether the child is normative (Y) or not (N) | optional | none |
| normative_criterion | how normative was decided; eg "unless the caregivers volunteered information whereby the child had a problem, we consider them normative by default" | optional | none |
| mother_id | unique ID of the mother | optional | none |
| father_id | unique ID of the father | optional | none |
| daytime | yes (Y) means recording launched such that most or all of the audiorecording happens during daytime; no (N) means at least 30% of the recording may happen at night | optional | none |




## recording notebook

| Name | Description | Required ? | Format |
|------|-------------|------------|--------|
| experiment | one word to capture the unique ID of the data collection effort; for instance Tsimane_2018, solis-intervention-pre | required | none |
| child_id | unique child ID -- unique within the experiment (Id could be repeated across experiments to refer to different children) | required | none |
| date_iso | date in which recording was started in ISO (eg 2020-09-17) | required | none |
| start_time | local time in which recording was started in format 24-hour (H)H:MM; if minutes are unknown, use 00. Set as ‘NA’ if unknown. | required | none |
| recording_device_type | lena, usb, olympus, babylogger (lowercase) | required | none |
| filename | the path to the file from the root of “recordings”), set to ‘NA’ if no valid recording available. It is unique (two recordings cannot point towards the same file). | required | none |
| recording_device_id | unique ID of the recording device | optional | none |
| experimenter | who collected the data (could be anonymized ID) | optional | none |
| location_id | unique location ID -- can be specified at the level of the child (if children do not change locations) | optional | none |
| its_filename | its_filename | optional | none |
| upl_filename | upl_filename | optional | none |
| lena_id |  | optional | none |
| age | age in months (rounded) | optional | none |
| notes | free-style notes about individual recordings (avoid tabs and newlines) | optional | none |
