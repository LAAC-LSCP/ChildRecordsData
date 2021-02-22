- [Introduction](#introduction)
  - [Overview](#overview)
  - [Chunk extraction](#chunk-extraction)
  - [Chunk upload](#chunk-upload)
  - [Classifications retrieval](#classifications-retrieval)

## Introduction

We are providing here a pipeline to create, upload and analyse long format recordings using the Zooniverse citizen science platform.

We have an open project aimed at adding vocal maturity labels to segments LENA labeled as being key child in Zooniverse (https://www.zooniverse.org/projects/chiarasemenzin/maturity-of-baby-sounds).

If you would like your data labeled with this project, here is what you'd need to do.
1. Get in touch with us, so we know you are interested! 
2. Have someone trustworthy & with some coding skills (henceforth, the RA) create a database using the [formatting instructions and specifications](http://laac-lscp.github.io/ChildRecordsData/FORMATTING.html).
4. Have the RA create an account on Zooniverse (top right of zooniverse.org) for them and yourself, & provide us with both handles. The RA should first update the team section to add you (have ready a picture and a blurb). The RA can also add your institution's logo if you'd like. Both of these are done in the [lab section](https://www.zooniverse.org/lab/10073)
5. The RA will then follow the instructions in the present README to create subjects and push up your data -- see below.
6. We also ask the RA to pitch in and help answer questions in the [forum](https://www.zooniverse.org/projects/chiarasemenzin/maturity-of-baby-sounds/talk), at least one comment a day. 
7. You can visit the [stats section](https://www.zooniverse.org/projects/chiarasemenzin/maturity-of-baby-sounds/stats) to look at how many annotations are being done.


You can also use this code and your own knowledge to set up a new project of your own. 

### Overview

```bash
$ child-project zooniverse --help
usage: child-project zooniverse [-h]
                                {extract-chunks,upload-chunks,retrieve-classifications}
                                ...

positional arguments:
  {extract-chunks,upload-chunks,retrieve-classifications}
                        action
    extract-chunks      extract chunks and store metadata in
                        DESTINATION/chunks.csv
    upload-chunks       upload chunks and updates DESTINATION/chunks.csv
    retrieve-classifications
                        retrieve classifications and save them into
                        DESTINATION/classifications.csv

optional arguments:
  -h, --help            show this help message and exit
```


### Chunk extraction

```bash
$ child-project zooniverse extract-chunks --help
usage: child-project zooniverse extract-chunks [-h] --keyword KEYWORD
                                               --destination DESTINATION
                                               --sample-size SAMPLE_SIZE
                                               [--annotation-set ANNOTATION_SET]
                                               [--target-speaker-type {CHI,OCH,FEM,MAL} [{CHI,OCH,FEM,MAL} ...]]
                                               [--batch-size BATCH_SIZE]
                                               [--threads THREADS]
                                               path

positional arguments:
  path                  path to the dataset

optional arguments:
  -h, --help            show this help message and exit
  --keyword KEYWORD     export keyword
  --destination DESTINATION
                        destination
  --sample-size SAMPLE_SIZE
                        how many samples per recording
  --annotation-set ANNOTATION_SET
                        annotation set
  --target-speaker-type {CHI,OCH,FEM,MAL} [{CHI,OCH,FEM,MAL} ...]
                        speaker type to get chunks from
  --batch-size BATCH_SIZE
                        batch size
  --threads THREADS     how many threads to run on
```

If it does not exist, DESTINATION is created.
Audio chunks are saved in wav and mp3 in `DESTINATION/chunks`.
Metadata is stored in a file named `DESTINATION/chunks.csv`.

<table>
<tr>
    <th>argument</th>
    <th>description</th>
    <th>default value</th>
</tr>
<tr>
    <td>path</td>
    <td>path to the dataset</td>
    <td></td>
</tr>
<tr>
    <td>destination</td>
    <td>where to write the output metadata and files. metadata will be saved to $destination/chunks.csv and audio chunks to $destination/chunks.</td>
    <td></td>
</tr>
<tr>
    <td>sample-size</td>
    <td>how many vocalization events per recording</td>
    <td></td>
</tr>
<tr>
    <td>batch-size</td>
    <td>how many chunks per batch</td>
    <td>1000</td>
</tr>
<tr>
    <td>annotation-set</td>
    <td>which annotation set to use for sampling</td>
    <td>vtc</td>
</tr>
<tr>
    <td>target-speaker-type</td>
    <td>speaker type to get chunks from</td>
    <td>CHI</td>
</tr>
<tr>
    <td>threads</td>
    <td>how many threads to perform the conversion on, uses all CPUs if <= 0</td>
    <td>0</td>
</tr>
</table>

### Chunk upload

```bash
$ child-project zooniverse upload-chunks --help
usage: child-project zooniverse upload-chunks [-h] --destination DESTINATION
                                              --zooniverse-login
                                              ZOONIVERSE_LOGIN
                                              --zooniverse-pwd ZOONIVERSE_PWD
                                              --project-slug PROJECT_SLUG
                                              --set-prefix SET_PREFIX
                                              [--batches BATCHES]

optional arguments:
  -h, --help            show this help message and exit
  --destination DESTINATION
                        destination
  --zooniverse-login ZOONIVERSE_LOGIN
                        zooniverse login
  --zooniverse-pwd ZOONIVERSE_PWD
                        zooniverse password
  --project-slug PROJECT_SLUG
                        zooniverse project name
  --set-prefix SET_PREFIX
                        subject prefix
  --batches BATCHES     amount of batches to upload
```

Uploads as many batches of audio chunks as specified to Zooniverse, and updates `chunks.csv` accordingly.

<table>
<tr>
    <th>argument</th>
    <th>description</th>
    <th>default value</th>
</tr>
<tr>
    <td>destination</td>
    <td>where to find the output metadata and files.</td>
    <td></td>
</tr>
<tr>
    <td>project-slug</td>
    <td>Zooniverse project slug (e.g.: lucasgautheron/my-new-project)</td>
    <td></td>
</tr>
<tr>
    <td>set-prefix</td>
    <td>prefix for the subject set</td>
    <td></td>
</tr>
<tr>
    <td>zooniverse-login</td>
    <td>zooniverse login</td>
    <td></td>
</tr>
<tr>
    <td>zooniverse-pwd</td>
    <td>zooniverse password</td>
    <td></td>
</tr>
<tr>
    <td>batches</td>
    <td>how many batches to upload. it is recommended to upload less than 10.000 chunks per day, so 10 batches of 1000 by default. upload all batches if set to 0</td>
    <td>0</td>
</tr>
</table>

### Classifications retrieval

```bash
$ child-project zooniverse retrieve-classifications --help
usage: child-project zooniverse retrieve-classifications [-h] --destination
                                                         DESTINATION
                                                         --zooniverse-login
                                                         ZOONIVERSE_LOGIN
                                                         --zooniverse-pwd
                                                         ZOONIVERSE_PWD
                                                         --project-id
                                                         PROJECT_ID

optional arguments:
  -h, --help            show this help message and exit
  --destination DESTINATION
                        destination
  --zooniverse-login ZOONIVERSE_LOGIN
                        zooniverse login
  --zooniverse-pwd ZOONIVERSE_PWD
                        zooniverse password
  --project-id PROJECT_ID
                        zooniverse project id
```

Retrieve classifications and save them into `DESTINATION/classifications.csv`.

<table>
<tr>
    <th>argument</th>
    <th>description</th>
    <th>default value</th>
</tr>
<tr>
    <td>destination</td>
    <td>where to find the output metadata and files.</td>
    <td></td>
</tr>
<tr>
    <td>project-id</td>
    <td>Numerical zooniverse project id (e.g.: 10073)</td>
    <td></td>
</tr>
<tr>
    <td>zooniverse-login</td>
    <td>zooniverse login</td>
    <td></td>
</tr>
<tr>
    <td>zooniverse-pwd</td>
    <td>zooniverse password</td>
    <td></td>
</tr>
</table>