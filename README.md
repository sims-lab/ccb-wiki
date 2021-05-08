# ccb-wiki

Wiki documenting the CBRG cluster setup

## General Cluster info
- [Setup remote desktop](https://www.imm.ox.ac.uk/research/units-and-centres/mrc-wimm-centre-for-computational-biology/ccb-account/Logging_in_via_PC/pc-using-RDP)
  - change keyboard mappings to mac = in RDP session Applications/Settings/Keyboard/Layout -> change to macbook pro 
    - note to get `#` - only right `option` key works - left will not give you `#`
    - if vpn or session connections drips `|` and `~` might swap around - to correct log out of sessions and log back on. 
- [FAQs](https://www.imm.ox.ac.uk/research/units-and-centres/mrc-wimm-centre-for-computational-biology/ccb-account/FAQ)
  - e.g. 
    - Slurm submission commands 
      - see queues = `sinfo`
        - for training use `teaching`
        - for general use `batch` 

      - qrsh 
         ```From Ewan:  you can do:

                 $ srun --pty bash

                which also takes all the usual parameters that squeue does for allocating memory
                and so forth. However, while you can do it if absolutely necessary or just for teaching purposes
                , in practice we don't generally recommend people do it 'for real' on our system 
                - our usual MO is to run stuff on the normal interactive login nodes (cbrglogin1 or cbrglogin2),
                -  if it's too big for them then run it on the large login node (cbrglogin3), 
                -  and if it's too big for *that* then just deal with it and run it as a batch job.
          
         - Lucy - this is what I have been doing: srun -p batch --cpus-per-task=5 --mem-per-cpu=10G --pty bash -i
       ```
    - Loading modules 
    - [Hosting public files / hubs](./public_trackhubs)
    - Transfering files 
    - Finding my quota
    - Shared genome repos 
- shared folder -> change permissions with chmod 770 ( 777 does not work)

## Conda environments 

  - Where to put them:
    - /t1-data/home/ = faster loading but limited to 20G - this will be too small maybe for most users but it is backed up - cn ask for quota to be increased if needed. 
    - It is not currently recommented to have envs in /t1-data/user/<username> as conda metadata is taking up too much space. 
  - [guide to installing conda on CCB cluster](https://github.com/OBDS-Training/Conda_Workshops/blob/master/1_Conda_intro_CCB.md) 
    - Note - recommended to source conda.sh in bashrc automatically but activate environments using alias once you are on the cluster as they can interfer with remote destop usage and take ages to load. 
  - exporting conda envs yml files 
    - if you are transfering conda envs from other systems use 
      - `conda env export --no-builds > environment_nobuild.yml`
    - other useful things to export and backup
      - `conda env export > environment.yml` = full env details, version and hash code for software build 
      - `conda env export --from-history > env_history.yml` = gives you just the main things you asked for (not all the dependencies) 
      - `conda list --revisions > env_revisions.txt` = the order and date you installed extra packages
      - `conda list --explicit > proj095_list_explicit.txt` = really thourgh list of exactly what you had in your environment 

### Conda Troubleshooting 
  - Mamba not detected in environments other then base and `which conda` path changes on `conda activate` -[see issue 1] (https://github.com/sims-lab/cbrg-wiki/issues/1)
  
 
## Running CGAT pipelines

- [Example bashrc](./example_bashrc)
- [Set up DRMAA](./DRMAA.md)
- [Set up CGAT configuration](./cgat-core.md)

