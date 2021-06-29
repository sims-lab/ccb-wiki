# ccb-wiki

Wiki documenting the CBRG cluster setup

## General Cluster info
- [Setup remote desktop](https://www.imm.ox.ac.uk/research/units-and-centres/mrc-wimm-centre-for-computational-biology/ccb-account/Logging_in_via_PC/pc-using-RDP)
  - change keyboard mappings to mac = in RDP session Applications/Settings/Keyboard/Layout -> change to macbook pro 
    - note to get `#` - only right `option` key works - left will not give you `#`
    - if vpn or session connections drips `|` and `~` might swap around - to correct log out of sessions and log back on. 
- [Official FAQs](https://www.imm.ox.ac.uk/research/units-and-centres/mrc-wimm-centre-for-computational-biology/ccb-account/FAQ) 
    - Loading modules 
    - Transfering files 
    - Finding my quota
    - Shared genome repos 
    - Slurm submission commands 
- [Hosting public files / hubs](./public_trackhubs)
- **Slurm**
    - See queues = `sinfo`
        ```
        - for training use `teaching`
        - for general use `batch` 
        ```
    - You can check how much your requesting using 
      ```
      squeue --me  -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R %C %d %D %A %H %J %m %S %z %Z"
      ```
          - This explains the different fields https://slurm.schedmd.com/squeue.html
          - %S details the time it thinks your job will start running

    - qrsh 
         ```
         From Ewan:  you can do:

         $ srun --pty bash

         which also takes all the usual parameters that squeue does for allocating memory
         and so forth. However, while you can do it if absolutely necessary or just for teaching purposes
         , in practice we don't generally recommend people do it 'for real' on our system 
         - our usual MO is to run stuff on the normal interactive login nodes (cbrglogin1 or cbrglogin2),
         -  if it's too big for them then run it on the large login node (cbrglogin3), 
         -  and if it's too big for *that* then just deal with it and run it as a batch job.
         ```
         
         ```
         - Lucy - this is what I have been doing: srun -p batch --cpus-per-task=5 --mem-per-cpu=10G --pty bash -i
         ```
       
- `sims-lab/shared` folder -> change permissions with chmod 770 ( 777 does not work)




## Conda environments 

  - **Where to put them:**
    - `/t1-data/home/` = faster loading but limited to 20G 
        - this will be too small maybe for most users but it is backed up 
        - can ask for quota to be increased if needed. 
    - It is not currently recommented to have envs in /t1-data/user/<username> as conda metadata is taking up too much space. 
  
  - [Guide to installing conda on CCB cluster](https://github.com/OBDS-Training/Conda_Workshops/blob/master/1_Conda_intro_CCB.md) 
    - It's not recommended to source conda.sh in bashrc automatically but activate environments using alias once you are on the cluster as they can interfer with remote destop usage and take ages to load. 
  
  
  - **Exporting conda envs yml files:**
    - Find a script to automate it here: [export_conda_envs.py](./export_conda_envs.py) 
    - if you are transfering conda envs from other systems use 
      - `conda env export --no-builds > environment_nobuild.yml`
    - other useful things to export and backup
      - `conda env export > environment.yml` = full env details, version and hash code for software build 
      - `conda env export --from-history > env_history.yml` = gives you just the main things you asked for (not all the dependencies) 
      - `conda list --revisions > env_revisions.txt` = the order and date you installed extra packages
      - `conda list --explicit > proj095_list_explicit.txt` = really thourgh list of exactly what you had in your environment 

### Conda Troubleshooting 
  - [issue1](https://github.com/sims-lab/cbrg-wiki/issues/1) - Mamba not detected in environments other then base and `which conda` path changes on `conda activate`
  - [conda env not being picked up correctly by by P.run()](https://github.com/sims-lab/ccb-wiki/issues/4)
  
 
## Running CGAT pipelines

- [Example bashrc](./example_bashrc)
- [Set up correct DRMAA path](./DRMAA.md)
- [Set up `.cgat.yml` config file to set default queues and memory requirements](./cgat-core.md)

