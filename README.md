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
    - Loading modules 
    - Hosting public files / hubs 
    - Transfering files 
    - Finding my quota
    - Shared genome repos 
- shared folder -> change permissions with chmod 770 ( 777 does not work)

## Running CGAT pipelines

- [Set up DRMAA](./DRMAA.md)
- [Set up CGAT configuration](./cgat-core.md)
