# SpatialVariationMMN

SpatialVariationMMN is a PsychoPy script that implements an auditory mismatch negativity task.

A full description of the stimuli used, the experimental design and code can be found in the [MethodsReport](MethodsReport.md) file.

## Requirements

In order to run this task you will need the following software (other versions of each software may work)

* PsychoPy (2021.1.4)
* InpOut32 parallel port driver modified for x64 compatibility (see http://www.highrez.co.uk/Downloads/InpOut32 for information)
* MATLAB (2021a)
* PsySound (https://github.com/gjcooper/psysound) - used for stimulus creation within MATLAB.


## Installation

### Get experiment code

```bash
git clone https://github.com/university-of-newcastle-research/SpatialVariationMMN.git
```

Alternatively you can download the main branch and unzip.

### Get parallel port drivers

Download the drivers and extract to the same folder as the experiment code

```bash
wget https://www.highrez.co.uk/scripts/download.asp?package=InpOutBinaries
unzip InpOutBinaries_1501.zip
```

### Create stimuli

* Install PsySound
* Run `matlab -nosplash -nodesktop -r "run soundgen.m; exit"`
* Move files to subdirectory called stimuli

```bash
mkdir stimuli
mv *.wav stimuli/.
```

## Usage

```bash
python SpatialVartiationMMN.py
```

## Troubleshooting

If there are parallel port problems you may need to adjust the port address in the `SpatialVariationMMN.py` code (line 44). It is also possible to run without a parallel port (although no stimulus codes will be delivered to any EEG equipment). To do this set the `no_parallel` variable to True in `config.py`

## License

MIT - see LICENSE file.
