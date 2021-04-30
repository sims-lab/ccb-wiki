# cbrg-wiki

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

              which also takes all the usual parameters that squeue does for allocating memory and so forth. However, while you can do it if absolutely necessary or just for teaching purposes, in practice we don't generally recommend people do it 'for real' on our system - our usual MO is to run stuff on the normal interactive login nodes (cbrglogin1 or cbrglogin2), if it's too big for them then run it on the large login node (cbrglogin3), and if it's too big for *that* then just deal with it and run it as a batch job.
     ```
     
    - Loading modules 
    - Hosting public files / hubs 
    - Transfering files 
    - Finding my quota
    - Shared genome repos 
- shared folder -> change permissions with chmod 770 ( 777 does not work)

## Running CGAT pipelines

- [Set up DRMAA](./DRMAA.md)
- [Set up CGAT configuration](./cgat-core.md)
