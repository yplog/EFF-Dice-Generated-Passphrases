# EFF Dice-Generated Passphrases

Please read the [article](https://www.eff.org/dice) before you start. For installation: *pip install -r requirements.txt*

## Usage:  
```bash
main.py [GENERATOR] [MODE] [SAVE]
```   
## Generator:  
For more information about generators: https://www.eff.org/dice  
* -l  --longwordlist   
* -s1 --shortwordlist1  
* -s2 --shortwordlist2  
#### Example:  
```bash
main.py -l 
``` 
## Mode:  
Default mode is offline. Last updated date of offline mode: 26/02/2019
* --online  
* --offline  
#### Example:  
```bash
main.py -l --online
``` 
## Save:
Saves the key value pair in the database. Keys produced in this way are always available. Used as database: [pickleDB](https://pythonhosted.org/pickleDB/).
* -ga --getall
* -gk --getkey
* -da --delall
* -dk --delkey

#### Example:
```bash
main.py -ga
``` 
